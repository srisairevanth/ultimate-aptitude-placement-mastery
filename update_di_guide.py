import os
import re

md_path = r"c:\Users\sai\OneDrive\Desktop\Aptitude\data_interpretation_study_guide.md"

with open(md_path, "r", encoding="utf-8") as f:
    content = f.read()

# Helper to apply and report regex replacements
def apply_regex(pattern, replacement, content, name):
    occ = len(re.findall(pattern, content, flags=re.DOTALL))
    if occ == 1:
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        print(f"[OK] {name}: Succeeded.")
        return content, True
    else:
        print(f"[FAIL] {name}: Failed. Found {occ} occurrences (expected 1).")
        return content, False

success = True

# --- 1. Q26 Boys/Girls Ratio ---
pattern_q26 = r"\*\*Q26\.\*\* In a table, the ratio of boys to girls in School A is 3:2 and in School B is 4:3\. If both schools have the same number of total students, and School A has 300 boys, how many girls are in School B\?\n- A\) 250  B\) 270  C\) 280  D\) 300"
rep_q26 = """**Q26.** In a table, the ratio of boys to girls in School A is 3:2 and in School B is 23:27. If both schools have the same number of total students, and School A has 300 boys, how many girls are in School B?
- A) 250  B) 270  C) 280  D) 300"""
content, s = apply_regex(pattern_q26, rep_q26, content, "Q26 Question")
success = success and s

# --- 2. Q35 Options ---
pattern_q35 = r"\*\*Q35\.\*\* A table shows student marks in 4 subjects\. Average of 3 subjects is 75\. The 4th subject has 85 marks\. What is the overall average\?\n- A\) 75  B\) 77  C\) 78  D\) 80"
rep_q35 = """**Q35.** A table shows student marks in 4 subjects. Average of 3 subjects is 75. The 4th subject has 85 marks. What is the overall average?
- A) 75  B) 77.5  C) 78  D) 80"""
content, s = apply_regex(pattern_q35, rep_q35, content, "Q35 Question")
success = success and s

# --- 3. Q38 Age group ---
pattern_q38 = r"\*\*Q38\.\*\* Two pie charts show population distribution of a city by age group for 2020 and 2030\. The 0-18 age group changes from 35% to 30%\. If the total population in 2030 is 12 Lakhs, and the 0-18 group decreases by 20,000 in absolute terms, what was the population in 2020\?\n- A\) 8 Lakhs  B\) 10 Lakhs  C\) 12 Lakhs  D\) Cannot be determined"
rep_q38 = """**Q38.** Two pie charts show population distribution of a city by age group for 2020 and 2030. The 0-18 age group changes from 35% in 2020 to 30% in 2030. If the total population in 2030 is 12 Lakhs, and the 0-18 group increases by 10,000 in absolute terms from 2020 to 2030, what was the population in 2020?
- A) 8 Lakhs  B) 10 Lakhs  C) 12 Lakhs  D) Cannot be determined"""
content, s = apply_regex(pattern_q38, rep_q38, content, "Q38 Question")
success = success and s

# --- 4. Q40 Train average speed ---
pattern_q40 = r"\*\*Q40\.\*\* A caselet: \"A train travels 600 km\. It covers 30% at 60 km/h, 40% at 80 km/h, and the remaining at 100 km/h\. What is the average speed\?\"\n- A\) 72 km/h  B\) 75 km/h  C\) 78 km/h  D\) 80 km/h"
rep_q40 = """**Q40.** A caselet: "A train travels 600 km. It covers 30% at 60 km/h, 40% at 80 km/h, and the remaining at 90 km/h. What is the average speed?"
- A) 72 km/h  B) 75 km/h  C) 78 km/h  D) 80 km/h"""
content, s = apply_regex(pattern_q40, rep_q40, content, "Q40 Question")
success = success and s

# --- 5. Q42 Market size ---
pattern_q42 = r"\*\*Q42\.\*\* A stacked bar chart shows monthly sales \(₹ Lakhs\) for 4 products across 6 months\. The chart reveals that Product X's share of total monthly sales remains constant at 25% throughout\. In Month 3, Product X sells ₹45 Lakhs\. What is the total market size in Month 3\?\n- A\) ₹1,60,000  B\) ₹1,75,000  C\) ₹1,80,000  D\) ₹1,95,000"
rep_q42 = """**Q42.** A stacked bar chart shows monthly sales (₹ Lakhs) for 4 products across 6 months. The chart reveals that Product X's share of total monthly sales remains constant at 25% throughout. In Month 3, Product X sells ₹45 Lakhs. What is the total market size in Month 3?
- A) ₹160 Lakhs  B) ₹175 Lakhs  C) ₹180 Lakhs  D) ₹195 Lakhs"""
content, s = apply_regex(pattern_q42, rep_q42, content, "Q42 Question")
success = success and s

# --- 6. Q45 Real Estate Portfolio ---
pattern_q45 = r"\*\*Q45\.\*\* Two pie charts show investment portfolio allocation for 2022 and 2023:.*?- A\) ₹2,20,000  B\) ₹2,60,000  C\) ₹2,86,000  D\) ₹3,00,000"
rep_q45 = """**Q45.** Two pie charts show investment portfolio allocation for 2022 and 2023:
2022: Stocks=40%, Bonds=30%, Real Estate=20%, Cash=10%
2023: Stocks=45%, Bonds=25%, Real Estate=22%, Cash=8%
If the total portfolio value grew from ₹10 Lakhs to ₹13 Lakhs, what is the absolute increase in Real Estate investment?
- A) ₹60,000  B) ₹86,000  C) ₹1,10,000  D) ₹1,20,000"""
content, s = apply_regex(pattern_q45, rep_q45, content, "Q45 Question")
success = success and s

# --- 7. Q46 consistent growth rate ---
pattern_q46 = r"\*\*Q46\.\*\* A table shows the number of students in 5 departments over 3 years with some missing values:.*?Find the value of 2023 for Dept B\.\n- A\) 87\.12  B\) 88  C\) 92\.4  D\) 96"
rep_q46 = """**Q46.** A table shows the number of students in 5 departments over 3 years with some missing values:
Dept | 2021 | 2022 | 2023
A | 80 | 100 | 120
B | 60 | 72 | ?
C | 90 | ?  | 130
D | ?  | 88  | 96
E | 70 | 75  | 82

Additional info: Average students per dept in 2022 = 85. Dept B grew at 20% per year consistently. Dept C's growth from 2021 to 2023 is 44.44%. Dept D had equal numbers in 2021 and 2023. Find the value of 2023 for Dept B.
- A) 86.4  B) 88  C) 92.4  D) 96"""
content, s = apply_regex(pattern_q46, rep_q46, content, "Q46 Question")
success = success and s

# --- 8. Q50 household expense total ---
pattern_q50 = r"\*\*Q50\.\*\* Two pie charts show expenses breakdown for Household A and Household B\. Household A's total monthly expense = ₹50,000\. Household B's total monthly expense = ₹75,000\. A's Food expense = 25% of A's total\. B's Food expense = 20% of B's total\. If A's Food expense = B's Food expense, what is the ratio of A's Food to B's total expense\?\n- A\) 1:3  B\) 1:4  C\) 1:5  D\) Cannot be determined"
rep_q50 = """**Q50.** Two pie charts show expenses breakdown for Household A and Household B. Household A's total monthly expense = ₹60,000. Household B's total monthly expense = ₹75,000. A's Food expense = 25% of A's total. B's Food expense = 20% of B's total. What is the ratio of A's Food expense to B's total expense?
- A) 1:3  B) 1:4  C) 1:5  D) Cannot be determined"""
content, s = apply_regex(pattern_q50, rep_q50, content, "Q50 Question")
success = success and s

# --- 9. Q51 oil contribution options fix ---
pattern_q51 = r"\*\*Q51\.\*\* A stacked bar chart shows percentage distribution of energy sources across 5 years\..*?- A\) Decrease of 5%  B\) Decrease of 10%  C\) Increase of 5%  D\) Cannot be determined"
rep_q51 = """**Q51.** A stacked bar chart shows percentage distribution of energy sources across 5 years. Coal decreases from 60% to 40%. Renewable increases from 10% to 25%. Nuclear stays constant at 5%. Gas increases from 15% to 20%. Oil makes up the remainder. In Year 5, total energy = 500 units. What is the change in Oil's contribution from Year 1 to Year 5?
- A) Decrease of 5%  B) Decrease of 10%  C) Increase of 5%  D) No change"""
content, s = apply_regex(pattern_q51, rep_q51, content, "Q51 Question")
success = success and s

# --- 10. Q53 shopkeeper total revenue redundancy ---
pattern_q53 = r"\*\*Q53\.\*\* A caselet: \"A shopkeeper sells two articles at the same selling price\. He makes a profit of 20% on one and a loss of 20% on the other\. The cost price of the first article is ₹500\. The total revenue from both articles is ₹2,400\. Find the profit/loss % overall\.\"\n- A\) 1% Loss  B\) 2% Profit  C\) 4% Loss  D\) 4% Profit"
rep_q53 = """**Q53.** A caselet: "A shopkeeper sells two articles at the same selling price. He makes a profit of 20% on one and a loss of 20% on the other. The cost price of the first article is ₹500. Find the profit/loss % overall."
- A) 1% Loss  B) 2% Profit  C) 4% Loss  D) 4% Profit"""
content, s = apply_regex(pattern_q53, rep_q53, content, "Q53 Question")
success = success and s

# --- 11. Q57 friends time-weighted profit ---
pattern_q57 = r"\*\*Q57\.\*\* A caselet: \"Three friends A, B, C invest in a business\. A invests ₹X for 6 months, B invests ₹2X for the entire year, C invests ₹3X for 4 months\. At the end of the year, the profit is ₹2,40,000\. A's share of profit is ₹60,000\.\" Find C's share\.\n- A\) ₹36,000  B\) ₹48,000  C\) ₹72,000  D\) ₹96,000"
rep_q57 = """**Q57.** A caselet: "Three friends A, B, C invest in a business. A invests ₹X for 6 months, B invests ₹2X for 6 months, and C invests ₹3X for 4 months. At the end of the year, the profit is ₹2,40,000. A's share of profit is ₹48,000." Find C's share.
- A) ₹36,000  B) ₹48,000  C) ₹72,000  D) ₹96,000"""
content, s = apply_regex(pattern_q57, rep_q57, content, "Q57 Question")
success = success and s

# --- 12. Q59 company D share addition ---
pattern_q59 = r"\*\*Q59\.\*\* A pie chart shows market share of 5 companies\. The angle of Company A's slice is 144°\. Company B's share is 1\.5 times Company C's\. Company D and E together account for 18% of the market\. If Company A's actual revenue = ₹360 Crores, what is Company D's revenue\?\n- A\) ₹48 Cr  B\) ₹54 Cr  C\) ₹60 Cr  D\) ₹72 Cr"
rep_q59 = """**Q59.** A pie chart shows market share of 5 companies. The angle of Company A's slice is 144°. Company B's share is 1.5 times Company C's. Company D and E together account for 18% of the market, with Company D's share being half of Company E's share. If Company A's actual revenue = ₹360 Crores, what is Company D's revenue?
- A) ₹48 Cr  B) ₹54 Cr  C) ₹60 Cr  D) ₹72 Cr"""
content, s = apply_regex(pattern_q59, rep_q59, content, "Q59 Question")
success = success and s

# --- 13. Q62 Table ---
pattern_q62_table = r"\| Year \| Company X Revenue \(₹ Cr\) \| Company Y Revenue \(₹ Cr\) \| X Profit Margin \(\%\) \| Y Profit Margin \(\%\) \|\n\|------\|--------------------------\|--------------------------\|---------------------\|---------------------\|.*?2023 \| 450 \| 375 \| 20\% \| 18\% \|"
rep_q62_table = """| Year | Company X Revenue (₹ Cr) | Company Y Revenue (₹ Cr) | X Profit Margin (%) | Y Profit Margin (%) |
|------|--------------------------|--------------------------|---------------------|---------------------|
| 2019 | 200 | 150 | 12% | 10% |
| 2020 | 250 | 180 | 10% | 15% |
| 2021 | 300 | 240 | 15% | 14% |
| 2022 | 360 | 300 | 18% | 16% |
| 2023 | 450 | 375 | 20% | 18% |"""
content, s = apply_regex(pattern_q62_table, rep_q62_table, content, "Q62 Table")
success = success and s

# --- 14. Q68 initial investment sum contradiction fix ---
pattern_q68 = r"\*\*Q68\.\*\* \*\(Complex Caselet\)\* Five friends — A, B, C, D, E — invest in a startup\..*?- E's investment = 10% of total investment"
rep_q68 = """**Q68.** *(Complex Caselet)* Five friends — A, B, C, D, E — invest in a startup. The following information is given:

- E's investment = ₹1,00,000
- D invests ₹1,20,000 more than E
- C and D together invest ₹3,00,000
- B invests ₹50,000 more than C
- A invests twice what B invests"""
content, s = apply_regex(pattern_q68, rep_q68, content, "Q68 Question")
success = success and s


# --- SOLUTIONS ---

# 15. Q26 Solution
pattern_sol_q26 = r"\*\*Q26\.\*\* A's boys = 300 = 3/5 × total\. Total in A = 500\. B's ratio 4:3 → B's girls = 3/7 × 500 = \*\*214\.3\*\* ≈ \*\*B\*\* \(closest match\)"
rep_sol_q26 = """**Q26.** A's boys = 300 = 3/5 × total. Total in A = 500. Since both schools have the same number of students, School B has 500 students. B's ratio of boys:girls = 23:27 → B's girls = (27/50) × 500 = **270** → **B**"""
content, s = apply_regex(pattern_sol_q26, rep_sol_q26, content, "Q26 Solution")
success = success and s

# 16. Q38 Solution
pattern_sol_q38 = r"\*\*Q38\.\*\* Let 2020 population = P\. 2020 group = 35% of P\. 2030 group = 30% of 12L = 3\.6L\. Decrease = 0\.2L\. So 35% of P - 3\.6L = 0\.2L → P = 3\.8L/0\.35 = \*\*10\.86L\*\* ≈ \*\*B\*\*"
rep_sol_q38 = """**Q38.** Let 2020 population = P. 0-18 group in 2020 = 35% of P. 0-18 group in 2030 = 30% of 12L = 3.6L. Given the 0-18 group increases by 10,000 (0.1L) from 2020 to 2030: 3.6L - 35% of P = 0.1L → 35% of P = 3.5L → P = **10 Lakhs** → **B**"""
content, s = apply_regex(pattern_sol_q38, rep_sol_q38, content, "Q38 Solution")
success = success and s

# 17. Q40 Solution
pattern_sol_q40 = r"\*\*Q40\.\*\* Distances: 30% of 600 = 180km @ 60 km/h → 3 hrs\. 40% = 240km @ 80 → 3 hrs\. Remaining 30% = 180km @ 100 → 1\.8 hrs\. Total = 7\.8 hrs\. Total distance = 600\. Avg speed = 600/7\.8 = \*\*76\.9\*\* ≈ \*\*B\*\*"
rep_sol_q40 = """**Q40.** Distances: 30% of 600 = 180km @ 60 km/h → 3 hrs. 40% = 240km @ 80 → 3 hrs. Remaining 30% = 180km @ 90 → 2 hrs. Total time = 3 + 3 + 2 = 8 hrs. Average speed = 600 / 8 = **75 km/h** → **B**"""
content, s = apply_regex(pattern_sol_q40, rep_sol_q40, content, "Q40 Solution")
success = success and s

# 18. Q45 Solution
pattern_sol_q45 = r"\*\*Q45\.\*\* 2022 Real Estate = 20% of 10L = 2L\..*?Real Estate 2023 = 2,86,000 → \*\*C\*\* \(matches closest interpretation\)"
rep_sol_q45 = """**Q45.** Real Estate in 2022 = 20% of 10L = ₹2.0 Lakhs. Real Estate in 2023 = 22% of 13L = ₹2.86 Lakhs. Absolute increase = 2.86L - 2.0L = 0.86L = **₹86,000** → **B**"""
content, s = apply_regex(pattern_sol_q45, rep_sol_q45, content, "Q45 Solution")
success = success and s

# 19. Q46 Solution
pattern_sol_q46 = r"\*\*Q46\.\*\* B's values: 60 → 72 → 79\.2 \(at 10% growth\).*?Note: The answer choice options need rechecking\."
rep_sol_q46 = """**Q46.** B's values: 2021 = 60, 2022 = 72 (grew 20%). Consistent 20% growth per year → 2023 value for Dept B = 72 × 1.20 = **86.4** → **A**"""
content, s = apply_regex(pattern_sol_q46, rep_sol_q46, content, "Q46 Solution")
success = success and s

# 20. Q50 Solution
pattern_sol_q50 = r"\*\*Q50\.\*\* A's food = 25% of 50,000 = 12,500\..*?\*\*D \(Cannot be determined / Data inconsistent\)\*\*"
rep_sol_q50 = """**Q50.** A's food = 25% of 60,000 = 15,000. B's total expense = 75,000. Ratio of A's food to B's total = 15,000 : 75,000 = **1:5** → **C**"""
content, s = apply_regex(pattern_sol_q50, rep_sol_q50, content, "Q50 Solution")
success = success and s

# 21. Q51 Solution
pattern_sol_q51 = r"\*\*Q51\.\*\* Year 1: Coal=60%, Renew=10%, Nuclear=5%, Gas=15%, Oil=10%\. Year 5: Coal=40%, Renew=25%, Nuclear=5%, Gas=20%, Oil=10%\. Change in Oil = 10% - 10% = \*\*0% \(No change\)\*\* → \*\*D\*\*.*?\)"
rep_sol_q51 = """**Q51.** Year 1: Coal=60%, Renew=10%, Nuclear=5%, Gas=15% → Oil = 10%. Year 5: Coal=40%, Renew=25%, Nuclear=5%, Gas=20% → Oil = 10%. Change in Oil's contribution = 10% - 10% = **0% (No change)** → **D**"""
content, s = apply_regex(pattern_sol_q51, rep_sol_q51, content, "Q51 Solution")
success = success and s

# 22. Q53 Solution
pattern_sol_q53 = r"\*\*Q53\.\*\* SP of both = same\. CP1 = 500, Profit 20% → SP = 600\. CP2 = SP/0\.8 = 750\. Total CP = 1250\. Total SP = 1200\. Loss = 50/1250 × 100 = \*\*4% Loss\*\* → \*\*C\*\*"
rep_sol_q53 = """**Q53.** SP of both is equal. Article 1: CP = 500, Profit = 20% → SP = 500 × 1.2 = 600. Thus, SP of article 2 is also 600. Article 2: SP = 600, Loss = 20% → CP = 600 / 0.8 = 750. Total CP = 500 + 750 = 1250. Total SP = 600 + 600 = 1200. Overall Loss = 50 / 1250 × 100 = **4% Loss** → **C**"""
content, s = apply_regex(pattern_sol_q53, rep_sol_q53, content, "Q53 Solution")
success = success and s

# 23. Q56 Solution
pattern_sol_q56 = r"\*\*Q56\.\*\* Y1: A\+B\+C = 100\..*?\*\*D \(Cannot be determined\)\*\*"
rep_sol_q56 = """**Q56.** In Year 1: Total = A + B + C = 100. In Year 5: C's revenue halves to become 20, meaning Y1 C's revenue was 40. Thus, Y1 A + B = 60. In Year 5, total revenue is 2A + 3B + 20. Since we don't know the individual values of A and B (only their sum is 60), the Year 5 total 2A + 3B + 20 is not uniquely determined. Thus, it **Cannot be determined** → **D**"""
content, s = apply_regex(pattern_sol_q56, rep_sol_q56, content, "Q56 Solution")
success = success and s

# 24. Q57 Solution
pattern_sol_q57 = r"\*\*Q57\.\*\* A invests X for 6 months = X×6 time-units\..*?C's share = 12/42 × 2,40,000 × 1\.75 = 1,20,000\. \*\*Answer: ₹1,20,000\*\* → \*\*D\*\*"
rep_sol_q57 = """**Q57.** Time-weighted investments: A = X × 6 = 6X units; B = 2X × 6 = 12X units; C = 3X × 4 = 12X units. Total units = 6 + 12 + 12 = 30X units. A's share of profit = 6/30 = 20% of total profit. Since A's profit share is ₹48,000, total profit = ₹2,40,000. C's share = 12/30 = 40% of total profit = 40% of 2,40,000 = **₹96,000** → **D**"""
content, s = apply_regex(pattern_sol_q57, rep_sol_q57, content, "Q57 Solution")
success = success and s

# 25. Q59 Solution
pattern_sol_q59 = r"\*\*Q59\.\*\* A = 144.*?\*\*D\*\* \(most likely\)"
rep_sol_q59 = """**Q59.** A occupies 144° → 144/360 = 40% of market. Total market revenue = 360 / 0.40 = ₹900 Crores. D and E together = 18% of market = ₹162 Crores. Since D's share is half of E's share, D accounts for 1/3 of their combined share = 6% of the market. D's revenue = 6% of 900 Cr = **₹54 Crores** → **B**"""
content, s = apply_regex(pattern_sol_q59, rep_sol_q59, content, "Q59 Solution")
success = success and s

# 26. Q62 Solution
pattern_sol_q62 = r"\*\*Q62a\.\*\* X profit by year: 24, 25, 45, 64\.8, 90\..*?Coefficient of variation: X has more volatile growth → \*\*Y is more consistent\*\*"
rep_sol_q62 = """**Q62a.** X profits: 2019: 200×12%=24; 2020: 250×10%=25; 2021: 300×15%=45; 2022: 360×18%=64.8; 2023: 450×20%=90. Y profits: 2019: 150×10%=15; 2020: 180×15%=27; 2021: 240×14%=33.6; 2022: 300×16%=48; 2023: 375×18%=67.5. Y first exceeds X in **2020** (27 > 25)
**Q62b.** Company X profit grew from 24 (2019) to 90 (2023). CAGR = (90/24)^(1/4) - 1 = 3.75^0.25 - 1 = 1.3916 - 1 = **39.2%**
**Q62c.** Company X revenue growth rate from 2022 to 2023 = (450 - 360) / 360 = 25%. Projected 2024 revenue = 450 × 1.25 = 562.5 Crores. Target is 540 Crores. Exceeds target by: ((562.5 - 540) / 540) × 100 = **4.17%**
**Q62d.** Combined profit 2021 = 45+33.6=78.6. Combined revenue 2023 = 450+375=825. % = 78.6/825×100 = **9.5%**
**Q62e.** X growth rates: 4.2%, 80%, 44%, 39%. Y: 44%, 55.6%, 42.9%, 25%. Coefficient of variation: X has more volatile growth → **Y is more consistent**"""
content, s = apply_regex(pattern_sol_q62, rep_sol_q62, content, "Q62 Solution")
success = success and s

# 27. Q68 Solution
pattern_sol_q68 = r"\*\*Q68a\.\*\* E = 10% of 10,00,000 = \*\*₹1,00,000\*\*.*?D gets the highest\."
rep_sol_q68 = """**Q68a.** E's investment = **₹1,00,000** (given directly)
**Q68b.** E = 1,00,000; D = 2,20,000; C = 80,000; B = 1,30,000; A = 2,60,000. Total initial investment = 7,90,000. Ratio A:B:C:D:E = 2,60,000 : 1,30,000 : 80,000 : 2,20,000 : 1,00,000 = **26:13:8:22:10**
**Q68c.** Time-weighted units (Investment × Months): A = 2,60,000 × 6 = 15,60,000; B = 1,30,000 × 12 = 15,60,000; C = 80,000 × 12 = 9,60,000; E = 1,00,000 × 12 = 12,00,000; D = (2,20,000 × 6) + (4,40,000 × 6) = 39,60,000. Total time-weighted units = 92,40,000. A's profit share = (15,60,000 / 92,40,000) × 2,00,000 = **₹33,766**"""
content, s = apply_regex(pattern_sol_q68, rep_sol_q68, content, "Q68 Solution")
success = success and s


# --- 28. INJECT SVG CHARTS ---

# 1) Q62 Mixed Chart SVG
q62_chart_svg = """
<div class="di-chart-container" style="display: flex; flex-direction: column; align-items: center; margin: 24px 0; background: var(--details-bg); padding: 20px; border-radius: var(--radius-md); border: 1px solid var(--border-color);">
  <div style="font-weight: 700; margin-bottom: 15px; color: var(--text-color); font-size: 0.95rem; text-align: center;">📊 Company X vs Company Y: Revenue (Bars) and Profit Margins (Lines)</div>
  <svg viewBox="0 0 650 350" style="width: 100%; max-width: 650px; height: auto;">
    <line x1="60" y1="50" x2="590" y2="50" stroke="var(--border-color)" stroke-dasharray="4" />
    <line x1="60" y1="100" x2="590" y2="100" stroke="var(--border-color)" stroke-dasharray="4" />
    <line x1="60" y1="150" x2="590" y2="150" stroke="var(--border-color)" stroke-dasharray="4" />
    <line x1="60" y1="200" x2="590" y2="200" stroke="var(--border-color)" stroke-dasharray="4" />
    <line x1="60" y1="250" x2="590" y2="250" stroke="var(--border-color)" stroke-dasharray="4" />
    <line x1="60" y1="300" x2="590" y2="300" stroke="var(--text-color)" stroke-width="1.5" />
    
    <line x1="60" y1="50" x2="60" y2="300" stroke="var(--text-color)" stroke-width="1.5" />
    <line x1="590" y1="50" x2="590" y2="300" stroke="var(--text-color)" stroke-width="1.5" />
    
    <text x="50" y="55" fill="var(--text-muted)" font-size="11" font-weight="600" text-anchor="end">500</text>
    <text x="50" y="105" fill="var(--text-muted)" font-size="11" font-weight="600" text-anchor="end">400</text>
    <text x="50" y="155" fill="var(--text-muted)" font-size="11" font-weight="600" text-anchor="end">300</text>
    <text x="50" y="205" fill="var(--text-muted)" font-size="11" font-weight="600" text-anchor="end">200</text>
    <text x="50" y="255" fill="var(--text-muted)" font-size="11" font-weight="600" text-anchor="end">100</text>
    <text x="50" y="305" fill="var(--text-muted)" font-size="11" font-weight="600" text-anchor="end">0</text>
    
    <text x="600" y="55" fill="var(--text-muted)" font-size="11" font-weight="600">25%</text>
    <text x="600" y="105" fill="var(--text-muted)" font-size="11" font-weight="600">20%</text>
    <text x="600" y="155" fill="var(--text-muted)" font-size="11" font-weight="600">15%</text>
    <text x="600" y="205" fill="var(--text-muted)" font-size="11" font-weight="600">10%</text>
    <text x="600" y="255" fill="var(--text-muted)" font-size="11" font-weight="600">5%</text>
    <text x="600" y="305" fill="var(--text-muted)" font-size="11" font-weight="600">0%</text>
    
    <text x="120" y="322" fill="var(--text-color)" font-size="11" font-weight="600" text-anchor="middle">2019</text>
    <text x="220" y="322" fill="var(--text-color)" font-size="11" font-weight="600" text-anchor="middle">2020</text>
    <text x="320" y="322" fill="var(--text-color)" font-size="11" font-weight="600" text-anchor="middle">2021</text>
    <text x="420" y="322" fill="var(--text-color)" font-size="11" font-weight="600" text-anchor="middle">2022</text>
    <text x="520" y="322" fill="var(--text-color)" font-size="11" font-weight="600" text-anchor="middle">2023</text>
    
    <rect x="98" y="200" width="20" height="100" fill="#3b82f6" rx="2" opacity="0.85" />
    <rect x="122" y="225" width="20" height="75" fill="#a78bfa" rx="2" opacity="0.85" />
    <rect x="198" y="175" width="20" height="125" fill="#3b82f6" rx="2" opacity="0.85" />
    <rect x="222" y="210" width="20" height="90" fill="#a78bfa" rx="2" opacity="0.85" />
    <rect x="298" y="150" width="20" height="150" fill="#3b82f6" rx="2" opacity="0.85" />
    <rect x="322" y="180" width="20" height="120" fill="#a78bfa" rx="2" opacity="0.85" />
    <rect x="398" y="120" width="20" height="180" fill="#3b82f6" rx="2" opacity="0.85" />
    <rect x="422" y="150" width="20" height="150" fill="#a78bfa" rx="2" opacity="0.85" />
    <rect x="498" y="75" width="20" height="225" fill="#3b82f6" rx="2" opacity="0.85" />
    <rect x="522" y="112.5" width="20" height="187.5" fill="#a78bfa" rx="2" opacity="0.85" />
    
    <path d="M 120 180 L 220 200 L 320 150 L 420 120 L 520 100" fill="none" stroke="#10b981" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" />
    <path d="M 120 200 L 220 150 L 320 160 L 420 140 L 520 120" fill="none" stroke="#f59e0b" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" />
    
    <circle cx="120" cy="180" r="5" fill="#10b981" />
    <circle cx="220" cy="200" r="5" fill="#10b981" />
    <circle cx="320" cy="150" r="5" fill="#10b981" />
    <circle cx="420" cy="120" r="5" fill="#10b981" />
    <circle cx="520" cy="100" r="5" fill="#10b981" />
    
    <circle cx="120" cy="200" r="5" fill="#f59e0b" />
    <circle cx="220" cy="150" r="5" fill="#f59e0b" />
    <circle cx="320" cy="160" r="5" fill="#f59e0b" />
    <circle cx="420" cy="140" r="5" fill="#f59e0b" />
    <circle cx="520" cy="120" r="5" fill="#f59e0b" />
  </svg>
  
  <div style="display: flex; gap: 15px; margin-top: 15px; font-size: 0.85rem; flex-wrap: wrap; justify-content: center;">
    <span style="display: flex; align-items: center; gap: 5px; color: var(--text-color); font-weight: 600;"><span style="display: inline-block; width: 12px; height: 12px; background: #3b82f6; border-radius: 2px;"></span> X Revenue</span>
    <span style="display: flex; align-items: center; gap: 5px; color: var(--text-color); font-weight: 600;"><span style="display: inline-block; width: 12px; height: 12px; background: #a78bfa; border-radius: 2px;"></span> Y Revenue</span>
    <span style="display: flex; align-items: center; gap: 5px; color: var(--text-color); font-weight: 600;"><span style="display: inline-block; width: 20px; height: 3px; background: #10b981;"></span> X Margin</span>
    <span style="display: flex; align-items: center; gap: 5px; color: var(--text-color); font-weight: 600;"><span style="display: inline-block; width: 20px; height: 3px; background: #f59e0b;"></span> Y Margin</span>
  </div>
</div>
"""
# Apply Q62 Table replacement
# In the updated text, let's locate the table and add the SVG right under it
# We do this by finding the table and appending the SVG.
table_anchor = r"\| Year \| Company X Revenue \(₹ Cr\) \| Company Y Revenue \(₹ Cr\) \| X Profit Margin \(\%\) \| Y Profit Margin \(\%\) \|\n\|------\|--------------------------\|--------------------------\|---------------------\|---------------------\|.*?2023 \| 450 \| 375 \| 20\% \| 18\% \|"
content, s = apply_regex(table_anchor, rep_q62_table + "\n" + q62_chart_svg, content, "Q62 Chart Injection")
success = success and s

# 2) Q64 Donut Chart SVG
pattern_q64 = r"\*\*Q64\.\*\* \*\(Pie Chart Analysis\)\* The following pie chart shows the distribution of monthly household expenses:\n\nHousing: 30% \| Food: 22% \| Education: 15% \| Transport: 12% \| Healthcare: 8% \| Others: 13%"
rep_q64 = """**Q64.** *(Pie Chart Analysis)* The following pie chart shows the distribution of monthly household expenses:

<div class="di-chart-container" style="display: flex; flex-wrap: wrap; align-items: center; justify-content: center; gap: 30px; margin: 24px 0; background: var(--details-bg); padding: 25px; border-radius: var(--radius-md); border: 1px solid var(--border-color);">
  <svg width="220" height="220" viewBox="0 0 220 220">
    <circle cx="110" cy="110" r="80" fill="transparent" stroke="#3b82f6" stroke-width="28" stroke-dasharray="150.8 502.65" stroke-dashoffset="0" transform="rotate(-90 110 110)" />
    <circle cx="110" cy="110" r="80" fill="transparent" stroke="#10b981" stroke-width="28" stroke-dasharray="110.6 502.65" stroke-dashoffset="-150.8" transform="rotate(-90 110 110)" />
    <circle cx="110" cy="110" r="80" fill="transparent" stroke="#f59e0b" stroke-width="28" stroke-dasharray="75.4 502.65" stroke-dashoffset="-261.4" transform="rotate(-90 110 110)" />
    <circle cx="110" cy="110" r="80" fill="transparent" stroke="#ec4899" stroke-width="28" stroke-dasharray="60.3 502.65" stroke-dashoffset="-336.8" transform="rotate(-90 110 110)" />
    <circle cx="110" cy="110" r="80" fill="transparent" stroke="#ef4444" stroke-width="28" stroke-dasharray="40.2 502.65" stroke-dashoffset="-397.1" transform="rotate(-90 110 110)" />
    <circle cx="110" cy="110" r="80" fill="transparent" stroke="#6b7280" stroke-width="28" stroke-dasharray="65.4 502.65" stroke-dashoffset="-437.3" transform="rotate(-90 110 110)" />
    
    <text x="110" y="105" fill="var(--text-color)" font-size="14" font-weight="700" text-anchor="middle">Expenses</text>
    <text x="110" y="125" fill="var(--text-muted)" font-size="11" font-weight="600" text-anchor="middle">Breakdown</text>
  </svg>
  
  <div style="display: flex; flex-direction: column; gap: 8px; font-size: 0.85rem;">
    <div style="display: flex; align-items: center; gap: 8px; color: var(--text-color); font-weight: 600;"><span style="display: inline-block; width: 12px; height: 12px; background: #3b82f6; border-radius: 50%;"></span> Housing (30%)</div>
    <div style="display: flex; align-items: center; gap: 8px; color: var(--text-color); font-weight: 600;"><span style="display: inline-block; width: 12px; height: 12px; background: #10b981; border-radius: 50%;"></span> Food (22%)</div>
    <div style="display: flex; align-items: center; gap: 8px; color: var(--text-color); font-weight: 600;"><span style="display: inline-block; width: 12px; height: 12px; background: #f59e0b; border-radius: 50%;"></span> Education (15%)</div>
    <div style="display: flex; align-items: center; gap: 8px; color: var(--text-color); font-weight: 600;"><span style="display: inline-block; width: 12px; height: 12px; background: #ec4899; border-radius: 50%;"></span> Transport (12%)</div>
    <div style="display: flex; align-items: center; gap: 8px; color: var(--text-color); font-weight: 600;"><span style="display: inline-block; width: 12px; height: 12px; background: #ef4444; border-radius: 50%;"></span> Healthcare (8%)</div>
    <div style="display: flex; align-items: center; gap: 8px; color: var(--text-color); font-weight: 600;"><span style="display: inline-block; width: 12px; height: 12px; background: #6b7280; border-radius: 50%;"></span> Others (13%)</div>
  </div>
</div>"""
content, s = apply_regex(pattern_q64, rep_q64, content, "Q64 Donut Injection")
success = success and s

# 3) Q65 Line Chart SVG
pattern_q65 = r"\*\*Q65\.\*\* \*\(Trend \+ Prediction DI\)\* The following table shows the monthly active users \(MAU\) of a social media app over 12 months:\n\n\| Month \| MAU \(Lakhs\) \|\n\|-+\|[-+]+\|.*?\| Dec \| 210 \|"
rep_q65 = """**Q65.** *(Trend + Prediction DI)* The following table shows the monthly active users (MAU) of a social media app over 12 months:

<div class="di-chart-container" style="display: flex; flex-direction: column; align-items: center; margin: 24px 0; background: var(--details-bg); padding: 20px; border-radius: var(--radius-md); border: 1px solid var(--border-color);">
  <div style="font-weight: 700; margin-bottom: 15px; color: var(--text-color); font-size: 0.95rem; text-align: center;">📈 Social Media App: Monthly Active Users (Lakhs)</div>
  <svg viewBox="0 0 650 300" style="width: 100%; max-width: 650px; height: auto;">
    <line x1="60" y1="50" x2="590" y2="50" stroke="var(--border-color)" stroke-dasharray="4" />
    <line x1="60" y1="100" x2="590" y2="100" stroke="var(--border-color)" stroke-dasharray="4" />
    <line x1="60" y1="150" x2="590" y2="150" stroke="var(--border-color)" stroke-dasharray="4" />
    <line x1="60" y1="200" x2="590" y2="200" stroke="var(--border-color)" stroke-dasharray="4" />
    <line x1="60" y1="250" x2="590" y2="250" stroke="var(--border-color)" stroke-dasharray="4" />
    <line x1="60" y1="260" x2="590" y2="260" stroke="var(--text-color)" stroke-width="1.5" />
    
    <line x1="60" y1="50" x2="60" y2="260" stroke="var(--text-color)" stroke-width="1.5" />
    
    <text x="50" y="55" fill="var(--text-muted)" font-size="11" font-weight="600" text-anchor="end">220</text>
    <text x="50" y="105" fill="var(--text-muted)" font-size="11" font-weight="600" text-anchor="end">180</text>
    <text x="50" y="155" fill="var(--text-muted)" font-size="11" font-weight="600" text-anchor="end">140</text>
    <text x="50" y="205" fill="var(--text-muted)" font-size="11" font-weight="600" text-anchor="end">100</text>
    <text x="50" y="255" fill="var(--text-muted)" font-size="11" font-weight="600" text-anchor="end">60</text>
    
    <text x="80" y="280" fill="var(--text-color)" font-size="10" font-weight="600" text-anchor="middle">Jan</text>
    <text x="125" y="280" fill="var(--text-color)" font-size="10" font-weight="600" text-anchor="middle">Feb</text>
    <text x="170" y="280" fill="var(--text-color)" font-size="10" font-weight="600" text-anchor="middle">Mar</text>
    <text x="215" y="280" fill="var(--text-color)" font-size="10" font-weight="600" text-anchor="middle">Apr</text>
    <text x="260" y="280" fill="var(--text-color)" font-size="10" font-weight="600" text-anchor="middle">May</text>
    <text x="305" y="280" fill="var(--text-color)" font-size="10" font-weight="600" text-anchor="middle">Jun</text>
    <text x="350" y="280" fill="var(--text-color)" font-size="10" font-weight="600" text-anchor="middle">Jul</text>
    <text x="395" y="280" fill="var(--text-color)" font-size="10" font-weight="600" text-anchor="middle">Aug</text>
    <text x="440" y="280" fill="var(--text-color)" font-size="10" font-weight="600" text-anchor="middle">Sep</text>
    <text x="485" y="280" fill="var(--text-color)" font-size="10" font-weight="600" text-anchor="middle">Oct</text>
    <text x="530" y="280" fill="var(--text-color)" font-size="10" font-weight="600" text-anchor="middle">Nov</text>
    <text x="575" y="280" fill="var(--text-color)" font-size="10" font-weight="600" text-anchor="middle">Dec</text>
    
    <path d="M 80 210 L 125 203.75 L 170 195 L 215 200 L 260 185 L 305 166.25 L 350 172.5 L 395 153.75 L 440 135 L 485 116.25 L 530 97.5 L 575 72.5" fill="none" stroke="#2563eb" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" />
    
    <circle cx="80" cy="210" r="4.5" fill="#3b82f6" stroke="#ffffff" stroke-width="1.5" />
    <circle cx="125" cy="203.75" r="4.5" fill="#3b82f6" stroke="#ffffff" stroke-width="1.5" />
    <circle cx="170" cy="195" r="4.5" fill="#3b82f6" stroke="#ffffff" stroke-width="1.5" />
    <circle cx="215" cy="200" r="4.5" fill="#3b82f6" stroke="#ffffff" stroke-width="1.5" />
    <circle cx="260" cy="185" r="4.5" fill="#3b82f6" stroke="#ffffff" stroke-width="1.5" />
    <circle cx="305" cy="166.25" r="4.5" fill="#3b82f6" stroke="#ffffff" stroke-width="1.5" />
    <circle cx="350" cy="172.5" r="4.5" fill="#3b82f6" stroke="#ffffff" stroke-width="1.5" />
    <circle cx="395" cy="153.75" r="4.5" fill="#3b82f6" stroke="#ffffff" stroke-width="1.5" />
    <circle cx="440" cy="135" r="4.5" fill="#3b82f6" stroke="#ffffff" stroke-width="1.5" />
    <circle cx="485" cy="116.25" r="4.5" fill="#3b82f6" stroke="#ffffff" stroke-width="1.5" />
    <circle cx="530" cy="97.5" r="4.5" fill="#3b82f6" stroke="#ffffff" stroke-width="1.5" />
    <circle cx="575" cy="72.5" r="4.5" fill="#3b82f6" stroke="#ffffff" stroke-width="1.5" />
  </svg>
</div>

| Month | MAU (Lakhs) |
|-------|-------------|
| Jan | 100 |
| Feb | 105 |
| Mar | 112 |
| Apr | 108 |
| May | 120 |
| Jun | 135 |
| Jul | 130 |
| Aug | 145 |
| Sep | 160 |
| Oct | 175 |
| Nov | 190 |
| Dec | 210 |"""
content, s = apply_regex(pattern_q65, rep_q65, content, "Q65 Line Chart Injection")
success = success and s

# 4) Q66 Double Donut Chart SVG
pattern_q66 = r"\*\*Q66\.\*\* \*\(Comparative Pie Charts\)\* The following pie charts show the revenue mix of Company M for 2022 and 2023:\n\n2022: Product A=30%, B=25%, C=20%, D=15%, E=10%\n2023: Product A=28%, B=27%, C=22%, D=13%, E=10%"
# Note: we check if there are pie charts or pie chart in pattern. The pattern in file has "revenue mix of Company M"
pattern_q66 = r"\*\*Q66\.\*\* \*\(Comparative Pie Charts\)\* Two pie charts show the revenue mix of Company M for 2022 and 2023:\n\n2022: Product A=30%, B=25%, C=20%, D=15%, E=10%\n2023: Product A=28%, B=27%, C=22%, D=13%, E=10%"
rep_q66 = """**Q66.** *(Comparative Pie Charts)* Two pie charts show the revenue mix of Company M for 2022 and 2023:

<div class="di-chart-container" style="display: flex; flex-wrap: wrap; align-items: center; justify-content: center; gap: 40px; margin: 24px 0; background: var(--details-bg); padding: 25px; border-radius: var(--radius-md); border: 1px solid var(--border-color);">
  <div style="display: flex; flex-direction: column; align-items: center;">
    <div style="font-weight: 700; margin-bottom: 10px; color: var(--text-color); font-size: 0.9rem;">2022 (Revenue: ₹500 Cr)</div>
    <svg width="180" height="180" viewBox="0 0 180 180">
      <circle cx="90" cy="90" r="70" fill="transparent" stroke="#3b82f6" stroke-width="24" stroke-dasharray="132.0 439.8" stroke-dashoffset="0" transform="rotate(-90 90 90)" />
      <circle cx="90" cy="90" r="70" fill="transparent" stroke="#10b981" stroke-width="24" stroke-dasharray="110.0 439.8" stroke-dashoffset="-132.0" transform="rotate(-90 90 90)" />
      <circle cx="90" cy="90" r="70" fill="transparent" stroke="#f59e0b" stroke-width="24" stroke-dasharray="88.0 439.8" stroke-dashoffset="-242.0" transform="rotate(-90 90 90)" />
      <circle cx="90" cy="90" r="70" fill="transparent" stroke="#ec4899" stroke-width="24" stroke-dasharray="66.0 439.8" stroke-dashoffset="-330.0" transform="rotate(-90 90 90)" />
      <circle cx="90" cy="90" r="70" fill="transparent" stroke="#6b7280" stroke-width="24" stroke-dasharray="44.0 439.8" stroke-dashoffset="-396.0" transform="rotate(-90 90 90)" />
      <text x="90" y="95" fill="var(--text-color)" font-size="11" font-weight="700" text-anchor="middle">Total: ₹500 Cr</text>
    </svg>
  </div>
  
  <div style="display: flex; flex-direction: column; align-items: center;">
    <div style="font-weight: 700; margin-bottom: 10px; color: var(--text-color); font-size: 0.9rem;">2023 (Revenue: ₹650 Cr)</div>
    <svg width="180" height="180" viewBox="0 0 180 180">
      <circle cx="90" cy="90" r="70" fill="transparent" stroke="#3b82f6" stroke-width="24" stroke-dasharray="123.1 439.8" stroke-dashoffset="0" transform="rotate(-90 90 90)" />
      <circle cx="90" cy="90" r="70" fill="transparent" stroke="#10b981" stroke-width="24" stroke-dasharray="118.7 439.8" stroke-dashoffset="-123.1" transform="rotate(-90 90 90)" />
      <circle cx="90" cy="90" r="70" fill="transparent" stroke="#f59e0b" stroke-width="24" stroke-dasharray="96.8 439.8" stroke-dashoffset="-241.8" transform="rotate(-90 90 90)" />
      <circle cx="90" cy="90" r="70" fill="transparent" stroke="#ec4899" stroke-width="24" stroke-dasharray="57.2 439.8" stroke-dashoffset="-338.6" transform="rotate(-90 90 90)" />
      <circle cx="90" cy="90" r="70" fill="transparent" stroke="#6b7280" stroke-width="24" stroke-dasharray="44.0 439.8" stroke-dashoffset="-395.8" transform="rotate(-90 90 90)" />
      <text x="90" y="95" fill="var(--text-color)" font-size="11" font-weight="700" text-anchor="middle">Total: ₹650 Cr</text>
    </svg>
  </div>
  
  <div style="width: 100%; display: flex; gap: 15px; font-size: 0.85rem; justify-content: center; flex-wrap: wrap; margin-top: 10px; border-top: 1px solid var(--border-color); padding-top: 15px;">
    <div style="display: flex; align-items: center; gap: 6px; color: var(--text-color); font-weight: 600;"><span style="display: inline-block; width: 12px; height: 12px; background: #3b82f6; border-radius: 50%;"></span> Prod A (30% vs 28%)</div>
    <div style="display: flex; align-items: center; gap: 6px; color: var(--text-color); font-weight: 600;"><span style="display: inline-block; width: 12px; height: 12px; background: #10b981; border-radius: 50%;"></span> Prod B (25% vs 27%)</div>
    <div style="display: flex; align-items: center; gap: 6px; color: var(--text-color); font-weight: 600;"><span style="display: inline-block; width: 12px; height: 12px; background: #f59e0b; border-radius: 50%;"></span> Prod C (20% vs 22%)</div>
    <div style="display: flex; align-items: center; gap: 6px; color: var(--text-color); font-weight: 600;"><span style="display: inline-block; width: 12px; height: 12px; background: #ec4899; border-radius: 50%;"></span> Prod D (15% vs 13%)</div>
    <div style="display: flex; align-items: center; gap: 6px; color: var(--text-color); font-weight: 600;"><span style="display: inline-block; width: 12px; height: 12px; background: #6b7280; border-radius: 50%;"></span> Prod E (10% vs 10%)</div>
  </div>
</div>"""
content, s = apply_regex(pattern_q66, rep_q66, content, "Q66 Double Donut Injection")
success = success and s

# 5) Q67 Stacked Bar Chart SVG
pattern_q67 = r"\*\*Q67\.\*\* \*\(Stacked Bar \+ Calculation\)\* A company sells 4 products across 4 quarters\. The stacked bar chart shows revenue \(₹ Lakhs\) per quarter with the following segment data:\n\nQ1: P=40, Q=30, R=20, S=10\nQ2: P=45, Q=35, R=25, S=15\nQ3: P=50, Q=40, R=30, S=20\nQ4: P=60, Q=48, R=36, S=24"
rep_q67 = """**Q67.** *(Stacked Bar + Calculation)* A company sells 4 products across 4 quarters. The stacked bar chart shows revenue (₹ Lakhs) per quarter with the following segment data:

<div class="di-chart-container" style="display: flex; flex-direction: column; align-items: center; margin: 24px 0; background: var(--details-bg); padding: 20px; border-radius: var(--radius-md); border: 1px solid var(--border-color);">
  <div style="font-weight: 700; margin-bottom: 15px; color: var(--text-color); font-size: 0.95rem; text-align: center;">📊 Quarterly Product Revenue Mix (Stacked ₹ Lakhs)</div>
  <svg viewBox="0 0 600 320" style="width: 100%; max-width: 600px; height: auto;">
    <line x1="60" y1="50" x2="550" y2="50" stroke="var(--border-color)" stroke-dasharray="4" />
    <line x1="60" y1="100" x2="550" y2="100" stroke="var(--border-color)" stroke-dasharray="4" />
    <line x1="60" y1="150" x2="550" y2="150" stroke="var(--border-color)" stroke-dasharray="4" />
    <line x1="60" y1="200" x2="550" y2="200" stroke="var(--border-color)" stroke-dasharray="4" />
    <line x1="60" y1="250" x2="550" y2="250" stroke="var(--border-color)" stroke-dasharray="4" />
    <line x1="60" y1="270" x2="550" y2="270" stroke="var(--text-color)" stroke-width="1.5" />
    
    <line x1="60" y1="50" x2="60" y2="270" stroke="var(--text-color)" stroke-width="1.5" />
    
    <text x="50" y="55" fill="var(--text-muted)" font-size="11" font-weight="600" text-anchor="end">180</text>
    <text x="50" y="105" fill="var(--text-muted)" font-size="11" font-weight="600" text-anchor="end">140</text>
    <text x="50" y="155" fill="var(--text-muted)" font-size="11" font-weight="600" text-anchor="end">100</text>
    <text x="50" y="205" fill="var(--text-muted)" font-size="11" font-weight="600" text-anchor="end">60</text>
    <text x="50" y="255" fill="var(--text-muted)" font-size="11" font-weight="600" text-anchor="end">20</text>
    <text x="50" y="275" fill="var(--text-muted)" font-size="11" font-weight="600" text-anchor="end">0</text>
    
    <text x="140" y="290" fill="var(--text-color)" font-size="11" font-weight="600" text-anchor="middle">Quarter 1</text>
    <text x="240" y="290" fill="var(--text-color)" font-size="11" font-weight="600" text-anchor="middle">Quarter 2</text>
    <text x="340" y="290" fill="var(--text-color)" font-size="11" font-weight="600" text-anchor="middle">Quarter 3</text>
    <text x="440" y="290" fill="var(--text-color)" font-size="11" font-weight="600" text-anchor="middle">Quarter 4</text>
    
    <rect x="115" y="257.8" width="50" height="12.2" fill="#ec4899" opacity="0.85" />
    <rect x="115" y="233.4" width="50" height="24.4" fill="#f59e0b" opacity="0.85" />
    <rect x="115" y="196.8" width="50" height="36.6" fill="#10b981" opacity="0.85" />
    <rect x="115" y="148.0" width="50" height="48.8" fill="#3b82f6" opacity="0.85" />
    
    <rect x="215" y="251.7" width="50" height="18.3" fill="#ec4899" opacity="0.85" />
    <rect x="215" y="221.2" width="50" height="30.5" fill="#f59e0b" opacity="0.85" />
    <rect x="215" y="178.5" width="50" height="42.7" fill="#10b981" opacity="0.85" />
    <rect x="215" y="123.6" width="50" height="54.9" fill="#3b82f6" opacity="0.85" />
    
    <rect x="315" y="245.6" width="50" height="24.4" fill="#ec4899" opacity="0.85" />
    <rect x="315" y="209.0" width="50" height="36.6" fill="#f59e0b" opacity="0.85" />
    <rect x="315" y="160.2" width="50" height="48.8" fill="#10b981" opacity="0.85" />
    <rect x="315" y="99.2" width="50" height="61.0" fill="#3b82f6" opacity="0.85" />
    
    <rect x="415" y="240.7" width="50" height="29.3" fill="#ec4899" opacity="0.85" />
    <rect x="415" y="196.8" width="50" height="43.9" fill="#f59e0b" opacity="0.85" />
    <rect x="415" y="138.2" width="50" height="58.6" fill="#10b981" opacity="0.85" />
    <rect x="415" y="65.0" width="50" height="73.2" fill="#3b82f6" opacity="0.85" />
  </svg>
  
  <div style="display: flex; gap: 15px; margin-top: 15px; font-size: 0.85rem; flex-wrap: wrap; justify-content: center;">
    <span style="display: flex; align-items: center; gap: 5px; color: var(--text-color); font-weight: 600;"><span style="display: inline-block; width: 12px; height: 12px; background: #3b82f6; border-radius: 2px;"></span> Product P (20% margin)</span>
    <span style="display: flex; align-items: center; gap: 5px; color: var(--text-color); font-weight: 600;"><span style="display: inline-block; width: 12px; height: 12px; background: #10b981; border-radius: 2px;"></span> Product Q (15% margin)</span>
    <span style="display: flex; align-items: center; gap: 5px; color: var(--text-color); font-weight: 600;"><span style="display: inline-block; width: 12px; height: 12px; background: #f59e0b; border-radius: 2px;"></span> Product R (10% margin)</span>
    <span style="display: flex; align-items: center; gap: 5px; color: var(--text-color); font-weight: 600;"><span style="display: inline-block; width: 12px; height: 12px; background: #ec4899; border-radius: 2px;"></span> Product S (25% margin)</span>
  </div>
</div>

Q1: P=40, Q=30, R=20, S=10
Q2: P=45, Q=35, R=25, S=15
Q3: P=50, Q=40, R=30, S=20
Q4: P=60, Q=48, R=36, S=24"""
content, s = apply_regex(pattern_q67, rep_q67, content, "Q67 Stacked Bar Injection")
success = success and s

# 6) Q70 Multi-Chart SVG
pattern_q70 = r"\*\*Table: Employee count by department over 4 years\*\*.*?2020: 50 \| 2021: 65 \| 2022: 85 \| 2023: 110"
rep_q70 = """**Table: Employee count by department over 4 years**

| Dept | 2020 | 2021 | 2022 | 2023 |
|------|------|------|------|------|
| Engineering | 200 | 240 | 300 | 380 |
| Sales | 150 | 180 | 200 | 250 |
| Operations | 100 | 110 | 130 | 140 |
| HR | 50 | 55 | 60 | 70 |

<div class="di-chart-container" style="display: flex; flex-wrap: wrap; align-items: center; justify-content: center; gap: 30px; margin: 24px 0; background: var(--details-bg); padding: 20px; border-radius: var(--radius-md); border: 1px solid var(--border-color);">
  <div style="display: flex; flex-direction: column; align-items: center; flex: 1; min-width: 260px;">
    <div style="font-weight: 700; margin-bottom: 10px; color: var(--text-color); font-size: 0.9rem;">💼 Avg Salary in 2023 (₹ Lakhs/annum)</div>
    <svg viewBox="0 0 250 180" style="width: 100%;">
      <line x1="80" y1="20" x2="80" y2="140" stroke="var(--text-color)" />
      <line x1="80" y1="140" x2="230" y2="140" stroke="var(--text-color)" />
      <line x1="130" y1="20" x2="130" y2="140" stroke="var(--border-color)" stroke-dasharray="3" />
      <line x1="180" y1="20" x2="180" y2="140" stroke="var(--border-color)" stroke-dasharray="3" />
      
      <text x="130" y="152" fill="var(--text-muted)" font-size="9" text-anchor="middle">5L</text>
      <text x="180" y="152" fill="var(--text-muted)" font-size="9" text-anchor="middle">10L</text>
      
      <rect x="80" y="25" width="120" height="20" fill="#3b82f6" rx="2" />
      <text x="70" y="38" fill="var(--text-color)" font-size="10" font-weight="600" text-anchor="end">Engineering</text>
      <text x="205" y="38" fill="var(--text-color)" font-size="10" font-weight="600">12L</text>
      
      <rect x="80" y="55" width="80" height="20" fill="#10b981" rx="2" />
      <text x="70" y="68" fill="var(--text-color)" font-size="10" font-weight="600" text-anchor="end">Sales</text>
      <text x="165" y="68" fill="var(--text-color)" font-size="10" font-weight="600">8L</text>
      
      <rect x="80" y="85" width="60" height="20" fill="#f59e0b" rx="2" />
      <text x="70" y="98" fill="var(--text-color)" font-size="10" font-weight="600" text-anchor="end">Operations</text>
      <text x="145" y="98" fill="var(--text-color)" font-size="10" font-weight="600">6L</text>
      
      <rect x="80" y="115" width="50" height="20" fill="#ec4899" rx="2" />
      <text x="70" y="128" fill="var(--text-color)" font-size="10" font-weight="600" text-anchor="end">HR</text>
      <text x="135" y="128" fill="var(--text-color)" font-size="10" font-weight="600">5L</text>
    </svg>
  </div>
  
  <div style="display: flex; flex-direction: column; align-items: center; flex: 1; min-width: 260px;">
    <div style="font-weight: 700; margin-bottom: 10px; color: var(--text-color); font-size: 0.9rem;">📈 Company Revenue Trend (₹ Crores)</div>
    <svg viewBox="0 0 250 180" style="width: 100%;">
      <line x1="40" y1="20" x2="40" y2="140" stroke="var(--text-color)" />
      <line x1="40" y1="140" x2="230" y2="140" stroke="var(--text-color)" />
      
      <line x1="40" y1="90" x2="230" y2="90" stroke="var(--border-color)" stroke-dasharray="3" />
      <line x1="40" y1="40" x2="230" y2="40" stroke="var(--border-color)" stroke-dasharray="3" />
      
      <text x="35" y="93" fill="var(--text-muted)" font-size="9" text-anchor="end">50</text>
      <text x="35" y="43" fill="var(--text-muted)" font-size="9" text-anchor="end">100</text>
      
      <text x="65" y="152" fill="var(--text-color)" font-size="10" font-weight="600" text-anchor="middle">2020</text>
      <text x="115" y="152" fill="var(--text-color)" font-size="10" font-weight="600" text-anchor="middle">2021</text>
      <text x="165" y="152" fill="var(--text-color)" font-size="10" font-weight="600" text-anchor="middle">2022</text>
      <text x="215" y="152" fill="var(--text-color)" font-size="10" font-weight="600" text-anchor="middle">2023</text>
      
      <path d="M 65 90 L 115 75 L 165 55 L 215 30" fill="none" stroke="#6366f1" stroke-width="2.5" />
      <circle cx="65" cy="90" r="4.5" fill="#6366f1" stroke="#ffffff" stroke-width="1" />
      <circle cx="115" cy="75" r="4.5" fill="#6366f1" stroke="#ffffff" stroke-width="1" />
      <circle cx="165" cy="55" r="4.5" fill="#6366f1" stroke="#ffffff" stroke-width="1" />
      <circle cx="215" cy="30" r="4.5" fill="#6366f1" stroke="#ffffff" stroke-width="1" />
      
      <text x="65" y="78" fill="var(--text-color)" font-size="9" font-weight="700" text-anchor="middle">50</text>
      <text x="115" y="63" fill="var(--text-color)" font-size="9" font-weight="700" text-anchor="middle">65</text>
      <text x="165" y="43" fill="var(--text-color)" font-size="9" font-weight="700" text-anchor="middle">85</text>
      <text x="215" y="18" fill="var(--text-color)" font-size="9" font-weight="700" text-anchor="middle">110</text>
    </svg>
  </div>
</div>

**Bar Chart: Average salary (₹ Lakhs per annum) by department in 2023**
Engineering: 12 | Sales: 8 | Operations: 6 | HR: 5

**Line Graph: Company's revenue (₹ Crores) over 4 years**
2020: 50 | 2021: 65 | 2022: 85 | 2023: 110"""
content, s = apply_regex(pattern_q70, rep_q70, content, "Q70 Multi-Chart Injection")
success = success and s


# Save modified markdown if everything is successful
if success:
    print("ALL REPLACEMENTS SUCCEEDED! Saving file...")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Save complete.")
else:
    print("WARNING: Some replacements failed. File not saved.")
