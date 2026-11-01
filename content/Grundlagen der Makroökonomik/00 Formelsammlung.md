Teil von [[Grundlagen der Makroökonomik]]

# Formelsammlung Makro

---

## 1 Grundbegriffe ([[01 Untersuchungsgegenstand der Makroökonomik|Kap. 01]])

| Größe | Formel | Hinweis |
| --- | --- | --- |
| Erwerbspersonen | $L = N + U$ | $N$ = Erwerbstätige, $U$ = Erwerbs-/Arbeitslose |
| Arbeitslosenquote | $u = \frac{U}{L}$ | Arbeitslose / Erwerbspersonen |
| 70er-Regel | $\text{Verdopplungszeit} \approx \frac{70}{\text{Wachstumsrate in \%}}$ | z. B. 2 % → ca. 35 Jahre |

---

## 2 Einkommenskonzepte ([[02 Grundzüge der Inlandsproduktion|Kap. 02]])

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

## 3 Nominales vs. reales BIP ([[02 Grundzüge der Inlandsproduktion|Kap. 02]])

| Größe | Formel | Bedeutung |
| --- | --- | --- |
| Nominales BIP | $BIP_t = P_t \cdot Y_t$ | zu **aktuellen** Preisen |
| Reales BIP | $Y_t = P_{0} \cdot X_t$ | zu Preisen des **Basisjahres** |
| BIP-Deflator | $P_t = \frac{BIP_t}{Y_t}$ | Preisniveau der Produktion |
| Basisjahr | $BIP_0 = Y_0$, $P_0 = 1$ | |

**Wachstumsraten** (allgemein: $g_{x,t} = \frac{x_t - x_{t-1}}{x_{t-1}}$)

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

**BIP-Deflator vs. VPI**

| | BIP-Deflator | VPI |
| --- | --- | --- |
| misst Preise der | Produktion | Konsumgüter |
| Gewichte | aktuelle Periode (Paasche) | Basisperiode (Laspeyres) |
| Importe | nicht enthalten | enthalten |

---

## 4 Gütermarkt ([[03 Gütermarkt|Kap. 03]])

**Annahmen:** geschlossene VW ($X = IM = 0$), keine Abschreibungen, keine indirekten Steuern/Subventionen → BIP = BNE = NIP = NNE = VE = $Y$

### Gleichungen

| Typ | Gleichung | Bedeutung |
| --- | --- | --- |
| Identität | $Z \equiv C + I + G$ | Güternachfrage |
| Identität | $Y_V \equiv Y - T$ | verfügbares Einkommen |
| Verhaltensgleichung | $C = c_0 + c_1 Y_V$ | Konsumfunktion |
| Gleichgewicht | $Y = Z$ | Produktion = Nachfrage |

| Symbol | Name | Typ |
| --- | --- | --- |
| $c_0$ | autonomer Konsum ($c_0 > 0$) | Parameter |
| $c_1$ | marginale Konsumneigung ($0 < c_1 < 1$) | Parameter |
| $G, T, \bar I$ | Staatsausgaben, Nettosteuern, Investitionen | exogen |
| $Y$ | Produktion = Einkommen | endogen |

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
| $\Delta G$, $\Delta \bar I$, $\Delta c_0$ | $\Delta Y = \frac{1}{1 - c_1} \cdot \Delta$ | +1 → **+5** |
| $\Delta T$ | $\Delta Y = \frac{-c_1}{1 - c_1} \cdot \Delta T$ | −1 → **+4** |

### Multiplikator in Runden

Jede Runde: $\Delta Y_n = c_1 \cdot \Delta Y_{n-1} = c_1^{\,n-1} \cdot \Delta G$

| Runde | 1 | 2 | 3 | 4 | … | Summe |
| --- | --- | --- | --- | --- | --- | --- |
| $\Delta Y_n$ ($c_1 = 0{,}8$, $\Delta G = 1$) | 1 | 0,8 | 0,64 | 0,512 | → 0 | **5** |

$$
\Delta Y = \Delta G \cdot (1 + c_1 + c_1^2 + \dots) = \frac{1}{1 - c_1} \cdot \Delta G
$$

Pro Runde versickert der Anteil $1 - c_1$ als Ersparnis → am Ende gilt $\Delta S = (1 - c_1)\,\Delta Y = \Delta G$.
