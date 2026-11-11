Teil von Einführung in die BWL

# Formelsammlung BWL

Aufbau je Kapitel: **Symbole** → **Formeln** → ggf. Vergleiche

---

## 1 Erfolgskennzahlen ([[01 Wintersemester 2026/Einführung in die BWL/01 Appetithappen|Kap. 01]])

### Symbole Erfolgskennzahlen

| Symbol | Bedeutung |
| --- | --- |
| ME | Mengeneinheiten |
| GE | Geldeinheiten |
| $G$ | Gewinn |
| $EK$ / $GK$ | Eigen-/Gesamtkapital |
| $U$ | Umsatz |
| $r_\Delta$ | Rendite der Differenzinvestition |

### Formeln Erfolgskennzahlen

| Größe | Formel | Hinweis |
| --- | --- | --- |
| Produktivität | $\frac{\text{Output in ME}}{\text{Input in ME}}$ | rein **mengenmäßig** |
| Wirtschaftlichkeit | $\frac{\text{Output in GE}}{\text{Input in GE}}$ | **wertmäßig** |
| Rentabilität (allg.) | $\frac{G}{\text{Bezugsgröße}}$ | |
| Eigenkapitalrentabilität | $\frac{G}{EK}$ | |
| Gesamtkapitalrentabilität | $\frac{G}{GK}$ | |
| Umsatzrentabilität | $\frac{G}{U}$ | |

### Ökonomisches Prinzip

| Maximalprinzip | Minimalprinzip | generelles Extremalprinzip |
| --- | --- | --- |
| Input gegeben → Output **max** | Output gegeben → Input **min** | Input/Output zu einer Größe verdichtet → max/min |

### Differenzinvestition

$$
G_A = G_B + r_\Delta \cdot (\text{Kapital}_A - \text{Kapital}_B)
\quad\Rightarrow\quad
\boxed{\,r_\Delta = \frac{G_A - G_B}{\text{Kapital}_A - \text{Kapital}_B}\,}
$$

| Alternativrendite für die Differenz | Entscheidung |
| --- | --- |
| $< r_\Delta$ | große Investition **A** besser |
| $> r_\Delta$ | kleine Investition **B** besser (Rest anderswo anlegen) |

Beispiel: $A$: 10.000 € zu 40 % → 4.000 € · $B$: 1.000 € zu 150 % → 1.500 € → $r_\Delta = \frac{2.500}{9.000} \approx 28\,\%$

### Liquiditätsnebenbedingung

$$
\text{Kassenanfangsbestand} + \text{Einzahlungen} - \text{Auszahlungen} \geq 0 \quad \text{(zu **jedem** Zeitpunkt)}
$$

→ Liquidität wird **nicht maximiert**, sie ist eine **Bedingung**

---

## 2 Fehler 1. und 2. Art ([[01 Wintersemester 2026/Einführung in die BWL/03 Planung|Kap. 03]])

| | $H_0$ richtig | $H_0$ falsch |
| --- | --- | --- |
| $H_0$ beibehalten | ✓ | **Fehler 2. Art** (falsch negativ) |
| $H_0$ abgelehnt | **Fehler 1. Art** (falsch positiv) | ✓ |

**Erwartete Fehlerzahl** $= \text{Anzahl der betroffenen Fälle} \cdot \text{Fehlerquote}$
Beispiel HIV-Test (99,5 % korrekt, 1 Mio. Getestete, 200 Infizierte): Fehler 1. Art $\approx 999.800 \cdot 0{,}005 \approx 5.000$ · Fehler 2. Art $= 200 \cdot 0{,}005 = 1$

---

## 3 Absatz ([[01 Wintersemester 2026/Einführung in die BWL/04 Absatz|Kap. 04]])

### Symbole Absatz

| Symbol | Bedeutung |
| --- | --- |
| $x_i$ | (alte) Absatzmenge von Produkt $i$ |
| $p_i$ | (alter) Preis von Produkt $i$ |
| $\Delta x_i = x_i^{neu} - x_i$ | Absatzänderung |
| $\Delta p_i = p_i^{neu} - p_i$ | Preisänderung |
| $\eta_i$ | direkte Preiselastizität der Nachfrage |
| $U = p \cdot x$ | Umsatz |
| $P(A \mid B)$ | Wahrscheinlichkeit von $A$ unter der Bedingung $B$ |

### Formeln Absatz

| Größe | Formel | Hinweis |
| --- | --- | --- |
| Preis-Absatz-Funktion | $x = f(p)$ bzw. $p = g(x)$ | Verlauf meist unbekannt |
| Direkte Preiselastizität | $\eta_i = \frac{\Delta x_i / x_i}{\Delta p_i / p_i} \approx \frac{dx_i}{dp_i} \cdot \frac{p_i}{x_i}$ | meist **negativ** |
| Absatzänderung (relativ) | $\frac{\Delta x}{x} \approx \eta \cdot \frac{\Delta p}{p}$ | lineare Näherung |
| Absatzänderung (absolut) | $\Delta x \approx \frac{dx}{dp} \cdot \Delta p$ | Kontrolle |
| Erwartete Käufer | $\text{Reichweite in Zielgruppe} \cdot P(\text{Kauf} \mid \text{Zielgruppe})$ | Medienplanung |

**Ableitungs-Merkregel** (Wurzel-PAF): $\left(\sqrt{u}\right)' = \frac{1}{2\sqrt{u}} \cdot u'$

### Elastizität und Umsatz

| Betrag | Nachfrage | Preis ↑ → Umsatz $p \cdot x$ |
| --- | --- | --- |
| $\lvert\eta\rvert > 1$ | **elastisch** | **sinkt** |
| $\lvert\eta\rvert = 1$ | proportional elastisch | bleibt gleich |
| $\lvert\eta\rvert < 1$ | **unelastisch** | **steigt** |

→ lineare PAF: gleiche Steigung, aber **hoher Preis = elastischer**

**Beispiel:** $x = \sqrt{16 - p}$, $p = 7$ → $x = 3$, $\frac{dx}{dp} = -\frac{1}{6}$, $\eta = -\frac{1}{6} \cdot \frac{7}{3} = -\frac{7}{18} \approx -0{,}39$ (unelastisch) → bei +5 % Preis: $\frac{\Delta x}{x} \approx -1{,}94\,\%$

---

## 4 Produktion und Kosten ([[01 Wintersemester 2026/Einführung in die BWL/05 Produktion|Kap. 05]])

### Symbole Produktion

| Symbol | Bedeutung |
| --- | --- |
| $x$ | Ausbringungsmenge (Output) |
| $r_i$ | Einsatzmenge von Faktor $i$ (Input) |
| $\varphi$ | Produktionsfunktion |
| $\alpha_0, \alpha_i$ | Parameter der Cobb-Douglas-PF ($\alpha_0 > 0$, $0 < \alpha_i < 1$) |
| $q_i$ | Preis von Faktor $i$ |
| $K$ / $K(x)$ | Kosten / (Minimal-)Kostenfunktion |
| $\overline{K}_F$ | Fixkosten (Strich = konstant) |
| $K_v(x)$ | variable Kosten |
| $DK(x)$ | Durchschnittskosten |
| $GK(x)$ | Grenzkosten |

### Formeln Produktion

| Größe | Formel | Bedeutung |
| --- | --- | --- |
| Produktionsfunktion | $x = \varphi(r_1, \dots, r_n)$ | max. Output je Faktorkombination |
| Cobb-Douglas | $x = \alpha_0 \cdot r_1^{\alpha_1} \cdots r_n^{\alpha_n}$ | VL: $x = \sqrt{r_1 r_2}$ |
| Isoquante | $\varphi(r_1, r_2) = x$ | **Output** fest, bestimmt durch **Technik** |
| Kostengerade | $q_1 r_1 + q_2 r_2 = K$ | **Kosten** fest, bestimmt durch **Preise** |
| Kostengerade (aufgelöst) | $r_2 = \frac{K}{q_2} - \frac{q_1}{q_2} \cdot r_1$ | Steigung $-\frac{q_1}{q_2}$, Achsen $\frac{K}{q_2}$ bzw. $\frac{K}{q_1}$ |

### Isoquantentypen

| | Limitationalität | perfekte Substitution | allgemein (Cobb-Douglas) |
| --- | --- | --- | --- |
| Form | L-förmig | Gerade | konvex |
| Faktoren | festes Verhältnis | konstante Austauschrate | teilweise austauschbar |
| effizient | nur Eckpunkt | jeder Punkt, auch ein Faktor allein | jeder Punkt, Achsen nie berührt |

### Minimalkostenkombination (MKK)

**Vorgehen:**
1. Ziel: $q_1 r_1 + q_2 r_2 \to \min$ · Nebenbedingung: $x = \varphi(r_1, r_2)$
2. NB nach $r_2$ auflösen und **einsetzen** → Funktion nur von $r_1$
3. **Ableiten = 0** → $r_1$, dann $r_2$
4. Kostenfunktion: $K(x) = q_1 r_1 + q_2 r_2$

**Lösung für $x = \sqrt{r_1 r_2}$:**
$$
r_1 = \sqrt{\frac{q_2}{q_1}} \cdot x, \qquad r_2 = \sqrt{\frac{q_1}{q_2}} \cdot x, \qquad
\boxed{\,K(x) = 2\sqrt{q_1 q_2} \cdot x\,}
$$

Beispiel Straßenbau ($q_1 = 50$, $q_2 = 20$): $r_1 \approx 0{,}63x$, $r_2 \approx 1{,}58x$, $K(x) \approx 63{,}25x$ → $x = 3$: $K \approx 190$ €

### Faktorpreisänderung (Lohn $q_1$ sinkt)

| Vergleich | Wirkung auf Arbeit $r_1$ | Grund |
| --- | --- | --- |
| gleicher Output | **steigt** sicher | nur Preiseffekt |
| gleiche Kosten | **unklar** | Preis- + Einkommenseffekt, hängt von Technik ab |

→ Lohn ↑ (Mindestlohn): Kostengerade steiler → MKK nach links oben → **Rationalisierung** (Arbeit durch Kapital ersetzt)

### Kostenbegriffe

| Größe | Formel | Bedeutung | grafisch |
| --- | --- | --- | --- |
| Gesamtkosten | $K(x) = \overline{K}_F + K_v(x)$ | fix + variabel | |
| Durchschnittskosten | $DK(x) = \frac{K(x)}{x}$ | Kosten **pro Stück** | Steigung des **Fahrstrahls** vom Ursprung |
| Grenzkosten | $GK(x) = K'(x)$ | Kosten des **nächsten** Stücks | Steigung der **Tangente** |

| Lage | Folge |
| --- | --- |
| $GK > DK$ | $DK$ **steigen** |
| $GK < DK$ | $DK$ **sinken** |

→ $DK$: Wirtschaftlichkeit insgesamt · $GK$: Entscheidungen über **Mengenvariation**

---

## 5 Informationen und Motivation ([[01 Wintersemester 2026/Einführung in die BWL/06 Informationen und Motivation|Kap. 06]])

### Symbole Motivation

| Symbol | Bedeutung |
| --- | --- |
| $U(y, l)$ | Nutzenfunktion |
| $y$ | Einkommen |
| $l$ | Arbeitszeit bzw. Anstrengung |

### Formeln Motivation

| Größe | Formel | Bedeutung |
| --- | --- | --- |
| Nutzen aus Einkommen | $\frac{\partial U}{\partial y} > 0$ | mehr Einkommen ist besser |
| Arbeitsleid (Typ X) | $\frac{\partial U}{\partial l} < 0$ | mehr Anstrengung ist schlechter |
| Folge | $y = y(l)$ | Vergütung muss Arbeitsanreiz setzen |

### Signaling-Bedingung (trennendes Gleichgewicht)

Signal lohnt sich für einen Typ, wenn: $\text{Lohn mit Signal} - \text{Signalkosten} > \text{Lohn ohne Signal}$

| Typ | Rechnung | Studium? |
| --- | --- | --- |
| hohe Produktivität | $150 - 40 = 110 > 100$ | **ja** |
| niedrige Produktivität | $150 - 60 = 90 < 100$ | nein |

→ Signal muss für die „Schlechten“ **zu teuer** sein

---

## 6 Organisation ([[01 Wintersemester 2026/Einführung in die BWL/07 Organisation|Kap. 07]])

### Symbole Organisation

| Symbol | Bedeutung |
| --- | --- |
| $s$ | Leitungsspanne (direkt unterstellte Stellen je Leitungsstelle) |
| $n$ | Anzahl der Hierarchieebenen (Leitungstiefe) |

### Formeln Organisation

| Größe | Formel | Hinweis |
| --- | --- | --- |
| Stellenanzahl gesamt | $1 + s + s^2 + \dots + s^{n-1} = \frac{s^n - 1}{s - 1}$ | geometrische Reihe |
| Ausführungsstellen | $s^{n-1}$ | unterste Ebene |
| Leitungsstellen | $\frac{s^{n-1} - 1}{s - 1}$ | alle Ebenen außer der untersten |
| Leitungsintensität | $\frac{\text{Leitungsstellen}}{\text{Ausführungsstellen}}$ | „Chefs pro Ausführungsstelle“ |

### Vergleich der VL-Beispiele

| | Bsp. 1 ($s = 3$, $n = 4$) | Bsp. 2 ($s = 6$, $n = 3$) |
| --- | --- | --- |
| Stellen | $\frac{3^4 - 1}{2} = 40$ | $\frac{6^3 - 1}{5} = 43$ |
| Leitungsstellen | $1 + 3 + 9 = 13$ | $1 + 6 = 7$ |
| Ausführungsstellen | $27$ | $36$ |
| Leitungsintensität | $\approx 0{,}48$ | $\approx 0{,}19$ |

→ größere Leitungsspanne ⇒ **flachere** Hierarchie und **geringere** Leitungsintensität
