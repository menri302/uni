---
share_link: https://share.note.sx/gw94v0jm#YivjkrX4dPeZ9beicatqlQ
share_updated: 2026-11-01T18:50:16+01:00
---
# Three Rules of Time Travel

> [!BUG] Three Rules of Time Travel
> It is only possible to compare or combine values at the same point in time
> To move cash flows **forward** in time, you must **compound** them
> To move cash flows **backward** in time you must **discount** them

## 1. It is only possible to compare or combine values at the same point in time

[[02 Financial Decision Making and the Law of One Price#Would you take 100.000USD now or 105.000USD in a year?|Would you take $100.000 now or $105.000 in a year]]

## 2. To move cash flows **forward** in time, you must **compound** them

**Compounding** (Aufzinsung): moving values or cash flows **forward** in time
**Future value** (Endwert): value of a cash flow that is moved forward
→ interest on interest = **compound interest** (Zinseszins)

> [!NOTE] Future Value
> ${}FV_{n}=C_{0}*(1+r)*(1+r)*\dots*(1+r)=C_{0}*(1+r)^{n}{}$


## 3. To move cash flows **backward** in time, you must **discount** them

**Discounting** (diskontieren, abzinsen): moving values or cash flows **backward** in time
**Present value** (Barwert): equivalent value today of a future cash flow
→ same intuition as rule 2, just applied backward

> [!NOTE] Present Value
> ${}PV=\frac{C_{n}}{(1+r)*(1+r)*\dots*(1+r)}=\frac{C_{n}}{(1+r)^{n}}{}$


## Overview

> [!BUG] Summary: Three Rules of Time Travel
> **Rule 1**: Only values at the same point in time can be compared or combined
>
> **Rule 2**: To move a cash flow **forward** in time, you must **compound** it
> ${}FV_{n}=C_{0}*(1+r)*(1+r)*\dots*(1+r)=C_{0}*(1+r)^{n}{}$
>
> **Rule 3**: To move a cash flow **backward** in time, you must **discount** it
> ${}PV_{0}=\frac{C_{n}}{(1+r)*(1+r)*\dots*(1+r)}=\frac{C_{n}}{(1+r)^{n}}{}$


# Valuation of a Stream of Cash Flows
![[Pasted image 20261026115341.png|893]]

> [!NOTE] Present Value of a cash flow stream
> ${}PV=C_{0}+\frac{C_{1}}{(1+r)}+\frac{C_{2}}{(1+r)^{2}}+\dots+\frac{C_{N}}{(1+r)^{N}}{}$
> The PV of a cash flow stream equals the **sum of the PVs** of the single cash flows

## Calculating the NPV
Using the three rules we an compare the costs and benefits occuring at multiplepoints in time using the NPV

**Example**: invest 1,000USD in your friend's tech start-up today, she pays back 500USD at the end of each of the next three years, market interest rate 10% → accept?

![[Pasted image 20261026151718.png|601]]

${}NPV=-1000+\frac{500}{1.1^{1}}+\frac{500}{1.1^{2}}+\frac{500}{1.1^{3}}=243.43>0{}$
→ positive NPV → **invest** in your friend's start-up

# Perpetuities
**Perpetuity** (ewige Rente): same cash flow C every year **forever**

> [!NOTE] Present Value of a perpetuity
> ${}PV=\frac{C}{(1+r)^{1}}+\frac{C}{(1+r)^{2}}+\frac{C}{(1+r)^{3}}+\dots=\sum_{n=1}^{\infty}\frac{C}{(1+r)^{n}}=\frac{C}{r}{}$

**Derivation**
1. multiply by ${}(1+r){}$: ${}PV*(1+r)=C+\underbrace{\frac{C}{(1+r)}+\frac{C}{(1+r)^{2}}+\dots}_{=PV}{}$
2. → ${}PV*(1+r)=C+PV{}$ → ${}PV*r=C{}$ → ${}PV=\frac{C}{r}{}$
![[Pasted image 20261026152401.png|448]]Perpetuities are like an ever-lasting pension


# Annuities
**Annuity** (Annuität): same cash flow C every year, but **ends after N payments** (unlike a perpetuity) - "ewige" Rente bis jahr n

> [!NOTE] Present Value of an annuity
> ${}PV=\frac{C}{(1+r)^{1}}+\frac{C}{(1+r)^{2}}+\dots+\frac{C}{(1+r)^{N}}=\sum_{n=1}^{N}\frac{C}{(1+r)^{n}}=C*\frac{1}{r}\left(1-\frac{1}{(1+r)^{N}}\right){}$

**Derivation**: Annuity = perpetuity from year 1 **minus** perpetuity from year N+1

1. Perpetuity 1: ${}PV_{1}=\frac{C}{r}{}$
2. Perpetuity 2: worth ${}\frac{C}{r}{}$ in year N (one period before its first payment) → discount N years: ${}PV_{2}=\frac{C}{r}*\frac{1}{(1+r)^{N}}{}$
3. ${}PV=PV_{1}-PV_{2}=\frac{C}{r}\left(1-\frac{1}{(1+r)^{N}}\right){}$

→ works because PVs are **additive** (Law of One Price / value additivity)

**Example**: C = 1,000USD, r = 4%, N = 5
${}PV=1000*\frac{1}{0.04}\left(1-\frac{1}{1.04^{5}}\right)=25000-20548.18=4451.82{}$USD


# Growing Perpetuities
**Growing perpetuity**: perpetuity whose cash flow **grows** until infinity at a constant rate g
- first payment C in period 1, grows from period 2 on
- at time n → n−1 periods of growth: ${}C*(1+g)^{n-1}{}$

> [!NOTE] Present Value of a growing perpetuity
> ${}PV=\frac{C}{(1+r)}+\frac{C*(1+g)}{(1+r)^{2}}+\frac{C*(1+g)^{2}}{(1+r)^{3}}+\dots=\sum_{n=1}^{\infty}\frac{C*(1+g)^{n-1}}{(1+r)^{n}}=\frac{C}{r-g}{}$ if ${}g<r{}$
> ${}PV=+\infty{}$ if ${}g\geq r{}$ (payments grow faster than they are discounted)

**Derivation** (same trick as for the perpetuity)
1. multiply by ${}(1+r){}$: ${}PV*(1+r)=C+(1+g)*\underbrace{\left(\frac{C}{(1+r)}+\frac{C*(1+g)}{(1+r)^{2}}+\dots\right)}_{=PV}{}$
2. → ${}PV*(1+r)=C+PV*(1+g){}$ → ${}PV*(r-g)=C{}$ → ${}PV=\frac{C}{r-g}{}$

**Example**: climate foundation pays 30,000USD adjusted for inflation every year, r = 8%, inflation g = 3% → money needed today?
${}PV=\frac{30000}{0.08-0.03}=600000{}$USD


# Growing Annuities
**Growing annuity**: cash flow **grows** at constant rate g, but **ends after N payments** (growing perpetuity + annuity)
- payments: ${}C,\ C*(1+g),\ \dots,\ C*(1+g)^{N-1}{}$

> [!NOTE] Present Value of a growing annuity
> ${}PV=C*\frac{1}{r-g}\left(1-\left(\frac{1+g}{1+r}\right)^{N}\right){}$
> → also works for ${}g\geq r{}$, because N is **finite** (unlike the growing perpetuity → ${}+\infty{}$)

**Example (slides)**: save 10,000USD after your bachelor's, saving 5% more each year (salary growth), r = 4%, buy a home in 20 years → how much can you afford?
1. **Present value** (here g > r!): ${}PV=10000*\frac{1}{0.04-0.05}\left(1-\left(\frac{1.05}{1.04}\right)^{20}\right)=210,930.44{}$USD
2. **Future value** (value in year 20): ${}FV=PV*(1+r)^{N}=210930.44*1.04^{20}=462,174.56{}$USD

**Example**: climate foundation only pays for 20 years: C = 30,000USD, r = 8%, g = 3%, N = 20
${}PV=\frac{30000}{0.05}\left(1-\left(\frac{1.03}{1.08}\right)^{20}\right)=600000*0.6125=367501{}$USD


# Internal Rate of Return
**Internal rate of return (IRR)**: interest rate at which the **NPV = 0**
> [!NOTE] Internal Rate of Return
> ${}NPV=0=C_{0}+\frac{C_{1}}{(1+IRR)}+\frac{C_{2}}{(1+IRR)^{2}}+\dots+\frac{C_{N}}{(1+IRR)^{N}}{}$ → solve for IRR

**Example**: invest 1,000USD in your friend's tech start-up today, payoff of 2,000USD in six years → IRR?
${}NPV=0=-1000+\frac{2000}{(1+IRR)^{6}}{}$ → ${}1+IRR=\sqrt[6]{\frac{2000}{1000}}=1.1225{}$ → ${}IRR{}$
analogue: ${}2000=1000*(1+r)^6\to {\sqrt[6]{2 }-1}=12.25\%$ 

> [!BUG] IRR investment rule
> IRR **exceeds** the corresponding interest rate → **undertake** the investment
> IRR does **not exceed** the interest rate → **turn down** the investment
> e.g. start-up above: invest if the interest rate is < 12.25%
> → only **guaranteed** to work for a stand-alone project if **all negative cash flows precede its positive cash flows**

> [!NOTE] IRR and sign changes
> **one** sign change (e.g. outflows first, then only inflows) → exactly **one** IRR
> **many** sign changes (e.g. outflows → inflows → outflows again) → **none, one or several** IRRs possible → computation can become involved


Dringend Beispiele nötig!!!!

