# 4.1 Interest Rate Quotes: EAR vs. APR

## EAR and APR

| | **EAR** – Effective annual rate (Effektiver Jahreszins) | **APR** – Annual percentage rate (Nominaler Jahreszins) |
|---|---|---|
| Meaning | **actual** interest earned at the end of one year | interest **without** the effect of compounding (simple interest) |
| Rate for one period | ${}r_{\tau}=(1+EAR)^{\tau}-1{}$ | ${}r=\frac{APR}{k}=APR\cdot\tau{}$ |

(τ = period length in years, ${}r_{\tau}{}$ = equivalent rate for one period of length τ, k = compounding periods per year, ${}\tau=\frac{1}{k}{}$)

$$1+EAR=\left(1+\frac{APR}{k}\right)^{k}$$

- The stated APR is usually **lower** than the actual interest earned **if** there are several compounding periods per year
- Reason: APR does not include **compound interest** (interest earned on prior interest payments)

---

## Example: bank account with monthly interest, savings of \$1,000

| | **EAR = 6 %** | **APR = 6 %** |
|---|---|---|
| Monthly rate | ${}(1+0.06)^{\frac{1}{12}}-1=0.4868\%{}$ | ${}\frac{6\%}{12}=0.5\%{}$ |
| Interest in the first month | ${}\char36{}1{,}000\cdot0.4868\%=\char36{}4.87{}$ | ${}\char36{}1{,}000\cdot0.5\%=\char36{}5{}$ |
| After one year (no withdrawals) | ${}\char36{}1{,}000\cdot\left((1+0.06)^{\frac{1}{12}}\right)^{12}=\char36{}1{,}000\cdot1.06=\char36{}1{,}060{}$ | ${}\char36{}1{,}000\cdot\left(1+\frac{0.06}{12}\right)^{12}=\char36{}1{,}061.6778{}$ |

---

## Continuous compounding

The smaller the interval (monthly → daily → hourly), the closer we get to continuous compounding:

$$1+EAR=e^{APR}$$

- e.g. 6 % APR: monthly 1.0617 → daily 1.061831 → continuous ${}e^{0.06}=1.061837{}$
- In practice: compounding more often than daily has a negligible effect; differences come from **day-count conventions** (e.g. 1 year ≙ 360 days = 12 · 30 days)

---

# 4.2 Discount Rates and Loans

## Loan balance and loan payments

**Core idea:** a loan = money today in exchange for payments in the future

$$\text{Outstanding loan balance}=PV(\text{remaining loan payments})$$

| Term | Meaning |
|---|---|
| **Loan balance** (Darlehensbetrag) | amount borrowed / still owed |
| **Loan payment** (Darlehenszahlung) | payment per period |
| **Redemption payment** (Tilgung) | part of the payment that reduces the balance |

- Holds at **every** point in time → remaining debt = PV of the payments still to come
- Know the balance → compute the payment, and vice versa
- APR without stated compounding interval → **interval = payment interval** (monthly payments → ${}r=\frac{APR}{12}{}$)

---

## Amortizing loans & annuities

- **Amortizing loan** (Tilgungsdarlehen): payment = interest + redemption
- **Annuity** (Annuitätendarlehen): all payments have the **same size**
- Balance falls, payment stays constant → interest share ↓, redemption share ↑

**Loan balance P:**
$$P=C\cdot\frac{1}{r}\left(1-\frac{1}{(1+r)^{N}}\right)$$

**Loan payment C:**
$$C=\frac{P}{\frac{1}{r}\left(1-\frac{1}{(1+r)^{N}}\right)}$$

(r = rate per payment period, N = number of payments)

---

## Examples (APR 4.8 %, 20 years, monthly → r = 0.4 %, N = 240)

> [!EXAMPLE] Example 1: Payment known (€1,000/month) → max. loan?
> - Loan balance: ${}€1{,}000\cdot\frac{1}{0.004}\left(1-\frac{1}{1.004^{240}}\right)=€154{,}093.30{}$
> - Balance after 1 year (228 payments left): ${}€149{,}387.14{}$
> - Redemption year 1: ${}€154{,}093.30-€149{,}387.14=€4{,}706.16{}$
> - Interest year 1: ${}€12{,}000-€4{,}706.16=€7{,}293.84{}$
>
> | Year | 1 | 10 | 20 |
> |---|---|---|---|
> | Interest share | 61 % | 40 % | 3 % |

> [!EXAMPLE] Example 2: Loan known (€250,000) → monthly payment?
> $$X=\frac{€250{,}000}{\frac{1}{0.004}\left(1-\frac{1}{1.004^{240}}\right)}=€1{,}622.39$$

---

## Trade credit (Lieferantenkredit)

**Core idea:** cash discount (**Skonto**) for paying early → paying later = **short-term loan from the supplier**

**Example:** invoice \$1,000 due in 60 days, 3 % discount if paid within 10 days

| Time (days) | 0 | 10 | 60 |
|---|---|---|---|
| Using the cash discount | 0 | −\$970 | 0 |
| Paying at the end | 0 | 0 | −\$1,000 |
| **Trade credit** (= difference) | 0 | **+\$970** | **−\$1,000** |

(signs from the buyer's view) → you "borrow" \$970 for **50 days** and pay back \$1,000

**IRR** = rate at which both options have the same PV:
$$\frac{\char36{}1{,}000\cdot(1-0.03)}{(1+r_{IRR})^{10/365}}-\frac{\char36{}1{,}000}{(1+r_{IRR})^{60/365}}=0\ \to\ r_{IRR}=24.90\%$$

**Simplified** (rate per 50 days, compounded 7.3 times per year → EAR):
$$r_{IRR}=\left(1+\frac{30}{970}\right)^{\frac{365}{50}}-1=1.0309^{7.3}-1=24.9\%$$

- Not taking the discount (= taking the loan) is **very expensive**
- Decision: alternative borrowing rate **< 24.9 %** → use the discount

---

# 4.3 The Determinants of Interest Rates

![[Pasted image 20261031133051.png|812]]

**Factors influencing interest rates:** inflation, expectations of future growth, government policy, monetary policy, individual preferences

## Inflation: real vs. nominal rates

| Rate | Meaning |
|---|---|
| **Nominal rate** r | growth of **money** |
| **Inflation rate** i | growth of **prices** (CPI, PPI, …) → purchasing power falls |
| **Real rate** ${}r_f{}$ | growth of **purchasing power** (Kaufkraft) |

$$1+r_f=\frac{1+r}{1+i}=\frac{\text{Growth of money}}{\text{Growth of prices}}\quad\Rightarrow\quad r_f=\frac{r-i}{1+i}\approx r-i$$

(approximation for low inflation)

- e.g. r = 5 %, i = 3 % → ${}r_f=\frac{0.05-0.03}{1.03}=1.94\%\approx2\%{}$
- **Ex ante** real rate: uses **expected** inflation
- **Ex post** real rate: uses **actual** inflation
- Data (US & Germany): nominal rates tend to **move with inflation**; since 2009 often **negative real rates** (nominal rates extremely low)

---

## Investment and interest rate policy

**Example:** CF = −10 in t = 0, then 3 in t = 1–4 → profitable at 5 % or 9 %?
$$NPV=-10+3\cdot\frac{1}{r}\left(1-\frac{1}{(1+r)^{4}}\right)$$
- r = 5 %: ${}NPV=-10+10.64=+0.64{}$ ✓
- r = 9 %: ${}NPV=-10+9.72=-0.28{}$ ✗

- Interest rate ↑ → PV of future cash flows ↓ → **fewer positive-NPV investments**
- → Central bank uses the interest rate to steer the economy (stimulate/reduce investment, influence inflation)

---

## The yield curve and discount rates

- Interest rates differ by investment horizon (6 months ≠ 1 year)
- **Term structure** (Zinsstruktur): relation between investment horizon and interest rate
- **Yield curve** (Zinsstrukturkurve): the corresponding graph (Europe: published by the ECB, estimated from coupon bonds with the Nelson/Siegel/Svensson method)
- **Spot rate** ${}r_t{}$ (Kassazins): risk-free rate observed **today** (t = 0) for an investment **until t**, quoted p.a.

**Example:** German Federal Treasury Notes (20.10.2026)

| Time to maturity (months) | 2 | 4 | 6 | 12 |
|---|---|---|---|---|
| Coupon (%) | 2.00 | 0.25 | 0.00 | 1.30 |
| Price | 99.92 | 99.25 | 98.70 | 98.43 |
| **Yield (%)** | 2.57 | 2.65 | 2.75 | 2.95 |

→ same (risk-free) issuer, only maturity differs → yield **rises** with maturity = normal yield curve
(Coupon ≠ yield: return also depends on the price, e.g. 6 months: pay 98.70, get 100)

**Types of yield curves**

| Type | Longer investments yield … | Rate as function of maturity | Occurred e.g. |
|---|---|---|---|
| **Normal** | higher returns | increasing | 1996, 2004 |
| **Flat** | the same return | constant | 1990, 2000 |
| **Inverse** | lower returns | decreasing | 1992, 2023 |

→ The yield curve **changes over time** (German government bonds 1990–2024 show all three types)

---

## Present value with different interest rates

> [!BUG] Very important: Present value with different interest rates
> The present value is the sum of all discounted future cash flows
> $$PV=\frac{C_{1}}{1+r_{1}}+\frac{C_{2}}{(1+r_{2})^{2}}+\dots+\frac{C_{N}}{(1+r_{N})^{N}}=\sum_{n=1}^{N}\frac{C_{n}}{(1+r_{n})^{n}}$$
> → each cash flow ${}C_{n}{}$ is discounted with the **spot rate** ${}r_{n}{}$ for **its own** maturity n
> → match the term of the cash flow and the term of the discount rate

**Example:** investment opportunity in the LSDFE AG – present value?

| Term (years) | t = 1 | t = 2 | t = 3 |
|---|---|---|---|
| Spot rate | 5 % | 3 % | 4 % |
| Payment | \$100 | \$110 | \$120 |
| Present value | ${}\frac{100}{1.05^{1}}=95.24{}$ | ${}\frac{110}{1.03^{2}}=103.69{}$ | ${}\frac{120}{1.04^{3}}=106.68{}$ |

$$PV=\frac{100}{1.05}+\frac{110}{1.03^{2}}+\frac{120}{1.04^{3}}=95.24+103.69+106.68=\char36{}305.61$$

- Each payment gets **its own** rate: t = 2 is discounted with 3 % (not 5 %), t = 3 with 4 %
- The exponent = the term t → the spot rate is a rate **p.a.**, compounded over t years
- Only one rate for all cash flows if the yield curve is **flat** (${}r_1=r_2=\dots=r{}$) → standard PV formula

---

# 4.4 Credit Risk

**New factor:** besides inflation, growth expectations, policy and preferences → **riskiness of the investment**

## Credit risk and credit spread

- Interest rates depend on **who** borrows:
	- **US Treasuries** → long seen as **risk-free** (government not expected to default)
	- **Other borrowers** (e.g. companies) → **default risk**: might not repay the loan entirely
- With credit risk, investors demand a **higher** interest rate
- **Credit spread** = risky rate − risk-free rate
- Size of the spread depends on: **probability of default** + **expected loss size**
- **Creditworthiness** (Kreditwürdigkeit): ability and willingness to repay debt

---

## Excursus: Ratings

Investigating every company yourself is difficult and inefficient → **rating agencies** (Moody's, S&P, Fitch) rate creditworthiness and sort bonds into classes by default risk

| Quality | Moody's | S&P / Fitch | Grade |
|---|---|---|---|
| Best quality | Aaa | AAA | **Investment grade** |
| High quality | Aa | AA | Investment grade |
| Good quality | A | A | Investment grade |
| Medium quality | Baa | BBB | Investment grade |
| Speculative | Ba | BB | **Speculative grade** |
| Highly speculative | B | B | Speculative grade |
| Junk bond | Caa, Ca, C | CCC, CC, C | Speculative grade |

→ Boundary: **BBB/Baa** is the lowest investment grade, from **BB/Ba** downwards = speculative

---

## Credit risk and interest rates

- Discount rates must match **the horizon** (→ yield curve) **and the default risk** of the cash flows
- Better rating → smaller credit spread (e.g. AAA) · worse rating → larger credit spread (e.g. B)
- Example 5-year bond yields (Sep 2025): Johnson & Johnson (AAA), Apple/Amazon (AA+) → lowest yields · Ford (BBB−), Carnival (BB+), Carvana (BB−) → higher · McAfee (CCC+) → highest
