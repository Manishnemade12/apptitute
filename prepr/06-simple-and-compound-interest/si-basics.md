# Simple Interest (SI) — Formula-based 🔴

## 📌 What is Simple Interest?
Interest calculated on the **original principal** only, for the entire duration. The interest remains **constant** every year.

---

## 📝 All Formulas

### Core Formula
```
SI = (P × R × T) / 100
```
Where:
- **P** = Principal (original amount)
- **R** = Rate of interest per annum (%)
- **T** = Time (in years)

### Amount (Total money after T years)
```
A = P + SI = P + (PRT/100) = P(1 + RT/100)
```

### Derived Formulas
```
P = (100 × SI) / (R × T)
R = (100 × SI) / (P × T)
T = (100 × SI) / (P × R)
P = (A × 100) / (100 + RT)
```

---

## 📝 Key Properties

| Property | Description |
|----------|-------------|
| SI is **constant** each year | SI for year 1 = year 2 = year 3 = PR/100 |
| SI is **linear** | SI grows linearly with time |
| Amount forms AP | A₁, A₂, A₃... are in Arithmetic Progression |
| Doubling time | T = 100/R years (when A = 2P) |
| Tripling time | T = 200/R years (when A = 3P) |
| n-times time | T = (n-1) × 100/R years |

### Money Doubling/Tripling Table

| Rate | Doubles in | Triples in |
|------|------------|------------|
| 5% | 20 years | 40 years |
| 8% | 12.5 years | 25 years |
| 10% | 10 years | 20 years |
| 12% | 8.33 years | 16.66 years |
| 15% | 6.66 years | 13.33 years |
| 20% | 5 years | 10 years |

---

## 📝 When Time is in Months/Days
```
T in months: SI = P × R × (T/12) / 100
T in days:   SI = P × R × (T/365) / 100
```

---

## ⚡ Tricks & Shortcuts

> 💡 **Trick 1 – Proportionality**: SI ∝ P × R × T. If any one doubles, SI doubles.

> 💡 **Trick 2 – Yearly SI**: SI per year = PR/100. Multiply by T.

> 💡 **Trick 3 – Ratio of SIs**: If P, R, T are in ratio, SI ratio = product of individual ratios.
> - P₁:P₂ = 2:3, R₁:R₂ = 3:4, T₁:T₂ = 4:5 → SI₁:SI₂ = 24:60 = 2:5

> 💡 **Trick 4 – Finding Rate from Doubling Time**: R = 100/T (if doubles), R = 200/3T (if triples)

---

## 📖 Solved Examples

### Example 1: Basic SI
**Q**: Find SI on ₹5000 at 8% for 3 years.  
**Solution**: SI = (5000 × 8 × 3)/100 = **₹1200**

---

### Example 2: Finding Principal
**Q**: SI is ₹900 at 10% for 3 years. Find principal.  
**Solution**: P = (100 × 900)/(10 × 3) = **₹3000**

---

### Example 3: Finding Rate
**Q**: ₹4000 becomes ₹5200 in 3 years at SI. Find rate.  
**Solution**:  
- SI = 5200 - 4000 = 1200
- R = (100 × 1200)/(4000 × 3) = **10%**

---

### Example 4: Doubling
**Q**: At what rate will money double in 8 years at SI?  
**Solution**: R = 100/8 = **12.5%**

---

### Example 5: Split Investment
**Q**: A sum of ₹10000 is divided into two parts. One at 5% and other at 8% gives equal SI in 2 years. Find the parts.  
**Solution**:  
- P₁ × 5 × 2 = P₂ × 8 × 2 → P₁/P₂ = 8/5
- P₁ = 10000 × 8/13 ≈ **₹6153.85**
- P₂ = 10000 × 5/13 ≈ **₹3846.15**

---

### Example 6: Time in Months
**Q**: Find SI on ₹2400 at 12% for 9 months.  
**Solution**: SI = (2400 × 12 × 9/12)/100 = (2400 × 12 × 0.75)/100 = **₹216**

---

## 🎯 Exam Tips
- SI problems are the easiest in interest — solve in under 30 seconds
- Know the doubling time table by heart for MCQs
- Split investment problems are very common — set up equations with equal SI or total SI
