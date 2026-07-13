# SI vs CI Difference (2yr/3yr Trick) 🔴

## 📌 Concept
The **difference between CI and SI** for the same P, R, T is one of the most frequently asked question types. There are direct formulas for 2-year and 3-year differences.

---

## 📝 All Formulas

### Difference for 2 Years
```
CI - SI = P × (R/100)²
```
This is because the extra interest in CI is the interest earned on 1st year's interest.

### Difference for 3 Years
```
CI - SI = P × (R/100)² × (3 + R/100)
```

### Alternative 3-Year Formula
```
CI - SI = P × (R/100)² × 3 + P × (R/100)³
```

### Relationship Between 2yr and 3yr Difference
```
Diff₃ = Diff₂ × (3 + R/100)
```

---

## 📝 Understanding Why (for 2 years)

| Year | SI earned | CI earned | Difference |
|------|-----------|-----------|------------|
| Year 1 | PR/100 | PR/100 | 0 |
| Year 2 | PR/100 | PR/100 + (PR/100)×(R/100) | P(R/100)² |
| **Total** | **2PR/100** | **2PR/100 + P(R/100)²** | **P(R/100)²** |

The extra amount = interest on 1st year's interest = (PR/100) × (R/100) = P(R/100)²

---

## 📝 Key Properties

| Property | Description |
|----------|-------------|
| CI - SI for 1 year | = 0 (no difference) |
| CI - SI for 2 years | = P × (R/100)² |
| CI always > SI | For T ≥ 2, CI is always greater |
| The difference grows with time | Exponentially, not linearly |
| If CI-SI and R are given | P can be found directly |

---

## ⚡ Tricks & Shortcuts

> 💡 **Trick 1 – 2-Year Shortcut**: CI - SI = P × (R/100)². Just one multiplication!
> - P=5000, R=10% → Diff = 5000 × 0.01 = **₹50**

> 💡 **Trick 2 – Given Diff, Find P**: P = Diff / (R/100)²
> - Diff=80, R=20% → P = 80 / 0.04 = ₹2000

> 💡 **Trick 3 – Given Diff, Find R**: R/100 = √(Diff/P)
> - P=10000, Diff=40 → R/100 = √(40/10000) = √0.004 = 0.0632... ≈ 6.32% → Wait, let me recalculate: √(40/10000) = √0.004 ≈ 0.0632 → R ≈ 6.32%... But if Diff=100, P=10000 → R = √(100/10000) × 100 = √0.01 × 100 = 0.1 × 100 = **10%**

> 💡 **Trick 4 – 3-Year from 2-Year**: Multiply 2-year diff by (3 + R/100).

---

## 📖 Solved Examples

### Example 1: 2-Year Difference
**Q**: Find the difference between CI and SI on ₹8000 at 5% for 2 years.  
**Solution**:  
- Diff = 8000 × (5/100)² = 8000 × 1/400 = **₹20**
- Verify: SI = 800, CI = 8000 × [(1.05)² - 1] = 8000 × 0.1025 = 820. Diff = 20 ✅

---

### Example 2: Finding Principal
**Q**: The difference between CI and SI on a certain sum at 10% for 2 years is ₹50. Find the sum.  
**Solution**:  
- P × (10/100)² = 50
- P × 0.01 = 50
- P = **₹5000**

---

### Example 3: Finding Rate
**Q**: CI - SI on ₹4000 for 2 years is ₹10. Find rate.  
**Solution**:  
- 4000 × (R/100)² = 10
- (R/100)² = 10/4000 = 1/400
- R/100 = 1/20 → R = **5%**

---

### Example 4: 3-Year Difference
**Q**: Find CI - SI on ₹10000 at 10% for 3 years.  
**Solution**:  
- Diff = 10000 × (0.1)² × (3 + 0.1)
- = 10000 × 0.01 × 3.1 = 100 × 3.1 = **₹310**
- Verify: SI = 3000, CI = 10000 × [(1.1)³ - 1] = 10000 × 0.331 = 3310. Diff = 310 ✅

---

### Example 5: Using 2-Year to Find 3-Year
**Q**: If CI - SI for 2 years is ₹40 at 10%, what is CI - SI for 3 years?  
**Solution**:  
- Diff₃ = 40 × (3 + 10/100) = 40 × 3.1 = **₹124**

---

### Example 6: Finding Time
**Q**: On ₹25000 at 20%, CI - SI = ₹1000. Find the time period.  
**Solution**:  
- For 2 years: Diff = 25000 × (0.2)² = 25000 × 0.04 = 1000 ✅
- Time = **2 years**

---

## 🎯 Exam Tips
- The 2-year formula P(R/100)² is asked in **almost every exam** — memorize it
- If given the difference, you can find P or R in seconds
- For 3 years, just multiply the 2-year answer by (3 + R/100)
- This is a top-5 most repeated question type across all service company exams
