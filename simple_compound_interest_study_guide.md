# Simple & Compound Interest
## The Ultimate Placement-Focused Study Guide

<div align="left">
  <img src="https://img.shields.io/badge/Rank-%234-blue?style=for-the-badge" alt="Rank" />
  <img src="https://img.shields.io/badge/Importance-★★★★☆-orange?style=for-the-badge" alt="Importance" />
  <img src="https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge" alt="Difficulty" />
  <img src="https://img.shields.io/badge/Focus-Placements-blueviolet?style=for-the-badge" alt="Focus" />
</div>



---

## 🥇 Rank & Importance

### Rank Among All Aptitude Topics

**#4 — Where Time Meets Money**

Simple & Compound Interest is the financial cousin of percentages — same underlying math, but with the dimension of time added. If percentages taught you how to compare numbers at a single point in time, SI/CI teaches you how money grows (or shrinks) across time. It appears in virtually every placement test, almost always as 2–5 questions, with moderate difficulty. The topic connects directly to Percentages (already mastered) and provides the foundation for more advanced financial reasoning in product company interviews.

| Rank | Topic | Relevance |
|------|-------|-----------|
| 1 | Number Systems & Simplification | Foundation |
| 2 | Percentages | Core tool |
| 3 | Profit, Loss & Discount | Business application |
| 4 | **Simple & Compound Interest** | Time-based financial math |
| 5 | Averages & Ratio | Often combined |
| 6 | Time, Speed & Distance | Different domain |
| 7 | Time & Work | Work-cost connection |
| 8 | Simple & Compound Interest | Different dimension |
| 9 | Permutations & Combinations | Pure math |
| 10 | Probability | Often combined with P&L |

### Why It Matters in Placements

- **Universal appearance**: Every aptitude test has 2–5 SI/CI questions without exception
- **Percentage application**: SI/CI is percentages applied over time — your percentage skills directly transfer here
- **Financial literacy signal**: Banks, finance companies, and product companies use SI/CI to test numerical reasoning
- **Speed-based**: Once the formulas are internalized, SI/CI questions are among the fastest to solve
- **Real-world relevance**: The compound interest vs. simple interest distinction is one of the most practical concepts in personal finance

### Expected Weightage

| Company Type | Questions (out of ~25) | Difficulty Spread |
|---|---|---|
| TCS Ninja / NQT | 2–4 | Easy–Medium |
| Accenture | 2–4 | Easy–Medium |
| Cognizant | 2–3 | Easy–Medium |
| Infosys | 2–4 | Easy–Medium |
| Deloitte | 2–4 | Medium |
| Wipro | 2–3 | Easy–Medium |
| Goldman Sachs | 3–5 | Medium–Hard |
| Amazon | 2–4 | Medium–Hard |
| Microsoft | 2–3 | Hard |
| Google | 1–2 | Hard |

### Importance Rating: ★★★★☆

---

## 📖 Concept Overview

### What Is Simple & Compound Interest?

Both concepts describe how money grows over time when interest is applied. The difference lies in whether interest is calculated only on the original principal (SI) or on the accumulated amount (CI).

**Simple Interest (SI)**: Interest is always calculated on the original principal. The interest amount is the same every year.

**Compound Interest (CI)**: Interest is calculated on the accumulated amount (principal + previously earned interest). Each period's interest becomes part of the principal for the next period.

The key insight: **CI always grows faster than SI over multiple periods, and the gap widens with time.**

### Complete Subtopic Map

```
SIMPLE & COMPOUND INTEREST
├── Simple Interest (SI) — Basic Formula
├── Compound Interest (CI) — Basic Formula
├── SI vs CI Comparison
├── Rate Conversion (Annual, Half-yearly, Quarterly, Monthly)
├── Population/Growth Problems (CI Application)
├── Depreciation (CI Application)
├── Installments (Equated Monthly Installments)
├── Present Worth / True Discount
├── Finding Principal, Rate, or Time
├── Amount Under SI
├── Amount Under CI
├── Effective Annual Rate
├── Fractional Periods (Partial Year)
├── Doubling and Tripling Time
├── Rule of 72 and Rule of 69
├── Mixture of SI and CI
├── Difference Between CI and SI
└── CI with Varying Rates
```

### Where Each Concept Is Used

| Subtopic | Used In |
|---|---|
| Basic SI formula | Every SI question |
| Basic CI formula | Every CI question |
| SI vs CI comparison | "Which is better?" questions |
| Rate conversion | Annual vs quarterly vs monthly |
| Population/growth | CI application |
| Depreciation | CI application (negative growth) |
| Installments | EMI problems, loan questions |
| Present worth | Discounting future payments |
| Doubling time | Investment growth questions |
| Difference SI-CI | Asked directly in many tests |

---

## 🎯 Core Concepts to Master

---

### 1. Simple Interest (SI)

**Definition**: Interest calculated only on the original principal amount, at a fixed rate per year.

**Formula**:

```
SI = (P × R × T) / 100
```

Where:
- P = Principal (initial amount)
- R = Rate of interest per year (%)
- T = Time (in years)

**Amount (A)**:

```
A = P + SI = P + (P × R × T) / 100 = P × (1 + RT/100)
```

> [!NOTE]
> **Intuition**
> Simple interest is linear growth. Think of it like renting money — you pay a fixed rental rate on the original amount, year after year, without compounding the rent.

**Example**: P = ₹10,000, R = 8% per annum, T = 3 years.
SI = (10000 × 8 × 3) / 100 = ₹2,400
Amount = 10000 + 2400 = ₹12,400

**Shortcuts**:

- SI for T years = SI for 1 year × T
- SI for 1 year at R% = P × R/100
- When T is in months: T = months/12
- When T is in days: T = days/365 (or 360 for some banks)

> [!WARNING]
> **Common Mistakes to Avoid**
> Using T in years without checking the time unit. 6 months = 0.5 years, not 6.

---

### 2. Compound Interest (CI)

**Definition**: Interest calculated on the accumulated principal (principal + previously earned interest) each period.

**Formula**:

```
A = P × (1 + R/100)^T
CI = A - P
```

Where A = Amount after T years.

> [!NOTE]
> **Intuition**
> Compound interest is exponential growth. Think of it like a snowball rolling down a hill — each year the snowball (principal + interest) gets bigger, so the next year's growth is on a larger base. The snowball grows faster and faster.

**Compounding Frequency**:
When interest is compounded more than once a year, adjust both rate and time:

```
A = P × (1 + R/n)^(nT)
```

Where n = number of compounding periods per year:
- Annually: n = 1
- Semi-annually (half-yearly): n = 2
- Quarterly: n = 4
- Monthly: n = 12
- Daily: n = 365

**Example**: P = ₹10,000, R = 8% p.a., compounded quarterly, T = 1 year.
n = 4, R/n = 2% per quarter, nT = 4 quarters.
A = 10000 × (1.02)^4 = 10000 × 1.08243 = ₹10,824.32
CI = ₹824.32 (vs. SI of ₹800 for the same period)

**Example (Annual Compounding, 2 years)**:
P = 10000, R = 10%, T = 2 years
Year 1: SI = 1000, Amount = 11000
Year 2: SI on 11000 = 1100, Amount = 12100
CI = 12100 - 10000 = ₹2,100
SI for 2 years = 2000

**Shortcut — The CI Formula for 2 Years**:
CI = P × [(1 + R/100)² - 1] = P × [2R/100 + R²/10000]

> [!WARNING]
> **Common Mistakes to Avoid**
> Using SI formula for CI problems or vice versa. Always check which one is asked.

---

### 3. SI vs CI — The Key Difference

**Simple Interest**: Grows linearly. SI = P × R × T / 100
**Compound Interest**: Grows exponentially. CI accumulates faster over time.

**Critical Comparison Table**:

| Time | SI Multiplier | CI Multiplier | CI Advantage |
|------|-------------|--------------|--------------|
| 1 year | 1 + R/100 | 1 + R/100 | Equal |
| 2 years | 1 + 2R/100 | 1 + 2R/100 + R²/10000 | CI > SI |
| 3 years | 1 + 3R/100 | (1 + R/100)³ | CI > SI |

**The Gap Widens**: For the same principal and rate, CI always produces more interest than SI after the first year. The difference grows larger with time.

**When to Use Which**:
- Banks typically use SI for short-term loans (up to 1 year)
- Investments and long-term deposits use CI
- Exams usually ask CI for growth/depreciation, SI for installment problems

**Formula for Difference Between CI and SI for 2 Years**:
```
CI - SI = P × (R²/10000)
```

For 3 years:
```
CI - SI = P × [3R²/10000 + R³/1000000]
```

> [!WARNING]
> **Common Mistakes to Avoid**
> Thinking CI is always double SI. It's only more by a growing margin, not by a fixed ratio.

---

### 4. Rate Conversion (Compounding Frequency)

**Concept**: When compounding is not annual, convert the rate appropriately.

**Example**: 12% per annum, compounded half-yearly, for 1 year.
- Actual rate per half-year = 12/2 = 6%
- Number of periods = 2
- A = P × (1 + 6/100)² = P × (1.06)²

**Annual Equivalent Rate** (Effective Rate):
For 12% p.a. compounded half-yearly:
Effective annual rate = (1 + 6/100)² - 1 = 0.1236 = **12.36%**

**The More Compounding, The Higher the Effective Rate**:

| Rate | Compounding | Effective Rate |
|------|-------------|----------------|
| 10% | Annual | 10.00% |
| 10% | Semi-annual | 10.25% |
| 10% | Quarterly | 10.38% |
| 10% | Monthly | 10.47% |
| 10% | Daily | 10.52% |

**Shortcut for Effective Annual Rate**:
- Semi-annual: Effective = R + R²/100
- Quarterly: Effective = R + 3R²/400 (approximately)
- Monthly: Effective = R + R²/83 (approximately)

> [!WARNING]
> **Common Mistakes to Avoid**
> Using the nominal rate (12%) directly in CI calculations when compounding is half-yearly. Always divide R by n and multiply nT by n.

---

### 5. Population/Growth Problems (CI Application)

**Concept**: CI formula applied to population, bacteria, or any quantity growing at a fixed percentage rate.

**Formula**:
```
P_n = P_0 × (1 + r/100)^n
```

Where P₀ = initial population, P_n = population after n years.

**Example**: Population of a town is 20,000, growing at 5% per year. What will it be after 3 years?
P = 20000 × (1.05)³ = 20000 × 1.157625 = **23,152**

**Finding Growth Rate from Population Data**:
```
r = [(P_n / P_0)^(1/n) - 1] × 100
```

**Example**: Population grew from 8,000 to 9,800 in 2 years. Find rate.
9800/8000 = 1.225 = (1 + r/100)²
1 + r/100 = √1.225 = 1.1068
r = 10.68%

**Depreciation (Reverse Growth)**:
```
P_n = P_0 × (1 - r/100)^n
```
> [!WARNING]
> **Common Mistakes to Avoid**
> Using simple interest formula for population growth. Population grows on accumulated population (like compound interest), not on the original.

---

### 6. Depreciation

**Concept**: Value decreases by a fixed percentage each year (opposite of CI growth).

**Formula**:
```
Value after n years = P × (1 - r/100)^n
```

**Example**: A machine worth ₹1,00,000 depreciates at 10% per year. Value after 3 years.
= 100000 × (0.90)³ = 100000 × 0.729 = **₹72,900**

**Finding Original Value from Depreciated Value**:
```
P = P_n / (1 - r/100)^n
```

**Common in Product Companies**: Computer equipment, vehicles, machinery — all depreciate. Goldman Sachs and Amazon ask depreciation in DI/quant sections.

> [!WARNING]
> **Common Mistakes to Avoid**
> Using subtraction (P - r% of P) for each year instead of multiplication by (1 - r/100)^n. Subtraction gives the wrong answer after the first year.

---

### 7. Installments (EMI / Equated Installments)

**Concept**: When a loan is repaid in equal installments, each installment is partly principal and partly interest.

**SI-Based Installment Formula**:
For a loan of P at rate R% for T years, paid in n equal annual installments:
```
Each Installment = [P × (1 + RT/100)] / n
```

**The Unitary Method for Installments**:
In installment problems, each rupee of the installment works at the given rate. The total amount (principal + interest) is distributed across installments.

**For SI-Based Installments**:
```
If P is borrowed at R% SI for T years, and repaid in T equal annual installments:
Each installment = P × (1 + RT/100) / T
```

**For CI-Based Installments** (more complex):
The present value of all installments equals the principal:
```
P = I₁/(1+R/100) + I₂/(1+R/100)² + ... + Iₙ/(1+R/100)ⁿ
```
When installments are equal (I = x):
```
P = x × [(1+R/100)^n - 1] / [R/100 × (1+R/100)^n]
```

**Example (SI Installment)**:
Borrow ₹1,000 at 10% SI for 2 years. Repay in 2 equal annual installments.
Total amount = 1000 × (1 + 10×2/100) = 1000 × 1.20 = ₹1,200
Each installment = 1200/2 = **₹600**

**Example (CI Installment)**:
Borrow ₹1,000 at 10% CI. Repay in 2 equal annual installments.
Present value of installments = 1000
x/(1.10) + x/(1.10)² = 1000
x × (0.9091 + 0.8264) = 1000
x × 1.7355 = 1000 → x = **₹576.19**

> [!WARNING]
> **Common Mistakes to Avoid**
> Using SI installment formula when CI is applied. The formula is different.

---

### 8. Present Worth / True Discount

**Concept**: The present value of a future sum, discounted at a given rate.

**Formula**:
```
Present Worth (PW) = A / (1 + R×T/100)    [for SI]
Present Worth (PW) = A / (1 + R/100)^T     [for CI]
```

**True Discount**: The difference between the future value (A) and the present worth (PW).
```
TD = A - PW
```

**Banker's Discount / Commercial Discount**: Discount calculated on the face value (not on present worth). Used in banking.
```
Banker's Discount = (A × R × T) / 100    [using SI formula on A]
```

**Difference Between True Discount and Banker's Discount**:
Banker's Discount > True Discount (for the same face value and rate).

> [!WARNING]
> **Common Mistakes to Avoid**
> Confusing true discount with banker's discount. True discount is on PW; banker's discount is on face value.

---

### 9. Doubling and Tripling Time

**The Rule of 72** (for CI):
```
Time to double ≈ 72 / R
```
This works well for rates between 6% and 15%.

**Example**: At 8% CI, time to double = 72/8 = **9 years**

**The Rule of 69** (more accurate):
```
Time to double ≈ 69 + 0.35/R
```
Or: T = 0.35 × ln(2) / ln(1 + R/100)

**For Exact Doubling**:
```
At R% CI: T = log₂(2) / log(1 + R/100) = 1 / log(1 + R/100) in base 10
```

**Tripling Time** (Rule of 115):
```
Time to triple ≈ 115 / R
```

**SI Doubling**: T = 100/R years. At 10% SI, doubles in exactly 10 years.
**CI Doubling**: T = log(2)/log(1+R/100). At 10% CI, doubles in approximately 7.27 years.

**The Contrast**: At 10% per year:
- SI: 10 years to double
- CI: ~7.27 years to double

This is the most important practical difference between SI and CI.

> [!WARNING]
> **Common Mistakes to Avoid**
> Applying the Rule of 72 to SI (it's only for CI). Rule of 72 assumes compounding.

---

### 10. Difference Between CI and SI for Multiple Years

**For 2 Years**:
```
CI - SI = P × (R² / 10000)
```

**For 3 Years**:
```
CI - SI = P × [3R²/10000 + R³/1000000]
```

**Example**: P=10,000, R=10%, for 2 years.
CI - SI = 10000 × (10²/10000) = 10000 × 0.01 = **₹100**

**Verification**:
SI = 10000 × 10 × 2/100 = ₹2,000
CI = 10000[(1.10)² - 1] = 10000[1.21 - 1] = ₹2,100
Difference = ₹100 ✓

**Commonly Asked Question**: "The difference between CI and SI on a sum at 10% per annum for 2 years is ₹31. Find the principal."
31 = P × (10²/10000) = P × 0.01 → P = **₹3,100**

---

### 11. Fractional Periods in CI

**Concept**: When time is not a complete number of years, use fractional exponents.

**Example**: P = ₹10,000, R = 10% CI, T = 1.5 years.
A = 10000 × (1.10)^1.5 = 10000 × √(1.10)³ = 10000 × 1.1537 = **₹11,537**

**For 2 years 6 months**: T = 2.5 years
A = P × (1 + R/100)^2 × √(1 + R/100)

**Common Trick**: Sometimes exam questions ask for interest for 1.5 years at CI. Always use fractional exponent, not simple average.

> [!WARNING]
> **Common Mistakes to Avoid**
> Calculating CI for 1 year + CI for half year separately and adding. CI for 1.5 years ≠ CI(1 yr) + SI(0.5 yr). Must use: A = P × (1+R/100)^1.5

---

### 12. CI with Varying Rates

**Concept**: When different rates apply in different years.

**Formula**:
```
A = P × (1 + R₁/100) × (1 + R₂/100) × (1 + R₃/100) × ...
```

**Example**: P=10,000. 10% for 1st year, 20% for 2nd year, 30% for 3rd year.
A = 10000 × 1.10 × 1.20 × 1.30 = **₹17,160**
CI = 10000[(1.10×1.20×1.30) - 1] = ₹7,160

**Comparison with Uniform Rate**: At uniform 20% for 3 years:
A = 10000 × (1.20)³ = 10000 × 1.728 = ₹17,280
At varying rates (10%, 20%, 30%), A = ₹17,160 (slightly less, because arithmetic mean of rates ≠ geometric mean)

**Common in Product Companies**: Investment return questions with changing market conditions.

---

## 🧠 Important Formula Sheet

### Simple Interest

| Formula | When to Use |
|---|---|
| SI = P × R × T / 100 | Finding simple interest |
| A = P(1 + RT/100) | Amount under SI |
| P = SI × 100 / (R × T) | Finding principal |
| R = SI × 100 / (P × T) | Finding rate |
| T = SI × 100 / (P × R) | Finding time |
| SI for T years = SI_annual × T | Annual interest × years |

### Compound Interest

| Formula | When to Use |
|---|---|
| A = P(1 + R/100)^T | Amount under CI (annual) |
| A = P(1 + R/n)^(nT) | CI with n compounding periods/year |
| CI = P[(1+R/100)^T - 1] | Finding CI amount (not total amount) |
| Effective annual rate = (1+R/n)^n - 1 | Effective rate comparison |
| PW = A / (1+R/100)^T | Present worth of future sum |

### Key Comparison Formulas

| Formula | When to Use |
|---|---|
| CI - SI (2 years) = P × R²/10000 | Difference for 2 years |
| CI - SI (3 years) = P × [3R²/10000 + R³/1000000] | Difference for 3 years |
| Rule of 72: T_doubling ≈ 72/R | Approximate doubling time (CI) |
| Rule of 69: T_doubling ≈ 69.3/R + 0.35 | More accurate doubling time |
| SI doubles at 100/R years | SI doubling time |
| Depreciation: V_n = P(1 - r/100)^n | Value after n years of depreciation |
| Growth: P_n = P_0(1 + r/100)^n | Population/value growth |

### Installment Formulas

| Formula | When to Use |
|---|---|
| SI Installment = P(1 + RT/100) / T | Equal annual installments at SI |
| CI Installment: P = x[(1+R)^n - 1]/[R(1+R)^n] | EMI formula (equal annual, CI) |

### Discount Formulas

| Formula | When to Use |
|---|---|
| True Discount = A - A/(1+RT/100) | True discount (SI) |
| Banker's Discount = (A × R × T)/100 | Discount on face value |
| Present Worth = A / (1 + RT/100) | PW under SI |

### Memory Tricks

**Rule of 72 Memory**: "Divide 72 by the rate, get the years to double. Divide 115 by the rate, get the years to triple."

**CI vs SI for 2 Years**: The difference is always P × (R²/10000). For P=10000, R=10%: difference = 100. For R=5%: difference = 25. Notice it's proportional to R².

**SI → CI Bridge**: For 2 years, CI - SI = P(R²/10000). This is the extra "interest on interest" for the second year.

**The n=2 CI Formula**: (1 + R/100)² = 1 + 2R/100 + R²/10000. The "extra" R²/10000 is the second-year compound.

---

## ⚡ Shortcut Techniques & Time-Saving Tricks

### 1. The Rule of 72 (Instant)

For any rate R% compound interest, years to double ≈ 72/R.

| Rate | Years to Double |
|------|----------------|
| 6% | 12 years |
| 8% | 9 years |
| 9% | 8 years |
| 12% | 6 years |
| 15% | 4.8 years |
| 18% | 4 years |

**Example**: At 12% CI, ₹5,000 doubles to ₹10,000 in approximately **6 years**.

### 2. SI = CI Only in Year 1

SI = CI for the first year at any rate. After that, CI > SI.

> [!TIP]
> **Shortcut Method**
> If a question asks for SI and CI "in the first year" or "for 1 year," they're the same. Save calculation time by recognizing this.

### 3. CI - SI for 2 Years = PR²/10000

This formula is asked in almost every test. Learn it cold.

**Fast calculation**:
- P = 10,000, R = 10% → difference = 10000 × 100/10000 = **₹100**
- P = 5,000, R = 5% → difference = 5000 × 25/10000 = **₹12.50**
- P = 8,000, R = 12% → difference = 8000 × 144/10000 = **₹115.20**

### 4. The Fractional Year Trick

For CI at R% for a fractional year (e.g., 1.5 years):
A = P × (1 + R/100) × √(1 + R/100)

**Example**: P=10000, R=10%, T=1.5 years
A = 10000 × 1.10 × √1.10 = 10000 × 1.10 × 1.0488 = **₹11,537**

### 5. Approximate CI for Small Rates

For R ≤ 10% and T ≤ 3 years, use binomial approximation:
(1 + R/100)^T ≈ 1 + TR/100 + T(T-1)R²/20000

**Example**: At 10% for 2 years: ≈ 1 + 0.20 + 0.01 = 1.21 exactly (this approximation is exact for R=10%, T=2)
At 8% for 2 years: ≈ 1 + 0.16 + 0.008 = 1.168 (actual: 1.1664, close)

### 6. Compare SI vs CI Without Full Calculation

**For 2 years**: SI amount = 1 + 2R/100; CI amount = 1 + 2R/100 + R²/10000
CI wins by R²/10000 (as percentage of principal).

**Quick comparison**:
- At 10%: CI is 1% more than SI after 2 years
- At 20%: CI is 4% more than SI after 2 years
- At 5%: CI is only 0.25% more after 2 years

### 7. Installment Fast Method (SI)

For SI installment problems, the total amount with interest = sum of all installments.

**Example**: P=5000, R=10%, T=2 years, 2 installments.
Total amount = 5000 × 1.20 = 6000
Each installment = 6000/2 = **₹3,000**

### 8. The CI Growth Rate from Ratio

If amount becomes x times in n years at R% CI:
x = (1 + R/100)^n
R = (x^(1/n) - 1) × 100

**Example**: Amount becomes 8 times in 3 years.
8 = (1 + R/100)³
1 + R/100 = 2 → R = **100%**

---

## 🔥 Most Frequently Asked Question Patterns

### Pattern 1: Find SI / CI Amount
**Concept**: Basic formula application
**Difficulty**: Easy
**Approach**: Plug into SI = P×R×T/100 or A = P(1+R/100)^T
**Fastest**: SI multiplier table
**Companies**: All companies

### Pattern 2: Find Principal / Rate / Time
**Concept**: Rearranging SI/CI formula
**Difficulty**: Easy
**Approach**: Isolate the unknown variable
**Fastest**: Cross-multiply and solve
**Companies**: All companies

### Pattern 3: SI vs CI Comparison
**Concept**: Difference or comparison over time
**Difficulty**: Medium
**Approach**: CI - SI for 2 years = PR²/10000
**Fastest**: Direct formula
**Companies**: TCS, Infosys, Amazon, Goldman

### Pattern 4: Amount at CI with Compounding Frequency
**Concept**: n compounding periods
**Difficulty**: Medium
**Approach**: A = P(1 + R/n)^(nT)
**Fastest**: Divide rate by n, multiply time by n
**Companies**: Infosys, Deloitte, Goldman

### Pattern 5: Installment Problems (SI)
**Concept**: Equal annual payments
**Difficulty**: Medium
**Approach**: Total amount with interest / number of installments
**Fastest**: SI installment formula
**Companies**: TCS, Infosys, Cognizant

### Pattern 6: Doubling / Tripling Time
**Concept**: Rule of 72 or exact formula
**Difficulty**: Easy–Medium
**Approach**: Rule of 72 for approximation; exact formula for precision
**Fastest**: Rule of 72
**Companies**: TCS, Infosys, Deloitte

### Pattern 7: Population / Growth (CI Application)
**Concept**: CI for non-financial growth
**Difficulty**: Medium
**Approach**: P_n = P_0(1 + r/100)^n
**Fastest**: Compound multiplier method
**Companies**: Infosys, Deloitte, Goldman

### Pattern 8: Depreciation
**Concept**: Negative growth
**Difficulty**: Medium
**Approach**: Value_n = P(1 - r/100)^n
**Fastest**: Depreciation multiplier
**Companies**: Deloitte, Goldman, Amazon

### Pattern 9: Present Worth / True Discount
**Concept**: Discounting future payments
**Difficulty**: Medium
**Approach**: PW = A / (1 + RT/100) for SI; A/(1+R/100)^T for CI
**Fastest**: Direct formula
**Companies**: Goldman, Amazon, Deloitte

### Pattern 10: CI with Varying Rates
**Concept**: Different rates each year
**Difficulty**: Medium–Hard
**Approach**: Multiply individual multipliers: A = P × ∏(1 + R_i/100)
**Fastest**: Chain multiplication
**Companies**: Goldman, Amazon, Microsoft

### Pattern 11: Find Rate Given Amount and Time
**Concept**: Rearranging CI formula
**Difficulty**: Medium
**Approach**: A/P = (1 + R/100)^T; use trial or log
**Fastest**: For 2 years: R = √(A/P × 10000) - 100
**Fastest**: For 3 years: R = ³√(A/P) - 1 × 100
**Companies**: Infosys, Amazon, Goldman

### Pattern 12: EMI / Loan Installment (CI)
**Concept**: Equal payments covering interest + principal
**Difficulty**: Hard
**Approach**: Present value of annuity formula
**Fastest**: Formula approach
**Companies**: Amazon, Goldman, Microsoft

### Pattern 13: Fractional Year in CI
**Concept**: Non-integer time period
**Difficulty**: Medium
**Approach**: A = P × (1 + R/100)^fractional part
**Fastest**: Fractional exponent method
**Companies**: Infosys, Amazon, Deloitte

### Pattern 14: Effective Annual Rate
**Concept**: Converting nominal to effective rate
**Difficulty**: Medium
**Approach**: (1 + R/n)^n - 1
**Fastest**: Formula
**Companies**: Goldman Sachs, Amazon (finance roles)

### Pattern 15: SI-CI Difference Over 3 Years
**Concept**: Difference for 3 years
**Difficulty**: Medium
**Approach**: CI - SI = P[3R²/10000 + R³/1000000]
**Fastest**: Direct formula
**Companies**: Infosys, Amazon, Goldman

### Pattern 16: Find P Given CI - SI Difference
**Concept**: Using difference formula backward
**Difficulty**: Easy–Medium
**Approach**: P = Difference × 10000 / R² (for 2 years)
**Fastest**: P = diff × 10000 / R²
**Companies**: TCS, Infosys, Cognizant

### Pattern 17: Mixed SI and CI (Same Principal)
**Concept**: SI for part, CI for part
**Difficulty**: Medium
**Approach**: Calculate separately, add interests
**Fastest**: Separate calculation
**Companies**: Infosys, Deloitte, Amazon

### Pattern 18: Partial Period Before First Compounding
**Concept**: Interest for partial first period
**Difficulty**: Hard
**Approach**: Use fractional exponent or prorate
**Fastest**: A = P(1 + R/100)^whole × (1 + R × fraction/100)
**Companies**: Goldman, Amazon

### Pattern 19: CI Growth Rate from Two Data Points
**Concept**: Find rate given initial and final values
**Difficulty**: Medium
**Approach**: (Final/Initial)^(1/n) - 1 × 100 = r
**Fastest**: nth root method
**Companies**: Infosys, Deloitte, Goldman

### Pattern 20: CI Interest for Fractional Year Only
**Concept**: Interest for 1.5 years specifically
**Difficulty**: Medium
**Approach**: A = P(1+R/100)^fraction
**Fastest**: √(1+R/100) for 0.5 year
**Companies**: All companies

---

## 💼 Placement & Interview Relevance

### Service-Based Companies

| Company | Frequency | Difficulty | Focus Areas |
|---|---|---|---|
| TCS NQT/Ninja | Medium (2-4 Qs) | Easy–Medium | Basic SI/CI, difference formulas |
| Infosys | Medium (2-4 Qs) | Easy–Medium | CI growth, installment, population |
| Cognizant | Low (2-3 Qs) | Easy | Basic SI/CI |
| Accenture | Low (2-3 Qs) | Easy | Basic SI/CI |
| Wipro | Low (2-3 Qs) | Easy–Medium | Basic formulas |

### Product-Based Companies

| Company | Frequency | Difficulty | Focus Areas |
|---|---|---|---|
| Amazon | Medium (2-4 Qs) | Medium–Hard | Investment growth, depreciation, varying rates |
| Goldman Sachs | High (3-5 Qs) | Medium–Hard | EMI, present worth, effective rate |
| Microsoft | Medium (2-3 Qs) | Hard | Complex CI, fractional periods |
| Google | Low (1-2 Qs) | Hard | Growth rate, compound problems |
| Adobe | Low (2-3 Qs) | Medium–Hard | Basic CI, depreciation |

### Difficulty Variation
- Service-based: 80% Easy, 20% Medium
- Product-based: 20% Medium, 60% Hard, 20% Very Hard
- Finance companies: Present worth, EMI, effective annual rate are standard

### Typical Questions Per Test
- TCS NQT: 2-4 questions
- Infosys: 2-4 questions
- Amazon: 2-4 questions
- Goldman Sachs: 3-5 questions (often combined with DI)
- Google: 1-2 questions (usually in mixed quant)

---

## 🚀 Beginner → Advanced Roadmap

### Phase 1: Fundamentals (Days 1-2)
1. Learn SI formula: SI = P×R×T/100
2. Learn CI formula: A = P(1+R/100)^T
3. Distinguish SI from CI clearly
4. Learn difference formula for 2 years: CI - SI = PR²/10000
5. Learn Rule of 72 for doubling time
6. Practice: 40 basic SI/CI questions
7. Target: Solve basic SI and CI questions in under 30 seconds

### Phase 2: Intermediate Concepts (Days 3-5)
1. Compounding frequency (n periods per year)
2. Effective annual rate
3. Population/growth problems
4. Depreciation problems
5. SI installment formula
6. Practice: 50 intermediate questions
7. Target: Solve compound period questions in under 45 seconds

### Phase 3: Advanced Concepts (Days 6-9)
1. CI installment (present value of annuity)
2. True discount and present worth
3. Fractional period CI
4. Varying rates in CI
5. Three-year CI - SI difference formula
6. Practice: 50 advanced questions
7. Target: Solve fractional period and varying rate problems in under 60 seconds

### Phase 4: Placement-Level Practice (Days 10-14)
1. Solve 200+ previous year questions (TCS, Infosys, Cognizant)
2. Focus on SI-CI difference questions (most frequently asked)
3. Take timed section tests
4. Review errors
5. Target: 85%+ accuracy, 1 question per 50 seconds

### Phase 5: Product-Based Level (Days 15-20)
1. Solve Goldman Sachs and Amazon-specific SI/CI problems
2. Practice EMI and present worth questions
3. Handle multi-step problems combining growth and depreciation
4. Practice effective rate comparisons
5. Target: 75%+ accuracy at hard level

---

## 📊 Difficulty Breakdown

### Easy
| Subtopic | Why Easy |
|---|---|
| Basic SI formula | Direct substitution |
| Basic CI formula (1 year) | SI = CI in year 1 |
| Finding P, R, or T | Direct rearrangement |
| Rule of 72 | Division only |
| SI for partial year | T in years (decimal) |
| CI - SI for 2 years (direct) | Formula plug-in |

### Medium
| Subtopic | Why Medium |
|---|---|
| CI for 2+ years | Power calculation |
| Compounding frequency | Rate and time adjustment |
| Effective annual rate | Conversion formula |
| Population growth | CI formula application |
| Depreciation | (1 - r/100)^n |
| SI installments | Total amount method |
| Fractional year CI | Fractional exponent |
| Varying rates | Multi-mplier chain |

### Hard
| Subtopic | Why Hard |
|---|---|
| CI installments (EMI) | Present value of annuity formula |
| Present worth (CI basis) | Discounting future value |
| True discount vs banker's discount | Conceptual distinction |
| Finding rate from amount (3+ years) | Root extraction |
| Fractional year with CI | √(1+R/100) type calculation |
| Three-year SI-CI difference | Complex formula |
| Partial period + full period | Multiple steps |

### Very Hard
| Subtopic | Why Very Hard |
|---|---|
| CI installments with multiple years | Log equation solving |
| Present value of irregular installments | Sum of geometric series |
| Growth rate with changing base | Recursive growth |
| Compound period with fractional | n-th root + fractional |
| Multi-step financial planning | Multiple formula chain |

---

## 🎓 Mastery Plan

### Questions for Basic Understanding
**Minimum: 70 questions** (Easy–Medium mix)
- 30 basic SI questions
- 25 basic CI questions
- 15 SI-CI comparison questions

### Questions for Placement Readiness
**Additional: 150 questions** (Medium difficulty)
- Target: 85% accuracy
- Time: Under 50 seconds per question
- Focus: TCS NQT, Infosys, Cognizant patterns
- Priority: SI-CI difference, basic CI growth

### Questions for Product Company Readiness
**Additional: 130 questions** (Hard–Very Hard)
- Target: 70% accuracy
- Focus: Goldman Sachs, Amazon, Microsoft patterns
- Priority: Installments, present worth, effective rate, varying CI

### Time Required for Mastery
| Level | Time | Daily Commitment |
|---|---|---|
| Basic (70 Qs) | 3 days | 1 hour/day |
| Placement (220 Qs) | 2 weeks | 1.5 hours/day |
| Product (350 Qs) | 3 weeks | 1.5-2 hours/day |
| **Total** | **~4.5 weeks** | — |

---

## ❌ Common Traps & Mistakes

### Mistake 1: Confusing SI with CI
**Error**: Using SI formula for a CI problem, or vice versa.
**Fix**: Check if interest is on original principal (SI) or accumulated amount (CI). SI always gives the same yearly interest; CI grows.

### Mistake 2: Wrong Time Unit for T
**Error**: Using T = 6 for 6 months, giving T = 6 in the SI formula.
**Fix**: T always in years. 6 months = 0.5 years. 3 months = 0.25 years.

### Mistake 3: Wrong Compounding Rate Adjustment
**Error**: Using R = 12% directly when compounding is quarterly. A = P(1+0.12)^4 (wrong!)
**Fix**: Divide rate by n, multiply time by n. A = P(1+0.03)^4.

### Mistake 4: Applying Rule of 72 to SI
**Error**: Saying money doubles in 72/R years under SI.
**Fix**: Rule of 72 is only for CI. SI doubles in exactly 100/R years.

### Mistake 5: Adding SI for Each Year in CI Calculation
**Error**: For CI, calculating interest as SI each year and adding.
**Fix**: Year 1: interest on P. Year 2: interest on P + Year 1 interest. Not the same as SI.

### Mistake 6: Using SI Installment Formula for CI Installment Problems
**Error**: Using Total Amount / n for CI-based installments.
**Fix**: CI installment problems require present value calculation. SI installment = Total Amount/n. CI installment = PV of annuity.

### Mistake 7: Forgetting That CI-CSI Difference Formula Is for 2 Years Only
**Error**: Using P×R²/10000 for 3 years.
**Fix**: For 3 years: P[3R²/10000 + R³/1000000]. The formula changes with time.

### Mistake 8: Ignoring Fractional Years in CI
**Error**: Treating 1.5 years as 1 year + 6 months simple interest.
**Fix**: Use A = P(1+R/100)^1.5 or A = P(1+R/100) × √(1+R/100).

### Mistake 9: Not Adjusting for Depreciation Correctly
**Error**: Subtracting depreciation each year (P - r% of P) instead of multiplying.
**Fix**: Value after n years = P × (1 - r/100)^n. Multiplication, not subtraction.

### Mistake 10: Mixing Up True Discount and Banker's Discount
**Error**: Using true discount formula for banker's discount or vice versa.
**Fix**: True discount is on present worth. Banker's discount is on face value (simple interest on A).

---

## 📝 Practice Section

### 🔰 Easy Questions (1-20)

1. Find the simple interest on ₹5,000 at 8% per annum for 3 years.
   <details>
   <summary>🔍 View Solution</summary>

   SI = P×R×T/100 = 5000×8×3/100 = 1200 × 3 = ₹1,200
   </details>
2. Find the compound interest on ₹10,000 at 10% per annum for 2 years.
   <details>
   <summary>🔍 View Solution</summary>

   A = 10000×(1.10)² = 10000×1.21 = ₹12,100. CI = 12100-10000 = ₹2,100
   </details>
3. The SI on a sum at 5% per annum for 3 years is ₹450. Find the sum.
   <details>
   <summary>🔍 View Solution</summary>

   SI = 450, R=5%, T=3. P = 450×100/(5×3) = 45000/15 = ₹3,000
   </details>
4. At what rate per annum will ₹2,000 become ₹2,400 in 4 years under SI?
   <details>
   <summary>🔍 View Solution</summary>

   SI = 2400-2000 = 400. R = 400×100/(2000×4) = 40000/8000 = 5%
   </details>
5. Find the amount if ₹8,000 is invested at 6% CI for 2 years.
   <details>
   <summary>🔍 View Solution</summary>

   A = 8000×(1.06)² = 8000×1.1236 = ₹8,988.80
   </details>
6. The difference between CI and SI on a sum at 10% per annum for 2 years is ₹50. Find the sum.
   <details>
   <summary>🔍 View Solution</summary>

   Difference = P×R²/10000. 50 = P×100/10000 = P×0.01 → P = ₹5,000
   </details>
7. In how many years will ₹1,000 become ₹2,000 at 10% SI?
   <details>
   <summary>🔍 View Solution</summary>

   SI to double: 1000 at 10% SI. 1000×10×T/100 = 1000 → T = 10 years
   </details>
8. Using the Rule of 72, how long will ₹5,000 take to double at 9% CI?
   <details>
   <summary>🔍 View Solution</summary>

   Rule of 72: 72/9 = 8 years
   </details>
9. Find the CI on ₹20,000 at 12% per annum for 1 year.
   <details>
   <summary>🔍 View Solution</summary>

   CI for 1 year = SI for 1 year (same). 20000×12/100 = ₹2,400
   </details>
10. A sum becomes 3 times itself in 5 years at SI. Find the rate.
   <details>
   <summary>🔍 View Solution</summary>

   3P = P + SI_5yr → SI_5yr = 2P = P×R×5/100 → R = 40%
   </details>
11. The CI on a sum at 8% for 2 years is ₹832. Find the principal.
   <details>
   <summary>🔍 View Solution</summary>

   CI for 2yr = 832. CI = P[(1+R/100)²-1] = P[2R/100+R²/10000]
   We need R. Using CI-SI diff = P×R²/10000. But we don't know SI.
   CI - SI = P×R²/10000 → SI = CI - P×R²/10000.
   But also: CI - SI = P×R²/10000 = 832 - SI.
   And SI = P×R×2/100 = P×R/50.
   832 - P×R/50 = P×R²/10000 → 832 = P×R/50 + P×R²/10000
   Try R=8%: 832 = P×8/50 + P×64/10000 = 0.16P + 0.0064P = 0.1664P → P = 5000.
   CI = 832, check: 5000×0.08×2 = 800 (SI), diff = 32. But diff formula gives 5000×64/10000 = 32.
   So if SI=800, diff=32, CI=832. But diff given is 832 itself.
   So CI - SI = 832 = P×R²/10000.
   Try R=10%: P = 832×10000/100 = 83,200 (too large).
   Try R=20%: P = 832×10000/400 = 20,800.
   But CI at 20% for 2yr on 20800 = 20800×(1.2)²-20800 = 20800×1.44-20800 = 29952-20800 = 9152. SI = 20800×20×2/100 = 8320. Diff = 832. ✓ P = ₹20,800, R = 20%.
   </details>
12. Find the SI on ₹1,200 at 7.5% per annum for 2.5 years.
   <details>
   <summary>🔍 View Solution</summary>

   T = 2.5 years. SI = 1200×7.5×2.5/100 = 1200×18.75/100 = ₹225
   </details>
13. At what rate will ₹1,000 amount to ₹1,500 in 5 years under CI?
   <details>
   <summary>🔍 View Solution</summary>

   A = P(1+R/100)^5 = 1500, P=1000. (1+R/100)^5 = 1.5
   (1+R/100) = 1.5^(1/5) = 1.0845 → R = **8.45%**
   </details>
14. Find the amount: Principal ₹6,000, Rate 10% CI, Time 3 years.
   <details>
   <summary>🔍 View Solution</summary>

   A = 6000×(1.10)³ = 6000×1.331 = ₹7,986
   </details>
15. A sum of ₹3,000 is invested at 8% SI. In how many years will it become ₹3,720?
   <details>
   <summary>🔍 View Solution</summary>

   SI = 3720-3000 = 720. 720 = 3000×8×T/100 → 72000 = 24000T → T = 3 years
   </details>
16. Find the SI on ₹15,000 at 6% for 4 months.
   <details>
   <summary>🔍 View Solution</summary>

   T = 4/12 = 1/3 year. SI = 15000×6×(1/3)/100 = 15000×2/100 = ₹300
   </details>
17. The amount after 2 years at SI is ₹5,200. The rate is 10%. Find the principal.
   <details>
   <summary>🔍 View Solution</summary>

   A = P(1+0.10×2/100)? No, SI: A = P(1+10×2/100) = P×1.20 = 5200 → P = ₹4,333.33
   </details>
18. Find the CI on ₹1,00,000 at 5% for 2 years compounded half-yearly.
   <details>
   <summary>🔍 View Solution</summary>

   Half-yearly: n=2, R/n=5%, nT=4. A = 100000×(1.05)^4 = 100000×1.2155 = ₹1,21,550. CI = ₹21,550
   </details>
19. A machine depreciates at 10% per year. Its value is ₹40,000. What will it be after 2 years?
   <details>
   <summary>🔍 View Solution</summary>

   Value = 40000×(0.90)² = 40000×0.81 = ₹32,400
   </details>
20. Find the rate at which SI and CI amounts are equal for 1 year at the same rate.
   <details>
   <summary>🔍 View Solution</summary>

   SI = CI for 1 year at any rate (equal). So rate can be any %. The question likely asks: find the rate such that amounts are equal for 1 year. Answer: **any rate** — SI = CI in year 1.

   ---
   </details>


---

### 🔶 Medium Questions (1-20)

1. The difference between CI and SI on a sum for 2 years at 5% per annum is ₹50. Find the sum.
   <details>
   <summary>🔍 View Solution</summary>

   Difference = P×R²/10000 = P×25/10000 = P/400 = 50 → P = ₹20,000
   </details>
2. A sum of ₹5,000 is invested at 12% CI. In how many years will it become ₹7,000?
   <details>
   <summary>🔍 View Solution</summary>

   7000 = 5000×(1.12)^n. (1.12)^n = 1.4
   n×log(1.12) = log(1.4) → n = 0.1461/0.0492 ≈ 2.97 ≈ **3 years**
   </details>
3. Find the effective annual rate for 12% per annum compounded quarterly.
   <details>
   <summary>🔍 View Solution</summary>

   Effective = (1+0.12/4)^4 - 1 = (1.03)^4 - 1 = 1.1255 - 1 = **12.55%
   </details>
4. A population of 20,000 grows at 5% per year. What will it be after 3 years?
   <details>
   <summary>🔍 View Solution</summary>

   A = 20000×(1.05)³ = 20000×1.157625 = **23,153**
   </details>
5. Find the CI on ₹25,000 at 10% for 1.5 years.
   <details>
   <summary>🔍 View Solution</summary>

   A = 25000×(1.10)^1.5 = 25000×1.10×√1.10 = 25000×1.10×1.0488 = **₹28,842
   </details>
6. A sum of ₹8,000 becomes ₹9,800 in 2 years under CI. Find the rate.
   <details>
   <summary>🔍 View Solution</summary>

   9800 = 8000×(1+R/100)². 9800/8000 = 1.225 = (1+R/100)²
   1+R/100 = √1.225 = 1.1068 → R = **10.68%**
   </details>
7. At what rate per annum will ₹1,000 become ₹1,331 in 3 years under CI?
   <details>
   <summary>🔍 View Solution</summary>

   1331 = 1000×(1+R/100)³. (1+R/100)³ = 1.331 = (1.1)³ → R = **10%
   </details>
8. The CI on a sum at 10% for 3 years is ₹3,310. Find the principal.
   <details>
   <summary>🔍 View Solution</summary>

   CI = P[(1.10)³-1] = P[1.331-1] = 0.331P = 3310 → P = **₹10,000
   </details>
9. A machine worth ₹1,00,000 depreciates at 20% per year. After how many years will its value be less than ₹50,000?
   <details>
   <summary>🔍 View Solution</summary>

   After 1 year: 100000×0.80 = 80000. After 2 years: 80000×0.80 = 64000.
   After 3 years: 64000×0.80 = 51200. Still above 50000.
   After 4 years: 51200×0.80 = 40960 < 50000.
   Answer: **4 years**
   </details>
10. ₹5,000 is invested at 8% SI for 3 years and ₹5,000 at 8% CI for 3 years. Find the difference between the amounts.
   <details>
   <summary>🔍 View Solution</summary>

   SI: A = 5000(1+0.08×3) = 5000×1.24 = 6200.
   CI: A = 5000×(1.08)³ = 5000×1.259712 = 6298.56.
   Difference = **₹98.56**
   </details>
11. Find the present worth of ₹5,000 due in 2 years at 10% SI.
   <details>
   <summary>🔍 View Solution</summary>

   PW = A/(1+RT/100) = 5000/(1+10×2/100) = 5000/1.20 = **₹4,166.67
   </details>
12. A sum at 15% CI becomes ₹5,000 in 2 years. What was the sum?
   <details>
   <summary>🔍 View Solution</summary>

   A = 5000 = P(1+0.15)² = P×1.3225 → P = **₹3,781.50
   </details>
13. The amount at CI is ₹6,610 and the rate is 10% for 2 years. Find the principal.
   <details>
   <summary>🔍 View Solution</summary>

   A = 6610, R=10%, T=2. A = P(1.10)² = P×1.21 → P = 6610/1.21 = **₹5,462.81
   </details>
14. At what rate will ₹800 become ₹1,000 in 2 years under CI?
   <details>
   <summary>🔍 View Solution</summary>

   1000 = 800×(1+R/100)². 1000/800 = 1.25 = (1+R/100)²
   1+R/100 = √1.25 = 1.1180 → R = **11.8%**
   </details>
15. A man borrowed ₹5,000 at 10% SI and repaid it in 2 equal annual installments. Find each installment.
   <details>
   <summary>🔍 View Solution</summary>

   Total amount with SI = 5000(1+0.10×2) = 5000×1.20 = 6000.
   Each installment = 6000/2 = **₹3,000**
   </details>
16. The population of a town was 1,00,000 two years ago and is now 1,21,000. Find the rate of growth.
   <details>
   <summary>🔍 View Solution</summary>

   Was 100000, now 121000 in 2 years. A/P = 1.21 = (1+r/100)²
   1+r/100 = √1.21 = 1.1 → r = **10%**
   </details>
17. Find the CI on ₹50,000 at 12% for 1 year compounded monthly.
   <details>
   <summary>🔍 View Solution</summary>

   Monthly: n=12, R/n=1%, nT=12. A = 50000×(1.01)^12 = 50000×1.1268 = **₹56,340
   </details>
18. A sum of ₹3,000 is invested at 10% CI. In how many years will it become ₹3,993?
   <details>
   <summary>🔍 View Solution</summary>

   3993 = 3000×(1.10)^n. (1.10)^n = 1.331 = (1.10)³ → n = **3 years
   </details>
19. The difference between CI and SI for 3 years at 10% per annum is ₹310. Find the sum.
   <details>
   <summary>🔍 View Solution</summary>

   CI-SI for 3 years = P[3R²/10000 + R³/1000000]
   = 20000[300/10000 + 1000/1000000] = 20000[0.03 + 0.001] = 20000×0.031 = 620? No.
   At R=10%, 3R²/10000 = 300/10000 = 0.03. R³/1000000 = 1000/1000000 = 0.001.
   CI - SI = P × [0.03 + 0.001] = P × 0.031.
   310 = P × 0.031 → P = **₹10,000**
   </details>
20. An article costs ₹50,000. Its value depreciates by 20% in the first year and 10% in the second year. What is its value after 2 years?
   <details>
   <summary>🔍 View Solution</summary>

   After year 1: 50000×0.80 = 40000. After year 2: 40000×0.90 = **₹36,000

   ---
   </details>


---

### 🔴 Hard Questions (1-20)

1. The CI on a sum at a certain rate for 2 years is ₹1,102 and the SI is ₹1,000. Find the rate and the sum.
   <details>
   <summary>🔍 View Solution</summary>

   CI = P[(1+R/100)²-1] = P[2R/100+R²/10000] = 1102
   SI = P×2R/100 = 1000 → P×2R/100 = 1000 → PR = 50000
   From CI formula: P[2R+R²/100]/100 = 1102
   P(2R + R²/100) = 110200
   Divide by PR=50000: (2R + R²/100)/R = 110200/50000 = 2.204
   2 + R/100 = 2.204 → R = **20.4%**
   P = 50000/20.4 = **₹2,451** (approx) — verify: SI = 2451×0.204×2 = 999.9 ≈ 1000 ✓
   CI = 2451[(1.204)²-1] = 2451×[1.4496-1] = 2451×0.4496 = 1102 ✓
   </details>
2. A sum of ₹10,000 is invested at 10% for 3 years. The rate changes to 15% for the next 2 years. Find the final amount.
   <details>
   <summary>🔍 View Solution</summary>

   After 3 years at 10%: 10000×(1.10)³ = 13310.
   After additional 2 years at 15%: A = 13310×(1.15)² = 13310×1.3225 = **₹17,600**
   </details>
3. At what rate per annum will ₹1,000 become ₹1,000,000 in 30 years under CI? (Approximate)
   <details>
   <summary>🔍 View Solution</summary>

   A = 1000×(1+R/100)^30 = 1000000. (1+R/100)^30 = 1000.
   1+R/100 = 1000^(1/30) = 10^(3/30) = 10^0.1 = 1.2589.
   R = **25.89%** (Rule of 72 gives 72/30 = 2.4% too slow. Actual requires higher rate.)
   </details>
4. The CI on a sum for 3 years at 10% is ₹3,310. Find the SI for the same period.
   <details>
   <summary>🔍 View Solution</summary>

   CI = 3310 = P[(1.10)³-1] = P×0.331 → P = 10000.
   SI = P×R×T/100 = 10000×10×3/100 = **₹3,000**
   </details>
5. A man borrows ₹20,000 at 10% CI. He pays back ₹6,000 at the end of 1 year and ₹12,000 at the end of 2 years. How much should he pay at the end of 3 years to clear the debt?
   <details>
   <summary>🔍 View Solution</summary>

   After 1 year: 20000×1.10 = 22000. Pays 6000 → balance = 16000.
   After 2 years: 16000×1.10 = 17600. Pays 12000 → balance = 5600.
   After 3 years: 5600×1.10 = **₹6,160**
   </details>
6. The population of a village is 10,000 and it grows at 5% per year. In what year will it exceed 20,000?
   <details>
   <summary>🔍 View Solution</summary>

   10000×(1.05)^n > 20000. (1.05)^n > 2. n×log(1.05) > log(2)
   n > 0.3010/0.0212 = 14.2. After **15 years** (year 2025)
   </details>
7. Find the present worth of ₹10,000 payable after 3 years at 10% CI.
   <details>
   <summary>🔍 View Solution</summary>

   PW = 10000/(1.10)³ = 10000/1.331 = **₹7,513.15
   </details>
8. A machine depreciates at 10% per year. After how many full years will its value become less than half of its original value?
   <details>
   <summary>🔍 View Solution</summary>

   Value < 0.5P: P×(0.90)^n < 0.5. (0.90)^n < 0.5.
   n×log(0.90) < log(0.5). n×(-0.0458) < -0.3010. n > 6.57.
   After **7 full years**
   </details>
9. The CI on a sum at 8% for 2 years is ₹832. Find the SI on the same sum for 3 years.
   <details>
   <summary>🔍 View Solution</summary>

   CI-SI for 2yr = P×R²/10000 = 832. SI = P×R×2/100 = 2PR/100.
   From CI = P[2R/100 + R²/10000] = 832, and PR/50 = SI.
   832 - SI = 832 - 2PR/100 = P×R²/10000.
   So 832 = 2PR/100 + PR²/10000.
   And PR/50 = SI, but we need R. From CI-SI = PR²/10000 = 832? No, that was for 2 years.
   Try R=8%: 832 = P×64/10000 → P = 832×10000/64 = **₹130,000**
   Check: SI = 130000×8×2/100 = 20800. CI = 130000×(1.08)²-130000 = 130000×0.1664 = 21632.
   Difference = 832. ✓
   SI for 3 years = 130000×8×3/100 = **₹31,200**
   </details>
10. A sum of ₹50,000 is invested at 12% CI. The rate is changed to 8% after 2 years. Find the total amount after 4 years.
   <details>
   <summary>🔍 View Solution</summary>

   After 2 years at 12%: 50000×(1.12)² = 50000×1.2544 = 62720.
   After 2 more at 8%: 62720×(1.08)² = 62720×1.1664 = **₹73,165**
   </details>
11. Find the rate at which CI and SI are equal for 2 years on a sum.
   <details>
   <summary>🔍 View Solution</summary>

   SI = CI for 2 years when: P×R×2/100 = P[(1+R/100)²-1]
   2R/100 = 2R/100 + R²/10000 → 0 = R²/10000 → R = 0%.
   So CI and SI are equal for 2 years only at **0% interest** — a trick question. Or: the question may mean find R such that amounts are equal: P(1+2R/100) = P(1+R/100)². 1+2R/100 = 1+2R/100+R²/10000 → R²=0 → R=0.
   </details>
12. A sum doubles in 10 years under SI. In how many years will it become 8 times at the same rate?
   <details>
   <summary>🔍 View Solution</summary>

   Doubles in 10 years → 100/R = 10 → R = 10% SI.
   8 times = 8P. SI for n years = P×10×n/100 = 8P → n = 80 years.
   Or: at SI, 8 times in 80 years.
   </details>
13. The effective annual rate is 21% for a certain nominal rate compounded yearly. What is the nominal rate?
   <details>
   <summary>🔍 View Solution</summary>

   Effective annual = 21% = (1+R)^1 - 1? No, if compounded yearly, nominal = effective = 21%.
   The question likely means nominal rate R, compounded more frequently, gives 21% effective.
   (1+R/n)^n - 1 = 0.21. Try n=2 (half-yearly): (1+R/2)² = 1.21 → 1+R/2 = √1.21 = 1.1 → R = 20%.
   Answer: **20% nominal**
   </details>
14. A person invests ₹X at 10% CI and another ₹X at 10% SI. After 5 years, the CI investment is ₹3,000 more than the SI investment. Find X.
   <details>
   <summary>🔍 View Solution</summary>

   CI investment after 5 years: X×(1.10)^5 = X×1.61051.
   SI investment after 5 years: X×(1+0.10×5) = X×1.50.
   Difference = X×0.11051 = 3000 → X = **₹27,150**
   </details>
15. ₹5,000 is borrowed at 10% CI. It is repaid in 2 equal annual installments. Find the value of each installment.
   <details>
   <summary>🔍 View Solution</summary>

   Let each installment = x.
   x/(1.10) + x/(1.10)² = 5000.
   x(0.9091 + 0.8264) = 5000.
   x×1.7355 = 5000 → x = **₹2,880.40**
   </details>
16. A sum of ₹4,000 is invested at 20% CI for 1.5 years. Find the amount.
   <details>
   <summary>🔍 View Solution</summary>

   A = 4000×(1.20)^1.5 = 4000×1.20×√1.20 = 4000×1.20×1.0954 = **₹5,258
   </details>
17. The difference between the amounts under CI and SI for 3 years at 10% per annum on a sum is ₹1,310. Find the sum.
   <details>
   <summary>🔍 View Solution</summary>

   CI-SI for 3 years = P[3R²/10000 + R³/1000000] = 1310.
   Try R=10%: P[0.03 + 0.001] = P×0.031 = 1310 → P = **₹42,258** (not round).
   Try R=20%: P[0.12 + 0.008] = P×0.128 = 1310 → P = **₹10,234**.
   Try R=5%: P[0.0075 + 0.000125] = P×0.007625 = 1310 → P = **₹171,803**.
   Given the structure, likely R=10% and P=10000 but diff=310.
   1310 at 10%? P = 1310/0.031 = **₹42,258**.
   At 12%: P = 1310/[3×144/10000 + 1728/1000000] = 1310/[0.0432 + 0.001728] = 1310/0.044928 = **₹29,160**.
   Without R given, the problem is underdetermined.
   </details>
18. Find the rate at which a sum will become 27 times itself in 6 years under CI.
   <details>
   <summary>🔍 View Solution</summary>

   27 = (1+R/100)^6. (1+R/100) = 27^(1/6) = (3³)^(1/6) = 3^(1/2) = √3 = 1.732. R = **73.2%
   </details>
19. A bank offers 12% per annum compounded quarterly. Another offers 12.5% per annum compounded annually. Which is better and by how much on ₹10,000 for 1 year?
   <details>
   <summary>🔍 View Solution</summary>

   Bank A: 12% quarterly = (1.03)^4 - 1 = 12.55%. Bank B: 12.5% annual.
   Bank B is better by 0.05% on ₹10,000 = **₹5** in one year.
   </details>
20. A sum of ₹10,000 is invested at 10% CI. In how many years will the interest earned equal the original principal?
   <details>
   <summary>🔍 View Solution</summary>

   Interest = P. A = 2P = P(1.10)^n. 2 = (1.10)^n.
   n = log(2)/log(1.10) = 0.3010/0.0414 = **7.27 years** ≈ 7 years and 3 months.

   ---
   </details>


---

### 🏆 Product-Based Company Level Questions (1-10)

1. An investor puts ₹50,000 into a fund that grows at 15% per year. After 3 years, she withdraws ₹20,000. What will be the amount in the account after 5 years from the start?
   <details>
   <summary>🔍 View Solution</summary>

   After 3 years: 50000×(1.15)³ = 50000×1.520875 = 76043.75.
   Withdraw 20000 → remaining = 56043.75.
   After 2 more years (5 total): 56043.75×(1.15)² = 56043.75×1.3225 = **₹74,118**
   </details>
2. A company takes a loan of ₹10,00,000 at 12% per annum compounded half-yearly. It repays ₹3,00,000 at the end of 1 year and ₹5,00,000 at the end of 2 years. What should be the final payment at the end of 3 years to clear the loan?
   <details>
   <summary>🔍 View Solution</summary>

   After 1 year (6 months: n=2, R/n=6%, nT=2): A = 1000000×(1.06)² = 1000000×1.1236 = 1123600.
   Pays 300000 → balance = 823600.
   After 2 years (total, i.e., 1 more year of compounding): 823600×(1.06)² = 823600×1.1236 = 925372.
   Pays 500000 → balance = 425372.
   After 3 years: 425372×(1.06)² = 425372×1.1236 = **₹477,936**
   </details>
3. A machine costs ₹2,00,000 and depreciates at 20% per year for the first 3 years and 10% per year thereafter. Find its value after 5 years.
   <details>
   <summary>🔍 View Solution</summary>

   After first 3 years at 20%: 200000×(0.80)³ = 200000×0.512 = 102400.
   After 2 more years at 10%: 102400×(0.90)² = 102400×0.81 = **₹82,944**
   </details>
4. The CI on a sum for 2 years at R% is ₹2,500 and the SI on the same sum for the same period is ₹2,000. Find the sum and the rate.
   <details>
   <summary>🔍 View Solution</summary>

   CI = 2500, SI = 2000. Difference = 500 = P×R²/10000.
   Also: SI = P×2R/100 = 2000 → P×R = 100000.
   From P×R²/10000 = 500: (P×R)×R/10000 = 500 → 100000×R/10000 = 500 → R = **50%**.
   P = 100000/50 = **₹2,000**.
   Check: SI = 2000×2×50/100 = 2000. ✓
   CI = 2000[(1.5)²-1] = 2000×[2.25-1] = 2500. ✓
   </details>
5. An amount at 10% CI becomes ₹12,100 in 2 years. In how many years will it become ₹26,620?
   <details>
   <summary>🔍 View Solution</summary>

   12100 = P×(1.10)² → P = 10000.
   Find n where 10000×(1.10)^n = 26620.
   (1.10)^n = 2.662. n×log(1.10) = log(2.662).
   n = 0.4253/0.0414 = **10.27 years** (approximately 10 years)
   </details>
6. A sum of ₹1,00,000 is invested. The rate of interest is 10% for the first 2 years, 20% for the next 2 years, and 5% for the remaining 1 year. Find the final amount.
   <details>
   <summary>🔍 View Solution</summary>

   After 2 years at 10%: 100000×(1.10)² = 121000.
   After 2 more at 20%: 121000×(1.20)² = 121000×1.44 = 174240.
   After 1 more at 5%: 174240×1.05 = **₹1,82,952**
   </details>
7. Two banks: Bank A offers 12% CI compounded quarterly. Bank B offers 12% CI compounded monthly. Which is better for ₹1,00,000 over 1 year, and by how much?
   <details>
   <summary>🔍 View Solution</summary>

   Bank A (quarterly): (1+0.12/4)^4 - 1 = (1.03)^4 - 1 = 0.1255 = 12.55%.
   Bank B (monthly): (1+0.125/12)^12 - 1 = (1.010417)^12 - 1 ≈ 0.1322 = 13.22%.
   Bank B is better by 0.67% on ₹1,00,000 for 1 year = **₹670** more.
   </details>
8. A sum of ₹50,000 is invested at 8% CI. After how many years will the interest earned exceed the principal?
   <details>
   <summary>🔍 View Solution</summary>

   Need CI > P: P(1.08)^n > 2P. (1.08)^n > 2.
   n > log(2)/log(1.08) = 0.3010/0.0334 = **9 years**.
   </details>
9. The population of a city was 20,00,000 in 2020 and grows at 8% per year. The government imposes a restriction and the growth rate halves after 2023. What will be the population in 2026?
   <details>
   <summary>🔍 View Solution</summary>

   2020-2023: 3 years at 8%. 2023-2026: 3 years at 4%.
   After 3 years: 20,00,000×(1.08)³ = 20,00,000×1.2597 = 25,19,400.
   After 3 more: 25,19,400×(1.04)³ = 25,19,400×1.1249 = **28,34,000** (approx).
   </details>
10. A sum of ₹5,00,000 grows at 12% per annum under CI. The inflation rate is 6% per annum. What is the real rate of return after 3 years?
   <details>
   <summary>🔍 View Solution</summary>

   Nominal return = 12%, inflation = 6%.
   Real rate = [(1+0.12)/(1+0.06)] - 1 = 1.12/1.06 - 1 = 0.0566 = **5.66%**.
   After 3 years real: P×(1.0566)³ = P×1.18. So ₹5,00,000 grows to ₹5,90,000 in real terms.

   ---
   </details>


---

## 📝 Detailed Solutions

> [!NOTE]
> All detailed solutions have been inlined directly under the questions in the **Practice Section** above for interactive study.

## 📚 Best Resources

### YouTube Channels (Ranked Best to Worst)

| Rank | Channel | Why It's Best |
|---|---|---|
| 1 | **Aditya Ranjan (RBE)** | Hindi, fast CI methods, Rule of 72 tricks |
| 2 | **Waji Academy** | English, clean SI/CI explanations |
| 3 | **Gagan Matta** | Shortcuts, installment formula |
| 4 | **Dear Sir** | Strong foundation |
| 5 | **Amar Sir** | Previous year questions |
| 6 | **Khan Academy** | Conceptual depth |

### Websites

| Rank | Website | Best For |
|---|---|---|
| 1 | **IndiaBix.com** | SI/CI practice questions |
| 2 | **Testbook.com** | Mock tests |
| 3 | **GeeksforGeeks** | Advanced SI/CI, formulas |
| 4 | **M4Maths.com** | TCS NQT archives |
| 5 | **Investopedia.com** | Understanding financial concepts |

### Books

| Rank | Book | Best For |
|---|---|---|
| 1 | **Quantum CAT by Sarvesh Verma** | Complete SI/CI coverage |
| 2 | **Arun Sharma (TMH)** | Systematic approach |
| 3 | **RS Agarwal** | Basic to medium |
| 4 | **Fast Track Objective Arithmetic** | Quick revision |
| 5 | **NCERT Class 8-10** | Foundation |

### Practice Platforms

| Rank | Platform | Best For |
|---|---|---|
| 1 | **IndiaBix** | Real exam patterns |
| 2 | **Testbook Mock Tests** | Timed tests |
| 3 | **Prepins (TCS)** | TCS-specific |
| 4 | **Campusgate** | Product company questions |

---

## 🎯 Final Verdict

### Importance Rating: ★★★★☆ (4/5)

SI/CI is the financial engine of aptitude — it turns percentage skills into real-world money problems. Every company tests it, the questions are formula-driven (fast to solve once formulas are memorized), and the concepts appear in interviews at finance and product companies.

### Placement ROI Score: **8/10**
- Appears in every test (2-5 questions)
- Formula-driven → fast solving once mastered
- SI-CI difference formula alone appears in 60% of questions
- Rule of 72 is a free shortcut that saves significant time

### Difficulty Score: **5/10**
- 70% Easy–Medium (formulas, substitution)
- 30% Hard (installments, fractional periods, varying rates)
- The hard parts are formula-based, not concept-based — learn the formulas and they're solvable

### Priority Order: **#4 — After Number Systems, Percentages, P&L**

The flow is logical: Numbers → Percentages → P&L → SI/CI. Each builds on the previous. SI/CI essentially applies percentages over time, and P&L already taught you the three-price framework (CP, SP, MP) which maps to (Principal, Amount, Interest).

### Company Level Verdict

| Target | Mandatory/Important/Optional | Reasoning |
|---|---|---|
| **10 LPA+ (Service)** | ✅ **Mandatory** | 2-4 questions, easy-medium, high accuracy possible |
| **20 LPA+ (Service)** | ✅ **Mandatory** | 2-4 questions, formula-heavy, moderate difficulty |
| **Product-Based (Amazon, Microsoft)** | ✅ **Important** | Growth, depreciation, varying rates appear |
| **Top Product (Google, Goldman)** | ✅ **Important** | EMI, present worth, effective rate, financial modeling |

---

### The One Insight That Changes Everything

**CI always beats SI after the first year, and the gap is P×R²/10000 for 2 years.**

That's the single most-asked formula in placement tests. If you remember nothing else from this topic, remember that one.

The second most important insight: **Rule of 72**. At any compound rate R%, your money doubles in approximately 72/R years. At 9%, it doubles in 8 years. At 12%, it doubles in 6 years. At 15%, it doubles in about 4.8 years. This is not just useful for exams — it's genuinely useful in life.

---

*Guide compiled for placement-focused aptitude preparation. Questions sourced and adapted from TCS NQT, Infosys, Amazon, Goldman Sachs, and Microsoft archives.*
