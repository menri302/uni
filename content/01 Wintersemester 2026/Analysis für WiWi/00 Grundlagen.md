# Zusammenfassung 0 · Grundlagen

> [!info] Quelle
> Folien 34–141 aus `Folien/anawiwihandout1x1.pdf` (Abschnitt 1.2 Grundlagen, Vorlesung 16.10.26). Stichpunkte, keine Originalformulierung.

---

## Mengen

- Menge: Sammlung unterscheidbarer Objekte.
- Darstellung: aufzählend $\{1, 7, 19\}$ oder beschreibend $\{x \in \mathbb{R} : x \geq 4,\ x \leq 18\}$.
- Element: $x \in A$.
- Teilmenge: $A \subseteq B$ bedeutet $\forall x: x \in A \Rightarrow x \in B$.
- Vereinigung $A \cup B$, Schnitt $A \cap B$.
- Differenz $A \setminus B = A \cap B^c = \{x : x \in A,\ x \notin B\}$. $B^c$ ist bezüglich einer vorgegebenen Grundmenge gebildet.

## Zahlbereiche und Intervalle

- Inklusionen: $\mathbb{N}_0 \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$.
- $\mathbb{N} = \{1, 2, 3, \dots\}$, $\mathbb{N}_0 = \{0, 1, 2, \dots\}$.
- $\mathbb{Q} = \{\tfrac{p}{q} : p \in \mathbb{Z},\ q \in \mathbb{N}\}$. Rationale Zahlen sind nicht abbrechende periodische Dezimalzahlen.
- $\mathbb{R}$ ist die Erweiterung von $\mathbb{Q}$ um die irrationalen Zahlen.
- Intervalle: $[a;b] = \{x : a \le x \le b\}$, $]a;b[ = \{x : a < x < b\}$, halboffen $[a;b[$ und $]a;b]$.
- Uneigentlich: $[a;\infty[$, $]-\infty;b]$, $]a;\infty[$, $]-\infty;b[$, $]-\infty;\infty[ = \mathbb{R}$.

## Variablen und Definitionsbereich

- Variable: Platzhalter für Elemente einer Menge $M$. Jedes Auftreten derselben Variable bekommt denselben Wert.
- Definitionsbereich: Menge der zulässigen Werte. Er wird eingeschränkt durch mathematische Gründe (Division durch Null, Wurzel aus negativer Zahl) oder durch den Kontext.

## Aussagen und Aussageformen

- Aussage: logischer Ausdruck mit Wahrheitswert wahr oder falsch.
- Aussageform wird durch Belegung der Variablen zur Aussage.
- Allgemeingültig: wahr für jede Belegung.
- Erfüllbar: es gibt eine wahre Belegung. Synonym: lösbar.
- Widerlegbar: es gibt eine falsche Belegung.
- Unerfüllbar: falsch für jede Belegung. Synonym: unlösbar.
- Die Eigenschaften hängen vom Definitionsbereich ab. $3 = 4 + x^2$ ist in $\mathbb{R}$ unerfüllbar, in $\mathbb{C}$ erfüllbar.
- Quantoren $\forall$ und $\exists$ binden Variablen. Die Reihenfolge ist wesentlich: von links nach rechts lesen.

## Terme und Termumformungen

- Term: Ausdruck aus Zahlen, Variablen und Operationen. Vorrangregeln und Klammern.
- Termumformung: $T_1 \to T_2$, so dass für alle Belegungen eine wahre Aussage entsteht.
- Erlaubte Umformungen:
  - Vertauschung und Klammersetzung (Assoziativ- und Kommutativgesetz).
  - Distributivgesetz $T_1(T_2+T_3) = T_1T_2 + T_1T_3$, in umgekehrter Richtung Faktorisieren (Ausklammern).
  - Brüche: $\tfrac{T_1}{T_2} \pm \tfrac{T_3}{T_4} = \tfrac{T_1T_4 \pm T_2T_3}{T_2T_4}$.
  - Minus: $T_1 \pm T_2 = T_1 \mp (-T_2)$.
  - „Fette Null“ (Teleskopsumme): $T_1 = T_1 + T_2 - T_2$.
- Abschätzungen:
  - Addition von $T_2 \geq 0$: $T_1 \le T_1 + T_2$.
  - Multiplikation von $T_1 \geq 0$ mit $T_2 \geq 1$: $T_1 \le T_1 T_2$.

## Gleichungen und Ungleichungen

- Gleichung: Aussage oder Aussageform $T_1 = T_2$. Ungleichung analog mit $\le, <, \ge, >$.
- Gleichung und Umformung unterscheiden: $5 \Leftrightarrow 3+2$ ist keine Aussage, $5 = 3+2$ schon.
- Lösungsmenge bleibt bei Äquivalenzumformungen unverändert.
- Äquivalenzumformungen von Gleichungen:
  - Vertauschung der Seiten.
  - Addition von $T_3$ auf beiden Seiten.
  - Transitivität.
  - Multiplikation mit $T_3 \neq 0$.
  - Ohne $T_3 \neq 0$ gilt nur eine Implikation. Die Lösungsmenge kann sich vergrößern.
- Äquivalenzumformungen von Ungleichungen:
  - Vertauschung der Seiten (dreht Zeichen).
  - Addition von $T_3$ auf beiden Seiten.
  - Multiplikation mit $-1$ (dreht Zeichen).
  - Multiplikation mit $T_3 > 0$.
- Ziel: Variable freistellen.

## Gleichungssysteme

- Gesucht ist eine Belegung, die alle Gleichungen gleichzeitig wahr macht.
- Drei Verfahren zur Variablenelimination:
  - Einsetzungsverfahren: eine Gleichung nach einer Variablen auflösen und einsetzen.
  - Gleichsetzungsverfahren: beide Gleichungen nach derselben Variablen auflösen und gleichsetzen.
  - Additionsverfahren: Vielfache der Gleichungen addieren, sodass eine Variable verschwindet.
- Beispiel aus der Vorlesung: $2x + y = 4$ und $x^2 + 3y = 3$ führen über Einsetzen auf $x^2 - 6x + 9 = 0$, also $(x-3)^2 = 0$ mit $x = 3$ und $y = -2$.
- Darstellung der Umformungen:
  - Alle Gleichungen fortführen: übersichtlich, nur Äquivalenzumformungen, aber schreibaufwändig.
  - Nur veränderte Gleichungen notieren: weniger Schreibaufwand, flexibel, aber unübersichtlich. Dann Rücksubstitution nötig.
- Probe: gefundene Lösung im Ausgangssystem einsetzen.
