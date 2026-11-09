Teil von Grundlagen der Makroökonomik

# Formelsammlung Makro

Aufbau je Kapitel: **Symbole** → **Formeln** → ggf. Vergleiche

---

## 1 Grundbegriffe ([[01 Wintersemester 2026/Grundlagen der Makroökonomik/01 Untersuchungsgegenstand der Makroökonomik|Kap. 01]])

### Symbole Grundbegriffe

| Symbol | Bedeutung |
| --- | --- |
| $L$ | Erwerbspersonen |
| $N$ | Erwerbstätige |
| $U$ | Arbeitslose |
| $u$ | Arbeitslosenquote |

### Formeln Grundbegriffe

| Größe | Formel | Hinweis |
| --- | --- | --- |
| Erwerbspersonen | $L = N + U$ | |
| Arbeitslosenquote | $u = \frac{U}{L}$ | Arbeitslose / Erwerbspersonen |
| 70er-Regel | $\text{Verdopplungszeit} \approx \frac{70}{\text{Wachstumsrate in \%}}$ | z. B. 2 % → ca. 35 Jahre |

---

## 2 Einkommenskonzepte ([[01 Wintersemester 2026/Grundlagen der Makroökonomik/02 Grundzüge der Inlandsproduktion|Kap. 02]])

### Symbole Einkommenskonzepte

| Symbol | Bedeutung |
| --- | --- |
| BIP / NIP | Brutto-/Nettoinlandsprodukt |
| BWS | Bruttowertschöpfung |
| BNE / NNE | Brutto-/Nettonationaleinkommen |
| VE | Volkseinkommen |
| $C$ | Konsum der Haushalte |
| $I$ | Bruttoinvestitionen |
| $G$ | Staatsausgaben |
| $X - IM$ | Exporte − Importe |

### Formeln Einkommenskonzepte

| Größe | Berechnung |
| --- | --- |
| **BIP** | Produktionswert im Inland − Vorleistungen |
| **NIP** | BIP − Abschreibungen |
| **BWS** | BIP − Gütersteuern + Gütersubventionen |
| **BNE** | BIP + Saldo der Primäreinkommen aus der übrigen Welt |
| **NNE** | BNE − Abschreibungen |
| **Volkseinkommen (VE)** | NNE − Produktions- und Importabgaben + Subventionen |
| | = Arbeitnehmerentgelte + Unternehmens- und Vermögenseinkommen |
| **Verfügb. Einkommen der Inländer** | NNE + Saldo der Sekundäreinkommen |
| **Verfügb. Einkommen der priv. HH** | VE − direkte Steuern − Sozialbeiträge + Transfers |

**Verwendungsrechnung:** $\text{BIP} = C + I + G + (X - IM)$

**Bruttoinvestitionen** = Ausrüstungen + Bauten + sonstige Anlagen (= Bruttoanlageinvestitionen) + Vorratsveränderungen

---

## 3 Nominales vs. reales BIP ([[01 Wintersemester 2026/Grundlagen der Makroökonomik/02 Grundzüge der Inlandsproduktion|Kap. 02]])

### Symbole BIP real und nominal

| Symbol | Bedeutung |
| --- | --- |
| $BIP_t$ | nominales BIP |
| $Y_t$ | reales BIP |
| $P_t$ | BIP-Deflator ($P_0 = 1$) |
| $X_t$ | Menge |
| $g_{x,t}$ | Wachstumsrate von $x$ |
| $\pi_t$ | Inflationsrate |

### Formeln BIP real und nominal

| Größe | Formel | Bedeutung |
| --- | --- | --- |
| Nominales BIP | $BIP_t = P_t \cdot Y_t$ | zu **aktuellen** Preisen |
| Reales BIP | $Y_t = P_{0} \cdot X_t$ | zu Preisen des **Basisjahres** |
| BIP-Deflator | $P_t = \frac{BIP_t}{Y_t}$ | Preisniveau der Produktion |
| Basisjahr | $BIP_0 = Y_0$, $P_0 = 1$ | |

| Wachstumsrate | Formel |
| --- | --- |
| nominales BIP | $g_{BIP,t} = \frac{BIP_t - BIP_{t-1}}{BIP_{t-1}}$ |
| reales BIP | $g_{Y,t} = \frac{Y_t - Y_{t-1}}{Y_{t-1}}$ |
| Inflation (BIP-Deflator) | $\pi_t = \frac{P_t - P_{t-1}}{P_{t-1}}$ |

**Zusammenhang:**
$$
g_{BIP,t} = \pi_t + g_{Y,t} + \pi_t \cdot g_{Y,t} \;\approx\; \pi_t + g_{Y,t}
$$
→ nominales Wachstum ≈ Inflation + reales Wachstum (für kleine Werte)

### Vergleich BIP-Deflator vs. VPI

| | BIP-Deflator | VPI |
| --- | --- | --- |
| misst Preise der | Produktion | Konsumgüter |
| Gewichte | aktuelle Periode (Paasche) | Basisperiode (Laspeyres) |
| Importe | nicht enthalten | enthalten |

---

## 4 Gütermarkt ([[01 Wintersemester 2026/Grundlagen der Makroökonomik/03 Gütermarkt|Kap. 03]])

**Annahmen:** geschlossene VW ($X = IM = 0$), keine Abschreibungen, keine indirekten Steuern/Subventionen → BIP = BNE = NIP = NNE = VE = $Y$

### Symbole Gütermarkt

| Symbol | Bedeutung |
| --- | --- |
| $Y$ | Produktion = Einkommen |
| $Z$ | Güternachfrage |
| $C$ | Konsum |
| $\bar I$ | Investitionen (exogen) |
| $G$ | Staatsausgaben |
| $T$ | Nettosteuern |
| $t$ | Steuersatz ($0 < t < 1$) |
| $Y_V$ | verfügbares Einkommen |
| $S$ | Ersparnis |
| $c_0$ | autonomer Konsum ($c_0 > 0$) |
| $c_1$ | marginale Konsumneigung ($0 < c_1 < 1$) |
| $1 - c_1$ | marginale Sparneigung ($0 < 1 - c_1 < 1$) |
| $\frac{1}{1 - c_1}$ | Multiplikator |
| $Y_N$ | natürliches Produktionsniveau |
| $dX$ | Änderung von $X$ |
| $\frac{\partial Y}{\partial G}$ | partielle Ableitung |
| $\left.\frac{dY}{dG}\right\|_{dT=0}$ | unter der Bedingung $dT = 0$ |

### Gleichungen

| Typ | Gleichung | Bedeutung |
| --- | --- | --- |
| Identität (gilt immer) | $Z \equiv C + I + G$ | Güternachfrage |
| Identität (gilt immer) | $Y_V \equiv Y - T$ | verfügbares Einkommen |
| Identität (gilt immer) | $S \equiv Y_V - C$ | private Ersparnis |
| Verhaltensgleichung (Annahme) | $C = c_0 + c_1 Y_V$ | Konsumfunktion |
| Gleichgewicht (Annahme) | $Y = Z$ | Produktion = Nachfrage (kurze Frist) |

→ Sparfunktion $S = -c_0 + (1-c_1)(Y-T)$ folgt aus Identität + Konsumfunktion (ohne $Y = Z$)
→ $\bar I = S + (T-G)$ und die Höhe von $Y$, $S$ folgen erst aus $Y = Z$

### Gleichgewicht

$$
Y = c_0 + c_1(Y - T) + \bar I + G
$$

$$
\boxed{\,Y = \underbrace{\frac{1}{1 - c_1}}_{\text{Multiplikator}} \cdot \underbrace{[c_0 + \bar I + G - c_1 T]}_{\text{autonome Ausgaben}}\,}
$$

**Als Gerade ($mx + b$):**
$$
Z = \underbrace{[c_0 + \bar I + G - c_1 T]}_{b} + \underbrace{c_1}_{m} \cdot Y
$$
Gleichgewicht = Schnittpunkt mit der 45°-Linie ($Y = Z$). Änderung autonomer Ausgaben → Parallelverschiebung um $\Delta b$.

### Multiplikatoreffekte

| Änderung | Wirkung auf $Y$ | Beispiel $c_1 = 0{,}8$ |
| --- | --- | --- |
| $dG$, $d\bar I$, $dc_0$ | $dY = \frac{1}{1 - c_1} \cdot d(\dots)$ | +1 → $Y$ **+5** |
| $dT$ | $dY = -\frac{c_1}{1 - c_1} \cdot dT$ | Steuer −1 → $Y$ **+4** |

### Totales Differential & Finanzierung

$$
dY = \frac{\partial Y}{\partial G}\,dG + \frac{\partial Y}{\partial T}\,dT = \frac{1}{1 - c_1}\,dG - \frac{c_1}{1 - c_1}\,dT
$$

| Finanzierung | Bedingung | Multiplikator $\frac{dY}{dG}$ | $c_1 = 0{,}8$, $dG = 1000$ |
| --- | --- | --- | --- |
| Kreditfinanziert | $dT = 0$ | $\frac{1}{1 - c_1}$ | $dY = 5000$ |
| Steuerfinanziert | $dG = dT$ | $\frac{1}{1-c_1} - \frac{c_1}{1-c_1} = 1$ | $dY = 1000$ |

**Haavelmo-Theorem:** Steuerfinanzierter Multiplikator $= 1$ → $dY = dG$
- Klammer-Sicht: $dY = c_1\,\underbrace{(dY - dT)}_{dY_V = 0} + dG$ → kein Zusatzkonsum
- Anstoß-Sicht: $dG - c_1\,dT = 1000 - 800 = 200$, mal 5 → $1000$

Wegen $0 < c_1 < 1$: kreditfinanziert wirkt **stärker** als steuerfinanziert.

### Einkommensabhängige Steuern ($T = tY$)

$$
\boxed{\,Y = \frac{1}{1 - c_1(1 - t)} \cdot [c_0 + \bar I + G]\,}
$$

| | $T$ fest | $T = tY$ |
| --- | --- | --- |
| Multiplikator | $\frac{1}{1 - c_1}$ | $\frac{1}{1 - c_1(1 - t)}$ (kleiner) |
| Beispiel $c_1 = 0{,}8$, $t = 0{,}25$ | 5 | 2,5 |

→ **Automatischer Stabilisator:** Schwankungen der autonomen Nachfrage wirken schwächer auf $Y$ (aber auch $dG$ wirkt schwächer).

### Investition = Ersparnis

| Größe | Formel |
| --- | --- |
| private Ersparnis | $S \equiv Y_V - C = Y - T - C$ |
| Sparfunktion | $S = -c_0 + (1 - c_1)(Y - T)$ |
| staatliche Ersparnis | $T - G$ ($> 0$ Überschuss, $< 0$ Defizit) |
| Gleichgewicht | $\bar I = S + (T - G)$ |

→ liefert dieselbe Lösung wie $Y = Z$; Multiplikator $= \frac{1}{\text{marg. Sparneigung}}$

**Sparparadoxon** ($dc_0 < 0$, $d\bar I = dG = dT = 0$):

| Weg | Rechnung | Ergebnis |
| --- | --- | --- |
| A (wie) | $dY = \frac{1}{1-c_1}dc_0$, dann $dS = -dc_0 + (1-c_1)dY$ | $dY < 0$, $dS = 0$ |
| B (dass) | $\bar I = S + (T-G)$ mit $\bar I, T, G$ fest | $dS = 0$ |

→ alle wollen mehr sparen, $S$ bleibt gleich, $Y$ sinkt
