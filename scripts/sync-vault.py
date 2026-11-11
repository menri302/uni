#!/usr/bin/env python3
"""Kopiert die Zusammenfassungen aus dem Obsidian-Vault in den Quartz-content-Ordner.

Veröffentlicht wird NUR der Inhalt jedes Ordners namens "Zusammenfassung"
irgendwo unter "01 Universität" (z. B. <Semester>/<Fach>/Zusammenfassung/),
plus die Bilder/Anhänge, die in diesen Notizen eingebettet sind (![[...]]).
Alles andere (Folien, Aufgaben, Anki, ToDos, ...) bleibt privat.
Die Startseite (content/index.md) wird mit allen Fächern neu erzeugt.

Aufruf:  python3 scripts/sync-vault.py
"""
import os
import re
import shutil
import sys
import unicodedata
from pathlib import Path

VAULT = Path.home() / "Library/Mobile Documents/iCloud~md~obsidian/Documents/home"
UNI = VAULT / "01 Universität"
ATTACHMENTS = VAULT / "03 Sonstige/Anhaenge"
SUBFOLDER = "Zusammenfassung"
# Fächer, die NICHT auf die Website sollen (Ordnername wie im Vault)
EXCLUDE = {
    "Analysis für WiWi",
}
# Fächer, die auf der Website anders heißen sollen als im Vault ("Vault-Name": "Website-Name")
DISPLAY_NAMES = {}

QUARTZ = Path(__file__).resolve().parent.parent
CONTENT = QUARTZ / "content"
INDEX_INTRO = """---
title: Uni-Zusammenfassungen
---

Zusammenfassungen zum **B.Sc. Volkswirtschaftslehre** an der Universität Münster.

Alle Kapitel findest du links in der Seitenleiste. Mit der Suche oben kannst du nach Begriffen suchen.
"""
# Hier parkt `npx quartz sync` den content-Ordner; bei Abbruch bleibt er dort liegen
CONTENT_CACHE = QUARTZ / ".quartz-cache" / "content-cache"

EMBED = re.compile(r"!\[\[([^\]]+?)\]\]")
LINK = re.compile(r"(?<!!)\[\[([^\]|#\\]+)(#[^\]|\\]*)?((?:\\?\|)[^\]]*)?\]\]")
NOTE_EMBED = re.compile(r"!\[\[([^\]|#\\]+)(#[^\]|\\]*)?((?:\\?\|)[^\]]*)?\]\]")
MEDIA_SUFFIX = re.compile(r"\.(png|jpe?g|gif|svg|webp|bmp|pdf|mp3|mp4|webm|mov|wav)$", re.I)


def clean_content():
    if not CONTENT.exists():
        if CONTENT_CACHE.is_dir():
            print("content-Ordner aus abgebrochenem Sync wiederhergestellt.")
            shutil.move(CONTENT_CACHE, CONTENT)
        else:
            CONTENT.mkdir()
    for item in CONTENT.iterdir():
        if item.is_dir():
            shutil.rmtree(item)
        else:
            item.unlink()


def fix_math_dollars(text):
    """Ersetzt \\$ innerhalb von $...$-Formeln durch \\char36{} (Dollarzeichen).

    Obsidian versteht ${}\\$1{,}000$, Quartz liest das \\$ aber als Formelende.
    \\$ im normalen Text bleibt unverändert.
    """
    out = []
    in_math = False
    in_fence = False
    for line in text.splitlines(keepends=True):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
        if in_fence:
            out.append(line)
            continue
        i = 0
        in_code = False
        while i < len(line):
            ch = line[i]
            if ch == "`" and not in_math:
                in_code = not in_code
            elif not in_code and line.startswith("\\$", i):
                out.append("\\char36{}" if in_math else "\\$")
                i += 2
                continue
            elif not in_code and line.startswith("$$", i):
                in_math = not in_math
                out.append("$$")
                i += 2
                continue
            elif not in_code and ch == "$":
                in_math = not in_math
            out.append(ch)
            i += 1
    return "".join(out)


def find_attachment(name):
    candidate = ATTACHMENTS / name
    if candidate.is_file():
        return candidate
    for path in VAULT.rglob(name):
        if ".obsidian" not in path.parts and path.is_file():
            return path
    return None


def nfc(text):
    return unicodedata.normalize("NFC", text)


def rewrite_links(notes):
    """Schreibt [[Notiz]]-Links auf den vollen Pfad in content/ um.

    Quartz löst kurze Links nicht immer auf. Links auf Notizen, die nicht
    veröffentlicht werden, werden zu normalem Text (statt toter Links).
    """
    by_stem = {}
    for note in notes:
        by_stem.setdefault(note.stem, []).append(note)

    for note in notes:
        def replace(match):
            target, heading, alias = match.group(1), match.group(2) or "", match.group(3) or ""
            candidates = by_stem.get(nfc(Path(target.strip()).stem), [])
            if not candidates:
                label = re.sub(r"^\\?\|", "", alias) if alias else Path(target).stem
                return label
            # Pfad im Link (z. B. "01 Universität/<Semester>/<Fach>/Zusammenfassung/<Notiz>")
            # entscheidet; sonst bei gleichen Namen die Notiz aus demselben Fach bevorzugen
            wanted = "/".join(p for p in Path(nfc(target.strip())).parts if p not in (UNI.name, SUBFOLDER))
            matching = [c for c in candidates if c.relative_to(CONTENT).with_suffix("").as_posix().endswith(wanted)] or candidates
            best = next((c for c in matching if c.parent == note.parent), matching[0])
            path = best.relative_to(CONTENT).with_suffix("").as_posix()
            return f"[[{path}{heading}{alias}]]"

        def replace_embed(match):
            # Notiz-Embeds (![[Notiz#Überschrift]]) ebenfalls auf vollen Pfad umschreiben,
            # sonst ist der Embed bei gleichnamigen Notizen (z. B. "00 Formelsammlung") mehrdeutig.
            # Bilder/Anhänge und nicht veröffentlichte Notizen bleiben unverändert.
            target = match.group(1)
            if MEDIA_SUFFIX.search(target.strip()):
                return match.group(0)
            if not by_stem.get(nfc(Path(target.strip()).stem)):
                return match.group(0)
            return "!" + replace(match)

        text = note.read_text(encoding="utf-8")
        new = LINK.sub(replace, text)
        new = NOTE_EMBED.sub(replace_embed, new)
        if new != text:
            stat = note.stat()
            note.write_text(new, encoding="utf-8")
            os.utime(note, (stat.st_atime, stat.st_mtime))


def write_index(courses):
    """Startseite mit allen Fächern, gruppiert nach Semester (Ordner über dem Fach)."""
    lines = [INDEX_INTRO]
    current_group = None
    for course_rel, first_note in courses:
        group = str(course_rel.parent) if course_rel.parent != Path(".") else "Fächer"
        if group != current_group:
            lines.append(f"\n## {group}\n")
            current_group = group
        link = (course_rel / first_note.stem).as_posix()
        lines.append(f"- [[{link}|{course_rel.name}]]")
    (CONTENT / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def find_sources():
    """Alle Zusammenfassung-Ordner; bricht ab, statt eine leere Website zu erzeugen."""
    try:
        os.listdir(UNI)
    except OSError as error:
        sys.exit(f"Abbruch: Vault-Ordner nicht lesbar ({error}). Es wurde nichts verändert.")
    sources = [
        s for s in sorted(UNI.rglob(SUBFOLDER))
        if s.is_dir() and ".obsidian" not in s.parts and any(s.rglob("*.md"))
        and nfc(s.parent.name) not in EXCLUDE
    ]
    if not sources:
        sys.exit(
            f"Abbruch: Keine Notizen in '{SUBFOLDER}'-Ordnern unter {UNI} gefunden. "
            "Es wurde nichts verändert und nichts hochgeladen.\n"
            "Tipp: Skript im normalen Terminal starten, nicht mit '!' im Claude-Chat."
        )
    return sources


SVG_EMBED = re.compile(r"!\[\[([^\]|#]+?\.svg)(?:\\?\|(\d+))?\]\]", re.I)


def svg_slug(name):
    """So benennt Quartz Anhänge in der URL: klein, Leerzeichen -> Bindestrich."""
    return nfc(name).strip().lower().replace(" ", "-")


def fix_svg_embeds(notes):
    """Quartz bettet SVGs als <object> mit falschem relativen Pfad ein (Bild fehlt).
    Deshalb SVG-Embeds als <img> mit absolutem Pfad schreiben."""
    def repl(m):
        width = f' width="{m.group(2)}"' if m.group(2) else ""
        return (f'<img src="/anhaenge/{svg_slug(m.group(1))}" alt="{nfc(m.group(1))[:-4]}"'
                f'{width} style="max-width:100%;height:auto">')
    for note in notes:
        text = note.read_text(encoding="utf-8")
        new = SVG_EMBED.sub(repl, text)
        if new != text:
            note.write_text(new, encoding="utf-8")


def main():
    sources = find_sources()
    clean_content()
    notes = []
    courses = []
    for source in sources:
        # .../01 Universität/<Semester>/<Fach>/Zusammenfassung -> content/<Semester>/<Fach>/
        # Umlaute in Pfaden einheitlich als NFC (macOS liefert teils NFD), sonst finden Links sie nicht
        course_rel = Path(nfc(str(source.parent.relative_to(UNI))))
        course_rel = course_rel.with_name(DISPLAY_NAMES.get(course_rel.name, course_rel.name))
        course_notes = []
        for note in sorted(source.rglob("*.md")):
            target = CONTENT / course_rel / nfc(str(note.relative_to(source)))
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(fix_math_dollars(note.read_text(encoding="utf-8")), encoding="utf-8")
            shutil.copystat(note, target)
            course_notes.append(target)
        if course_notes:
            notes.extend(course_notes)
            courses.append((course_rel, course_notes[0]))
    rewrite_links(notes)
    write_index(courses)

    embeds = set()
    for note in notes:
        for match in EMBED.findall(note.read_text(encoding="utf-8")):
            # "bild.png|375" bzw. in Tabellen "bild.png\|375" -> "bild.png"
            name = re.split(r"\\?\|", match)[0].split("#")[0].strip()
            if Path(name).suffix and Path(name).suffix.lower() != ".md":
                embeds.add(name)

    missing = []
    attachment_dir = CONTENT / "Anhaenge"
    for name in sorted(embeds):
        path = find_attachment(name)
        if path is None:
            missing.append(name)
            continue
        attachment_dir.mkdir(exist_ok=True)
        shutil.copy2(path, attachment_dir / path.name)

    fix_svg_embeds(notes)
    print(f"{len(courses)} Fächer, {len(notes)} Notizen und {len(embeds) - len(missing)} Anhänge kopiert.")
    for name in missing:
        print(f"  Anhang nicht gefunden: {name}")


if __name__ == "__main__":
    main()
