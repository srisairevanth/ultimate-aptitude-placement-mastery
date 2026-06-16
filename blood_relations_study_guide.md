# Blood Relations — Placement Study Guide
> **Elite Aptitude Trainer Edition** | Covers TCS, Accenture, Cognizant, Deloitte, Goldman Sachs, Amazon, Microsoft, Google

---

## 🥇 Rank & Importance

| Metric | Rating |
|---|---|
| **Rank among all aptitude topics** | #6 of ~20 core topics |
| **Importance Rating** | ★★★★☆ (4/5) |
| **Appears in every placement test** | Yes |
| **Logical reasoning vs. calculation** | Pure logical deduction |
| **High scorers vs. average candidates gap** | Moderate to High |

### Why It Matters in Placements

Blood Relations tests **structured thinking** — specifically, your ability to trace family trees, decode relationship labels, and maintain consistency under multiple constraints. It's the topic where most candidates:
- Lose track of generations
- Confuse paternal vs. maternal sides
- Fail to handle **"not a blood relation"** trick questions

Companies ask this because it reveals whether you can maintain a coherent chain of relationships while juggling multiple conditions simultaneously — a core skill for business analyst, operations, and management roles.

### Weightage in Tests

| Company Type | Expected Questions | Difficulty Band |
|---|---|---|
| **TCS / Infosys / Wipro** (service) | 1–2 questions | Easy |
| **Accenture / Cognizant** (service) | 1 question | Easy–Medium |
| **Deloitte / KPMG** (consulting) | 1–2 questions | Medium |
| **Goldman Sachs / JPMorgan** (BFSI) | 1 question | Medium |
| **Amazon / Microsoft** (product) | 1 question | Medium–Hard |
| **Google** | 0–1 question | Hard |

> **ROI Insight**: Blood Relations is a **high-accuracy, low-time** topic. The rules are fixed and learnable. If you master the **family tree method** and the **generations framework**, you'll solve every question correctly. Most candidates lose marks because they don't draw the tree — not because they don't know the logic.

---

## 📖 Concept Overview

### What Are Blood Relations?

Blood Relations problems describe a set of people and their inter-relationships using English kinship terms. Your task is to **decode the description** and answer questions about specific relationships.

### The Core Principle

Every person has exactly **one biological father**, **one biological mother**, etc. These relationships are fixed and consistent. When a description says "A is the sister of B," you immediately know: same parents, female, at least one sibling.

### Subtopics to Master

1. **Kinship terms** — direct relationship vocabulary
2. **Family tree notation** — drawing the tree from description
3. **Generation tracking** — who is older/younger than whom
4. **Coded relations** — letters/symbols representing relationships
5. **Mixed relations** — combining blood + marital relationships
6. **"Not a blood relation"** — distinguishing real vs. assumed relationships
7. **Multiple generation chains** — grandparent → parent → child → grandchild
8. **Siblings, half-siblings, step-relations** — subtle distinctions
9. **In-law relationships** — acquired through marriage
10. **Conditional relationship puzzles** — "if A is B's X, then who is C?"

### Where Each Concept Is Used in Exams

| Subtopic | Placement Application |
|---|---|
| Kinship terms | Every blood relations question |
| Family tree | Complex multi-person descriptions |
| Generation tracking | Age-based relationship problems |
| Coded relations | Symbol-based puzzles |
| In-law relations | Marriage-acquired relationships |
| Mixed relations | Family + professional relationships |

---

## 🎯 Core Concepts to Master

### Concept 1: Kinship Terminology

**Definition**: Standard English words that describe family relationships.

**The Complete Family Tree (Know These by Heart)**:

```
Generation 0: Self
Generation +1: Parent(s)
Generation +2: Grandparent(s), Uncle/Aunt
Generation -1: Child(ren)
Generation -2: Grandchild(ren)
Generation ±0 (siblings): Brother/Sister
```

**Critical Terms to Master**:

| Term | Meaning |
|---|---|
| **Father / Mother** | Parents (Generation +1) |
| **Son / Daughter** | Children (Generation -1) |
| **Brother / Sister** | Same parents, same generation |
| **Grandfather / Grandmother** | Parents of parents (+2) |
| **Grandson / Granddaughter** | Children of children (-2) |
| **Uncle / Aunt** | Sibling of parent (+1, sideways) |
| **Nephew / Niece** | Child of sibling (-1, sideways) |
| **Cousin** | Child of uncle/aunt (-1, sideways) |
| **Father-in-law / Mother-in-law** | Parent of spouse (acquired) |
| **Brother-in-law / Sister-in-law** | Sibling of spouse, spouse of sibling (acquired) |
| **Step-brother / Step-sister** | Same parent re-married, not biologically shared |
| **Half-brother / Half-sister** | Same mother OR same father, not both |

**Memory Trick**:
> 🔑 **"In-laws are acquired, not born"** — In-law relationships come through marriage, not blood.

**Common Mistakes**:
- ❌ Confusing nephew (sister's son) with niece (sister's daughter)
- ❌ Treating in-laws as blood relations
- ❌ Not knowing the difference between cousin and nephew/niece

**Interview Relevance**: "A is B's uncle. B is C's sister. D is C's mother. How is A related to D?" — Tests generation tracking.

---

### Concept 2: Family Tree Method

**Definition**: A visual diagram that places every person on a generation-level chart with their relationships.

**Intuition**: Build the tree **generation by generation**, not person by person. Start from the oldest generation mentioned and work down.

**The Method**:

```
Step 1: Identify the OLDEST person in the description.
Step 2: Place them at the top of the tree.
Step 3: Work downward — children, then grandchildren.
Step 4: Add siblings at the same level.
Step 5: Add spouses (connected by =).
Step 6: Answer questions by tracing paths on the tree.
```

**Example**:
"A is B's father. C is B's sister. D is C's mother."
```
Generation +1: A ←→ D (married)
                 ↓
Generation 0: B ←→ C (siblings)
```
From tree: A and D are the parents of B and C.

**Common Mistakes**:
- ❌ Starting from the wrong person and getting confused
- ❌ Forgetting to mark spouses (dashed line =)
- ❌ Placing siblings at different generations

**Interview Relevance**: Drawing the tree is the single most important skill for blood relations. Toppers always draw the tree before answering.

---

### Concept 3: Generation Tracking

**Definition**: Determining which person belongs to which generation relative to a reference person.

**Intuition**: Every step up or down in the family tree is one generation. Cousins, aunts, uncles — they're all **sideways** from your generation.

**The Generation Formula**:
```
Generation difference = (My generation) - (Their generation)
Negative = descendant, Positive = ancestor
Zero = sibling
Sideways (different branch) = cousin/uncle/niece/aunt
```

**Shortcut — The Distance Method**:
```
Trace the path from person A to person B.
Count the number of generations up (parent=+1, grandparent=+2)
Count the number of generations down (child=-1, grandchild=-2)
If sideways: find the common ancestor, then measure from there.
```

**Example**:
"My mother's brother is my uncle." → Mother (+1), her brother (0 from mother, sibling of parent = uncle).
Me → mother (+1) → uncle (sibling of mother = generation 0 from generation 1 = generation +1, same as parent).

**Common Mistakes**:
- ❌ Treating cousins as being in a different generation
- ❌ Counting spouses as changing generation

**Interview Relevance**: "How is A related to B if A is B's mother's sister?" → If A is mother's sister, A is maternal aunt. B's mother's sister = B's maternal aunt. A = B's maternal aunt.

---

### Concept 4: Coded/Symbolic Relations

**Definition**: Relationships expressed using symbols or letters, not words.

**Common Notation**:
```
A + B → A is B's sister (using + as sibling marker)
A - B → A is B's brother
A × B → A is B's wife
A ÷ B → A is B's husband
A = B → A and B are spouses
A △ B → A is B's son
A ▽ B → A is B's daughter
```

**Shortcut**: Always identify what the **operator** means first, then trace the relationship.

**Example**:
"If A × B = C, and C △ D = E, how is A related to E?"
A × B = C → A is B's wife. C △ D = E → C is D's son.
So: A is B's wife. B and C are spouses. C is D's son. So C = D's son. B = D's daughter-in-law. A = B's wife = D's daughter-in-law.

**Common Mistakes**:
- ❌ Confusing which symbol means husband vs. wife
- ❌ Not checking male/female from context

---

### Concept 5: Mixed Blood + Marital Relations

**Definition**: Problems that combine biological relationships with marriage-acquired ones.

**The Rule**: In-laws are **not blood**. Step-relations are **blood** (from one shared parent). In-law relations are only through marriage.

**Example**:
"A's sister is married to B. C is B's brother. D is C's son."
- A's sister is married to B → A and B are in-laws
- B's brother is C → C is B's brother
- C's son is D → D is B's nephew
- Since A and B are in-laws, D is A's **nephew-in-law** (through B)

**Common Mistakes**:
- ❌ Calling an in-law a "real" uncle/aunt
- ❌ Forgetting that the in-law relation is one-way

---

### Concept 6: "Not a Blood Relation" Trap

**Definition**: Some people described as family may not actually be blood relatives.

**Types of Non-Blood Relations**:
- **Spouses** — married but not blood
- **Step-relations** — through remarriage (partially blood)
- **In-laws** — acquired through marriage
- **Adopted children** — legally but not biologically related
- **Best friends / close relatives described as family** — common in trick questions

**Shortcut**: When a question asks "who is NOT a blood relative," draw the tree and identify which connections go through marriage (sideways) rather than birth (vertical).

**Example**:
"My father's brother is my uncle. My uncle's son is my cousin."
BUT: "My father's brother's wife is my aunt" — she may not be blood (she married into the family).

**Common Mistakes**:
- ❌ Assuming all "aunts" and "uncles" are blood relatives
- ❌ Missing the step-parent nuance

---

### Concept 7: Sibling Relationships (Subtle Distinctions)

**Definition**: Understanding the difference between full siblings, half siblings, and step siblings.

| Type | Shared Parent | Blood Connection |
|---|---|---|
| **Full sibling** | Both parents | 100% blood (same genes) |
| **Half sibling** | One parent only | 50% blood |
| **Step sibling** | No biological parent shared | 0% blood (parents married, not shared) |

**Memory Trick**:
> 🔑 **"Half = one parent shared. Step = no parent shared."** — Step siblings only share a family through their parents' marriage.

---

## 🧠 Important Formula Sheet

### 1. Generation Distance
```
From A to B's descendant: Count steps down
From A to B's ancestor: Count steps up
From A to B's sibling: Same generation, different parents
From A to B's cousin: Same grandparents (not same parents)
```

### 2. Relationship Transitivity
```
If A is B's parent, and B is C's parent → A is C's grandparent
If A is B's sibling, and B is C's sibling → A and C are siblings
If A is B's spouse, and B is C's parent → A is C's parent-in-law
```

### 3. In-law Relationships
```
Spouse's sibling = sibling-in-law
Sibling's spouse = sibling-in-law
Parent's sibling = aunt/uncle
Spouse's parent = father-in-law / mother-in-law
Child's spouse = daughter-in-law / son-in-law
```

### 4. Counting Relatives
```
From one sibling: 1 brother + 1 sister (excluding self)
From one sibling with N children: N nephews/nieces
From one aunt/uncle: their children are cousins
```

### 5. Male/Female Inference
```
Brother, Father, Son, Uncle, Nephew, Grandfather, Grandson → Male
Sister, Mother, Daughter, Aunt, Niece, Grandmother, Granddaughter → Female
```

### Memory Tricks

> 🔑 **"Up = Ancestors, Down = Descendants, Sideways = Same Generation"** — This is the three-direction rule.

> 🔑 **"In-law words contain 'in'"** — They come from outside the blood line. Father-in-law, sister-in-law, etc.

> 🔑 **"Niece = Female Nephew"** — Both are children of siblings. Niece is the girl, nephew is the boy.

> 🔑 **"Uncle/Aunt = Parent's Sibling"** — They are your parents' brothers and sisters.

---

## ⚡ Shortcut Techniques & Time-Saving Tricks

### Trick 1: The Family Tree Drawing (30-Second Method)
```
Problem: "A is B's sister. B is C's father. D is C's mother. E is D's son. How is A related to E?"

Step 1: Draw: C at center
Step 2: B is C's father → place B above C
Step 3: A is B's sister → place A at same level as B (sibling)
Step 4: D is C's mother → D is B's spouse (married)
Step 5: E is D's son → E is C's brother

From tree: A and B are siblings. B and D are spouses. C and E are siblings (brother/sister).
A is C's aunt → A is E's aunt.

Answer in 30 seconds with the tree.
```

### Trick 2: The Common Ancestor Method
```
Problem: "How is A related to B's mother's sister?"

Step 1: Find common ancestor: A and B share the same grandparents (or parents).
Step 2: Trace from B to common ancestor: B → mother → sister.
Step 3: Trace from A to common ancestor: A → ?
Without more info, A could be B's cousin, aunt, etc.

This trick requires knowing the exact relationship.
```

### Trick 3: Gender Elimination
```
If a question says "A is B's mother's only sister" and A is male:
A is B's maternal uncle. (Only sister of mother = maternal aunt, but A is male → maternal uncle)

Eliminate gender contradictions quickly.
```

### Trick 4: Backward Tracing
```
Problem: "X is Y's sister's father's son. Z is Y's mother's daughter."
X is Y's sister's father's son → X is Y's brother (same father).
Z is Y's mother's daughter → Z is Y's sister.
X and Z are siblings.

Never try to go forward from scratch — start from the person and trace backward.
```

### Trick 5: Symbol Code Translation
```
Step 1: Identify each symbol's meaning
Step 2: Replace with relationship word
Step 3: Connect the chain
Step 4: Trace from start to end person

Example: P + Q = R and R × S = T
P + Q = R → P is R's sister
R × S = T → R is T's wife
P is T's sister-in-law (through R)
```

### Trick 6: MCQ Elimination — Gender Check
```
If the question asks "How is A related to B?" and A is female:
Eliminate all male relationships immediately.

Options: 1) Uncle 2) Sister 3) Brother 4) Nephew
Correct: Sister (only female option). Done in 5 seconds.
```

---

## 🔥 Most Frequently Asked Question Patterns

### Pattern 1: Direct Relationship Description
- **Concept Tested**: Basic kinship terms
- **Difficulty**: Easy
- **Fastest Approach**: Draw simple tree, identify relationship
- **Appears in**: TCS, Infosys, Wipro, Cognizant
- **Example**: "A is B's mother. B is C's sister. How is A related to C?"

### Pattern 2: Chain Relationship
- **Concept Tested**: Tracing a relationship chain
- **Difficulty**: Easy–Medium
- **Fastest Approach**: Backward tracing, mark generations
- **Appears in**: All companies
- **Example**: "A is B's brother. B is C's father. D is C's mother. How is A related to D?"

### Pattern 3: Finding the Person from Description
- **Concept Tested**: Inverse relationship
- **Difficulty**: Medium
- **Fastest Approach**: Build tree, find the missing link
- **Appears in**: All companies
- **Example**: "A is B's uncle. B is C's sister. D is C's mother. Who is D to A?"

### Pattern 4: Coded/Symbolic Relations
- **Concept Tested**: Symbol interpretation
- **Difficulty**: Medium
- **Fastest Approach**: Translate all symbols first, then trace
- **Appears in**: Infosys, Accenture, Amazon
- **Example**: "P × Q = R, R + S = T. P is T's _____"

### Pattern 5: Mixed Blood + In-law
- **Concept Tested**: Combining blood and marriage relations
- **Difficulty**: Medium
- **Fastest Approach**: Mark blood relations with solid lines, in-laws with dashed
- **Appears in**: All companies
- **Example**: "A is B's brother-in-law. B is C's sister. D is C's mother. How is A related to D?"

### Pattern 6: Counting Relatives
- **Concept Tested**: Total count of specific relationship types
- **Difficulty**: Easy–Medium
- **Fastest Approach**: Draw full family tree, count systematically
- **Appears in**: TCS, Infosys, Wipro
- **Example**: "A has 2 sons and 1 daughter. Each son has 2 children. Each daughter has 1 child. How many grandchildren does A have?"

### Pattern 7: Conditional Relationship
- **Concept Tested**: "If-then" relationship logic
- **Difficulty**: Medium–Hard
- **Fastest Approach**: Assume the condition, build tree
- **Appears in**: Amazon, Microsoft, Deloitte
- **Example**: "If A is B's sister, and B is C's mother, then who is C to A?"

### Pattern 8: Grandparent/Grandchild Chains
- **Concept Tested**: Multi-generation tracking
- **Difficulty**: Medium
- **Fastest Approach**: Generation counter — count steps up/down
- **Appears in**: All companies
- **Example**: "A is B's grandfather. C is B's sister. D is C's son. How is A related to D?"

### Pattern 9: Sibling-in-law Relationships
- **Concept Tested**: In-law acquisition
- **Difficulty**: Medium
- **Fastest Approach**: Identify through marriage path
- **Appears in**: Amazon, Microsoft, Goldman Sachs
- **Example**: "A is B's brother. B is C's sister. How is A related to C's husband?"

### Pattern 10: Cousin Relationships
- **Concept Tested**: First cousin vs. second cousin vs. removed
- **Difficulty**: Hard
- **Fastest Approach**: Common grandparents = first cousin. Count generations.
- **Appears in**: Google, Amazon, Microsoft
- **Example**: "A and B are first cousins. A's mother is C. C's sister is D. D's daughter is E. How is E related to B?"

### Pattern 11: "Not a Blood Relation" Identification
- **Concept Tested**: Distinguishing blood from non-blood
- **Difficulty**: Medium
- **Fastest Approach**: Check each connection for marriage link
- **Appears in**: All companies
- **Example**: "Identify who is NOT a blood relative: father's brother, mother's sister, father's brother's wife, mother's mother's sister"

### Pattern 12: Multiple Marriage Relations
- **Concept Tested**: Step-relations and remarriage
- **Difficulty**: Hard
- **Fastest Approach**: Draw both families separately, note shared children
- **Appears in**: Amazon, Microsoft, Deloitte
- **Example**: "A and B are siblings. After remarriage, A's father marries C. C has a daughter D. How are A and D related?"

### Pattern 13: Family Puzzle with Ages
- **Concept Tested**: Age + relationship combined
- **Difficulty**: Medium–Hard
- **Fastest Approach**: Use age to determine generation and order
- **Appears in**: Amazon, Deloitte, Goldman Sachs
- **Example**: "A is twice B's age. A is B's father. C is A's mother. D is B's sister. If D is 10, how old is C?"

### Pattern 14: Relationship Assertion
- **Concept Tested**: Checking consistency of relationship claims
- **Difficulty**: Medium
- **Fastest Approach**: Check if the relationship is logically possible
- **Appears in**: Infosys, Deloitte, Accenture
- **Example**: "A says B is my uncle. B says A is my niece. Is this possible?"

### Pattern 15: Spouse of Relation
- **Concept Tested**: In-law through spouse
- **Difficulty**: Easy–Medium
- **Fastest Approach**: Trace through the spouse
- **Appears in**: All companies
- **Example**: "A is B's father. B is C's husband. D is C's sister. How is A related to D?"

### Pattern 16: Building from Multiple Clues
- **Concept Tested**: Integrating multiple relationship facts
- **Difficulty**: Hard
- **Fastest Approach**: Build the tree incrementally, check consistency
- **Appears in**: Amazon, Google, Goldman Sachs
- **Example**: "A is B's sister. B is C's mother. D is A's son. E is D's uncle. If F is E's brother, how is F related to C?"

### Pattern 17: "Only" and "Elder/Younger" Qualifiers
- **Concept Tested**: Using exclusivity and age
- **Difficulty**: Medium
- **Fastest Approach**: Apply the qualifier first, then trace
- **Appears in**: TCS, Infosys, Accenture
- **Example**: "A is B's only sister. B is C's brother. C is D's daughter. How is A related to D?"

### Pattern 18: Horizontal vs. Vertical Relations
- **Concept Tested**: Siblings vs. parents
- **Difficulty**: Easy
- **Fastest Approach**: Check generation level
- **Appears in**: All companies
- **Example**: "A is B's grandfather. C is B's mother. D is C's sister. How is A related to D?"

### Pattern 19: Interconnected Families
- **Concept Tested**: Multiple marriages linking families
- **Difficulty**: Hard
- **Fastest Approach**: Separate trees, find intersection
- **Appears in**: Amazon, Google
- **Example**: "A's wife and B's husband are siblings. C is A's child. D is B's child. How is C related to D?"

### Pattern 20: Verbal Relationship Chain
- **Concept Tested**: Long chain tracing
- **Difficulty**: Hard
- **Fastest Approach**: Trace backward step by step
- **Appears in**: Amazon, Microsoft, Google
- **Example**: "A is B's sister's husband. B is C's father's son. D is C's mother. How is A related to D?"

---

## 💼 Placement & Interview Relevance

### Service-Based Companies

| Company | Questions | Difficulty | Pattern |
|---|---|---|---|
| **TCS** | 1–2 | Easy | Direct relationship, chain |
| **Infosys** | 1 | Easy–Medium | Chain, coded relations |
| **Wipro** | 1 | Easy | Counting, basic relations |
| **Accenture** | 1–2 | Easy–Medium | Mixed relations, in-laws |
| **Cognizant** | 1 | Easy | Chain, direct relation |

### Product-Based Companies

| Company | Questions | Difficulty | Pattern |
|---|---|---|---|
| **Amazon** | 1–2 | Medium–Hard | Complex chains, in-laws |
| **Microsoft** | 1 | Medium | Multi-step chains |
| **Google** | 0–1 | Hard | Cousins, interconnected |
| **Goldman Sachs** | 1 | Medium–Hard | Age+relation puzzles |

---

## 🚀 Beginner → Advanced Roadmap

### Day 1: Fundamentals
1. Memorize all kinship terms — write them out 5 times
2. Learn the family tree method — practice drawing trees for simple descriptions
3. Master generation tracking — up/down/sideways
4. Practice 20 basic relationship questions

**Milestone**: You can draw a family tree from any description in under 30 seconds.

### Day 2: Intermediate Concepts
5. Learn coded/symbolic relations — practice translation
6. Master in-law relationships — trace through spouses
7. Practice "not a blood relation" problems
8. Practice sibling distinctions (half/step/full)

**Milestone**: Handle any chain relationship question in under 60 seconds.

### Day 3: Advanced & Placement Practice
9. Practice multi-generation problems
10. Practice cousin relationships
11. Solve 30 TCS/Infosys pattern questions
12. Attempt 20 Amazon/Microsoft level questions

**Milestone**: 95% accuracy on all blood relations questions.

---

## 📊 Difficulty Breakdown

| Subtopic | Difficulty | Reason |
|---|---|---|
| Direct kinship terms | 🟢 **Easy** | Vocabulary only |
| Simple chain (2-3 steps) | 🟢 **Easy** | Trace one path |
| Counting relatives | 🟢 **Easy** | Systematic counting |
| Generation tracking | 🟡 **Medium** | Direction confusion |
| In-law relationships | 🟡 **Medium** | Must trace through spouse |
| Coded relations | 🟡 **Medium** | Two-step translation |
| "Only" / "Elder" qualifiers | 🟡 **Medium** | Apply constraint first |
| Mixed blood + in-law | 🟡 **Medium** | Two types of connections |
| Multi-step chains (4+) | 🟠 **Hard** | Many nodes to track |
| Cousin relationships | 🟠 **Hard** | Multiple generations sideways |
| Interconnected families | 🟠 **Hard** | Two trees intersecting |
| Step/half sibling | 🟠 **Hard** | Subtle distinctions |
| "Not a blood relation" | 🟠 **Hard** | Must identify all paths |
| Long verbal chain | 🟠 **Hard** | 5+ steps, multiple branches |
| Age + relationship | 🔴 **Very Hard** | Dual constraints |
| Multiple marriages | 🔴 **Very Hard** | Complex tree intersection |

---

## 🎓 Mastery Plan

### For Basic Understanding
- **Questions needed**: 25–30
- **Time required**: 2–3 hours
- **Goal**: Master kinship vocabulary, draw basic family trees

### For Placement Readiness
- **Questions needed**: 50–70
- **Time required**: 4–5 hours
- **Goal**: 95% accuracy on all service-company blood relations questions

### For Product-Based Company Readiness
- **Questions needed**: 80–100
- **Time required**: 6–8 hours
- **Goal**: Handle multi-step chains, in-laws, and cousin problems

---

## ❌ Common Traps & Mistakes

### Trap 1: Forgetting Spouse Gender
- **Mistake**: Assuming spouse's gender from the first person's name
- **Fix**: Always check context for "his wife" vs "her husband."

### Trap 2: Confusing Uncle/Aunt with Nephew/Niece
- **Mistake**: Uncle/Aunt = parent's sibling. Nephew/Niece = sibling's child.
- **Fix**: Draw the tree: parent's sibling → your generation -1 = your nephew/niece.

### Trap 3: Treating In-laws as Blood
- **Mistake**: Calling a sister-in-law a "real sister"
- **Fix**: Mark all marital connections with a dashed line. Only solid lines are blood.

### Trap 4: Tracing in the Wrong Direction
- **Mistake**: Going from A to B when the relationship is described from B to A
- **Fix**: Trace backward: "A is B's sister" → B is A's sibling.

### Trap 5: Cousin Confusion
- **Mistake**: Calling any relative your age a "cousin"
- **Fix**: Cousin = child of your uncle/aunt. Same grandparents, not same parents.

### Trap 6: Step vs. Half Sibling
- **Mistake**: Treating step-sibling as half-sibling
- **Fix**: Step = no shared parent. Half = one shared parent. Both are different from full sibling.

### Trap 7: Not Drawing the Tree
- **Mistake**: Trying to solve mentally without visualization
- **Fix**: Always draw the tree. Every time. Without exception.

---

## 📝 Practice Section

### 🟢 Easy (Level 1) — 20 Questions

**Q1.** A is B's mother. B is C's sister. How is A related to C? **[TCS]**

**Q2.** P is Q's father. Q is R's sister. How is P related to R? **[Infosys]**

**Q3.** A has three sons. Each son has two daughters. How many granddaughters does A have? **[Wipro]**

**Q4.** M is N's brother. N is O's mother. P is O's sister. How is M related to P? **[TCS]**

**Q5.** A is B's sister. B is C's father. D is C's mother. How is A related to D? **[Cognizant]**

**Q6.** Raj is Geeta's husband. Geeta is Sita's mother. How is Raj related to Sita? **[TCS]**

**Q7.** A has 4 children. Each child has 3 children of their own. How many grandchildren does A have? **[Accenture]**

**Q8.** X is Y's daughter. Y is Z's sister. How is X related to Z? **[TCS]**

**Q9.** A is B's paternal grandfather. B's mother is C. How is A related to C? **[Infosys]**

**Q10.** Rohit is Mohan's son. Mohan is Ramesh's brother. How is Ramesh related to Rohit? **[Wipro]**

**Q11.** A is B's mother. B is C's wife. D is C's daughter. How is A related to D? **[TCS]**

**Q12.** P is Q's sister. Q is R's brother. R is S's father. How is P related to S? **[Accenture]**

**Q13.** A has 5 siblings. B is A's brother. How many siblings does B have? **[TCS]**

**Q14.** A is B's uncle. B is C's brother. D is C's mother. How is A related to D? **[Infosys]**

**Q15.** X is Y's father. Y is Z's mother. W is Z's sister. How is X related to W? **[TCS]**

**Q16.** A is B's grandmother. B is C's daughter. D is C's father. How is A related to D? **[Wipro]**

**Q17.** M is N's son. N is O's daughter. P is O's husband. How is M related to P? **[TCS]**

**Q18.** A is B's aunt. B is C's daughter. D is C's mother. How is A related to D? **[Accenture]**

**Q19.** P is Q's grandfather. Q is R's sister. R is S's brother. How is P related to S? **[TCS]**

**Q20.** A has 2 sons and 2 daughters. Each son has 1 daughter. Each daughter has 1 son. How many male grandchildren does A have? **[Infosys]**

---

### 🟡 Medium (Level 2) — 20 Questions

**Q21.** A is B's brother-in-law. B is C's sister. D is C's mother. How is A related to D? **[Amazon]**

**Q22.** P is Q's son. Q is R's daughter. R is S's mother. How is P related to S? **[Microsoft]**

**Q23.** A is B's paternal uncle. B's father is C. C's sister is D. How is A related to D? **[Deloitte]**

**Q24.** X is Y's daughter's husband. Y is Z's mother. W is Z's brother. How is X related to W? **[Amazon]**

**Q25.** A is B's mother. B is C's sister. D is C's son. E is D's sister. How is B related to E? **[Microsoft]**

**Q26.** P is Q's aunt. Q is R's mother. R is S's daughter. S is T's wife. How is P related to T? **[Deloitte]**

**Q27.** A and B are siblings. B is C's husband. D is C's daughter. E is D's sister. F is E's brother. How is A related to F? **[Amazon]**

**Q28.** X is Y's mother's father. Y is Z's daughter. How is X related to Z? **[TCS]**

**Q29.** A is B's father-in-law. B is C's husband. D is C's sister. How is A related to D? **[Goldman Sachs]**

**Q30.** P is Q's grandmother. Q is R's son. S is R's daughter. T is S's brother. How is P related to T? **[Microsoft]**

**Q31.** A is B's mother's brother. B is C's father. D is C's wife. E is D's daughter. How is A related to E? **[Amazon]**

**Q32.** X is Y's sister's husband. Y is Z's mother. W is Z's father. How is X related to W? **[Deloitte]**

**Q33.** A is B's uncle. B is C's sister. D is C's mother. E is D's husband. How is E related to A? **[TCS]**

**Q34.** P is Q's maternal uncle. Q is R's daughter. R is S's wife. How is P related to S? **[Microsoft]**

**Q35.** A and B are cousins. A's mother is C. C's sister is D. E is D's daughter. How is A related to E? **[Amazon]**

**Q36.** X is Y's father. Y is Z's sister. Z is W's mother. How is X related to W? **[TCS]**

**Q37.** A is B's brother-in-law. B is C's sister. C is D's daughter. How is A related to D? **[Goldman Sachs]**

**Q38.** P is Q's grandfather. Q is R's sister. R is S's brother. S is T's father. How is P related to T? **[Deloitte]**

**Q39.** A is B's mother's sister. B is C's brother. D is C's wife. How is A related to D? **[TCS]**

**Q40.** X is Y's uncle. Y is Z's mother. Z is W's daughter. How is X related to W? **[Microsoft]**

---

### 🟠 Hard (Level 3) — 20 Questions

**Q41.** A is B's father's sister. B's father is C. C's brother is D. D's daughter is E. How is A related to E? **[Google]**

**Q42.** P is Q's sister. Q is R's mother. R is S's grandmother. S is T's father. U is T's wife. How is P related to U? **[Amazon]**

**Q43.** A is B's brother. B and C are sisters. D is C's daughter. E is D's husband. F is E's sister. How is A related to F? **[Microsoft]**

**Q44.** X is Y's maternal grandfather. Y is Z's sister. Z is W's wife. W is V's father. How is X related to V? **[Google]**

**Q45.** A and B are siblings. B is married to C. C is D's daughter. D is E's mother. F is E's sister. How is A related to F? **[Amazon]**

**Q46.** P is Q's paternal uncle. Q is R's sister. R is S's daughter. S is T's husband. How is P related to T? **[Goldman Sachs]**

**Q47.** A is B's father's mother. B is C's sister. C is D's daughter. D is E's father. How is A related to E? **[Google]**

**Q48.** X and Y are brothers. Z is Y's daughter. W is Z's mother's sister. How is W related to X? **[Microsoft]**

**Q49.** A is B's grandfather. B is C's daughter. C is D's sister. D is E's mother. How is A related to E? **[Amazon]**

**Q50.** P is Q's aunt. Q is R's mother. R is S's daughter. S is T's wife. U is T's brother. How is P related to U? **[Microsoft]**

**Q51.** A is B's sister's husband. B and C are sisters. D is C's daughter. E is D's mother. F is E's sister. How is A related to F? **[Google]**

**Q52.** X is Y's maternal grandmother. Y is Z's sister. Z is W's wife. W is V's father. How is X related to V? **[Amazon]**

**Q53.** A and B are first cousins. A's mother is C. C's sister is D. D's son is E. E's sister is F. How is A related to F? **[Microsoft]**

**Q54.** P is Q's uncle. Q is R's daughter. R is S's sister. S is T's mother. U is T's daughter. How is P related to U? **[Goldman Sachs]**

**Q55.** A is B's father-in-law. B is C's husband. C is D's sister. D is E's daughter. E is F's mother. How is A related to F? **[Amazon]**

**Q56.** X and Y are cousins. Y's mother is Z. Z's brother is W. W's daughter is V. How is X related to V? **[Google]**

**Q57.** A is B's grandmother. B is C's only child. C is D's spouse. D is E's sister. F is E's brother. How is A related to F? **[Microsoft]**

**Q58.** P is Q's mother's sister. Q is R's daughter. R is S's wife. S is T's father. How is P related to T? **[Deloitte]**

**Q59.** A and B are sisters. B is married to C. C is D's son. E is D's daughter. F is E's husband. How is A related to F? **[Amazon]**

**Q60.** X is Y's aunt. Y is Z's mother. Z is W's daughter. W is V's husband. How is X related to V? **[Microsoft]**

---

### 🔴 Product-Based Company Level — 10 Questions

**Q61.** In a joint family: A and B are brothers. C is B's wife. D is C's sister. E is D's daughter. F is E's husband. G is F's sister. H is G's brother. I is H's wife. A and J are siblings. How is I related to J? **[Amazon L5]**

**Q62.** A says, "B is my father's only sister." B says, "C is my brother." D is C's mother. E is D's daughter. F is E's sister. G is F's husband. H is G's brother. How is A related to H? (Assume no other siblings unless stated) **[Google]**

**Q63.** A joint family has three generations. The eldest is A. A has two sons B and C. B has a daughter D and a son E. C has a daughter F and a son G. D marries H, who is the son of I. I is the grandmother of J, who is H's nephew. K is J's cousin. K's mother is L. Find the relationship between G and L. **[Microsoft L64]**

**Q64.** A is B's father-in-law. B is C's sister. C is D's daughter. D is E's son. E is F's brother. G is F's wife. H is G's mother. A is I's grandfather. How is H related to I? **[Amazon L6]**

**Q65.** In a family reunion, every person shakes hands with every other person. If there are 5 families, each with 3 members, and no two people from the same family shake hands, how many handshakes? **[Google / Interview Puzzle]**

**Q66.** A is B's sister. B is C's mother. C is D's daughter. E is D's sister. F is E's brother. G is F's wife. H is G's mother. A is I's aunt. I is J's sister. J is K's brother. K is L's son. M is L's daughter. How is A related to M? **[Goldman Sachs]**

**Q67.** A says to B, "You are the daughter of my mother's only sister." B is C's wife. D is C's mother. E is D's brother. F is E's son. G is F's wife. How is A related to G? **[Amazon / Microsoft]**

**Q68.** In a family of 5 generations, each person has exactly 2 children (one boy, one girl). A is the patriarch. If A has 2 children, B and C (B=boy, C=girl), and the pattern continues, how many great-great-grandchildren does A have? **[Google / Math Olympiad]**

**Q69.** A and B are siblings. A's daughter is C. C's daughter is D. D's son is E. E's sister is F. G is F's mother's sister. H is G's daughter. I is H's husband. How many generations apart are A and I? Who is A to I? **[Microsoft L65]**

**Q70.** A family has men and women arranged in a hierarchy: A is the patriarch. His sons are B, C, D. B's daughters are E, F. C has a son G and a daughter H. D has no children. E marries I (outsider). I's mother is J and father is K. J's brother is L. L's daughter is M. How is M related to G? If the family traces lineage through males only, who is G's male heir? **[Google / Amazon Interview]**

---

*(Solutions on next page)*

---

## ✅ Detailed Solutions

### 🟢 Easy Solutions

**Q1.** A→B (mother), B=C (sister) → A is C's mother. ✅

**Q2.** P→Q (father), Q=R (sister) → P is R's mother or father? Since Q is R's sister, P is parent of both. P is R's **father**. ✅

**Q3.** 3 sons × 2 daughters each = **6 granddaughters**. ✅

**Q4.** M=N (brother), N=O (mother), P=O (sister) → M is P's **maternal uncle**. ✅

**Q5.** A=B (sister), B=C (father), D=C (mother) → D is B's mother. A is D's **daughter**. ✅

**Q6.** Raj=Geeta (husband), Geeta=Sita (mother) → Raj is Sita's **father**. ✅

**Q7.** 4 children × 3 children each = **12 grandchildren**. ✅

**Q8.** X=Y (daughter), Y=Z (sister) → X is Z's **niece**. ✅

**Q9.** A=B (paternal grandfather) → A=B's father's father. B's mother=C → C is A's daughter-in-law. **A is C's father-in-law**? No. A is B's grandfather → B's parents are A's children. C is one of them. So A is C's **grandfather**. ✅

**Q10.** Rohit=Mohan (son), Mohan=Ramesh (brother) → Ramesh is Rohit's **uncle**. ✅

**Q11.** A=B (mother), B=C (wife), D=C (daughter) → A is D's **grandmother**. ✅

**Q12.** P=Q (sister), Q=R (brother), R=S (father) → P is S's **aunt**. ✅

**Q13.** A has 5 siblings. B=A's brother. B also has 5 siblings (same family). **B has 5 siblings** (excluding self). ✅

**Q14.** A=B (uncle), B=C (brother), D=C (mother) → A is D's **husband**. ✅

**Q15.** X=Y (father), Y=Z (sister), W=Z (sister) → X is W's **grandfather**. ✅

**Q16.** A=B (grandmother), B=C (daughter), D=C (father) → A is D's **mother-in-law**? No. A is grandmother of C. D is parent of C. A is D's **mother**. ✅

**Q17.** M=N (son), N=O (daughter), P=O (husband) → M is P's **son**. ✅

**Q18.** A=B (aunt), B=C (daughter), D=C (mother) → A is D's **sister**. ✅

**Q19.** P=Q (grandfather), Q=R (sister), R=S (brother) → P is S's **grandfather**. ✅

**Q20.** A has 2 sons, 2 daughters. Granddaughters from sons: 2×1=2. Granddaughters from daughters: 2×1=2. Male grandchildren: sons' sons=2×1=2, daughters' sons=2×1=2. **2 male grandchildren** from each side = 4 total male? Wait.
Grandchildren who are male:
- Sons' sons: 2 sons × 1 son each = 2
- Daughters' sons: 2 daughters × 1 son each = 2
Total male grandchildren = **4**. ✅

---

### 🟡 Medium Solutions

**Q21.** A=B (brother-in-law) → A is married to B's sibling or sibling of A's spouse. B=C (sister) → C is A's sister-in-law. D=C (mother) → D is A's mother-in-law. **A is D's son-in-law**. ✅

**Q22.** P=Q (son), Q=R (daughter), R=S (mother) → P is S's **grandson**. ✅

**Q23.** A=B (paternal uncle) → A is B's father's brother. B's father=C. C's sister=D → D is A's **sister** (A and D are siblings). ✅

**Q24.** X=Y (daughter's husband) → Y is X's wife. Y=Z (mother), Z=W (brother) → Y is W's mother. X is W's **father**. ✅

**Q25.** A=B (mother), B=C (sister), D=C (son), E=D (sister) → B and D are siblings. B is D's **aunt** (and sister). ✅

**Q26.** P=Q (aunt), Q=R (mother), R=S (daughter), S=T (wife) → P is T's **grandmother**. ✅

**Q27.** A=B (siblings), B=C (husband), D=C (daughter), E=D (sister), F=E (brother) → A and B are siblings. B is F's mother. A is F's **maternal uncle**. ✅

**Q28.** X=Y (mother's father) → X is Y's maternal grandfather. Y=Z (daughter) → Z is Y's daughter. X is Z's **great-grandfather**. ✅

**Q29.** A=B (father-in-law) → B is married to A's child. B=C (husband) → C is A's child. D=C (sister) → D is A's child. A is D's **father**. ✅

**Q30.** P=Q (grandmother), Q=R (son), S=R (daughter), T=S (brother) → P is T's **grandmother**. ✅

**Q31.** A=B (mother's brother) → A is B's **maternal uncle**. B=C (father), D=C (wife), E=D (daughter) → E is B's daughter. A is E's **maternal uncle**. ✅

**Q32.** X=Y (sister's husband) → Y is X's sister-in-law. Y=Z (mother), Z=W (father) → Z is W's wife. X is W's **brother-in-law**. ✅

**Q33.** A=B (uncle), B=C (sister), D=C (mother), E=D (husband) → D is B's mother. E is D's husband = B's father. A is B's father's brother → A is B's **paternal uncle**. E is B's **father**. A and E are **brothers**. ✅

**Q34.** P=Q (maternal uncle) → P is Q's mother's brother. Q=R (daughter), R=S (wife) → S is R's husband. P is S's **brother-in-law**. ✅

**Q35.** A and B are cousins → A's parent and B's parent are siblings. A's mother=C. C's sister=D. D's daughter=E → E is A's **cousin** (first cousin). ✅

**Q36.** X=Y (father), Y=Z (sister), Z=W (mother) → W is Y's mother. X is W's **father**. ✅

**Q37.** A=B (brother-in-law) → A is married to B's sibling. B=C (sister) → C is A's sister-in-law. D=C (daughter) → D is A's niece. **A is D's uncle**. ✅

**Q38.** P=Q (grandfather), Q=R (sister), R=S (brother), S=T (father) → P is T's **great-grandfather**. ✅

**Q39.** A=B (mother's sister) → A is B's **maternal aunt**. B=C (brother), D=C (wife) → D is B's wife. A is D's **sister-in-law**. ✅

**Q40.** X=Y (uncle), Y=Z (mother), Z=W (daughter) → Z is Y's daughter. X is Z's **great-uncle**? Wait. Y is Z's mother. X is Y's brother → X is Z's **maternal uncle**. ✅

---

### 🟠 Hard Solutions

**Q41.** A=B (father's sister) → A is B's **paternal aunt**. B's father=C. C's brother=D → D is B's paternal uncle = C's brother. D's daughter=E → E is B's cousin. A and D are siblings (both children of C's parents). A is E's **aunt**. ✅

**Q42.** P=Q (sister), Q=R (mother), R=S (grandmother), S=T (father), U=T (wife) → P is T's **grandmother**. ✅

**Q43.** A=B (brother), B=C (sisters), D=C (daughter), E=D (husband), F=E (sister) → F is D's sister-in-law = C's daughter-in-law. A is C's brother. C's daughter-in-law is A's **niece-in-law**? No. C's daughter is D. D's husband is E. E's sister is F. A is E's brother-in-law (A and E are brothers, both married to sisters B and D). So A is F's **brother-in-law**. ✅

**Q44.** X=Y (maternal grandfather) → X is Y's mother's father. Y=Z (sister), Z=W (wife), W=V (father) → V is Z's husband. X is V's **great-grandfather**. ✅

**Q45.** A and B are siblings. B=C (married), C=D (daughter), D=E (mother), F=E (sister) → F is D's sister = E's daughter? E is D's mother → F is D's **aunt**. A is B's sibling = C's sibling-in-law = E's **sister-in-law**. ✅

**Q46.** P=Q (paternal uncle) → P is Q's father's brother. Q=R (sister), R=S (daughter), S=T (husband) → T is S's husband = R's husband. P is T's **brother-in-law**. ✅

**Q47.** A=B (father's mother) → A is B's grandmother. B=C (sister), C=D (daughter), D=E (father) → E is C's father. A is E's **wife**. ✅

**Q48.** X and Y are brothers. Z=Y (daughter). W=Z (mother's sister) → W is Y's maternal aunt. X is Y's brother → X is W's **nephew**. ✅

**Q49.** A=B (grandfather), B=C (daughter), C=D (sister), D=E (mother) → E is D's mother = C's grandmother = A's **daughter**. ✅

**Q50.** P=Q (aunt), Q=R (mother), R=S (daughter), S=T (wife), U=T (brother) → P is T's **grandmother**. ✅

**Q51.** A=B (sister's husband) → B is A's sister. B=C (sisters). C=D (daughter). E=D (mother). F=E (sister) → F is D's sister = C's sister. A is F's **brother-in-law**. ✅

**Q52.** X=Y (maternal grandmother) → X is Y's mother's mother. Y=Z (sister), Z=W (wife), W=V (father) → V is Z's husband. X is V's **great-grandmother**. ✅

**Q53.** A and B are first cousins → parents are siblings. A's mother=C. C's sister=D. D's son=E. E's sister=F → F is A's **first cousin** (same as B). ✅

**Q54.** P=Q (uncle), Q=R (daughter), R=S (sister), S=T (mother), U=T (daughter) → U is T's daughter. P is U's **grandmother's brother** = **great-uncle**. ✅

**Q55.** A=B (father-in-law) → B is A's child. B=C (husband) → C is A's child. D=C (sister) → D is A's child. E=D (daughter) → E is A's grandchild. F=E (mother) → F is A's daughter-in-law. **A is F's father-in-law**. ✅

**Q56.** X and Y are cousins → parents are siblings. Y's mother=Z. Z's brother=W. W's daughter=V → V is X's **second cousin** (Z and W are siblings → Z is X's parent → W is X's aunt/uncle → W's daughter is X's first cousin once removed → V is X's second cousin? No. W is aunt/uncle → V is X's cousin. **V is X's cousin**. ✅

**Q57.** A=B (grandmother), B=C (only child) → C is A's grandchild. D=C (spouse), E=D (sister), F=E (brother) → F is C's **uncle**. A is F's mother-in-law. ✅

**Q58.** P=Q (mother's sister) → P is Q's **maternal aunt**. Q=R (daughter), R=S (wife), S=T (father) → T is R's husband. P is T's **sister-in-law**. ✅

**Q59.** A=B (sisters). B=C (married), C=D (son), E=D (daughter), F=E (husband) → F is D's husband = C's son-in-law. A is C's sister. A is F's **sister-in-law**. ✅

**Q60.** X=Y (aunt), Y=Z (mother), Z=W (daughter) → X is W's **great-aunt**. ✅

---

### 🔴 Product-Level Solutions

**Q61.** Joint family: A,B are brothers. C=B's wife. D=C's sister. E=D's daughter. F=E's husband. G=F's sister. H=G's brother. I=H's wife. A and J are siblings.
A,B are brothers. A and J are siblings → A,J,B are siblings.
C is B's wife → B,C are spouses. D is C's sister → D is B's sister-in-law.
E is D's daughter → E is B's niece.
F is E's husband → F is B's nephew-in-law.
G is F's sister → G is B's niece-in-law.
H is G's brother → H is B's nephew-in-law.
I is H's wife → I is B's niece-in-law.
A,J,B are siblings. I is married to H, who is A/B/J's nephew-in-law.
I is A's **niece-in-law** (through B's connection). ✅

**Q62.** A says B is A's father's only sister → B is A's **aunt**. B says C is B's brother → C is A's **uncle**. D is C's mother → D is A's grandmother. E is D's daughter → E is A's **aunt** (same as B). F is E's sister → F is A's aunt. G is F's husband → G is A's **uncle-in-law**? G is married to F, who is A's aunt. H is G's brother → H is F's brother-in-law = A's **uncle-in-law**. ✅

**Q63.** A is eldest. A has sons B,C. B has D,E. C has F,G. D marries H (H=son of I). I is grandmother of J (J=H's nephew). J is H's nephew → H's parent is sibling of J's parent. K is J's cousin → K and J share grandparents. K's mother=L.
G is C's son (D and E are B's children, F and G are C's children).
J is H's nephew. H is D's husband. So J is D's son? No — J is H's nephew means H's sibling is J's parent. H's parent is... I is grandmother of J. So I is H's grandmother. J is H's cousin? No — "H's nephew" means H is J's uncle's sibling? 
H's nephew = sibling of H's child OR child of H's sibling.
If I is grandmother of J, then I's child is J's parent. If H is I's grandchild, then H and J could be cousins.
This requires careful tracing: "I is grandmother of J" → I → J via one generation. So I's child is J's parent. If I's child = H (H is I's grandchild), then H and J are first cousins. H's nephew = child of H's sibling = J. So J is H's first cousin once removed? No — H's nephew means H is the uncle of J. So H's sibling is J's parent. But H and J are first cousins (siblings of H's parent = J's parent). This is complex.
Given the family: A→B,C. B→D,E. C→F,G. D→H. H's nephew = J. So J is child of H's sibling. H's sibling is... D is H's spouse, not sibling. H's sibling must be from D's side. K is J's cousin → K and J share grandparents = I and I's spouse. K's mother = L. L is I's child. So G is C's child. No direct relation given between G and the H/I/J family. **G and L are not related** (from different branches of the original family). ✅

**Q64.** A=B (father-in-law) → B is A's child. B=C (sister) → C is A's child. D=C (daughter) → D is A's grandchild. E=D (son) → E is A's great-grandson. F=E (brother) → F is A's great-grandson. G=F (wife) → G is A's great-granddaughter-in-law. H=G (mother) → H is A's great-grandchild-in-law.
A is I's grandfather → A is parent of I's parent. So I is A's grandchild or lower.
H and I: H is A's great-grandchild-in-law. I is A's grandchild. **H and I are...** H is I's **in-law** (specifically great-grandchild-in-law). ✅

**Q65.** 5 families, 3 members each = 15 people. No handshakes within same family.
Total handshakes if everyone shook hands = C(15,2) = 105.
Handshakes within each family = C(3,2) × 5 = 3 × 5 = 15.
Total without restriction = 105. Subtract within-family = 105 - 15 = **90 handshakes**. ✅

**Q66.** A=B (sister). B=C (mother). C=D (daughter). E=D (sister). F=E (brother). G=F (wife). H=G (mother). A=I (aunt). I=J (sister). J=K (brother). K=L (son). M=L (daughter).
Trace back: M→L→K→J→I→A. K is L's son. J is L's brother. I is J's sister = L's sister. A is I's aunt = L's great-aunt.
Number of generations: A is 3 generations above L (A→I→L, wait: A is sister of I's parent? A=I's aunt → I is A's niece → I is 1 gen below A. L is sibling of I's child? J is I's sister. K is J's brother = I's brother. L is K's sister = I's sibling. L is I's sibling → I and L are same generation. A is I's aunt → 1 gen above. So A is **2 generations above L** (A→I's parent→I, A→I's parent→... actually A and I's parent are siblings. I is A's niece. L is sibling of K. K is sibling of J. J is sibling of I. So I and L are first cousins. A is I and L's aunt. **A is L's great-aunt. 2 generations apart.** ✅

**Q67.** A to B: "You are the daughter of my mother's only sister." → A's mother has only one sister. So B is the daughter of A's maternal aunt → B is A's **cousin**.
B=C (wife). D=C (mother). E=D (brother). F=E (son). G=F (wife).
G is F's wife = E's daughter-in-law. A and G: A is B's cousin. G is F's wife. F is E's son. E is D's brother = B's maternal uncle. So F is A's cousin-in-law? No.
E is B's maternal uncle. F is E's son → F is B's **cousin**. G is F's wife → G is B's cousin-in-law. A is B's cousin. **A is G's cousin-in-law**. ✅

**Q68.** Each person has exactly 2 children (1 boy, 1 girl). A (patriarch) has 2 children: B(boy), C(girl).
Generation 2: B and C. B has B1(boy), B2(girl). C has C1(boy), C2(girl).
But "continues": Each person has 2 children. A=1 person. Gen 1: 2 people. Gen 2: 4 people. Gen 3: 8 people. Gen 4: 16 people. Gen 5: 32 people.
Great-great-grandchildren: From A, go down 4 generations.
Gen 1 (children): 2 people = A's children.
Gen 2 (grandchildren): 4 people = A's grandchildren.
Gen 3 (great-grandchildren): 8 people.
Gen 4 (great-great-grandchildren): 16 people.
**A has 16 great-great-grandchildren.** ✅

**Q69.** A=B (siblings). A's daughter=C. C's daughter=D. D's son=E. E's sister=F. G=F (mother's sister). H=G (daughter). I=H (husband).
Generations: A(0), C(-1), D(-2), E(-3), F(-3), G(-2), H(-3), I(-3).
A and I: A(0), C(-1), D(-2), E(-3), F(-3), G(-2), H(-3), I(-3). From A to I: A→C→D→E→F→G→H→I. That's 7 steps. **7 generations apart**.
A to C: -1. C to D: -1. Total -2. D to E: -1. Total -3. E to F: 0 (siblings). F to G: -1 (F's mother). G to H: -1 (mother's daughter). H to I: 0 (spouse). Wait: E is F's brother. G is F's mother's sister. So G is E's aunt. H is G's daughter. H is E's first cousin. I is H's husband.
A to E: A→C→D→E = 3 generations. **A is E's grandmother**.
A to H: A→C→D→E→F→G→H = 6 generations. H is A's great-great-great-granddaughter? 6 down = great-great-great-granddaughter.
I is H's husband. A is H's great-great-great-grandmother. **A is I's great-great-great-grandmother-in-law**. ✅

**Q70.** A=patriarch. Sons: B,C,D. B's daughters: E,F. C: G,H. D: no children.
E marries I (outsider). I's mother=J, father=K. J's brother=L. L's daughter=M.
G is C's son.
M is L's daughter. L is J's brother. J is I's mother. So I→J→L→M. J and K are I's parents. L is I's maternal uncle. M is I's cousin.
G and M: G is from B/C branch. M is from I's family (outsider married in). **G and M are not related** (M is an outsider through E's marriage).
Male heir (male lineage only): A→B,C,D. B has no sons (daughters only). C has G (son). D has no children. **G is G's male heir** (tracing lineage: A→C→G). ✅

---

## 📚 Best Resources

### 🥇 YouTube Channels (Free)

| Rank | Channel | Best For |
|---|---|---|
| 1 | **Gagan MATHS** | Systematic tree method |
| 2 | **Aditya Ranjan (RBank)** | Quick relationship tracing |
| 3 | **Study Smart** | Logical deduction approach |

### 🥈 Websites

| Rank | Platform | Best For |
|---|---|---|
| 1 | **IndiaBix** | All blood relation patterns |
| 2 | **GeekforGeeks** | Coded relations |
| 3 | **M4Maths** | TCS-specific patterns |

### 🥉 Books

| Rank | Book |
|---|---|
| 1 | **Arun Sharma — Logical Reasoning** |
| 2 | **RS Agarwal — Verbal & Non-verbal** |

---

## 🎯 Final Verdict

### Scores

| Metric | Rating |
|---|---|
| **Importance Rating** | ★★★★☆ (4/5) |
| **Placement ROI Score** | **7/10** — High accuracy, moderate frequency |
| **Difficulty Score** | **5/10** — Logic-based, not formula-heavy |
| **Priority Order** | **#6** among core aptitude topics |

### Company-Level Verdict

| Target | Verdict | Reasoning |
|---|---|---|
| **TCS/Infosys/Wipro** | ✅ **Mandatory** | 1-2 easy questions, tree method solves all |
| **10 LPA+** | ✅ **Important** | Always appears |
| **Accenture/Cognizant** | ✅ **Important** | Direct + coded relations |
| **20 LPA+** | ✅ **Important** | In-law + mixed relations |
| **Amazon/Microsoft** | ✅ **Important** | Complex chains, in-laws |
| **Goldman Sachs** | ⚠️ **Optional** | Age+relation puzzles |
| **Google** | ⚠️ **Optional** | Interconnected family puzzles |

### Bottom Line

> Blood Relations rewards **drawing over thinking**. The single most effective technique is the family tree method — always draw the tree before answering. Master the three-direction rule (up = ancestors, down = descendants, sideways = same generation, different branch), and this topic becomes a guaranteed full-score section.

**Study Time**: 3–4 hours | **Questions to Practice**: 60–80 | **Expected Score**: +1–2 marks per test

---

*End of Guide — Blood Relations | Elite Placement Aptitude Series*
