# Percentage Word Problems 🔴

## 📌 Overview
Percentage word problems are among the **most frequently asked** questions in aptitude exams. They typically involve population, marks, income/expenditure, elections, and mixtures.

---

## 📝 Type 1: Population Problems

### Formulas
```
Population after n years (growth):    P × (1 + R/100)^n
Population n years ago (growth):      P / (1 + R/100)^n
Population after n years (decline):   P × (1 - R/100)^n
Population n years ago (decline):     P / (1 - R/100)^n
```

### Example
**Q**: Population of a town is 50000. It increases at 10% per year. What will it be after 2 years?  
**Solution**:  
- P = 50000 × (1 + 10/100)² = 50000 × (11/10)² = 50000 × 121/100 = **60500**

---

## 📝 Type 2: Marks / Examination Problems

### Pattern: "Fails by x marks / Passes with y marks above"
```
If scoring a% → fails by F marks
If scoring b% → passes by P marks
Then:
(b - a)% of Total = F + P
Total Marks = (F + P) / [(b - a)/100]
Pass marks = a% of Total + F = b% of Total - P
```

### Example
**Q**: A student scores 30% and fails by 10 marks. Another student scores 40% and gets 15 marks more than passing. Find total and pass marks.  
**Solution**:  
- (40% - 30%) × Total = 10 + 15
- 10% × Total = 25
- Total = **250**
- Pass marks = 30% of 250 + 10 = 75 + 10 = **85**
- Verify: 40% of 250 = 100, 100 - 85 = 15 ✅

---

## 📝 Type 3: Income & Expenditure Problems

### Formulas
```
Savings = Income - Expenditure
Savings % = (Savings / Income) × 100

If income increases by x% and expenditure increases by y%:
New Savings = (1 + x/100) × Income - (1 + y/100) × Expenditure
```

### Example
**Q**: A person spends 75% of income. If income increases by 20% and expenditure by 10%, find % increase in savings.  
**Solution**:  
Let Income = 100, Expenditure = 75, Savings = 25  
- New Income = 120, New Expenditure = 82.5
- New Savings = 120 - 82.5 = 37.5
- % increase = (37.5 - 25)/25 × 100 = **50%**

---

## 📝 Type 4: Election Problems

### Two-Candidate Election
```
If winner gets x% votes:
Loser gets (100 - x)% votes
Difference in votes = (2x - 100)% of Total votes
```

### With Invalid Votes
```
Valid Votes = Total × (100 - Invalid%) / 100
Winner's votes = x% of Valid Votes
```

### Example
**Q**: In an election, candidate A gets 60% of valid votes and wins by 1200 votes. 20% votes are invalid. Total voters?  
**Solution**:  
- A gets 60%, B gets 40% of valid votes
- Difference = 20% of valid votes = 1200
- Valid votes = 6000
- Valid = 80% of Total → Total = 6000 × 100/80 = **7500**

---

## 📝 Type 5: Depreciation / Value Decrease

### Formula
```
Value after n years = Original × (1 - R/100)^n
```
(Same as population decline — just applied to assets)

### Example
**Q**: A machine worth ₹50000 depreciates by 20% annually. Value after 2 years?  
**Solution**:  
- Value = 50000 × (80/100)² = 50000 × 0.64 = **₹32000**

---

## 📝 Type 6: Mixture / Solution Problems

### Formula
```
If x litres of water added to y litres of milk:
Milk concentration = [y / (x + y)] × 100
```

### Example
**Q**: 40 litres of milk has 10% water. How much water must be added to make water 20%?  
**Solution**:  
- Current water = 10% of 40 = 4L, Milk = 36L
- After adding w litres: water = 4 + w, total = 40 + w
- (4 + w)/(40 + w) = 20/100 = 1/5
- 5(4 + w) = 40 + w → 20 + 5w = 40 + w → 4w = 20 → w = **5 litres**

---

## 📝 Type 7: Percentage Change in Product/Revenue

### Formula
```
Revenue = Price × Quantity
If price changes by x% and quantity changes by y%:
% change in revenue = x + y + (xy/100)
```
(This is the successive percentage change formula)

### Example
**Q**: Shopkeeper increases price by 20% and as a result sales drop by 15%. What is the net effect on revenue?  
**Solution**: Net = 20 - 15 + (20 × (-15))/100 = 5 - 3 = **2% increase**

---

## ⚡ Tricks & Shortcuts

> 💡 **Trick 1 – Assume Values**: For income/expenditure problems, assume Income = 100. For marks, let Total = 100 or whatever makes math easy.

> 💡 **Trick 2 – Election Shortcut**: Difference % = |2 × Winner% - 100|%. Then: Total = Difference in votes / Difference%.

> 💡 **Trick 3 – Two-Period Growth**: For 2-year compound growth at R%, use multiplier: Final = P × [(100+R)/100]². Don't expand unnecessarily.

> 💡 **Trick 4 – Marks Pattern**: The gap between two percentages always equals the sum of "failed by" and "passed by" marks.

---

## 📖 More Solved Examples

### Example: Finding Required Percentage
**Q**: A student needs 40% to pass. He gets 178 marks and fails by 22 marks. Find total marks.  
**Solution**:  
- Pass marks = 178 + 22 = 200
- 40% of Total = 200
- Total = 200/0.4 = **500**

---

### Example: Income Tax Problem
**Q**: A person's income is ₹300000. He pays 10% tax on first ₹100000, 20% on next ₹100000, and 30% on the rest. Total tax?  
**Solution**:  
- Tax = 10% of 100000 + 20% of 100000 + 30% of 100000
- = 10000 + 20000 + 30000 = **₹60000**
- Effective rate = (60000/300000) × 100 = **20%**

---

### Example: Combined Percentage
**Q**: 60% of students in a school are boys. 40% of boys and 30% of girls pass. What % of total students pass?  
**Solution**:  
- Let total = 100. Boys = 60, Girls = 40
- Boys passed = 40% of 60 = 24
- Girls passed = 30% of 40 = 12
- Total passed = 36/100 = **36%**

---

## 🎯 Exam Tips
- Marks problems (Type 2) appear in almost every exam — learn the pattern by heart
- Election problems are easy marks — just identify total valid votes
- Always check: is the percentage on the original or the new value?
- Use the "assume 100" technique whenever possible
