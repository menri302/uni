**Was ist Planung?**

> [!abstract] Planung
> **Planung** umfasst **alle Maßnahmen und Überlegungen**, durch die es möglich wird, aus einer **Anzahl von Alternativen** zur Lösung eines Problems die im Hinblick auf ein **Ziel günstigste Alternative** herauszufinden.

**Was wird geplant?**

| Bereich                    | Beispiele                                    |
| -------------------------- | -------------------------------------------- |
| **Absatz**                 | Preise, Mengen, Strategien, Märkte, Produkte |
| **Werbung / Marketing**    | Werbe- und Marketingmaßnahmen                |
| **Personal**               | Personaleinsatz                              |
| **Betriebsmittel**         | Kapazitäten                                  |
| **Rohstoffe**              | Material                                     |
| **Liquidität**             | liquide Mittel, Einzahlungen, Auszahlungen   |
| **Investitionen**          |                                              |
| **Unternehmensübernahmen** |                                              |


## Warum planen?

> [!warning] Planung kostet Geld, aber keine bzw. schlechte Planung auch

| Beispiel               | Problem ohne Planung                          | Folge                                    |
| ---------------------- | --------------------------------------------- | ---------------------------------------- |
| **Überziehungskredit** | nicht genügend flüssige Mittel                | Kosten der Illiquidität (Zinsen)         |
| **Produktionsplanung** | Termine nicht eingehalten, zu wenig Rohstoffe | Kosten fehlender Lieferbereitschaft      |
| **Absatzplanung**      | nicht jederzeit lieferbereit                  | Kunden springen ab, Umsatz geht verloren |


## Wie plant man?

**Planungsprozess**
1. Zielbildung
2. Problemanalyse
3. Alternativensuche, Prognose und Bewertung
4. Entscheidung
5. Realisation
6. Kontrolle
7. Abweichungsanalyse und Korrekturmaßnahmen

**Planungsrichtung**
- **Top-Down**: von der Unternehmensleitung nach unten
- **Bottom-Up**: von den Bereichen nach oben
- **Gegenstromprinzip**: Kombination aus Top-Down und Bottom-Up

**Planungsinstanz**: Wer plant?
- **Unternehmensleitung** (v. a. bei Top-Down)
- **Bereiche** (auf unterschiedlichen Aggregationsstufen)
- **Controlling** (?)

**Planungszeitraum**
**strategische** Planung: langfristig
**taktische** Planung: mittelfristig
**operative** Planung: kurzfristig


**Beispielhafte Planung im Unternehmensprozess**
![[Pasted image 20261026182601.png|649]]
## Arten der Planung
1. **Sequenzielle Planung** (TP1-->TP2-->TP3-->TP4-->...)
   **Voraussetzung**: Keine Interdependenzen zwischen Teilplänen (Abhängigkeit maximal eine Richtung)
   **Problem**: Konkurrenz um gemeinsam genutzte Ressourcen
2. **Simultane Planung** (Alle werden gleichzeitig geplant)
   Beste Lösung, sollten Interdependenzen vorliegen, keine Problem bei Ressourcenkonkurrenz
   **Problem**: erhöhte Planungskosten
3. **Planung mittels Szenariotechnik**
   **Einordnung** in average-/, worst-/, best-case und entsprechende **Einschätzungen** künftiger Entwicklungen (Im "Idealfall" für gesamtes Unternehmen und Umfeld) 
   Möglich auch: Zuordnung zu Eintrittswahrscheinlichkeiten und Ausprägungen


# Prognosemethoden
## Zeitreihenanalyse
Idee: Fortschreibung eines Trends, auch mit mehreren Faktorne möglich

## Stichprobenanalyse
Idee: Hochrechnungen von Beobachtungen
Daraus resultierende Frage: gewichteter oder einfacher Durchschnitt oder Durchschnittsrendite eines Unternehmens oder des gesamt eingesetzen Branchenkapitals

## Weitere.
**Delphi Methode**: 1. Meinung wird abgegeben 2. Meinungsgeber wird mit Gruppenmeinungen konfrontiert 3. weitere Meinungsabgebung
**(Kunden)Befragungen**
**(Kunden)Beobachtungen**


# Herausforderungen bei Planungsproblemen
**Daten und Umfeld**
- **Unsicherheit der Daten**: Prognoseproblem
- **Abhängigkeiten**: z. B. Just-in-time-Fertigung
- **Wechselwirkungen**: z. B. Absatzverbund
- **Dynamische Unternehmenswelt**: z. B. sich ändernde Kundenwünsche
- **Ungenaue Prognoseverfahren**: Fehler 1. und 2. Art

**Defekte**
- **Zielsetzungsdefekte**: z. B. hoher Gewinn vs. niedriges Risiko
- **Wirkungsdefekte**: z. B. fehlende Daten
- **Bewertungsdefekte**: z. B. mangelnde Datenqualität, falsche Anreize
- **Lösungsdefekte**: z. B. Travelling-Salesman-Problem

## Fehler 1. und 2. Art
**Nullhypothese** ${}H_{0}{}$: Ausgangshypothese, z. B. *Proband ist nicht infiziert*

|                                    | **${}H_{0}{}$ richtig** (wahrer Zustand) | **${}H_{0}{}$ falsch** (wahrer Zustand) |
| ---------------------------------- | ---------------------------------------- | --------------------------------------- |
| **Prognose: ${}H_{0}{}$ gilt**         | richtige Entscheidung                    | **Fehler 2. Art**                       |
| **Prognose: ${}H_{0}{}$ abgelehnt**    | **Fehler 1. Art**                        | richtige Entscheidung                   |

- **Fehler 1. Art**: ${}H_{0}{}$ wird abgelehnt, obwohl sie stimmt → *gesund, aber als infiziert gemeldet* (**falsch positiv**)
- **Fehler 2. Art**: ${}H_{0}{}$ wird beibehalten, obwohl sie falsch ist → *infiziert, aber als gesund gemeldet* (**falsch negativ**)

**Beispiel**: HIV-Test, 99,5 % richtig (in beide Richtungen), 1.000.000 Getestete
- **0 Infizierte** → ca. **5.000** fälschlicherweise als infiziert gemeldet (Fehler 1. Art)
- **200 Infizierte** → ca. **1** fälschlicherweise als nicht infiziert gemeldet (Fehler 2. Art) + weiterhin ca. 5.000 falsch positiv