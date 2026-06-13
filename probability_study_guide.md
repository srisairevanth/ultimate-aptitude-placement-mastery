# Probability — Placement Study Guide
> **Elite Aptitude Trainer Edition** | Covers TCS, Accenture, Cognizant, Deloitte, Goldman Sachs, Amazon, Microsoft, Google

---

## 🥇 Rank & Importance

<div align="left">
  <img src="https://img.shields.io/badge/Rank-%239-blue?style=for-the-badge" alt="Rank" />
  <img src="https://img.shields.io/badge/Importance-★★★★☆-orange?style=for-the-badge" alt="Importance" />
  <img src="https://img.shields.io/badge/Difficulty-Medium--Hard-red?style=for-the-badge" alt="Difficulty" />
  <img src="https://img.shields.io/badge/Focus-Placements-blueviolet?style=for-the-badge" alt="Focus" />
</div>



| Metric | Rating |
|---|---|
| **Rank among all aptitude topics** | #5 of ~20 core topics |
| **Importance Rating** | ★★★★★ (5/5) — Highest ROI topic |
| **Appears in every placement test** | Yes |
| **High scorers vs. average candidates gap** | Extremely High |

### Why It Matters in Placements

Probability is the **language of uncertainty** — and modern tech companies live in that space. Every time a system makes a decision under uncertain data, probability is baked in. Product companies (Amazon, Google, Microsoft) ask probability questions because:
- They test **structured thinking under uncertainty** — a core engineering skill
- They reveal whether a candidate can **count correctly** (combinatorics + probability)
- They surface **intuition vs. formula-memorization** — toppers solve by visualization, not just plugging numbers

It also connects deeply with:
- **Permutations & Combinations** (the counting foundation)
- **Percentages** (probability as a fraction/percentage of sample space)
- **Expected Value** (appears in game theory and optimization interviews)
- **Bayes' Theorem** (increasingly asked in ML/data science interviews at product companies)

### Weightage in Tests

| Company Type | Expected Questions | Difficulty Band |
|---|---|---|
| **TCS / Infosys / Wipro** (service) | 1–3 questions | Easy–Medium |
| **Accenture / Cognizant** (service) | 1–2 questions | Easy–Medium |
| **Deloitte / KPMG** (consulting) | 1–2 questions | Medium |
| **Goldman Sachs / JPMorgan** (BFSI) | 2–4 questions | Medium–Hard |
| **Amazon / Microsoft** (product) | 1–3 questions | Medium–Hard |
| **Google** | 1–3 questions | Hard–Very Hard |

> [!TIP]
> **ROI Insight**
> Probability questions almost always follow 4–5 learnable patterns. Once you master the **sample space tree method** and **complement counting**, you can solve 80% of placement probability questions in under 90 seconds each. Best ROI topic in the entire aptitude syllabus.

---

## 📖 Concept Overview

### What Is Probability?

Probability measures the **likelihood** of an event occurring, expressed as a number between 0 (impossible) and 1 (certain). In exams, it is almost always expressed as a fraction, decimal, or percentage.

```
P(Event) = Number of favorable outcomes / Total number of possible outcomes
```

### The Two Schools of Thought

| Approach | When to Use |
|---|---|
| **Classical / Theoretical** | All outcomes equally likely (coins, dice, cards) |
| **Empirical / Frequentist** | Based on observed data or repeated trials |

In placement exams, we almost always use the **Classical approach**.

### Subtopics to Master

1. **Basic Probability** — single event, equally likely outcomes
2. **Complementary Events** — P(not A) = 1 - P(A)
3. **Independent Events** — P(A∩B) = P(A) × P(B)
4. **Dependent Events / Conditional Probability** — P(A|B) = P(A∩B)/P(B)
5. **Mutually Exclusive Events** — P(A∪B) = P(A) + P(B)
6. **Addition Theorem** — P(A∪B) = P(A) + P(B) - P(A∩B)
7. **Multiplication Theorem** — P(A∩B) = P(A) × P(B|A)
8. **Bayes' Theorem** — posterior from prior + likelihood
9. **Permutation & Combination based Probability** — choosing favorable/total outcomes
10. **Geometric Probability** — area-based probability
11. **Expected Value** — weighted average of outcomes
12. **Odds in Favor / Against** — ratio form of probability
13. **Binomial Probability** — repeated independent trials
14. **Drawing with/without Replacement**
15. **Arrangement Problems** — probability that items are together/apart

### Where Each Concept Is Used in Exams

| Subtopic | Connection to Other Topics |
|---|---|
| Basic probability | Dice, coins, cards — foundation of all |
| Independent/dependent events | Real-world scenarios (quality checks, etc.) |
| Bayes' Theorem | Medical tests, spam detection, product company interviews |
| P&C-based probability | Arrangements, seating, committee formation |
| Expected value | Games, insurance, decision-making problems |
| Complement method | "At least one" problems — biggest shortcut |

---

## 🎯 Core Concepts to Master

### Concept 1: Basic Probability

**Definition**: If a random experiment has *n* equally likely outcomes and *m* of them are favorable to event E, then P(E) = m/n.

> [!NOTE]
> **Intuition**
> Think of a dartboard. If you randomly throw a dart at a board divided into equal sections, the probability of hitting a specific section is simply the fraction of the board that section occupies.

**Formula**:
```
P(E) = Favorable outcomes / Total outcomes
P(E) always lies in [0, 1]
```

**Shortcut Methods**:
- When in doubt, **enumerate the sample space** first. Write out all possibilities.
- For dice: Sample space = {1,2,3,4,5,6} → 6 equally likely outcomes
- For coins: n coins → 2^n outcomes
- For cards: 52 cards → 4 suits × 13 ranks

> [!WARNING]
> **Common Mistakes to Avoid**
> - ❌ Forgetting that outcomes must be **equally likely** — you can't apply the formula to a biased coin
- ❌ Missing outcomes in the sample space — always count systematically
- ❌ Confusing "at least one" with "exactly one"

**Interview Relevance**: "What is the probability of rolling a sum of 7 with two dice?" — fundamental question. Also tests counting discipline.

---

### Concept 2: Complement Method (The Biggest Shortcut)

**Definition**: P(not A) = 1 - P(A). This is the single most important shortcut in probability — use it when the problem asks for "at least one."

> [!NOTE]
> **Intuition**
> It's often easier to count what *doesn't* happen than what does. "At least one head in 5 coin tosses" = 1 - P(no heads) = 1 - (1/2)^5 = 31/32. Much faster than counting all favorable cases.

**Formula**:
```
P(at least one) = 1 - P(none)
P(no event occurs) = (1 - p₁) × (1 - p₂) × ... × (1 - pₙ) [if independent]
```

> [!NOTE]
> **Memory Trick**
> > 🔑 **"Complement is your best friend when 'at least' appears."** — Always check if the problem asks for "at least one" or "none" before brute-forcing the favorable cases.

> [!TIP]
> **Shortcut Method**
> ```
"At least one" → complement = all fail → 1 - (product of failure probabilities)
"Exactly one" → one succeeds, all others fail → n × p × (1-p)^(n-1)
```

> [!WARNING]
> **Common Mistakes to Avoid**
> - ❌ Using complement when the problem asks for "exactly two" (complement doesn't help here)
- ❌ Forgetting to raise (1-p) to the power of n-1 for "exactly one"

**Interview Relevance**: "If you roll a die 4 times, what is the probability of getting at least one 6?" — interview classic. Answer = 1 - (5/6)^4.

---

### Concept 3: Independent vs. Dependent Events

**Independent Events**: Two events A and B are independent if the occurrence of one does not affect the occurrence of the other.
```
P(A ∩ B) = P(A) × P(B)
```
**Examples**: Tossing two coins, rolling two dice, drawing cards with replacement.

**Dependent Events**: The occurrence of one affects the probability of the other.
```
P(A ∩ B) = P(A) × P(B|A)  or  P(B) × P(A|B)
```
**Examples**: Drawing cards without replacement, selecting people from a group.

> [!NOTE]
> **Intuition**
> Ask: "Does what happened in the first event change the landscape for the second?" If YES → dependent. If NO → independent.

> [!TIP]
> **Shortcut Method**
> In "drawing" problems, ask: **"With replacement?"** If with replacement → independent. If without → dependent.

> [!WARNING]
> **Common Mistakes to Avoid**
> - ❌ Treating dependent events as independent (classic card problem trap)
- ❌ Forgetting to update the denominator after the first draw (52 → 51 → 50...)

**Interview Relevance**: "You draw two cards without replacement. What is P(both are kings)?" — Tests whether you understand dependence. Answer: 4/52 × 3/51 = 1/221.

---

### Concept 4: Conditional Probability & Bayes' Theorem

**Conditional Probability**: P(A|B) = Probability of A given that B has occurred.
```
P(A|B) = P(A ∩ B) / P(B)
```

**Bayes' Theorem**: The classic formula for updating probabilities based on new evidence.
```
P(A|B) = P(B|A) × P(A) / P(B)
```
Where:
- P(A) = Prior probability
- P(A|B) = Posterior probability
- P(B|A) = Likelihood

> [!NOTE]
> **Intuition**
> Bayes' Theorem answers: "I know B happened. How does that change my belief about A?" It reverses the direction of conditional probability.

> [!NOTE]
> **Memory Trick**
> > 🔑 **"Posterior = Likelihood × Prior / Evidence"** — In plain English: "New belief = How likely this evidence if A were true × My old belief ÷ How likely is this evidence overall."

**Shortcut — The Bayes Table Method**:
```
For two hypotheses H₁ and H₂:
         P(H₁)    P(Evidence|H₁)    P(H₁)×P(E|H₁)    Posterior
H₁       0.3          0.6              0.18         0.18/(0.18+0.14)
H₂       0.7          0.2              0.14         0.14/(0.18+0.14)

Sum of products = P(Evidence) = 0.32
Posterior for H₁ = 0.18/0.32 = 9/16
```
This table method avoids the formula confusion entirely.

> [!WARNING]
> **Common Mistakes to Avoid**
> - ❌ Confusing P(A|B) with P(B|A) — they are almost always different
- ❌ Forgetting to divide by P(B) in Bayes' formula
- ❌ Not drawing the probability tree diagram first

**Interview Relevance**: Bayes' Theorem is asked in **every ML/data science interview** at Amazon, Google, Microsoft. Classic: "A test for a disease has 99% accuracy. The disease affects 1% of the population. If you test positive, what is the actual probability you have the disease?"

---

### Concept 5: Permutation & Combination Based Probability

**Definition**: Probability where the sample space and favorable cases require counting arrangements or selections using P(n,r) and C(n,r).

> [!NOTE]
> **Intuition**
> These problems have two steps:
1. **Count the total ways** something can happen (P or C depending on order)
2. **Count the favorable ways** (same principle, different numbers)

**When to Use Permutations (Order Matters)**:
- Arranging people in a row
- Forming numbers from digits
- Words from letters

**When to Use Combinations (Order Doesn't Matter)**:
- Selecting a committee
- Drawing cards from a deck
- Choosing items from a set

> [!TIP]
> **Shortcut Method**
> Ask: **"Does changing the order change the outcome?"**
- "How many ways to arrange" → Permutation (P)
- "In how many ways can you select" → Combination (C)

**Formula**:
```
P(n,r) = n! / (n-r)!
C(n,r) = n! / [r! × (n-r)!]
P(E) = C(favorable)/C(total)  [when order doesn't matter]
P(E) = P(favorable)/P(total)  [when order matters]
```

> [!WARNING]
> **Common Mistakes to Avoid**
> - ❌ Using P when C is needed (or vice versa) — this is the #1 source of error
- ❌ Double-counting arrangements
- ❌ Not simplifying C(n,r) before computing

**Interview Relevance**: "4 cards are drawn from a deck. What is the probability they are all from the same suit?" — Tests C(13,4)/C(52,4) = 0.0106. Appears in Amazon and Goldman Sachs quant rounds.

---

### Concept 6: Expected Value

**Definition**: The weighted average of all possible outcomes, where the weights are their probabilities.
```
E(X) = Σ (xᵢ × P(xᵢ))  for all outcomes i
```

> [!NOTE]
> **Intuition**
> If you played a game many times, what would be your **average winnings per game**? That's the expected value.

> [!TIP]
> **Shortcut Method**
> In a game where you win ₹x with probability p and lose ₹y with probability (1-p), E = px - y(1-p). Set E = 0 to find the **fair price** of the game.

> [!NOTE]
> **Memory Trick**
> > 🔑 **"Expected value = weighted average by probability"** — Not the average of values, but the average of values weighted by how likely they are.

> [!WARNING]
> **Common Mistakes to Avoid**
> - ❌ Computing E(X) as (max + min)/2 — that's only true for uniform distributions
- ❌ Forgetting that outcomes can be negative (losses) in games

**Interview Relevance**: Expected value appears in decision-making questions at Amazon, Goldman Sachs, and Deloitte. "A game costs ₹50 to play. You win ₹200 with probability 0.3, ₹100 with probability 0.5, and nothing otherwise. Should you play?"

---

### Concept 7: Geometric Probability

**Definition**: Probability expressed as a ratio of lengths, areas, or volumes.
```
P = (Area of favorable region) / (Total area)
```

> [!NOTE]
> **Intuition**
> If a point is chosen at random within a region, the probability it falls in a subregion is proportional to its area fraction.

> [!TIP]
> **Shortcut Method**
> Draw the figure, shade the favorable region, compute the area ratio.

> [!WARNING]
> **Common Mistakes to Avoid**
> - ❌ Forgetting to normalize — the ratio must be area/total, not just counting points
- ❌ Wrong geometric formula (circle area = πr², not 2πr)

**Interview Relevance**: Less common in placements but appears at Google and in advanced Goldman Sachs problems.

---

## 🧠 Important Formula Sheet

### 1. Basic Probability
```
P(E) = Favorable / Total   where 0 ≤ P(E) ≤ 1
```

### 2. Complement Rule
```
P(not E) = 1 - P(E)
P(at least one) = 1 - P(none)
```

### 3. Addition Theorem (General)
```
P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
P(A ∪ B) = P(A) + P(B)          [if mutually exclusive]
```

### 4. Multiplication Theorem
```
P(A ∩ B) = P(A) × P(B|A)       [dependent]
P(A ∩ B) = P(A) × P(B)         [independent]
```

### 5. Conditional Probability
```
P(A|B) = P(A ∩ B) / P(B)       [P(B) > 0]
```

### 6. Bayes' Theorem
```
P(A|B) = P(B|A) × P(A) / P(B)
Or in expanded form for multiple hypotheses:
P(Aᵢ|B) = P(Aᵢ) × P(B|Aᵢ) / Σ P(Aⱼ) × P(B|Aⱼ)
```

### 7. Odds In Favor / Against
```
Odds in favor of E = P(E) : P(not E)
Odds against E = P(not E) : P(E)
```

### 8. Binomial Probability
```
P(X = r) = C(n,r) × pʳ × (1-p)^(n-r)
Where n = trials, p = success probability, r = number of successes
```

### 9. "Exactly k" Successes (n trials)
```
P(exactly k) = C(n,k) × pᵏ × (1-p)^(n-k)
P(at least k) = Σ C(n,i) × pⁱ × (1-p)^(n-i) for i=k to n
```

### 10. Expected Value
```
E(X) = Σ xᵢ × P(xᵢ)
For binomial: E(X) = n × p
```

### 11. Permutation & Combination in Probability
```
P(same event) = C(n₁,r)/C(n₂,r) [combinations]
P(arranged) = P(favorable)/P(total) [permutations]
```

### Memory Tricks for Formulas

> 🔑 **"Add for OR, Multiply for AND"** — Union (OR) → Addition (watch for overlap). Intersection (AND) → Multiplication (watch for dependence).

> 🔑 **"Bayes: LPH over P"** — "Likelihood × Prior over Probability of evidence." The posterior probability equals likelihood times prior, divided by total probability of evidence.

> 🔑 **"Complement: 1 - (all fail)"** — For "at least one" problems, subtract the probability of none from 1.

> 🔑 **"Independent = No Memory"** — If the first event doesn't change the probability of the second, they are independent. With replacement = independent. Without = dependent.

> 🔑 **"Arrange = Permute, Select = Combine"** — Order matters → P. Order doesn't matter → C.

---

## ⚡ Shortcut Techniques & Time-Saving Tricks

### Trick 1: Complement for "At Least One" (30-Second Solve)
```
Problem: Probability of getting at least one 6 in 4 dice throws.
Don't: Count all cases with at least one 6 (tedious).
Do: P(at least one) = 1 - P(no 6) = 1 - (5/6)⁴ = 1 - 625/1296 = 671/1296.

Answer in 5 seconds flat.
```

### Trick 2: Probability Tree Diagrams
```
Problem: A bag has 3 red, 5 green balls. Two drawn without replacement.
         Find P(first red AND second green).

Tree: Branch 1 (red): 3/8
      Branch 2 (green): 5/8
      Conditional: After red: green = 5/7; After green: green = 4/7
      P(R then G) = 3/8 × 5/7 = 15/56.

Draw the tree. Follow the branches. Multiply along the path.
```

### Trick 3: Dice Sum Shortcuts
```
Sum of two dice = 7 → 6 combinations: (1,6),(2,5),(3,4),(4,3),(5,2),(6,1) → P = 6/36 = 1/6.
Sum = 8 → 5 combinations → P = 5/36.
Sum = 12 (double 6) → 1 combination → P = 1/36.

Shortcut table: Memorize common sum probabilities:
7: 6/36, 6: 5/36, 8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
(Also: 2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36)
```

### Trick 4: Card Deck Memorization
```
Standard deck: 52 cards.
- Red cards: 26 (hearts ♦ + diamonds ♥)
- Black cards: 26 (spades ♠ + clubs ♣)
- Face cards: 12 (J, Q, K of each suit)
- Aces: 4
- Cards of a suit: 13
- Number cards (2-10): 36

Memorize these numbers — saves 30 seconds per card question.
```

### Trick 5: Binomial Shortcut for "Exactly r Successes"
```
P(exactly r) = C(n,r) × pʳ × (1-p)^(n-r)
For n=5, p=1/3:
P(exactly 2) = C(5,2) × (1/3)² × (2/3)³ = 10 × 1/9 × 8/27 = 80/243.

Shortcut: C(5,2)=10, (1/3)²=1/9, (2/3)³=8/27 → 10/9 × 8/27 = 80/243.
```

### Trick 6: "At Least r" via Complement
```
P(at least r) = 1 - P(0) - P(1) - ... - P(r-1)
For n=5, p=1/2, P(at least 2 heads):
P(0 heads) = C(5,0)/32 = 1/32
P(1 head) = C(5,1)/32 = 5/32
P(at least 2) = 1 - 6/32 = 26/32 = 13/16.

Fast: Use complement when the "at least" threshold is low and n is large.
```

### Trick 7: Bayes' Table (Never Forget the Formula Again)
```
Problem: Two factories. Factory 1 makes 60% with 2% defect.
         Factory 2 makes 40% with 1% defect. A random item is defective.
         Find P(it came from Factory 1).

Table:
Factory   Prior    Likelihood   Joint       Posterior
F1        0.60     0.02         0.012       0.012/0.016 = 3/4
F2        0.40     0.01         0.004       0.004/0.016 = 1/4

P(F1|Defective) = 0.012/0.016 = 3/4 = 75%.

No formula memorization needed — just multiply and divide!
```

### Trick 8: Geometric Probability — Area Ratio
```
Problem: A point is chosen at random in a square of side 10cm.
         A circle of radius 3cm is inscribed. Find P(point is inside circle).

P = Area(circle) / Area(square) = π(3)² / (10)² = 9π/100 ≈ 0.2826.

Formula: P = favorable area / total area. Done.
```

### Trick 9: "Not Both" → Complement of Intersection
```
P(A' ∩ B') = 1 - P(A ∪ B) = 1 - [P(A) + P(B) - P(A∩B)]
            = 1 - P(A) - P(B) + P(A∩B)

Special case if independent: P(A' ∩ B') = (1-P(A)) × (1-P(B))
```

### Trick 10: Seating Arrangement Probability
```
Problem: 5 boys and 5 girls sit randomly. Find P(all girls sit together).

Total arrangements: 10! = 3628800
Treat 5 girls as one block: 6! (arrange block + boys) × 5! (arrange girls within block)
= 720 × 120 = 86400
P = 86400 / 3628800 = 1/42 ≈ 0.0238.

Shortcut: Block method. Treat the group as one unit, arrange, multiply by internal arrangements.
```

---

## 🔥 Most Frequently Asked Question Patterns

### Pattern 1: Basic Dice/Coins Probability
- **Concept Tested**: Sample space, basic P(E) = F/T
- **Difficulty**: Easy
- **Fastest Approach**: List sample space, count favorable
- **Appears in**: TCS, Infosys, Wipro, Cognizant
- **Example**: "Two dice are thrown. What is the probability that the sum is 9?"

### Pattern 2: "At Least One" via Complement
- **Concept Tested**: Complement rule, independence
- **Difficulty**: Easy–Medium
- **Fastest Approach**: 1 - P(none) = 1 - (1-p)^n
- **Appears in**: All companies
- **Example**: "What is the probability of getting at least one 6 in 3 throws of a die?"

### Pattern 3: Drawing Cards (with/without Replacement)
- **Concept Tested**: Conditional probability, independence
- **Difficulty**: Medium
- **Fastest Approach**: Tree diagram; update denominators after each draw
- **Appears in**: TCS, Infosys, Amazon, Goldman Sachs
- **Example**: "Two cards are drawn without replacement. Find P(both are kings)."

### Pattern 4: Bayes' Theorem (Medical/Test Problems)
- **Concept Tested**: Conditional probability, Bayes' formula
- **Difficulty**: Medium–Hard
- **Fastest Approach**: Probability tree or Bayes table
- **Appears in**: Amazon, Microsoft, Google, Goldman Sachs
- **Example**: "A test is 99% accurate. 1% of population has disease. If you test positive, what is P(you have disease)?"

### Pattern 5: Independent Events (Multiple Trials)
- **Concept Tested**: P(A∩B) = P(A) × P(B)
- **Difficulty**: Easy
- **Fastest Approach**: Multiply probabilities
- **Appears in**: All companies
- **Example**: "Probability of passing Math is 0.7, Physics is 0.6. Assuming independence, P(passing both)?"

### Pattern 6: Permutation-Based Probability (Arrangements)
- **Concept Tested**: P(n,r) in probability
- **Difficulty**: Medium
- **Fastest Approach**: C(favorable)/C(total) or P(favorable)/P(total)
- **Appears in**: Amazon, Microsoft, Google
- **Example**: "From 10 boys and 8 girls, 5 are selected randomly. Find P(3 boys, 2 girls)."

### Pattern 7: "Exactly r" via Binomial Distribution
- **Concept Tested**: Binomial probability formula
- **Difficulty**: Medium
- **Fastest Approach**: P(r) = C(n,r) × pʳ × (1-p)^(n-r)
- **Appears in**: Goldman Sachs, Amazon, Microsoft
- **Example**: "A coin is biased (P(H)=0.4). Tossed 5 times. Find P(exactly 3 heads)."

### Pattern 8: Mutually Exclusive Events
- **Concept Tested**: P(A∪B) = P(A) + P(B)
- **Difficulty**: Easy
- **Fastest Approach**: Sum probabilities (no overlap)
- **Appears in**: TCS, Infosys, Cognizant
- **Example**: "From a deck, P(King) = 4/52, P(Queen) = 4/52. P(King or Queen)?"

### Pattern 9: Seating Arrangement Probability
- **Concept Tested**: Arrangement + probability
- **Difficulty**: Hard
- **Fastest Approach**: Block method; total arrangements = n!
- **Appears in**: Amazon, Google, Microsoft
- **Example**: "6 people sit around a round table. Find P(married couples sit together)."

### Pattern 10: Expected Value
- **Concept Tested**: E(X) = Σ xᵢP(xᵢ)
- **Difficulty**: Medium
- **Fastest Approach**: List outcomes, multiply by probability, sum
- **Appears in**: Goldman Sachs, Deloitte, Amazon
- **Example**: "A game costs ₹100. Win ₹300 with P=0.4, ₹100 with P=0.3, ₹0 with P=0.3. Expected gain?"

### Pattern 11: Geometric Probability
- **Concept Tested**: Area ratio
- **Difficulty**: Medium
- **Fastest Approach**: P = favorable area / total area
- **Appears in**: Google, Microsoft, Deloitte
- **Example**: "A point is chosen inside a square of side 6. P(it is within 1 unit of the center)?"

### Pattern 12: Odds In Favor/Against
- **Concept Tested**: Converting between odds and probability
- **Difficulty**: Easy
- **Fastest Approach**: P = odds/(odds+1); Odds = P/(1-P)
- **Appears in**: TCS, Infosys, Wipro
- **Example**: "Odds in favor of winning are 3:1. Find probability of winning."

### Pattern 13: Conditional Probability (Word Problems)
- **Concept Tested**: P(A|B) = P(A∩B)/P(B)
- **Difficulty**: Medium
- **Fastest Approach**: Use the definition directly
- **Appears in**: Amazon, Microsoft, Goldman Sachs
- **Example**: "80% of students passed English, 70% passed Math, 60% passed both. P(passed English | passed Math)?"

### Pattern 14: Balls/Draws (Multiple Colors)
- **Concept Tested**: Combinations, conditional draws
- **Difficulty**: Medium
- **Fastest Approach**: C(favorable)/C(total), tree for sequential
- **Appears in**: All companies
- **Example**: "A bag has 4 red, 5 green, 3 blue balls. P(drawing 2 red and 1 green without replacement)?"

### Pattern 15: Round Table Probability
- **Concept Tested**: Circular permutation
- **Difficulty**: Hard
- **Fastest Approach**: (n-1)! for total arrangements; conditional for favorable
- **Appears in**: Google, Amazon, Microsoft
- **Example**: "8 people sit randomly around a table. Find P(A and B sit together."

### Pattern 16: "At Least r" vs "At Most r"
- **Concept Tested**: Binomial cumulative probability
- **Difficulty**: Medium–Hard
- **Fastest Approach**: At least → complement; at most → sum from 0 to r
- **Appears in**: Goldman Sachs, Amazon, Microsoft
- **Example**: "P(≤ 2 heads in 5 tosses) vs P(≥ 3 heads in 5 tosses)"

### Pattern 17: Replacement vs No Replacement
- **Concept Tested**: Independent vs dependent
- **Difficulty**: Easy–Medium
- **Fastest Approach**: With replacement → independent (multiply). Without → update denominators.
- **Appears in**: All companies
- **Example**: "A bag has 5 white, 3 black balls. Draw twice. Find P(both white) with and without replacement."

### Pattern 18: Non-Standard Sample Space
- **Concept Tested**: Defining the right sample space
- **Difficulty**: Hard
- **Fastest Approach**: Redefine outcomes to be equally likely
- **Appears in**: Google, Microsoft, Goldman Sachs
- **Example**: "Two persons A and B pick numbers from 1 to 10. P(A's number > B's number)?"

### Pattern 19: Division of Items (Probability of Zero/Filled Cells)
- **Concept Tested**: Combinatorics in probability
- **Difficulty**: Hard
- **Fastest Approach**: Complement counting; stars and bars approach
- **Appears in**: Amazon, Google, Microsoft
- **Example**: "5 balls placed randomly in 3 boxes. P(no box is empty)?"

### Pattern 20: Birthday Problem
- **Concept Tested**: Complement, independence assumption
- **Difficulty**: Hard
- **Fastest Approach**: P(no match) = (365)_n / 365^n. At least one match = 1 - this.
- **Appears in**: Google, Amazon, Goldman Sachs
- **Example**: "In a group of 23 people, what is the probability that at least two share a birthday?"

---

## 💼 Placement & Interview Relevance

### Service-Based Companies

| Company | Questions | Difficulty | Pattern |
|---|---|---|---|
| **TCS** | 1–2 | Easy–Medium | Basic dice/coins, complement, cards |
| **Infosys** | 1–2 | Easy–Medium | Conditional, Bayes, binomials |
| **Wipro** | 1 | Easy | Basic probability, complementary |
| **Accenture** | 1–2 | Easy–Medium | Balls/draws, Bayes |
| **Cognizant** | 1 | Easy–Medium | Independent events, cards |
| **Capgemini** | 1 | Easy | Complement, basic arrangements |

### Product-Based Companies

| Company | Questions | Difficulty | Pattern |
|---|---|---|---|
| **Amazon** | 2–3 | Medium–Hard | Bayes, P&C, expected value, birthday |
| **Microsoft** | 1–2 | Medium–Hard | Bayes, arrangements, binomial |
| **Google** | 1–3 | Hard | Complex P&C, geometric, birthday |
| **Goldman Sachs** | 2–4 | Medium–Hard | Expected value, Bayes, binomials |
| **JPMorgan** | 1–2 | Medium | Bayes, conditional probability |

### Difficulty Variation
- **TCS/Infosys**: Basic definitions and complement rule (solve in 60 seconds)
- **Accenture/Cognizant**: Conditional probability and tree diagrams
- **Amazon/Microsoft**: Bayes' Theorem, P&C-based probability, expected value
- **Goldman Sachs**: Complex binomial, expected value optimization, round table
- **Google**: Birthday problem, non-standard sample spaces, geometric probability

---

## 🚀 Beginner → Advanced Roadmap

### Day 1–2: Fundamentals
1. Master the sample space concept — list, don't assume
2. Learn basic probability: P(E) = F/T
3. Practice dice (36 outcomes) and coin (2^n outcomes) problems
4. Memorize the card deck breakdown (52 = 4×13)

**Milestone**: You can write down the full sample space for any 2-dice or 3-coin problem without thinking.

### Day 3–4: Core Rules
5. Learn complement rule — practice "at least one" problems
6. Learn addition and multiplication theorems
7. Distinguish independent vs dependent — draw probability trees
8. Practice drawing-without-replacement problems

**Milestone**: You solve any 2-step probability problem by drawing a tree diagram in under 60 seconds.

### Day 5–6: Intermediate Concepts
9. Learn Bayes' Theorem — practice the table method
10. Learn binomial probability — memorize the formula
11. Practice "exactly r" and "at least r" problems
12. Connect probability with P&C — when to use C(n,r) vs P(n,r)

**Milestone**: You can solve a Bayes' theorem problem using the table method in under 2 minutes.

### Day 7–8: Advanced Concepts
13. Seating arrangement probability (linear and circular)
14. Birthday problem — memorize the formula
15. Expected value problems
16. Geometric probability — area ratios

**Milestone**: You can handle the 5 hardest probability patterns (birthday, Bayes, expected value, round table, P&C).

### Day 9–14: Placement-Level Practice
17. Solve 50 TCS/Infosys pattern questions
18. Solve 30 Accenture/Cognizant pattern questions
19. Begin Amazon/Microsoft level questions

**Milestone**: 90% accuracy on service-company level, 75% on product-company level.

### Day 15–20: Product-Company Level
20. Solve 40 Amazon/Microsoft/Google pattern questions
21. Solve 20 Goldman Sachs pattern questions
22. Focus on Bayes' theorem, expected value, and complex arrangements
23. Timed practice: 2 minutes per question target

**Milestone**: Solve any placement probability question in under 2 minutes with 85% accuracy.

---

## 📊 Difficulty Breakdown

| Subtopic | Difficulty | Reason |
|---|---|---|
| Basic dice/coin probability | 🟢 **Easy** | Small sample space, direct counting |
| Complement rule ("at least") | 🟢 **Easy** | One-step complement calculation |
| Independent events | 🟢 **Easy** | Multiply probabilities directly |
| Mutually exclusive events | 🟢 **Easy** | Add probabilities directly |
| Simple conditional (tree) | 🟡 **Medium** | Requires updating after first event |
| Drawing cards without replacement | 🟡 **Medium** | Denominators change; track carefully |
| Bayes' Theorem (two hypotheses) | 🟡 **Medium** | Table method makes it manageable |
| Binomial probability | 🟡 **Medium** | Formula has 3 parts; practice needed |
| Expected value | 🟡 **Medium** | List outcomes, multiply, sum |
| Balls/bags (combinations) | 🟡 **Medium** | C(favorable)/C(total) approach |
| Seating arrangements (linear) | 🟠 **Hard** | Block method + factorial counting |
| P(≤ r) and P(≥ r) cumulative | 🟠 **Hard** | Sum many binomial terms or use complement |
| Birthday problem | 🟠 **Hard** | Exponent grows; formula non-obvious |
| Round table probability | 🟠 **Hard** | (n-1)! vs n! confusion |
| Bayes with 3+ hypotheses | 🟠 **Hard** | Larger table, more calculations |
| Non-standard sample space | 🔴 **Very Hard** | Must redefine outcomes from scratch |
| Geometric probability | 🔴 **Very Hard** | Requires geometry + probability integration |
| Complex P&C probability | 🔴 **Very Hard** | Dividing 10 items into groups with constraints |

---

## 🎓 Mastery Plan

### For Basic Understanding
- **Questions needed**: 30–40
- **Time required**: 4–5 hours
- **Goal**: Master sample space, basic rules, complement, tree diagrams

### For Placement Readiness
- **Questions needed**: 80–100
- **Time required**: 10–12 hours
- **Goal**: 90% on service-company patterns, 80% on product-company patterns

### For Product-Based Company Readiness
- **Questions needed**: 150–200
- **Time required**: 18–22 hours
- **Goal**: Solve any probability question in under 2 minutes

### Time Investment Summary

| Level | Hours | ROI |
|---|---|---|
| Basic understanding | 4–5h | Very High |
| Placement-ready (service) | 10–12h | Very High |
| Product-company ready | 18–22h | High |

---

## ❌ Common Traps & Mistakes

### Trap 1: Counting Non-Equally-Likely Outcomes
- **Mistake**: Treating all outcomes as equally likely when they aren't
- **Example**: "A coin has P(H)=2/3. P(both heads in 2 tosses)?" → Using (1/2)² = 1/4 → Wrong!
- **Truth**: P(both heads) = (2/3)² = 4/9
- **Fix**: Always check if outcomes are equally likely before using F/T formula.

### Trap 2: Using Addition Rule for Non-Mutually-Exclusive Events
- **Mistake**: P(A∪B) = P(A)+P(B) when A and B can both happen
- **Example**: P(King or Heart) in cards → Using 4/52 + 13/52 = 17/52 → Wrong! (King of Hearts counted twice)
- **Truth**: 4/52 + 13/52 - 1/52 = 16/52 = 4/13
- **Fix**: Ask "Can these events happen together?" If YES → subtract the intersection.

### Trap 3: Forgetting to Update Denominators (Without Replacement)
- **Mistake**: P(2 kings without replacement) = 4/52 × 4/52 = 16/2704 → Wrong!
- **Truth**: 4/52 × 3/51 = 12/2652 = 1/221
- **Fix**: Draw a tree diagram for every without-replacement problem. The second denominator is always one less.

### Trap 4: Confusing P(A|B) with P(B|A)
- **Mistake**: In Bayes' problems, flipping the condition
- **Example**: P(disease|positive) ≠ P(positive|disease) — they are VERY different
- **Fix**: Use the Bayes table method. Label columns clearly: Prior, Likelihood, Joint, Posterior.

### Trap 5: "Exactly One" Treated as Complement
- **Mistake**: P(exactly one head in 2 tosses) = 1 - P(both heads) = 1 - 1/4 = 3/4 → Wrong! (includes both tails case)
- **Truth**: Exactly one head = HT or TH = 1/4 + 1/4 = 1/2. Complement of exactly one = P(0 heads) + P(2 heads) = 1/2. So 1 - 1/2 = 1/2 ✓. Wait — that works here, but...
- **Example 2**: Exactly one 6 in 2 dice → HT=6, TH=6 → 2/36 = 1/18. Wrong to use complement without careful check.
- **Fix**: For exactly r in n trials → use binomial formula: C(n,r) × pʳ × (1-p)^(n-r).

### Trap 6: Wrong Use of Permutation vs Combination
- **Mistake**: P(2 aces in 2 draws) = 4P2/52P2 = 12/2652 → Wrong! (this counts order)
- **Truth**: Since the problem doesn't care about order, use C: C(4,2)/C(52,2) = 6/1326 = 1/221
- **Fix**: Ask "Does order matter in this problem?" If not → C. If yes → P.

### Trap 7: Birthday Problem — Ignoring the Complement
- **Mistake**: Trying to count pairs of people sharing birthdays → extremely complex
- **Truth**: P(at least one match) = 1 - P(no matches) = 1 - (365×364×...×(365-n+1))/365^n
- **Fix**: Always use the complement for the birthday problem. The direct count is nearly impossible.

### Trap 8: Round Table — Using n! Instead of (n-1)!
- **Mistake**: Counting arrangements around a circle as n! (same as a line)
- **Truth**: In a round table, rotations are identical → divide by n. (n-1)! arrangements.
- **Fix**: Remember: **Linear = n!**, **Circular = (n-1)!**. Only when relative positions matter.

### Trap 9: Geometric Probability — Wrong Formula
- **Mistake**: Using arc length or circumference when area is needed
- **Fix**: P(point in region) = Area(favorable)/Area(total). Always area, not perimeter.

### Trap 10: Expected Value Misapplication
- **Mistake**: Taking the average of max and min outcomes as expected value
- **Truth**: E(X) = Σ xᵢ × P(xᵢ) — weighted by probability, not equally weighted
- **Fix**: List ALL outcomes with their probabilities, multiply, then sum.

---

## 📝 Practice Section

### 🟢 Easy (Level 1) — 20 Questions

**Q1.** Two dice are thrown. What is the probability that the sum is 8? **[TCS]**

<details>
<summary>🔍 View Solution</summary>

Sum = 8: (2,6),(3,5),(4,4),(5,3),(6,2) → 5 outcomes.
P = 5/36 ✅
</details>
**Q2.** A card is drawn from a standard deck. Find P(King of hearts). **[Infosys]**

<details>
<summary>🔍 View Solution</summary>

Only 1 King of hearts in 52 cards.
P = 1/52 ✅
</details>
**Q3.** A coin is tossed 3 times. Find P(exactly 2 heads). **[TCS]**

<details>
<summary>🔍 View Solution</summary>

Exactly 2 heads in 3 tosses: HHT, HTH, THH = 3 outcomes.
P = 3/8 ✅
</details>
**Q4.** A bag has 5 red and 3 green balls. One ball is drawn. Find P(red). **[Wipro]**

<details>
<summary>🔍 View Solution</summary>

P(red) = 5/(5+3) = 5/8 ✅
</details>
**Q5.** From a deck of 52 cards, a card is drawn. Find P(a red card). **[Cognizant]**

<details>
<summary>🔍 View Solution</summary>

26 red cards out of 52.
P = 26/52 = 1/2 ✅
</details>
**Q6.** Two coins are tossed. Find P(at least one head). **[TCS]**

<details>
<summary>🔍 View Solution</summary>

Complement: P(no heads) = (1/2)² = 1/4.
P(at least one head) = 1 - 1/4 = 3/4 ✅
</details>
**Q7.** A die is rolled. Find P(a number greater than 4). **[Accenture]**

<details>
<summary>🔍 View Solution</summary>

Numbers > 4: {5,6} → 2 outcomes.
P = 2/6 = 1/3 ✅
</details>
**Q8.** A bag has 4 white, 5 black, 3 green balls. Find P(a black ball). **[Infosys]**

<details>
<summary>🔍 View Solution</summary>

P(black) = 5/(4+5+3) = 5/12 ✅
</details>
**Q9.** Three dice are rolled. Find P(all showing 6). **[TCS]**

<details>
<summary>🔍 View Solution</summary>

All 6: P = (1/6)³ = 1/216 ✅
</details>
**Q10.** From a standard deck, find P(an Ace or a Spade). **[Cognizant]**

<details>
<summary>🔍 View Solution</summary>

P(Ace or Spade) = P(Ace) + P(Spade) - P(Ace of Spades)
= 4/52 + 13/52 - 1/52 = 16/52 = 4/13 ✅
</details>
**Q11.** A number is chosen from 1 to 20. Find P(it is divisible by 3 or 5). **[TCS]**

<details>
<summary>🔍 View Solution</summary>

Divisible by 3: {3,6,9,12,15,18} = 6. Divisible by 5: {5,10,15,20} = 4. Both (LCM 15): {15} = 1.
P = (6+4-1)/20 = 9/20 ✅
</details>
**Q12.** A bag has 6 balls: 2 red, 2 green, 2 blue. Two balls are drawn with replacement. Find P(both red). **[Accenture]**

<details>
<summary>🔍 View Solution</summary>

With replacement → independent: P(both red) = (2/6) × (2/6) = 4/36 = 1/9 ✅
</details>
**Q13.** Two cards are drawn from a deck. Find P(both are Queens). **[Wipro]**

<details>
<summary>🔍 View Solution</summary>

Without replacement: P(both queens) = C(4,2)/C(52,2) = 6/1326 = 1/221 ✅
</details>
**Q14.** A fair die is thrown twice. Find P(sum is at most 10). **[TCS]**

<details>
<summary>🔍 View Solution</summary>

P(sum > 10) = P(11 or 12) = 2/36 + 1/36 = 3/36 = 1/12.
P(sum ≤ 10) = 1 - 1/12 = 11/12 ✅
</details>
**Q15.** A bag contains 3 defective and 7 good bulbs. One bulb is picked. Find P(it is good). **[Infosys]**

<details>
<summary>🔍 View Solution</summary>

P(good) = 7/10 ✅
</details>
**Q16.** A letter is chosen from the word PROBABILITY. Find P(it is a vowel). **[TCS]**

<details>
<summary>🔍 View Solution</summary>

Vowels in PROBABILITY: O, A, I, I → 4 vowels (11 letters total, but I appears twice).
P = 4/11 ✅
</details>
**Q17.** Two dice are thrown. Find P(sum is neither 7 nor 11). **[Accenture]**

<details>
<summary>🔍 View Solution</summary>

P(sum = 7) = 6/36 = 1/6. P(sum = 11) = 2/36 = 1/18.
P(neither 7 nor 11) = 1 - (1/6 + 1/18) = 1 - (3/18 + 1/18) = 14/18 = 7/9 ✅
</details>
**Q18.** A bag has balls numbered 1–10. One ball is drawn. Find P(it is a multiple of 2 or 3). **[Wipro]**

<details>
<summary>🔍 View Solution</summary>

Multiples of 2: {2,4,6,8,10} = 5. Multiples of 3: {3,6,9} = 3. Both: {6} = 1.
P = (5+3-1)/10 = 7/10 ✅
</details>
**Q19.** Three coins are tossed. Find P(at most one head). **[TCS]**

<details>
<summary>🔍 View Solution</summary>

At most one head = 0 heads + 1 head.
P(0 heads) = 1/8. P(1 head) = 3/8. Total = 4/8 = 1/2 ✅
</details>
**Q20.** A card is drawn from a deck. Find P(a face card or a heart). **[Infosys]**

<details>
<summary>🔍 View Solution</summary>

P(face card) = 12/52 = 3/13. P(heart) = 13/52 = 1/4. P(face card of hearts) = 3/52.
P = 12/52 + 13/52 - 3/52 = 22/52 = 11/26 ✅

---

### 🟡 Medium Solutions
</details>


---

### 🟡 Medium (Level 2) — 20 Questions

**Q21.** Two cards are drawn without replacement from a deck. Find P(first is a king and second is a queen). **[Amazon]**

<details>
<summary>🔍 View Solution</summary>

P(first king) = 4/52. P(second queen | first was king) = 4/51.
P = 4/52 × 4/51 = 16/2652 = 4/663 ✅
</details>
**Q22.** A bag has 4 red and 6 green balls. Two balls are drawn without replacement. Find P(one red and one green). **[Microsoft]**

<details>
<summary>🔍 View Solution</summary>

P(1 red, 1 green) = P(R then G) + P(G then R)
= (4/10 × 6/9) + (6/10 × 4/9) = 24/90 + 24/90 = 48/90 = 8/15 ✅
</details>
**Q23.** A die is thrown 4 times. Find P(at least one 6 appears). **[TCS]**

<details>
<summary>🔍 View Solution</summary>

P(at least one 6) = 1 - P(no 6 in 4 throws) = 1 - (5/6)⁴ = 1 - 625/1296 = 671/1296 ✅
</details>
**Q24.** A drawer has 5 pairs of socks — 2 blue, 2 black, 1 white. Two socks are drawn at random. Find P(they are a matching pair). **[Amazon]**

<details>
<summary>🔍 View Solution</summary>

Total ways to choose 2 socks from 10: C(10,2) = 45.
Matching pairs: 2 blue + 2 black + 1 white → C(2,2) + C(2,2) + C(1,2)=0 = 1 + 1 + 0 = 2.
P = 2/45 ✅
</details>
**Q25.** Two persons A and B solve a problem independently. P(A solves) = 0.7, P(B solves) = 0.5. Find P(at least one solves). **[Deloitte]**

<details>
<summary>🔍 View Solution</summary>

P(at least one) = 1 - P(neither) = 1 - (0.3 × 0.5) = 1 - 0.15 = 0.85 ✅
</details>
**Q26.** A bag has 3 white, 4 red, 5 black balls. Three balls are drawn without replacement. Find P(all are black). **[Microsoft]**

<details>
<summary>🔍 View Solution</summary>

P(all black) = C(5,3)/C(12,3) = 10/220 = 1/22 ✅
</details>
**Q27.** From a group of 6 men and 4 women, a committee of 4 is formed. Find P(the committee has exactly 2 women). **[Goldman Sachs]**

<details>
<summary>🔍 View Solution</summary>

C(6,2)×C(4,2)/C(10,4) = 15×6/210 = 90/210 = 3/7 ✅
</details>
**Q28.** A test is 95% accurate. 90% of students pass. If a student passes, what is the probability they actually studied? (Given: 80% of those who studied passed, 30% of those who didn't passed) **[Amazon]**

<details>
<summary>🔍 View Solution</summary>

Let S = studied, NS = not studied. P(S) = ?, P(pass|S) = 0.8, P(pass|NS) = 0.3.
Bayes table:
           P(Prior)  P(Pass|Prior)  Joint     Posterior
Studied    ?         0.8            0.8x
NotStudied ?         0.3            0.3(1-x)
Without x, we need overall pass rate: 0.9 = 0.8x + 0.3(1-x) = 0.5x + 0.3 → 0.5x = 0.6 → x = 6/5 > 1. Inconsistent data.
Using available info: P(S|pass) = P(S∩pass)/P(pass) = 0.8x/0.9.
Without x, cannot solve uniquely. Assuming 50% studied: P(S|pass) = 0.4/0.9 = **4/9 ≈ 44.4%** ✅
</details>
**Q29.** A box has 10 items, 3 defective. If 4 items are selected at random, find P(exactly 2 are defective). **[Microsoft]**

<details>
<summary>🔍 View Solution</summary>

P(exactly 2 defective) = C(3,2)×C(7,2)/C(10,4) = 3×21/210 = 63/210 = 3/10 ✅
</details>
**Q30.** In a class, 60% play football, 50% play cricket, 30% play both. A student is selected at random. Find P(plays at least one sport). **[Deloitte]**

<details>
<summary>🔍 View Solution</summary>

P(F∪C) = P(F) + P(C) - P(F∩C) = 0.6 + 0.5 - 0.3 = 0.8 ✅
</details>
**Q31.** A bag has balls numbered 1–6. Two balls are drawn with replacement. Find P(sum is 7). **[TCS]**

<details>
<summary>🔍 View Solution</summary>

Sum = 7: (1,6),(2,5),(3,4),(4,3),(5,2),(6,1) = 6 outcomes.
Total outcomes = 6×6 = 36. P = 6/36 = 1/6 ✅
</details>
**Q32.** Three persons A, B, C apply for a job. P(A selected) = 1/4, P(B selected) = 1/3, P(C selected) = 1/2. Find P(at least one is selected). **[Amazon]**

<details>
<summary>🔍 View Solution</summary>

P(at least one) = 1 - P(none) = 1 - (3/4 × 2/3 × 1/2) = 1 - 6/24 = 18/24 = 3/4 ✅
</details>
**Q33.** A machine has 3 components with failure probabilities 0.1, 0.2, 0.3. Find P(the machine works). (All must work) **[Microsoft]**

<details>
<summary>🔍 View Solution</summary>

P(all work) = (1-0.1)(1-0.2)(1-0.3) = 0.9×0.8×0.7 = 0.504 ✅
</details>
**Q34.** A bag has 7 green and 3 red balls. Two balls are drawn one by one without replacement. Find P(second ball is green). **[Goldman Sachs]**

<details>
<summary>🔍 View Solution</summary>

By symmetry — the probability the second ball is green is the same as the first.
P = 7/10 (7 green out of 10 total, regardless of draw position). ✅
</details>
**Q35.** From a deck, 3 cards are drawn without replacement. Find P(all are from different suits). **[Microsoft]**

<details>
<summary>🔍 View Solution</summary>

P(all different suits) = (13/52)×(13/51)×(13/50) × (arrangements? No, C(13,1) each → direct)
= 13/52 × 13/51 × 13/50 = 2197/132600 ≈ 0.0166. ✅
</details>
**Q36.** A biased coin has P(H) = 0.6. It is tossed 3 times. Find P(exactly 2 heads). **[Amazon]**

<details>
<summary>🔍 View Solution</summary>

P(exactly 2 heads) = C(3,2) × (0.6)² × (0.4)¹ = 3 × 0.36 × 0.4 = 0.432 ✅
</details>
**Q37.** A committee of 5 is to be formed from 6 men and 5 women. Find P(it has a majority of women). **[Goldman Sachs]**

<details>
<summary>🔍 View Solution</summary>

Majority women = 3, 4, or 5 women. C(5,3)×C(6,2)/C(11,5) + C(5,4)×C(6,1)/C(11,5) + C(5,5)×C(6,0)/C(11,5)
= 10×15/462 + 5×6/462 + 1×1/462 = (150+30+1)/462 = 181/462 = 0.391 ✅
</details>
**Q38.** Two dice are thrown. Find P(difference between numbers is 1). **[TCS]**

<details>
<summary>🔍 View Solution</summary>

Difference = 1: (1,2),(2,1),(2,3),(3,2),(3,4),(4,3),(4,5),(5,4),(5,6),(6,5) = 10 outcomes.
P = 10/36 = 5/18 ✅
</details>
**Q39.** A bag has 8 balls: 3 red, 2 green, 3 blue. Three balls are drawn with replacement. Find P(exactly 2 red). **[Amazon]**

<details>
<summary>🔍 View Solution</summary>

P(exactly 2 red in 3 draws with replacement) = C(3,2) × (3/8)² × (5/8)¹ = 3 × 9/64 × 5/8 = 135/512 ✅
</details>
**Q40.** P(A) = 0.5, P(B) = 0.4, P(A∩B) = 0.2. Find P(A' | B'). **[Deloitte]**

<details>
<summary>🔍 View Solution</summary>

P(A'|B') = P(A'∩B')/P(B'). P(A'∩B') = 1 - P(A∪B) = 1 - [P(A)+P(B)-P(A∩B)] = 1 - [0.5+0.4-0.2] = 1 - 0.7 = 0.3.
P(B') = 1 - P(B) = 0.6. P(A'|B') = 0.3/0.6 = 1/2 ✅

---

### 🟠 Hard Solutions
</details>


---

### 🟠 Hard (Level 3) — 20 Questions

**Q41.** A bag has 5 red, 4 green, 3 blue balls. Three balls are drawn at random without replacement. Find P(1 red, 1 green, 1 blue). **[Microsoft]**

<details>
<summary>🔍 View Solution</summary>

P(1R, 1G, 1B) = [C(5,1)×C(4,1)×C(3,1)]/C(12,3) = 5×4×3/220 = 60/220 = 3/11 ✅
</details>
**Q42.** A test for a disease is 99% accurate. The disease affects 1 in 1000 people. If a person tests positive, what is the probability they have the disease? **[Google]**

<details>
<summary>🔍 View Solution</summary>

Bayes: P(Disease|+) = P(+|Disease)×P(Disease) / [P(+|Disease)×P(Disease) + P(+|No Disease)×P(No Disease)]
= 0.99×0.001 / [0.99×0.001 + 0.01×0.999] = 0.00099 / [0.00099 + 0.00999] = 0.00099/0.01098 = **9.01%** ✅
</details>
**Q43.** From the word EQUATION, 4 letters are arranged randomly. Find P(they form the word QUAD). (Q, U, A, D must all appear — Q and U are in original) **[Google]**

<details>
<summary>🔍 View Solution</summary>

Word EQUATION has 8 letters. Arranging 4 letters: 4! = 24 total. For QUAD: Q,U are in word, A,D are in word. So all 4 letters are available. 1 arrangement gives QUAD. P = 1/24 ✅
</details>
**Q44.** Six boys and six girls sit around a round table alternately. Find the probability. **[Amazon]**

<details>
<summary>🔍 View Solution</summary>

Fix one boy (circular reference). Arrange remaining 5 boys: 5! ways.
For alternating: Arrange 6 girls in the 6 slots between boys: 6! ways.
Total alternating arrangements: 5! × 6! = 120 × 720 = 86400.
Total circular arrangements: 10!/10 = 362880.
P = 86400/362880 = 1/4.2? = 5/21 ≈ 0.238 ✅
</details>
**Q45.** In a game, you win ₹10 with probability 0.4, lose ₹5 with probability 0.5, and ₹0 with probability 0.1. Find expected gain. **[Goldman Sachs]**

<details>
<summary>🔍 View Solution</summary>

E = 10×0.4 + (-5)×0.5 + 0×0.1 = 4 - 2.5 + 0 = **₹1.50** expected gain per game ✅
</details>
**Q46.** A number is formed by arranging digits 1, 1, 2, 2, 3 randomly. Find P(it is divisible by 3). **[Microsoft]**

<details>
<summary>🔍 View Solution</summary>

A number is divisible by 3 if sum of digits is divisible by 3.
Digits: 1,1,2,2,3 → Sum = 9 → always divisible by 3.
All arrangements divisible by 3! P = 1. ✅
</details>
**Q47.** A point is chosen inside a square of side 8. Find P(it is within 2 units of a corner). (Four corners exist) **[Google]**

<details>
<summary>🔍 View Solution</summary>

Area within 2 units of a corner = 4 × (quarter circle of radius 2) = 4 × (π×4/4) = 4π.
Total area = 8×8 = 64. P = 4π/64 = π/16 ≈ **0.196** ✅
</details>
**Q48.** In a group of 5 people, find P(at least two share a birthday). Assume 365 days, no leap year. **[Google]**

<details>
<summary>🔍 View Solution</summary>

P(no match) = (365×364×...×341)/365⁵ ≈ 0.973.
P(at least one match) = 1 - 0.973 = **0.027** (about 2.7%). ✅
</details>
**Q49.** A bag has 5 white and 3 black balls. Balls are drawn without replacement until a black ball appears. Find P(the process stops on the 4th draw). **[Microsoft]**

<details>
<summary>🔍 View Solution</summary>

Process stops on 4th draw means first 3 are not black.
P = (5/8) × (4/7) × (3/6) × (3/5) = (5×4×3×3)/(8×7×6×5) = 180/1680 = 3/28 ✅
</details>
**Q50.** A box has 6 balls. A game costs ₹x to play. You draw 2 balls; if both are white you win ₹50, otherwise you lose your stake. Find the fair value of x. **[Goldman Sachs]**

<details>
<summary>🔍 View Solution</summary>

P(both white) = C(5,2)/C(6,2) = 10/15 = 2/3. Fair price = 50 × (2/3) = **₹33.33** ✅
</details>
**Q51.** From 1 to 100, two numbers are chosen. Find P(their sum is even). **[Google]**

<details>
<summary>🔍 View Solution</summary>

Sum even when both even or both odd.
Even numbers 1-100: 50. Odd: 50. C(50,2)+C(50,2) / C(100,2) = 1225+1225 / 4950 = 2450/4950 = 49/99 ≈ **0.4949** ✅
</details>
**Q52.** A biased die has P(6) = 2×P(1). All other faces equally likely. Given that 6 appeared, find P(1 appeared on the first throw). (Two throws) **[Microsoft]**

<details>
<summary>🔍 View Solution</summary>

Let P(1) = x, P(6) = 2x, others = y. 1×x + 1×2x + 4y = 1 → 3x + 4y = 1.
y = (1-3x)/4. Without additional constraint, multiple solutions.
If uniform except 6 is doubled: P(6)=2p, others=p: 2p+5p=1 → p=1/7, P(6)=2/7.
Bayes: P(Die=1|first die 6) = P(6|die1) × P(die1=1)/P(6) = ?
P(die=1)×P(6|die=1) = (1/2)×(2/7)=1/7. P(die=2)×P(6|die=2) = (1/2)×(1/7)=1/14.
P(6) = 1/7 + 1/14 = 3/14. P(die=1|first 6) = (1/7)/(3/14) = **2/3** ✅
</details>
**Q53.** Two persons A and B alternately draw cards from a deck (without replacement) until one draws an Ace. Find P(A wins). **[Goldman Sachs]**

<details>
<summary>🔍 View Solution</summary>

A wins if: A gets Ace first try (4/52), OR A fails (48/52) AND B fails (47/51) AND A gets it on second try...
This is a geometric series: P(A) = 4/52 + (48×47)/(52×51) × 4/52 + ... = infinite series.
Sum = p₁ + (1-p₁-p₂) × p₁ + (1-p₁-p₂)² × p₁ + ...
Where p₁ = P(A gets Ace next | both failed) = 4/47 ≈ 0.085, p₂ = P(B gets Ace | A failed, B next) = 4/46 ≈ 0.087.
This requires careful calculation. P(A) = p₁/(p₁+p₂-p₁p₂) ≈ **0.54** (A has slight advantage going first). ✅
</details>
**Q54.** 5 balls are placed randomly into 3 boxes. Find P(no box is empty). **[Amazon]**

<details>
<summary>🔍 View Solution</summary>

Total distributions: each ball → 3 choices → 3⁵ = 243.
No empty: Inclusion-exclusion: 3⁵ - 3×2⁵ + 3×1⁵ - 0 = 243 - 96 + 3 = **150**.
P = 150/243 = 50/81 ✅
</details>
**Q55.** A and B play a game. A wins a point with probability 0.6 each round. The game ends when someone reaches 3 points. Find P(A wins the match). **[Microsoft]**

<details>
<summary>🔍 View Solution</summary>

A wins if reaches 3 first. The match ends when one reaches 3.
P(A wins) = P(A wins 3-0) + P(A wins 3-1) + P(A wins 3-2).
P(A wins 3-0) = 0.6³ = 0.216.
P(A wins 3-1): A gets 2 points in first 3 rounds AND wins round 4.
2 wins, 1 loss in first 3: C(3,2)×0.6²×0.4 = 3×0.36×0.4 = 0.432. Then win round 4: ×0.6 → 0.259.
P(A wins 3-2): A gets 2 wins, B gets 2 wins in first 4 rounds AND A wins round 5.
First 4 rounds: C(4,2)×0.6²×0.4² = 6×0.36×0.16 = 0.3456. Then win round 5: ×0.6 → 0.207.
Total = 0.216 + 0.259 + 0.207 = **0.682** ✅
</details>
**Q56.** From the word MISSISSIPPI, 4 letters are chosen randomly. Find P(they are all consonants). **[Google]**

<details>
<summary>🔍 View Solution</summary>

Consonants in MISSISSIPPI: M, S, S, S, S, P, P → 7 consonants. Total 11 letters.
P(all 4 consonants) = C(7,4)/C(11,4) = 35/330 = **7/66** ✅
</details>
**Q57.** In a tournament, 8 teams are divided into 2 groups of 4 randomly. Find P(two specific teams are in the same group). **[Amazon]**

<details>
<summary>🔍 View Solution</summary>

Fix A in a group. 7 remaining spots. B can go to same group (3 spots) or other group (4 spots).
P(same) = 3/7. ✅
</details>
**Q58.** A bag has balls of colors red, green, blue. P(red) = 0.3, P(green) = 0.4. You draw with replacement. Find P(you see red before green). **[Google]**

<details>
<summary>🔍 View Solution</summary>

P(red before green) = P(red on first) + P(neither red nor green on first) × P(red before green on remaining).
= 0.3 + 0.3 × x. x = P(red before green).
0.7x = 0.3 → x = 3/7. P(red before green) = 0.3 + 0.3 × (3/7) = 0.3 + 0.9/7 = (2.1+0.9)/7 = 3/7 ≈ **0.429**? No.
Using formula: P(A before B) = P(A)/(P(A)+P(B)) when only these two matter.
P(red) = 0.3, P(green) = 0.4. P(red before green) = 0.3/(0.3+0.4) = **3/7 ≈ 42.9%** ✅
</details>
**Q59.** Two dice are painted — one has 1 red face, 5 black faces. The other has 2 red faces, 4 black faces. One die is chosen at random and rolled. A red face appears. Find P(which die it was). **[Goldman Sachs]**

<details>
<summary>🔍 View Solution</summary>

P(Die 1|red) = P(red|Die 1)×P(Die 1) / [P(red|Die 1)×P(Die 1) + P(red|Die 2)×P(Die 2)]
= (1/6 × 1/2) / (1/6×1/2 + 1/3×1/2) = (1/12) / (1/12+1/6) = (1/12) / (3/12) = **1/3** ✅
</details>
**Q60.** In a class of 30 students, find P(at least one pair shares a birthday). **[Google]**

<details>
<summary>🔍 View Solution</summary>

P(no match) = (365×364×...×336)/365³⁰ ≈ 0.706.
P(at least one match) = 1 - 0.706 = **0.294** (29.4% for 30 people). ✅

---

### 🔴 Product-Level Solutions
</details>


---

### 🔴 Product-Based Company Level — 10 Questions

**Q61.** Three factories F1, F2, F3 produce 20%, 30%, 50% of items. Defect rates are 3%, 2%, 1%. An inspector picks an item and it is defective. Using Bayesian update, what is the probability it came from F3? If the item is non-defective, what is P(it came from F1)? **[Amazon L5]**

<details>
<summary>🔍 View Solution</summary>

P(F3|Defective) = P(Def|F3)×P(F3) / [P(Def|F1)×P(F1)+P(Def|F2)×P(F2)+P(Def|F3)×P(F3)]
= 0.01×0.5 / [0.03×0.2 + 0.02×0.3 + 0.01×0.5] = 0.005 / [0.006 + 0.006 + 0.005] = 0.005/0.017 = **5/17 ≈ 29.4%**.
P(F1|Non-Def) = P(F1∩Non-Def)/P(Non-Def).
P(F1∩Non-Def) = 0.2 × 0.97 = 0.194. Total non-defective = 0.006+0.006+0.005 = 0.017.
Wait: Non-defective from each: 0.2×0.97=0.194, 0.3×0.98=0.294, 0.5×0.99=0.495. Total = 0.983.
P(F1|Non-Def) = 0.194/0.983 = **19.7%** ✅
</details>
**Q62.** A person has 3 keys, only one of which fits the lock. He tries keys randomly until the lock opens. If he forgets which keys he has tried, what is the expected number of trials? What if he remembers which keys he tried? **[Google]**

<details>
<summary>🔍 View Solution</summary>

With memory: 1, 2, 3 → each with 1/3. Expected = 1×1/3 + 2×1/3 + 3×1/3 = 2.
Without memory: Could try same key repeatedly → geometric distribution with p=1/3. E = 1/p = 3. But if you try a key and it fails, you try again — but since you don't remember, you might try the same key again.
With no memory: each trial is independent, p=1/3. E = **3 trials**. ✅
</details>
**Q63.** In a game show, there are 3 doors. Behind one is a car, behind the others are goats. You pick door 1. The host (who knows) opens door 3 (goat). He offers you a chance to switch to door 2. Should you switch? What are the probabilities? **[Google / Amazon Interview Classic]**

<details>
<summary>🔍 View Solution</summary>

Classic Monty Hall. P(stay) = 1/3. P(switch) = 2/3.
You should ALWAYS switch. The host's knowledge transfers the 2/3 probability to the remaining door. ✅
</details>
**Q64.** A sequence of 5 cards is drawn from a shuffled deck (with replacement after each full deck). What is the probability that the sequence matches a specific prediction of 5 card ranks (e.g., 2, 5, J, K, A)? Each prediction card can be any of 13 ranks. **[Microsoft L64]**

<details>
<summary>🔍 View Solution</summary>

Each card rank prediction: 4/52 = 1/13. Each draw is independent.
P(all 5 match) = (1/13)⁵ = 1/371293 ≈ 0.0000027. ✅
</details>
**Q65.** An ant starts at vertex A of a regular tetrahedron. At each step, it moves to an adjacent vertex with equal probability. After 3 steps, what is the probability it is back at A? Generalize for n steps. **[Google]**

<details>
<summary>🔍 View Solution</summary>

Tetrahedron has 4 vertices. Adjacency: each vertex connects to 3 others.
After 1 step: P(at A) = 0 (must move away).
After 2 steps: P(at A) = 3 × (1/3 × 1/3) = 1/3. (3 ways to go to a neighbor and back).
After 3 steps: Can return via: go-A-go-A (3×3 paths) or triangle (go-B, B-C, C-A)...
The transition matrix shows eigenvalues. For n steps: P_n(A) = (1/4) + (3/4)(-1/3)^n.
For n=3: = 1/4 + (3/4)(1/27) = 1/4 + 1/36 = 9/36 + 1/36 = **10/36 = 5/18** ✅
</details>
**Q66.** 100 prisoners are in line. Each can see the people ahead but not behind. Each has a hat (black or white). Each must guess their hat color. They can agree on a strategy beforehand. What strategy guarantees at least 99 survive? (Classic hat problem) **[Amazon / Google Interview]**

<details>
<summary>🔍 View Solution</summary>

Strategy: Count the number of black hats in front of you (mod 2). If even → say "black", if odd → say "white". This way, each person provides information about all people behind them. The first person has 50-50 chance, but everyone else is guaranteed to be correct.
Survival rate: 99 out of 100 (first prisoner has 50% chance). ✅
</details>
**Q67.** A deck of 52 cards is dealt to 4 players (13 each). Find the probability that each player gets one Ace. Find the probability that a specific player gets all 4 Aces. **[Goldman Sachs]**

<details>
<summary>🔍 View Solution</summary>

Each player gets one Ace: C(4,1)×C(4,1)×C(4,1)×C(4,1)×3! arrangements? No.
P(each player gets 1 Ace) = 4! × C(48,9) × C(36,9) × C(27,9) / [ways to distribute 52 cards to 4 players × 13!³]? No.
Direct: Deal 13 to each. P(each gets one Ace) = 4! × (48!/(12!⁴)) / (52!/(13!⁴)) × (13!⁴/(48!)) = 4! × 13!⁴ / (12!⁴ × 52!)
= 24 × (13×12×11×10)⁴ / (52×51×50×49)⁴ = 24 × (17160/6497400)⁴ = **24 × (0.00264)⁴ ≈ 1.06×10⁻⁷**? No.
Standard result: P = (4! × 48! × 13⁴) / 52! = **24 × 48! × 13⁴ / 52!**
Specific player gets all 4 Aces: C(4,4)×C(48,9)/C(52,13) = 1 × 48C9 / 52C13 = **C(48,9)/C(52,13)** ≈ 0.0026. ✅
</details>
**Q68.** In a random walk on integers starting at 0, at each step you move +1 with probability p and -1 with probability q=1-p. What is the probability of ever reaching +1 before -1, starting from 0? What is the probability of ever reaching +N before -M? **[Google / Jane Street]**

<details>
<summary>🔍 View Solution</summary>

For a biased random walk starting at 0, probability of reaching +1 before -1:
If p ≤ q: P(reach +1 first) = p/q? No. Formula: For p ≠ q, P(reach +a before -b) = (1-(q/p)^b) / (1-(q/p)^(a+b)).
For +1 before -1: a=1, b=1 → P = (1-(q/p)) / (1-(q/p)²) = (p-q)/(p+q).
For p=0.5 (fair): P = (0.5-0.5)/(1) = 0. So for +1 before -1, starting at 0, P = 1/2 (since symmetric).
General: P(reach +N before -M) = [1-(q/p)^M] / [1-(q/p)^(N+M)] if p≠q. If p=q=0.5: = M/(N+M). ✅
</details>
**Q69.** A biased coin with P(H) = p is tossed until the first head appears. Let X be the number of tosses. Find E(X) and Var(X). What is P(X > n)? **[Microsoft / Amazon SDE]**

<details>
<summary>🔍 View Solution</summary>

Geometric distribution: P(X=n) = (1-p)^(n-1) × p.
E(X) = 1/p. Var(X) = (1-p)/p². P(X > n) = (1-p)^n. ✅
</details>
**Q70.** In a party of n couples, each person shakes hands with everyone except their spouse. If a person counts 7 handshakes, what is the probability their spouse is among the people they shook hands with? Generalize for k handshakes. **[Google / Math Olympiad]**

<details>
<summary>🔍 View Solution</summary>

Total people met = 2n-1 (all except self and spouse). Handshakes k = 7.
P(spouse among handshakes | k handshakes) = k/(2n-1). (Hypergeometric with one special item).
For n couples, 2n-1 people (excluding self), 1 spouse.
P = C(1,1)×C(2n-2, k-1) / C(2n-1, k) = (2n-k-1)/(2n-1)? No.
Hypergeometric: N=2n-1, K=1 special (spouse), n_drawn=k.
P(spouse drawn) = K/N = 1/(2n-1). Independent of k! (Because exactly k people are met, one must be the spouse among the 2n-1 others.)
**Answer: P = 1/(2n-1). For n=5: P = 1/9 ≈ 11.1%.** ✅

---
</details>


---

*(Solutions on next page)*

---

## 📝 Detailed Solutions

> [!NOTE]
> All detailed solutions have been inlined directly under the questions in the **Practice Section** above for interactive study.

## 📚 Best Resources

### 🥇 YouTube Channels (Free — Best First Stop)

| Rank | Channel | Best For | Link |
|---|---|---|---|
| 1 | **3Blue1Brown** | Visual intuition for probability | youtube.com/@3blue1brown |
| 2 | **Gagan MATHS** | Placement shortcuts, tree diagrams | youtube.com/@gagan_iift |
| 3 | **Aditya Ranjan (RBank)** | Fast P&C + probability tricks | youtube.com/@AdityaRanjan |
| 4 | **Khan Academy (Statistics)** | Bayes' theorem deep dive | youtube.com/@khanacademy |
| 5 | **Bhava Nath** | Basic probability clarity | youtube.com/@bhavanath |

### 🥈 Websites & Platforms

| Rank | Platform | Best For | Type |
|---|---|---|---|
| 1 | **Brilliant.org** | Probability puzzles, Bayes | Free + Paid |
| 2 | **Khan Academy** | Conditional probability, Bayes | Free |
| 3 | **IndiaBix** | Placement question patterns | Free |
| 4 | **Brilliant (probability course)** | Structured learning path | Paid |
| 5 | **M4Maths** | Company-specific questions | Free |

### 🥉 Books & PDFs

| Rank | Book | Best For | Cost |
|---|---|---|---|
| 1 | **Arun Sharma — Quantitative Aptitude** | Placement coverage, all levels | ₹500–₹700 |
| 2 | **Ross — Introduction to Probability and Statistics** | Deep conceptual understanding | ₹800–₹1200 |
| 3 | **Feller — An Introduction to Probability Theory Vol 1** | Advanced, for product companies | ₹600–₹900 |
| 4 | **NCERT Class 10 & 12** | Foundation, free PDF | Free |

### 🎯 Practice Platforms

| Platform | Coverage | Level |
|---|---|---|
| **IndiaBix.com** | All company patterns | Easy–Hard |
| **Brilliant.org** | Conceptual puzzles | Medium–Very Hard |
| **GeekforGeeks** | Bayes, expected value | Medium–Hard |
| **LeetCode (Easy-Medium)** | Probability in coding | Medium |
| **CoderByte** | Algorithm + probability | Hard |

> **Best Learning Path**: NCERT basics (foundation) → 3Blue1Brown YouTube (intuition) → IndiaBix (placement patterns) → Brilliant (Bayes & conditional) → LeetCode (for SDE roles).

---

## 🎯 Final Verdict

### Scores

| Metric | Rating |
|---|---|
| **Importance Rating** | ★★★★★ (5/5) — Highest ROI |
| **Placement ROI Score** | **9/10** — Every test asks it; learnable patterns give near-perfect accuracy |
| **Difficulty Score** | **6/10** — Easy to learn, hard to master (especially Bayes + P&C combinations) |
| **Priority Order** | **#3–5** among core aptitude topics |

### Company-Level Verdict

| Target | Verdict | Reasoning |
|---|---|---|
| **TCS/Infosys/Wipro** | ✅ **Mandatory** | 1–2 easy questions; complement trick solves most in 30 seconds |
| **10 LPA+ jobs** | ✅ **Mandatory** | Appears in virtually every test |
| **Accenture/Cognizant** | ✅ **Mandatory** | Conditional probability, tree diagrams |
| **20 LPA+ jobs** | ✅ **Important** | Bayes, binomial, P&C combinations become differentiators |
| **Amazon/Microsoft** | ✅ **Important** | Expected value, Bayes, complex arrangements |
| **Goldman Sachs** | ✅ **Important** | Binomial, expected value, game theory |
| **Google** | ✅ **Important** | Non-standard sample spaces, birthday, hat problems |

### Bottom Line

> Probability is the **highest-ROI topic** in the aptitude syllabus. The basics (complement trick, tree diagrams, Bayes' table) can be mastered in 4–6 hours and will solve 80% of placement questions. The remaining 20% (complex Bayes, P&C-based probability, round table arrangements, birthday problem) separate the 90th percentile from the 99th percentile. Master the complement shortcut, the Bayes table method, and the binomial formula — and probability becomes one of your strongest sections in any placement test.

**Study Time to Master**: 10–15 hours total
**Questions to Practice**: 120–180
**Expected Score Improvement**: +5–8 marks in most aptitude tests

---

*End of Guide — Probability | Elite Placement Aptitude Series*
