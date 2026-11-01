
> [!BUG] Very important: Exam questions
> 50% of questions will come from concept checks/ tutorials/ quizzes


> [!NOTE] Basis for this chapter
> perfectly **Competitive Market**: goods can bought and sold at the same competitive market price

### Would you take 100.000USD now or 105.000USD in a year?
Solution 1: direct comparison (+5000)
--> lacks consideration for the **time value of money**

2 methods of comparison: Value of investment **today** vs value of investment **in a year**
**discount rate**: risk-free interest rate (for example 7%)
**discount factor:** ${}\frac{1}{(1+r_{f})}{}$ means of calculating todays value of future cash flow


| ${}t_{o }{}$ (invest now) - PV                       | m${}t_{1}{}$ (investment in a year) - FV                  |
| ---------------------------------------------------- | --------------------------------------------------------- |
| 100000USD                                            | 105000USD                                                 |
| ${}\frac{105000}{1+0,07}= 98,130.84{}$USD            | ${}100000*1,07=107000{}$USD                               |
| --> reject bc you have to invest more at ${}t_{o}{}$ | --> reject investment because you get less at ${}t_{1}{}$ |

> [!NOTE] decision rule
> Decision remains the same regardless whether you look at **Present value (PV)** or **Future value (FV)**

# NPV
Investments crete flows which need to be evaluated
**Problems:** hard to quanitfy, occuring at different points in time, different risks
**Solution**: NPV - Evalutating in terms of todays money
NPV = PV (${}Benefits_{inv}{}$) – PV (Costs${}_{inv}{}$)

**Example**: risk-free interest rate of 8% on your bank account, risk-free 550USD investment return at 500USD investment after one year

1. **Future Value**: You take a 500USD loan, invest these 500USD
   ![[Pasted image 20261024144516.png]]
2. **Present value:**
   ![[Pasted image 20261024144506.png]]

> [!BUG] Decision rule
> NPV > 0 Investment creates additional value --> run investment
> Positive NPV means an investment is a good decision regardless of current cash needs
> NPV = 0 Investment creates no additional value --> indifferent
> NPV < 0 Investment creates negative value --> do not run ivestment

# Arbitrage 
> [!NOTE] Arbitrage
> exploiting a price difference between **equivalent assets** (identical cash flows) by buying the cheaper one and selling the more expensive one
> → **risk-free profit** without **net investment**
> 1. equivalent assets (same cash flows)
> 2. no net investment (own capital = 0)
> 3. risk-free (profit is certain, no possible loss)
> --> if one condition is missing, it is **not** arbitrage (e.g. carry trade: borrow in JPY, invest in USD → exchange rate risk)

![[Pasted image 20261024145028.png]]Buying LSDFE AG @ NYSE an selling at LSE will create a profit of 25ct --> **Arbitrage opportunity**

> [!NOTE] Law of one price
> equivalent investment opportunities trade for the same price in competitive markets → no arbitrage opportunities
> --> supply and demand will close the arbitrage opportunity

# No Arbitrage and Security Prices
### Valuing a security with the Law of One Price
**Example**: risk-free bond pays 1,000USD in one year, ${}r_{f}=5\%{}$ → price?
**Approach**: **replication** – find an alternative investment with the same cash flow (bank account)
${}PV=\frac{1000}{1+0,05}=952.38{}$USD → investing 952.38USD at the bank gives the same 1,000USD in one year
→ Price (Bond) = 952.38USD = **no-arbitrage price**

> [!NOTE] Law of One Price
> If two transactions generate equivalent cash flows, they must have the same price in a competitive market → any other price creates an arbitrage opportunity

### Exploiting a wrong price: buy low, sell high
**Variant a** – arbitrage gain realised **in one year** (FV)

| Case 1a: bond too cheap (940USD) | ${}t_{0}{}$ | ${}t_{1}{}$ |
| -------------------------------- | ----------- | ----------- |
| Buy the bond                     | −940        | +1,000      |
| Borrow from the bank             | +940        | −987        |
| **Net**                          | **0**       | **+13**     |

| Case 2a: bond too expensive (960USD) | ${}t_{0}{}$ | ${}t_{1}{}$ |
| ------------------------------------ | ----------- | ----------- |
| Sell the bond                        | +960        | −1,000      |
| Invest at the bank                   | −960        | +1,008      |
| **Net**                              | **0**       | **+8**      |

**Variant b** – arbitrage gain cashed in **today** (PV = positive NPV)
→ borrow/invest exactly 952.38USD, so that the ${}t_{1}{}$ cash flows cancel out

| Case 1b: bond too cheap (940USD) | ${}t_{0}{}$ | ${}t_{1}{}$ |
| -------------------------------- | ----------- | ----------- |
| Buy the bond                     | −940        | +1,000      |
| Borrow from the bank             | +952.38     | −1,000      |
| **Net**                          | **+12.38**  | **0**       |

| Case 2b: bond too expensive (960USD) | ${}t_{0}{}$ | ${}t_{1}{}$ |
| ------------------------------------ | ----------- | ----------- |
| Sell the bond                        | +960        | −1,000      |
| Invest at the bank                   | −952.38     | +1,000      |
| **Net**                              | **+7.62**   | **0**       |

> [!NOTE] Variant a vs. b
> Same arbitrage, just shifted in time: ${}12.38*1,05=13{}$ and ${}7.62*1,05=8{}$


### Determining the interest rate from bond prices
**Example**: risk-free bond trades at 929.80USD, pays 1,000USD in one year
${}929.80=\frac{1000}{1+r_{f}}{}$ → ${}1+r_{f}=\frac{1000}{929.80}=1.0755{}$ → ${}r_{f}=7.55\%{}$ (= bond's return)
**Return** ${}=\frac{\text{Gain at end of year}}{\text{Initial cost}}=\frac{1000-929.80}{929.80}=7.55\%{}$

> [!BUG] No arbitrage applied to bonds
> All risk-free investments must offer investors the same return

### Valuing a portfolio
Law of One Price also applies to **portfolios** of securities
**Example**: securities A and B, security C has the same cash flows as A and B combined

> [!NOTE] Value Additivity
> Price (C) = Price (A + B) = Price (A) + Price (B)
> → identical cash flows must have the same price (Law of One Price)

**Otherwise arbitrage opportunity:**
- Price (A + B) < Price (C) → buy A and B, sell C
- Price (A + B) > Price (C) → sell A and B, buy C

**Example**: a fund share holds one Apple and one Microsoft stock and costs 770USD
Apple 240USD + Microsoft 515USD = 755USD < 770USD
→ sell the fund share, buy the stocks individually → +15USD risk-free profit

# The Role of Risk
So far: only **risk-free** investments
Reality: returns of many investments are **stochastic** (depend on state of the economy, success of a new product, ...)

**Example**: ${}r_{f}=4\%{}$, economy next year good (50%) or bad (50%)
- **Risk-free bond** pays 1,100USD in both states → Price ${}=\frac{1100}{1,04}=1,058{}$USD
- **Stock market index** pays 1,400USD (good) or 800USD (bad) → Expected payoff ${}=0,5*1400+0,5*800=1,100{}$USD

> [!NOTE] Same expected payoff, different price
> Both pay 1,100USD on average, but the stock index is risky → its price must be lower → **risk premium**

### Risk premium
Would you accept a coin flip for +100USD / −100USD?
- Most investors dislike risk: losing 100USD in bad times hurts more than gaining 100USD in good times → **risk aversion** (part of personal preferences)
- To buy the risky stock index, investors require a higher expected return → **risk premium**

| Security    | Price ${}t_{0}{}$ | CF ${}t_{1}{}$ weak | CF ${}t_{1}{}$ strong | Expected return |
| ----------- | ----------------- | ------------------- | --------------------- | --------------- |
| Bond        | 1,058             | +1,100              | +1,100                | 4%              |
| Stock index | 1,000             | +800                | +1,400                | 10%             |

**Expected return** ${}=\frac{\text{Expected gain}}{\text{Initial cost}}=\frac{0,5*(-200)+0,5*400}{1000}=10\%{}$
**Risk premium** = Expected return − ${}r_{f}{}$ = 10% − 4% = **6%**

> [!BUG] Valuing a risky investment
> Discount the **expected** cash flows with the **risk-free rate + an appropriate risk premium**
> ${}Price=\frac{E[CF]}{1+r_{f}+RP}=\frac{0,5*800+0,5*1400}{1+(4\%+6\%)}=\frac{1100}{1.10}=1,000{}$USD
> → risk-free bond: discount with ${}r_{f}{}$ only → ${}\frac{1100}{1.04}=1,058{}$USD


### Pricing risky securities by replication
**Problem**: risk premium of a new security unknown → can't simply discount with 6% (that's the index's premium)
**Solution**: Law of One Price → **replicate** the security with bond and stock index, then derive its risk premium from the price

> [!NOTE] Buying vs. selling
> **Buy**: pay today (−), receive the cash flows later (+)
> **Sell**: receive today (+), owe the cash flows later (−) → you take over the payment obligation
> - **Sell bond** = take a loan: get money today, pay back a **fixed** amount (+4% interest)
> - **Sell stock index** = short selling: borrow the share & sell it, later pay back whatever it is **worth** (incl. gains)

**Method** (b = bond shares, s = stock index shares)
1. One equation per state: ${}b*1100+s*\text{CF}_{index}=\text{CF}_{security}{}$
2. strong − weak → s, insert → b
3. sign of b / s: positive → **buy**, negative → **sell**
4. Price = cost of the replicating portfolio → expected return → RP

#### Security A: pays 0USD (weak) / 600USD (strong)
- Weak: ${}1100b+800s=0{}$
- Strong: ${}1100b+1400s=600{}$
- ${}600s=600{}$ → ${}s=1{}$ (buy index) → ${}1100b=-800{}$ → ${}b=-\frac{8}{11}=-0.7272{}$ (sell bond)

| Security        | Price ${}t_{0}{}$             | CF ${}t_{1}{}$ weak | CF ${}t_{1}{}$ strong | Expected return |
| --------------- | ----------------------------- | ------------------- | --------------------- | --------------- |
| Buy stock index | −1,000                        | +800                | +1,400                | 10%             |
| Sell bond       | ${}+\frac{8}{11}*1058=+769{}$ | −800                | −800                  | 4%              |
| **Buy A**       | **−231**                      | **0**               | **+600**              | **30%**         |

**Intuition**: A = stock index **on credit** (769USD borrowed, 231USD own money) → leverage
- loan (800USD) is always covered by the index (min. 800USD) → you can't lose **more** than 231USD, but you can lose **all** 231USD
- **Expected return** ${}=\frac{0,5*0+0,5*600}{231}-1=30\%{}$ → only **on average**: −100% (weak) or +160% (strong)
- **RP** = 30% − 4% = **26%** (vs. 6% for the index) → more risk, higher risk premium

#### Security B: pays 600USD (weak) / 0USD (strong) → Market risk
- Weak: ${}1100b+800s=600{}$
- Strong: ${}1100b+1400s=0{}$
- ${}600s=-600{}$ → ${}s=-1{}$ (sell index) → ${}1100b=1400{}$ → ${}b=\frac{14}{11}=1.2727{}$ (buy bond)

| Security         | Price ${}t_{0}{}$               | CF ${}t_{1}{}$ weak | CF ${}t_{1}{}$ strong | Expected return |
| ---------------- | ------------------------------- | ------------------- | --------------------- | --------------- |
| Sell stock index | +1,000                          | −800                | −1,400                | 10%             |
| Buy bond         | ${}-\frac{14}{11}*1058=-1346{}$ | +1,400              | +1,400                | 4%              |
| **Buy B**        | **−346**                        | **+600**            | **0**                 | **−13.3%**      |

- **Expected return** ${}=\frac{0,5*600+0,5*0}{346}-1=-13.3\%{}$
- **RP** = −13.3% − 4% = **−17.3%** → negative expected return & negative risk premium
- Investors still accept it: B pays money in **economic hardship** → works like an **insurance** (expected payout < premium, but protects in bad times)

#### A vs. B
|                 | A               | B                |
| --------------- | --------------- | ---------------- |
| Cash flows      | 0 / **600**     | **600** / 0      |
| Expected payoff | 300USD          | 300USD           |
| Volatility      | same            | same             |
| **Price**       | **231USD**      | **346USD**       |
| **RP**          | **+26%**        | **−17.3%**       |

> [!BUG] Market risk: not *how much* it fluctuates, but *when* it pays
> Pays in **good** times (moves with the market) → amplifies risk → **positive** RP
> Pays in **bad** times (moves against the market) → insurance → **negative** RP
> → only risk linked to the market / overall economy is rewarded

### Market risk: the general rule
Risk of a security depends on multiple characteristics, e.g. its **relation to the market index** (not only on how much it fluctuates → see A vs. B)
**Market index**: combines shares of all available securities, weighted by market size → represents the **overall economy** (e.g. S&P 500, MSCI World, DAX)
**Correlation**: do the cash flows move in the **same** (positive) or **opposite** (negative) direction as the market?

| Correlation with market index      | Type of investment                     | Risk premium | Example     |
| ---------------------------------- | -------------------------------------- | ------------ | ----------- |
| **positive** (pays in good times)  | risky investment                       | **positive** | A (+26%)    |
| **negative** (pays in bad times)   | hedge / insurance against market risk  | **negative** | B (−17.3%)  |

**Why? → Risk aversion**: 1USD is not worth the same in every situation

| Economic prosperity                    | Economic hardship                       |
| -------------------------------------- | --------------------------------------- |
| → additional money is of **low value** | → additional money is of **high value** |


- **A** pays when you need money the **least** + loses when you lose your job anyway → amplifies risk → investors demand a **high reward**
- **B** pays when you need money the **most** → catches you like an insurance → investors pay **more** and accept a negative expected return

Securities that create cash flows in times of economic hardship work like an insurance against bad economic development resp. low market returns