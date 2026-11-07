# Motivation: Why bonds?

Bonds = one of the **main sources of financing** for governments and companies (→ debt financing, see [[01 Wintersemester 2026/Finance und Investment/01 The Corporation and Financial Markets#Financing Options|Financing Options]])

| For … | Advantage |
|---|---|
| **Companies** | raise capital **without** owners **losing control** (unlike stocks) |
| **Investors** | can be **creditors** → **flexible** through exchange trading (sell before maturity) |

---

# Cash Flows, Prices and Yields

## Key terms

| Term | Meaning |
|---|---|
| **Face value** FV (Nennwert) | amount repaid at **maturity** (Fälligkeit); basis for the coupons |
| **Coupon rate** | annual rate set by the issuer, stated as an **APR** |
| **Coupon payment** CPN | interest payment per period (formula below) |
| **Price** P | what the bond costs **today** = PV of all future cash flows |
| **YTM** | return p.a. if bought at P and held until maturity |

$$CPN=\frac{APR\cdot Face\ Value}{\text{Number of Coupon Payments per Year}}$$

---

## Two types of bonds

| | **Coupon bond** (Kuponanleihe) | **Zero-coupon bond** (Nullkuponanleihe) |
|---|---|---|
| Payments | CPN every period + FV at maturity | **only FV** at maturity |
| Timeline | ${}-P \to CPN \to \dots \to CPN+FV{}$ | ${}-P \to FV{}$ |
| Price | annuity (coupons) + PV of face value | PV of face value → **discounted price** |
| Example | FV \$1,000, 5 % APR, semi-annual, 5 years → CPN = \$25 | FV \$100,000, 1 year, P = \$95,000 → quoted as **95 %** |

**Coupon bond:**
$$P=\underbrace{CPN\cdot\frac{1}{r}\left(1-\frac{1}{(1+r)^{N}}\right)}_{\text{coupons = annuity}}+\underbrace{\frac{Face\ Value}{(1+r)^{N}}}_{\text{face value}}$$

**Zero-coupon bond:**
$$P=\frac{Face\ Value}{(1+r)^{N}}$$

- r and N per **coupon period** (N = number of periods, **not** years)
- Prices are often **quoted in % of the face value**

---

**Example – price of the coupon bond** at a market rate of 10 % (EAR):
semi-annual rate ${}r=1.10^{0.5}-1=4.88\%{}$ ([[01 Wintersemester 2026/Finance und Investment/04 Interest Rates#EAR and APR|EAR → period rate]]), N = 10

$$P=\char36{}25\cdot\frac{1}{0.0488}\left(1-\frac{1}{1.0488^{10}}\right)+\frac{\char36{}1{,}000}{1.0488^{10}}=\char36{}815.09$$

→ P < FV, because coupon (5 %) < market rate (10 %)

---

## Yield to Maturity (YTM)

**YTM** (Rendite bis zur Fälligkeit) = rate at which **NPV = 0** ("IRR for bonds")
→ return p.a. if you buy at the market price and hold until maturity (coupons **+** price gain)
→ same price formula, but **reversed**: P known → solve for the rate

**Zero-coupon bond:**
$$Price=\frac{Face\ Value}{(1+YTM)^{N}}\quad\Rightarrow\quad YTM=\left(\frac{Face\ Value}{Price}\right)^{1/N}-1$$

e.g. FV \$100, P \$76, 10 years: ${}YTM=\left(\frac{100}{76}\right)^{1/10}-1=2.78\%{}$

**Coupon bond:**
$$P=CPN\cdot\frac{1}{YTM}\left(1-\frac{1}{(1+YTM)^{N}}\right)+\frac{FV}{(1+YTM)^{N}}$$

→ for N > 2 not solvable by rearranging → trial and error / solver

e.g. FV \$1,000, CPN \$50, P \$900, 5 years:
$$\char36{}900=\char36{}50\cdot\frac{1}{YTM}\left(1-\frac{1}{(1+YTM)^{5}}\right)+\frac{\char36{}1{,}000}{(1+YTM)^{5}}\ \to\ YTM=7.47\%$$

| Price | YTM vs. coupon rate |
|---|---|
| P < FV (below par) | YTM **>** coupon |
| P = FV (at par) | YTM **=** coupon |
| P > FV (above par) | YTM **<** coupon |

**Decision:** buy if YTM > return of the best alternative (same risk)
