Frage: **Wie werden knapope Ressourcen am besten verwendet?** 
Analyse dieser Frage mittels:
1. **Beschränkungen**: Welche Entscheiodugnen sind möglich?
2. **Präferenzen**: Wie gut sind verschiedene Handlungsalternativen

# Beschränkungen

> [!NOTE] Güterbündel
> Ein Güterbündel ist ein Vektor $x = (x_1, \dots, x_n)$, der für jedes Gut $i$ die Menge $x_i$ angibt
> Zwei Güter: Güterbündel wird mit $(x_1, x_2)$ bezeichnet
> **Beispiel:** Gut 1 ist Brot (in kg), Gut 2 ist Milch (in l). $(x_1, x_2) = (2, 4)$ bedeutet: 2 kg Brot und 4 l Milch

$p_1, p_2$: Preise der Güter 1 und 2 (in Euro)
$m$: Budget des Konsumenten (in Euro)

**$x_1, x_2$** sind **endogen**: werden über das Modell erklärt
**$p_1, p_2, m$** sind **exogen**: von außen vorgegeben


> [!NOTE] **Budgetbeschränkung**
> $p_1 \cdot x_1 + p_2 \cdot x_2 \leq m$ 
> Die Ausgaben des Konsumenten dürfen sein Budget nicht überschreiten


**Budgetmenge:** Alle Güterbündel, die die Budgetbeschränkung erfüllen, also alle Güterbündel, die sich der Konsument leisten kann

### Budgetgerade 
> [!NOTE] Budgetgerade
>Alle Güterbündel $(x_1, x_2)$, die genau $m$ kosten, also für die gilt: $p_1 \cdot x_1 + p_2 \cdot x_2 = m$

Umstellen der Budgetgerade nach $x_2$ ergibt: $x_2 = \frac{m}{p_2} - \frac{p_1}{p_2} \cdot x_1$
Dies beschreibt eine Gerade mit Achsenabschnitt $\frac{m}{p_2}$ und Steigung $\frac{dx_2}{dx_1} = -\frac{p_1}{p_2}$

Alle Güterbündel auf und unterhalb dieser Gerade kosten nicht mehr als $m$ und bezeichnen daher die Budgetmenge.

Im 2-Güter-Fall lassen sich diese Konzepte grafisch in einem $x_2$-$x_1$-Diagramm veranschaulichen.
>![[Pasted image 20261025122940.png|485]]

### Budgetgeraden-Steigung
- Steigung der BG = Verzicht auf Gut 2, um eine weitere Einheit Gut 1 zu erhalten
- **Beispiel:** $p_1 = 10$, $p_2 = 2$, gesamtes Einkommen wird ausgegeben
	$\Rightarrow$ Steigung $= -\frac{p_1}{p_2} = -5$
	HH kauft 1 Einheit Gut 1 mehr $\rightarrow$ gibt 10 Euro zusätzlich aus
	--> $x_2$ muss um 5 Einheiten sinken, damit die Ausgaben für Gut 2 um 10 Euro sinken

> [!NOTE] Interpretation
> Absolutbetrag der Steigung = **Preis** für eine weitere Einheit Gut 1, ausgedrückt in Einheiten Gut 2
> Absolutbetrag der Steigung = **Opportunitätskosten** für eine weitere Einheit Gut 1, ausgedrückt in Einheiten Gut 2


| **Anwendung 1** - D-Ticket                                       | **Anwendung 2 - Zweckgebundene Entwicklungshilfe**                         |
| ---------------------------------------------------------------- | -------------------------------------------------------------------------- |
| ${}x_{2:}{}$: ÖPNV-Kilometer<br>${}x_{1}{}$:  Auto-Kilometer<br> | Haushalt kann Budget ${}B_{0}{}$ für Bildung und E oder Rüstung R ausgeben |
| ![[Pasted image 20261025124004.png\|562]]                        | ![[Pasted image 20261025124803.png\|506]]                                  |

# Präferenzen

**Frage:** Wie bewerten Menschen unterschiedliche Handlungsalternativen und welche Trade-offs sind sie bereit einzugehen?

Präferenzen bilden die Vorlieben eines Entscheidungsträgers ab.

> [!NOTE] Präferenzordnung
> Rangfolge aller Handlungsoptionen (hier: Warenkörbe) in der Reihenfolge ihrer Präferenz

$(x_1^A, x_2^A) \succ (x_1^B, x_2^B)$: Haushalt zieht Güterbündel $A = (x_1^A, x_2^A)$ gegenüber $B = (x_1^B, x_2^B)$ **vor**
$(x_1^A, x_2^A) \sim (x_1^B, x_2^B)$: Haushalt ist **indifferent** zwischen den Güterbündeln $A$ und $B$ (diese sind aus seiner Sicht gleich gut)

## Annahmen an Präferenzen
**Annahme 1: Vollständigkeit:** Der HH kann für jedes beliebige Paar von Güterbündeln entscheiden, welches er besser findet, bzw. ob er indifferent ist.

**Annahme 2: Transitivität:** Für drei Warenkörbe $A$, $B$, $C$ gilt:
- wenn $A \succ B$ und $B \succ C$, dann auch $A \succ C$
- wenn $A \sim B$ und $B \sim C$, dann auch $A \sim C$

**Kommentar:** Ist Transitivität verletzt, sind die Präferenzen zyklisch: $A \succ B$ und $B \succ C$, aber $C \succ A$ impliziert $A \succ B \succ C \succ A \succ B \dots$
Ein bestes Güterbündel ist damit nicht mehr (eindeutig) definiert.

Konsumenten mit nicht-transitiven Präferenzen können auch **ausgebeutet** werden.
Angenommen es gilt: $A \succ B$, $B \succ C$, $C \succ A$, und der Konsument ist bereit, für jeden vorteilhaften Wechsel 1 Euro zu bezahlen.
--> Ein findiger Geschäftsmann lässt den Konsumenten im Kreis von $A$ über $B$ und $C$ zurück zu $A$ wechseln und kassiert jedes Mal 1 Euro

 
> [!NOTE] Rationalität
> Ein Entscheidungsträger heißt **rational**, wenn seine Präferenzen vollständig und transitiv sind.

**Bemerkungen:**
- Rationalität ist also (in den Wirtschaftswissenschaften) eine Anforderung an die **Struktur** von Präferenzen, nicht an deren **Gehalt**.
- Vollständigkeit stellt sicher, dass alle Alternativen vergleichbar sind; Transitivität sorgt für eine konsistente Rangordnung.
- Rationalität bedeutet nicht, egoistisch (oder gierig) zu sein.

Lange Präferenzordnungs-Listen sind unhandlich, deshalb:
1. Grafische Repräsentation: **Indifferenzkurven**
2. mathematische Repräsentation: **Nutzenfunktion**

## Indifferenzkurven
Mit Hilfe von Indifferenzkurven lassen sich Präferenzen graphisch darstellen.


**Beachte:** Güterbündel rechts-oberhalb von $A$ enthalten eine höhere Menge beider Güter und sind wegen Monotonie besser.
Man sagt auch: sie liegen in der **Bessermenge**.

- Vollständigkeit $\Rightarrow$ jedes Güterbündel liegt auf irgendeiner Indifferenzkurve
- Transitivität $\Rightarrow$ Indifferenzkurven können sich nicht schneiden (vgl. Tutorium)


**Annahme (Monotonie oder Nicht-Sättigung):** Mehr-Konsum stellt den Haushalt besser, d.h. für jedes $\epsilon > 0$ gilt:
$(x_1^A + \epsilon, x_2^A) \succ (x_1^A, x_2^A)$ und $(x_1^A, x_2^A + \epsilon) \succ (x_1^A, x_2^A)$

**Konsequenz:**
- Indifferenzkurven verlaufen fallend
- Rechts-oberhalb liegende Güterbündel sind besser

**Grafische Konstruktion:**
1. Starte bei einem Bündel $A$.
2. Erhöhe die Menge von Gut 1 um $\Delta x_1$. Der Konsument ist nun bessergestellt ($\rightarrow$ Monotonie).
3. Verringere die Menge von Gut 2 um $\Delta x_2$, bis der Konsument wieder genau so zufrieden ist wie bei $A \Rightarrow$ Bündel $B$.
4. Die Indifferenzkurve verläuft durch beide Punkte.

![[Konstruktion Indifferenzkurve.png|485]]