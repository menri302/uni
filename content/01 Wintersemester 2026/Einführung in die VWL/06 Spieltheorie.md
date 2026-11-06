# Einführung

**Problem:** Das optimale Verhalten des einen hängt vom Verhalten des anderen ab → mit unseren bisherigen (nicht-strategischen) Werkzeugen nicht analysierbar.

> [!BUG] Spieltheorie
> Instrumentarium zur Analyse von Situationen mit **strategischen Interaktionen**


## Definitionen
> [!NOTE] Ein Spiel hat drei Schlüsselelemente
> 1. **Spieler**
> 2. **Strategien** jedes Spielers
> 3. **Auszahlungen** für jeden Spieler, abhängig von den **eigenen** und den Strategien der **anderen**

**Spiele mit vollständiger Information**: Alle Spieler kennen das Spiel und die Auszahlungen aller anderen Spieler.


# Simultane Spiele

> [!NOTE] Simultane Spiele
> Alle Spieler wählen ihre Strategie gleichzeitig
> --> Entscheidend ist nicht der genaue Zeitpunkt, sondern dass die Spieler die **Wahl des anderen nicht kennen**, wenn sie ihre Entscheidung treffen

### Beispiel: Gefangenendilemma
![[Pasted image 20261030125450.png|530]]

> [!NOTE] Beste-Antwort Funktion
> Optimal Strategie eines für alle möglichen Strategien des anderen Spielers
> Bspw. hier: Immer gestehen


> [!BUG] Dominante Strategie
> Wenn ein Spieler für jede mögliche Strategie eines anderen Spielers die gleich beste Antwort hat
>


> [!EXAMPLE] Gleichgewicht in dominanten Strategien
> Eine Strategiekombination ist im GIDS wenn alle Gleichgewichtsstrategien dominante Strategien sind (bspw. Gefangenendilemma)

Voraussetzung: Alle Teilnehmenden gleichzeitig Optimierend
Eine Spieler mit dominanter Strategie muss keine Erwartung über das Verhalten anderer bilden

## Wie kann das Gefangenendilemma gelöst werden?
1. Vertrag, welcher das Verhalten festlegt
2. Wiederholte Interaktion der Spieler
   - Jeder Spieler droht, in Zukunft unkooperativ zu spielen, wenn der andere von der Kooperation abweicht
   - **Trade-off**: heute abweichen (höhere Auszahlung **heute**, aber Bestrafung **morgen**) vs. kooperieren (höhere Auszahlungen in der **Zukunft**)
   --> Kooperation ist ein **Gleichgewicht**, wenn die Spieler die zukünftigen Auszahlungen **hoch genug bewerten** 
## Anwendung: Laborexperiment „Öffentliches Gut“-Spiel
**Warum Laborexperimente?** Teilnehmende bekommen ein strukturiertes Entscheidungsproblem nahe am Modell, Strategien und Auszahlungen sind genau kontrollierbar → Test, ob echtes Verhalten zur Theorie passt.

- 4 Spieler A, B, C, D, jeder erhält Startkapital $I$
- Jeder entscheidet, wie viel ($g$) er in ein öffentliches Gut einzahlt
- Pro eingezahltem Euro erhalten **alle** Gruppenmitglieder **0,40 €**

$$\pi_A = I - g_A + 0{,}4 \cdot (g_A + g_B + g_C + g_D)$$

- Privater Grenznutzen eines Euros: **0,40 €** (< 1 € Kosten)
- Sozialer Grenznutzen: $4 \cdot 0{,}40\,€ =$ **1,60 €** pro eingezahltem Euro (> 1 € Kosten)

**Prognose:**
- **Dominante Strategie:** nichts einzahlen → GIDS: alle zahlen 0 → jeder erhält $I$
- **Optimal für die Gruppe:** alle zahlen alles ein → jeder erhält $1{,}6 \cdot I$

**Ergebnisse:**
- Im Schnitt werden **< 10 %** der Ausstattung beigetragen
- **75 %** tragen **gar nichts** bei
- Bei wiederholter Interaktion: anfangs höhere Beiträge, dann Rückgang auf **nahe Null**

→ Verhalten stimmt gut mit der spieltheoretischen Vorhersage überein, obwohl die Teilnehmenden keine Spieltheorie kennen

## Nash-Gleichgewicht
Bei vielen Spielen gibt es **kein GIDS**.

### Beispiel: Zwei Zeitschriften
Beide wählen **gleichzeitig** Promi A oder B fürs Titelblatt. Promi A zieht mehr Leser an. Allein mit einem Promi → alle interessierten Leser. Gleicher Promi → Leser werden geteilt, Z1 bekommt mehr (beliebter).

| (Z1, Z2) | **Z2: Promi A** | **Z2: Promi B** |
|---|---|---|
| **Z1: Promi A** | 450, 200 | **500, 300** ← Nash-GG |
| **Z1: Promi B** | 400, 400 | 300, 0 |

- **Z1**: Promi A ist **dominante Strategie** (450 > 400, 500 > 300)
- **Z2**: **keine** dominante Strategie, beste Antwort hängt von Z1 ab (Z1 wählt A → B; Z1 wählt B → A)
- → **kein GIDS**, aber Nash-GG **(A, B)**

Das Nash-GG ist ein **schwächeres** Konzept: Die Strategie muss nicht die beste Antwort auf **alle** Strategien der anderen sein, sondern nur auf die **optimale** Strategie der anderen.

> [!NOTE] Definition Nash-Gleichgewicht
> Eine Strategiekombination $(s_1^*, s_2^*)$ ist ein Nash-GG, wenn:
> - $s_2^*$ die beste Antwort von Spieler 2 ist, wenn Spieler 1 $s_1^*$ wählt
> - $s_1^*$ die beste Antwort von Spieler 1 ist, wenn Spieler 2 $s_2^*$ wählt
>
> → Situation **wechselseitig bester Antworten**, kein Spieler hat einen Anreiz, sein Verhalten zu ändern

Lesart: $(s_1^*, s_2^*)$ = eine **Zelle** der Matrix (1. Stelle: Strategie von Spieler 1, 2. Stelle: Strategie von Spieler 2)

**Anmerkung:** Jedes GIDS ist ein Nash-GG, aber **nicht umgekehrt**.

**Bestimmung (Unterstreichungsmethode):**
1. Beste Antworten von Spieler 1: in **jeder Spalte** die höchste Auszahlung von Spieler 1 unterstreichen
2. Beste Antworten von Spieler 2: in **jeder Zeile** die höchste Auszahlung von Spieler 2 unterstreichen
3. Zelle, in der **beide** Auszahlungen unterstrichen sind = **Nash-GG**

## Multiple Nash-Gleichgewichte
Bei vielen Spielen gibt es **mehrere** Nash-GG.

### Beispiel: Aufrüsten vs. Abrüsten
Zwei Länder entscheiden, ob sie neue Waffen produzieren (**aufrüsten**) oder bestehende zerstören (**abrüsten**).

| (L1, L2) | **L2: Aufrüsten** | **L2: Abrüsten** |
|---|---|---|
| **L1: Aufrüsten** | **2, 2** ← Nash-GG | 3, 1 |
| **L1: Abrüsten** | 1, 3 | **4, 4** ← Nash-GG |

1. Rüstet ein Land **auf**, zieht das andere es vor, ebenfalls aufzurüsten → (aufrüsten, aufrüsten) ist Nash-GG
2. Rüstet ein Land **ab**, zieht das andere es vor, ebenfalls abzurüsten → (abrüsten, abrüsten) ist Nash-GG

> [!NOTE] Problem
> Bei mehreren Nash-GG ist **im Vorhinein unklar**, welches die Spieler wählen. Hier ist (abrüsten, abrüsten) für beide besser (4 > 2) und scheint daher die naheliegendere Wahl.


# Sequenzielle Spiele
![[Pasted image 20261031120528.png|737]]
**Wie löse ich das?**

> [!NOTE] Rückwärtsinduktion
> Es wird zunächst die optimale Strategie des letzten Spielers (hier Disney) betrachtet, darauf aufbauend die des vorletzten usw.

> [!BUG] Strategie in sequentiellen Spielen
> Eine Strategie muss an **jedem Entscheidungsknoten** festlegen, was zu tun ist
> (Disney: „Frühling, wenn Dreamworks Weihnachten wählt; Weihnachten, wenn Dreamworks Frühling wählt“)
> --> Darauf beruht die Logik der **unglaubwürdigen Drohung**: Rückwärtsinduktion verlangt optimales Verhalten an **jedem** Knoten, nicht nur auf dem Gleichgewichtspfad


|                             | **Disney: Weihnachten** | **Disney: Frühling** |
| --------------------------- | ----------------------- | -------------------- |
| **Dreamworks: Weihnachten** | 50, 50                  | **100, 60** ← Lösung |
| **Dreamworks: Frühling**    | 60, 100                 | 30, 30               |

- Würden beide **gleichzeitig** wählen: **zwei** Nash-GG, (Weihnachten, Frühling) und (Frühling, Weihnachten), es wäre unklar, welches eintritt
- Da Dreamworks **zuerst** zieht, kann es sich das bessere GG aussuchen → (Weihnachten, Frühling)
- Die Tafel zeigt die Reihenfolge **nicht**, dafür braucht man den Spielbaum

## First-Mover-Vorteil
> [!NOTE] First-Mover-Vorteil
> Beide Unternehmen sind **symmetrisch**, sie unterscheiden sich nur darin, **wer zuerst agiert**. Da der First-Mover (Dreamworks) eine höhere Auszahlung erhält (100 > 60) → **First-Mover-Vorteil**.

Können beide beeinflussen, wann sie handeln, wollen **beide zuerst ziehen**, z.B.:
- Film so schnell wie möglich fertigstellen
- Früh **Verträge** mit hohen Strafzahlungen an Kinos unterschreiben, falls der Film nicht zu Weihnachten erscheint (→ glaubwürdige Festlegung)

**First-Mover-Nachteil**: Es gibt auch Fälle, in denen es besser ist, zuletzt zu ziehen
Beispiel **eBay**: Wer am Ende das höchste Gebot hat, erhält das Produkt
→ Anreiz, so lange wie möglich zu warten und kurz vor Ende etwas mehr zu bieten als die anderen
= **Sniping**, v.a. bei Online-Auktionen beobachtet (Roth & Ockenfels, 2002)

## Unglaubwürdige Drohung
Es gibt noch ein **zweites Nash-GG**: Disney veröffentlicht **immer** an Weihnachten, Dreamworks im Frühling
- Disney droht: „Wir kommen an Weihnachten raus, egal was ihr macht“
- Glaubt Dreamworks das, ist Frühling die beste Antwort (60 > 50)

**Aber die Drohung ist nicht glaubwürdig**: Wählt Dreamworks wirklich Weihnachten, wäre Frühling für Disney besser (60 > 50) → Disney würde die Drohung nicht wahr machen
--> Dreamworks durchschaut das und nimmt trotzdem Weihnachten

> [!NOTE] Erkenntnis
> Rückwärtsinduktion sortiert Nash-GG mit **unglaubwürdigen Drohungen** aus. Nash guckt nur ob es jeweils die beste Strategie ist, hinterfragt Grundprämisse (unglaubwürdige Drohung) nicht



## Anwendung: Marktzutrittsabschreckung
Häufigste Anwendung von (un)glaubwürdigen Drohungen.

**Spiel:**
1. Ein **Wettbewerber** entscheidet: Markteintritt oder nicht
2. Tritt er ein, entscheidet das **etablierte Unternehmen** (bisher Monopolist): Preiskampf oder Markt teilen

| Ausgang | Wettbewerber, Etabliertes U. (Mio. $) |
|---|---|
| Kein Eintritt | 0, 50 |
| Eintritt → Preiskampf | −10, −10 |
| Eintritt → Markt teilen | **20, 20** ← Lösung |

**Rückwärtsinduktion:** Nach Eintritt ist Markt teilen besser für das etablierte U. (20 > −10) → Wettbewerber weiß das und tritt ein (20 > 0) → GG: **(Eintritt, Markt teilen)**

**Zweites Nash-GG:** Etabliertes U. droht mit Preiskampf, Wettbewerber glaubt das und bleibt draußen
--> Drohung ist **unglaubwürdig**, nach dem Eintritt würde das etablierte U. doch teilen

### Wie kann der Markteintritt trotzdem verhindert werden?
**1. Selbstverpflichtung zum Preiskampf**, z.B. CEO-Gehalt hängt von der **Verkaufsmenge** ab statt vom Gewinn
--> CEO will hohe Menge = niedrigen Preis, Preiskampf lohnt sich für ihn

| Ausgang | Wettbewerber, CEO |
|---|---|
| Kein Eintritt | **0, 50** ← Lösung |
| Eintritt → Preiskampf | −10, 20 |
| Eintritt → Markt teilen | 20, 10 |

--> Nach Eintritt wählt der CEO Preiskampf (20 > 10) → Drohung ist jetzt **glaubwürdig** → Wettbewerber bleibt draußen (0 > −10)

> [!NOTE] Wichtig
> Funktioniert nur, wenn die Verpflichtung (hier der CEO-Vertrag) **öffentlich beobachtbar** ist

**2. Gewinn des Wettbewerbers im Voraus senken**
- **Treueprogramme** (z.B. Bonusmeilen) binden Kunden → Marktanteil des Neuen zu klein, um rentabel zu sein
- **Exklusivverträge** mit Händlern → Neuer hat keine oder nur schlechte Vertriebskanäle
- --> solche Verträge werden von **Wettbewerbsbehörden** geprüft


> [!EXAMPLE] Southwest Airlines (Goolsbee & Syverson 2008)
> Etablierte Airlines reagieren auf den **drohenden** Markteintritt von Southwest:
> - Preise **−21 %** schon **vor** der neuen Strecke, **−28 %** danach → ca. **¾ der Reaktion vorab**
> - Ziel: Kunden gewinnen und binden, v.a. auf Strecken mit vielen **Geschäftskunden**
> --> Markteintritt wurde trotzdem meist **nicht verhindert**
