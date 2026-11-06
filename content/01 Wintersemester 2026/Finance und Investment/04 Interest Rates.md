# EAR vs. APR
## Effective annual rate (EAR) - Effektiver Jahreszins

> [!NOTE] EAR
> Actual interest that will be earned at the end of one year
> ${}\tau=(1+EAR)^\tau{-1}$ (${}\tau=\text{period length in years}{}$)

> [!EXAMPLE] Example: monthly interest with EAR = 6 %
> Bank account pays monthly interest with an EAR of 6 %, savings of \$1,000. Interest in the first month? Money after one year?
> 1. Equivalent monthly rate (τ = 1/12): ${}r_{monthly}=(1+0.06)^{\frac{1}{12}}-1=0.4868\%{}$
> 2. Interest in the first month: ${}\char36{}1{,}000\cdot0.4868\%=\char36{}4.87{}$
> 3. After one year (no withdrawals): ${}\char36{}1{,}000\cdot\left((1+0.06)^{\frac{1}{12}}\right)^{12}=\char36{}1{,}000\cdot1.06=\char36{}1{,}060{}$
>

## Annual Percentage Rate (APR) - Nominaler Jahreszins

> [!NOTE] APR
> Amount of interest earned without the effect of compounding (simple interest)
> ${}\frac{APR}{k\text{ periods}}{}$ (${}\tau=\frac{1}{k}{}$)${}\to APR*\tau{}$

> [!EXAMPLE] Example: monthly interest with APR = 6 %
> Bank account pays monthly interest with an APR of 6 %, savings of \$1,000. Interest in the first month? Money after one year?
> 1. Equivalent monthly rate: ${}r_{monthly}=\frac{6\%}{12}=0.5\%{}$
> 2. Interest in the first month: ${}\char36{}1{,}000\cdot0.5\%=\char36{}5{}$
> 3. After one year (no withdrawals): ${}\char36{}1{,}000\cdot\left(1+\frac{0.06}{12}\right)^{12}=\char36{}1{,}061.6778{}$
>
> For comparison: with an EAR of 6 %, the monthly rate was 0.4868 % and the balance after one year \$1,060

> [!NOTE] APR vs. EAR
> The stated APR is usually **lower** than the actual interest earned **if** there are several compounding periods in a year
> → Reason: APR does not include the effect of compound interest (interest earned on prior interest payments)
> ${}\left(1+\frac{APR}{k}\right)^{k}=1+EAR{}$


## Continuous Compounding 

> [!NOTE] Continuous compounding
> The smaller the interval (monthly → daily → hourly), the closer we get to continuous compounding
> ${}1+EAR=e^{APR}{}$
> e.g. 6 % APR: monthly 1.0617 → daily 1.061831 → continuous ${}e^{0.06}=1.061837{}$
> → in practice: compounding more often than daily has a negligible effect; differences come from day-count conventions 
> (e.g. 1 year ≙ 360 days = 12 · 30 days)

---

![[Pasted image 20261031133051.png|812]]
# The determinants of interest rates

> [!BUG] Very important: Present value with different interest rates
> The present value is the sum of all discounted future cash flows
> ${}PV=\frac{C_{1}}{1+r_{1}}+\frac{C_{2}}{(1+r_{2})^{2}}+\dots+\frac{C_{N}}{(1+r_{N})^{N}}=\sum_{n=1}^{N}\frac{C_{n}}{(1+r_{n})^{n}}{}$
> → each cash flow ${}C_{n}{}$ is discounted with the interest rate ${}r_{n}{}$ for **its own** maturity n


# Discount Rates and Loans
