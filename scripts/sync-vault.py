#!/usr/bin/env python3
"""Kopiert die Zusammenfassungen aus dem Obsidian-Vault in den Quartz-content-Ordner.

Veröffentlicht wird NUR: <Semester>/<Fach>/Zusammenfassung/*.md
plus die Bilder/Anhänge, die in diesen Notizen eingebettet sind (![[...]]).
Alles andere (Folien, Aufgaben, Anki, ToDos, ...) bleibt privat.

Aufruf:  python3 scripts/sync-vault.py
"""
import re
import shutil
from pathlib import Path

VAULT = Path.home() / "Library/Mobile Documents/iCloud~md~obsidian/Documents/home"
SEMESTER = VAULT / "01 Universität/01 Wintersemester 2026"
ATTACHMENTS = VAULT / "03 Sonstige/Anhaenge"
SUBFOLDER = "Zusammenfassung"

QUARTZ = Path(__file__).resolve().parent.parent
CONTENT = QUARTZ / "content"
KEEP = {"index.md"}  # Dateien in content/, die nicht überschrieben werden
# Hier parkt `npx quartz sync` den content-Ordner; bei Abbruch bleibt er dort liegen
CONTENT_CACHE = QUARTZ / ".quartz-cache" / "content-cache"

EMBED = re.compile(r"!\[\[([^\]]+?)\]\]")


def clean_content():
    if not CONTENT.exists():
        if CONTENT_CACHE.is_dir():
            print("content-Ordner aus abgebrochenem Sync wiederhergestellt.")
            shutil.move(CONTENT_CACHE, CONTENT)
        else:
            CONTENT.mkdir()
    for item in CONTENT.iterdir():
        if item.name in KEEP:
            continue
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


def main():
    clean_content()
    notes = []
    for course in sorted(SEMESTER.iterdir()):
        source = course / SUBFOLDER
        if not source.is_dir():
            continue
        target = CONTENT / course.name
        target.mkdir(parents=True, exist_ok=True)
        for note in sorted(source.glob("*.md")):
            text = fix_math_dollars(note.read_text(encoding="utf-8"))
            (target / note.name).write_text(text, encoding="utf-8")
            shutil.copystat(note, target / note.name)
            notes.append(target / note.name)

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

    print(f"{len(notes)} Notizen und {len(embeds) - len(missing)} Anhänge kopiert.")
    for name in missing:
        print(f"  Anhang nicht gefunden: {name}")


if __name__ == "__main__":
    main()
