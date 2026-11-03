# Produktionsfunktion

> [!NOTE] Produktionsfunktion
> Beschreibt die Beziehung zwischen **Faktoreinsatzmengen** und **maximaler Ausbringungsmenge**.
> $$x = \varphi(r_1, r_2, \dots, r_n)$$

$r_i$ = Einsatzmenge von Faktor $i$ (Input), $x$ = Ausbringungsmenge (Output)
Betrachtet wird **1 Produkt** bei mehreren Faktoren

**Beispiel Cobb-Douglas**: $x = \alpha_0 \cdot r_1^{\alpha_1} \cdot r_2^{\alpha_2} \cdots r_n^{\alpha_n}$ mit $\alpha_0 > 0$, $0 < \alpha_i < 1$
--> VL-Beispiel Straßenbau: $x = r_1^{1/2} \cdot r_2^{1/2} = \sqrt{r_1 \cdot r_2}$

---

# Isoquanten

> [!NOTE] Isoquante
> Alle Faktorkombinationen $(r_1, r_2)$, mit denen eine **gegebene Ausbringungsmenge** $x$ **technisch effizient** („ohne Verschwendung“) hergestellt werden kann.
> $$\varphi(r_1, r_2) = x$$

**Koordinatensystem lesen**
- Achsen = **Inputs** ($r_1$, $r_2$) --> jeder Punkt = eine Faktorkombination
- Output $x$ steht **nicht auf einer Achse**, sondern ist die „Höhe“ --> Isoquante = **Höhenlinie des Produktionsgebirges**
- weiter vom Ursprung weg = **höhere Isoquante** (mehr Output)
- Form hängt nur von der **Technik** des Produktionsprozesses ab

## Isoquantentypen

|                    | **Typ 1: Limitationalität**                                                                                                                   | **Typ 2: „perfekte“ Substitutionalität**                                            | **Typ 3: „allgemeine“ Produktionsfunktion** (z.B. Cobb-Douglas)                                                                       |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Bild**           | ![[BWL Isoquanten Typ 1.svg\|210]]                                                                                                            | ![[BWL Isoquanten Typ 2.svg\|210]]                                                  | ![[BWL Isoquanten Typ 3.svg\|210]]                                                                                                    |
| **Faktoren**       | **festes Verhältnis** (z.B. 1 Maschine = 1 h Arbeit + 1 Satz Einzelteile)                                                                     | **vollständig austauschbar** zu **konstanter Rate** (z.B. 1 h Jäten = 1 l Herbizid) | **teilweise** austauschbar, mit **abnehmender Ersatzwirkung**                                                                         |
| **Form**           | **L-förmig**: mehr von nur einem Faktor bringt **keinen** zusätzlichen Output --> der **knappste Faktor limitiert**                           | **Geraden**: Ersatzbedarf ist immer gleich, egal wie viel man schon hat             | **konvex** (zum Ursprung gewölbt): je extremer die Mischung, desto mehr vom reichlichen Faktor braucht man als Ersatz für den knappen |
| **Besonderheiten** | technisch effizient ist **nur der Eckpunkt** (Äste = Verschwendung)<br>Eckpunkte auf **Strahl aus dem Ursprung** (= festes Einsatzverhältnis) | **ein Faktor allein** möglich (Geraden schneiden die Achsen)                        | Achsen werden **nie berührt** --> beide Faktoren nötig<br>unendlich viele effiziente Mischungen auf einer Isoquante                   |

---

# Kosten

> [!NOTE] Kosten
> **Wert aller** für die Erstellung der **betrieblichen Leistungen verbrauchten Güter und Dienstleistungen**.

- **Mengengerüst**: Verzehr von Gütern/DL bzw. Einsatz von Produktionsfaktoren
- **Bewertung**: nötig, um Faktoreinsatzmengen **vergleichbar** zu machen
- **Bezug zur betrieblichen Leistung**: nur Faktoreinsatz für **produktive Zwecke** führt zu Kosten (vgl. Kap. 9)

## Kostengerade

> [!NOTE] Kostengerade
> Alle Faktorkombinationen mit **gleichen Kosten** $K$.
> $$q_1 r_1 + q_2 r_2 = K \quad\Leftrightarrow\quad r_2 = \frac{K}{q_2} - \frac{q_1}{q_2} \cdot r_1$$

$q_i$ = Preis von Faktor $i$
- **Steigung** $-\frac{q_1}{q_2}$ = **Preisverhältnis**; Achsenabschnitte $\frac{K}{q_2}$ bzw. $\frac{K}{q_1}$
- $K$ höher --> **parallel nach außen**
- Bsp. Straßenbau: 1 h Arbeit = 50 €, 100 kWh = 20 € --> **1 Arbeitsstunde kostet so viel wie 250 kWh**

---

# Minimalkostenkombination

> [!NOTE] Minimalkostenkombination (MKK)
> Faktorkombination $(r_1, r_2)$, mit der eine **vorgegebene Ausbringungsmenge** $x$ zu **minimalen Kosten** hergestellt wird.
> Zu jedem $x$ gibt es (mind.) eine MKK --> Minimalkosten $K = K(x)$

> [!NOTE] Kostenfunktion
> $K(x)$ ordnet jeder Ausbringungsmenge $x$ ihre **Minimalkosten** zu.

## Grafisch

![[BWL Minimalkostenkombination.svg|580]]

| Linie                       | Formel                                              | fest              | bestimmt durch          |
| --------------------------- | --------------------------------------------------- | ----------------- | ----------------------- |
| **Schwarz**: Isoquante      | $\sqrt{r_1 r_2} = 3 \Leftrightarrow r_2 = 9 / r_1$  | **Output** $x=3$  | **Technik** (PF)        |
| **Blau/Rot**: Kostengeraden | $q_1 r_1 + q_2 r_2 = K$                             | **Kosten** $K$    | **Preise** $q_1, q_2$   |

## Rechnerisch

> [!example] Straßenbau: $q_1 = 50$ €/h, $q_2 = 20$ €/100 kWh, $x = \sqrt{r_1 r_2}$
> 1. **Ziel**: $f(r_1, r_2) = q_1 r_1 + q_2 r_2$ --> min, **Nebenbedingung**: $x = \sqrt{r_1 r_2}$
> 2. NB nach $r_2$: $x^2 = r_1 r_2$ --> $r_2 = \frac{x^2}{r_1}$
> 3. **Einsetzen**: $g(r_1) = q_1 r_1 + q_2 \cdot \frac{x^2}{r_1}$
> 4. **Ableiten = 0**: $g'(r_1) = q_1 - q_2 \cdot \frac{x^2}{r_1^2} = 0$ (2. Ableitung nicht nötig)
> 5. **MKK**: $r_1 = \sqrt{\frac{q_2}{q_1}} \cdot x$, $\quad r_2 = \frac{x^2}{r_1} = \sqrt{\frac{q_1}{q_2}} \cdot x$
> 6. **Kostenfunktion**: $K(x) = q_1 r_1 + q_2 r_2 = 2\sqrt{q_1 q_2} \cdot x$
>
> **Zahlen**: $r_1 \approx 0{,}63x$, $r_2 \approx 1{,}58x$, $K(x) \approx 63{,}25x$ --> für $x = 3$: $r_1 \approx 1{,}90$, $r_2 \approx 4{,}74$, $K \approx 190$ €

---

# Variation der Lohnkosten

## Drehung der Kostengeraden

![[BWL Lohnsenkung Drehung.svg|650]]

## Änderung der Faktornachfrage

![[BWL Lohnsenkung Faktornachfrage.svg|640]]

Lohn $q_1$ sinkt --> zwei Vergleichssituationen:

| Situation                  | was passiert                                                                                       | Arbeit                                    |
| -------------------------- | -------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| **gleicher Output** (A --> B) | bleibt auf $x_0$, flachere Kostengerade berührt weiter rechts                                     | **steigt sicher** (nur Preiseffekt)       |
| **gleiche Gesamtkosten** (rot) | gleiches Budget reicht für **höhere Isoquante**; wo sie die Gerade berührt, hängt von der Technik ab | **unklar**: Fall 1 ↓, Fall 2 ↑            |

- **Fall 1 / Fall 2** = **zwei verschiedene Techniken** (nicht zwei Isoquanten derselben Firma) --> bei **einer** Technik gibt es genau **einen** Berührpunkt
- Bögen nur **Ausschnitte**, weil die Form der höheren Isoquante unbekannt ist

> [!important] Effekte und Folgerungen der Faktorpreissenkung (Arbeit)
> **Effekte**
> - **Preiseffekt**: Arbeit wird **relativ** billiger --> mehr Arbeit, weniger Energie
> - **Einkommenseffekt**: Produktion wird **insgesamt** billiger --> mehr Output möglich
>
> **Folgerungen**
> - bei **gleichem Output**: Arbeitseinsatz **steigt** (nur Preiseffekt)
> - bei **konstanten Kosten**: bei **Mengenvariation** ist die **Gesamtwirkung unklar**
>   - Mengenvariation = gleiches Budget reicht für **mehr Output**
>   - Gesamtwirkung = Preis- **und** Einkommenseffekt zusammen --> ob mehr oder weniger Arbeit, hängt von der Technik ab (Fall 1 / Fall 2)

- --> Lohnsenkung schafft **nicht automatisch** mehr Arbeitsplätze (umgekehrt: Mindestlohn --> Rationalisierung bei gleichem Output)

## Rationalisierungsinvestitionen

Gegenstück: **Lohn steigt** (z.B. Mindestlohn) --> Kostengerade **steiler** --> MKK wandert auf $x_0$ **nach links oben** --> Arbeit wird durch **Kapital** (Maschinen) ersetzt

![[BWL Rationalisierung.svg|600]]

| Aspekt                      | Bewertung                                                                                                     |
| --------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **ökonomisch**              | **sinnvoll** bei Ersatz höherer Arbeitskosten durch niedrigere Kapitalkosten (= neue MKK)                     |
| **moralisch**               | evtl. **angreifbar** (Wegfall von Arbeitsplätzen)                                                             |
| **volkswirtschaftlich**     | **nicht eindeutig** (externe Effekte: z.B. Arbeitslosengeld, Steuerausfall vs. Jobs bei Maschinenherstellern) |
| **betriebswirtschaftlich**  | evtl. **problematisch** wegen **Imagewirkungen** bei Kunden, Arbeitnehmern, …                                 |
| **öffentliche Unternehmen** | **besonderer Konflikt**: Wirtschaftlichkeit vs. öffentlicher Auftrag (Gemeinwohl, Beschäftigung)              |

--> rechnerisch optimale MKK ist **nur ein Teil** der Entscheidung

---

# Fixe und variable Kosten

> [!NOTE] Fixe und variable Kosten
> **Fixkosten** $K_f$: **mengenunabhängige** Kosten (fallen auch bei $x = 0$ an)
> **Variable Kosten** $K_v(x)$: **mengenabhängige** Kosten (wachsen mit $x$)
> $$K(x) = K_f(x) + K_v(x) = \overline{K}_F + K_v(x)$$

$\overline{K}_F$: Strich = **Konstante** --> hängt nicht von $x$ ab

![[BWL Fixe und variable Kosten.svg|680]]

---

# Grenz- und Durchschnittskosten

|                | **Durchschnittskosten**                         | **Grenzkosten**                                |
| -------------- | ----------------------------------------------- | ---------------------------------------------- |
| **formal**     | $DK(x) = \frac{K(x)}{x}$                        | $GK(x) = K'(x)$                                |
| **Bedeutung**  | Kosten **pro Stück** im Schnitt                 | Kosten des **nächsten** Stücks                 |
| **relevant für** | Beurteilung der **Wirtschaftlichkeit insgesamt** | Entscheidungen über **Mengenvariation**      |
| **grafisch**   | Steigung des **Fahrstrahls** vom Ursprung zu $(x \mid K(x))$ | Steigung der **Tangente** in $x$   |

![[BWL Grenz- und Durchschnittskosten.svg|760]]

- Fahrstrahl startet im **Ursprung**, nicht auf der Kurve --> 2. Schnittpunkt mit $K(x)$ ist **Zufall**
- Sekante zwischen zwei Kurvenpunkten = Differenzenquotient --> für $t \to 0$ **Grenzkosten** 
- im Bild: Tangente steiler als Fahrstrahl --> $GK > DK$ --> DK **steigen**


