# Weighted Average 🟡

## 📌 Concept
Weighted average is used when **different groups contribute differently** (have different "weights" or frequencies). Unlike simple average where every observation has equal importance, here each group has a weight.

---

## 📝 Formula
```
Weighted Average = (n₁×A₁ + n₂×A₂ + n₃×A₃ + ...) / (n₁ + n₂ + n₃ + ...)
```
Where:
- A₁, A₂, A₃ = averages of individual groups
- n₁, n₂, n₃ = number of items (weights) in each group

---

## 📝 Properties

| Property | Description |
|----------|-------------|
| Weighted avg lies between min and max group averages | min(Aᵢ) ≤ Weighted Avg ≤ max(Aᵢ) |
| Closer to the group with more weight | Avg "gravitates" towards the larger group |
| If all weights are equal | Weighted average = Simple average |
| If all groups have same average | Weighted average = that same average |

---

## 📝 Connection to Alligation (Shortcut)

For **two groups** with averages A₁ and A₂ and weighted average = Aw:
```
n₁ / n₂ = (A₂ - Aw) / (Aw - A₁)
```
This is the **Alligation Rule** (covered in detail in Mixtures topic).

---

## ⚡ Tricks & Shortcuts

> 💡 **Trick 1 – Alligation Diagram**: For 2 groups, draw:
> ```
>    A₁         A₂
>      \       /
>        Aw
>      /       \
>  (A₂-Aw)  (Aw-A₁)
> ```
> Ratio of quantities = (A₂ - Aw) : (Aw - A₁)

> 💡 **Trick 2 – Proportional Contribution**: If groups are equal in size, weighted avg = simple avg of group averages. If one group dominates, avg is close to that group's avg.

> 💡 **Trick 3 – Work Backwards**: If given the weighted avg and one group's details, you can find the other group's average using the formula rearranged.

---

## 📖 Solved Examples

### Example 1: Basic Weighted Average
**Q**: Class A has 30 students with avg marks 60. Class B has 20 students with avg marks 80. Find combined average.  
**Solution**:  
- = (30×60 + 20×80) / (30+20)
- = (1800 + 1600) / 50
- = 3400/50 = **68**

---

### Example 2: Using Alligation
**Q**: (Same as above) Solve using alligation.  
**Solution**:  
```
   60         80
     \       /
       Aw
     /       \
  (80-Aw)  (Aw-60)
```
Ratio = 30:20 = 3:2
- (80-Aw)/(Aw-60) = 3/2
- 160 - 2Aw = 3Aw - 180
- 5Aw = 340 → Aw = **68** ✅

---

### Example 3: Finding Group Average
**Q**: Average salary of 75 workers is ₹5200. Average of 25 managers is ₹8000. Average of rest of the workers?  
**Solution**:  
- Total salary = 75 × 5200 = 390000
- Managers salary = 25 × 8000 = 200000
- Workers salary = 190000
- Workers count = 50
- Workers avg = 190000/50 = **₹3800**

---

### Example 4: Three Groups
**Q**: Section A (40 students, avg 70), B (35 students, avg 65), C (25 students, avg 80). Find overall average.  
**Solution**:  
- = (40×70 + 35×65 + 25×80) / (40+35+25)
- = (2800 + 2275 + 2000) / 100
- = 7075/100 = **70.75**

---

### Example 5: Weighted Average of Percentages
**Q**: A student scores 60% in Math (weight 3), 70% in English (weight 2), 80% in Science (weight 1). Find weighted average percentage.  
**Solution**:  
- = (3×60 + 2×70 + 1×80) / (3+2+1)
- = (180 + 140 + 80) / 6
- = 400/6 = **66.67%**

---

## 🎯 Exam Tips
- Weighted average is just a generalized version of simple average — don't overcomplicate it
- The alligation rule is the fastest shortcut for 2-group problems
- Always check: your answer must lie between the two group averages
