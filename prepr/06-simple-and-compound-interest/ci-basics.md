# Compound Interest (CI) — Formula-based 🔴

## 📌 What is Compound Interest?
Interest calculated on the **principal + accumulated interest**. Interest "compounds" — you earn interest on interest.

---

## 📝 All Formulas

### Core Formula
```
Amount = P × (1 + R/100)^T
CI = Amount - P = P × [(1 + R/100)^T - 1]
```

### Different Compounding Periods
| Compounding | Formula |
|-------------|---------|
| Annually | A = P(1 + R/100)^T |
| Half-yearly | A = P(1 + R/200)^(2T) |
| Quarterly | A = P(1 + R/400)^(4T) |
| Monthly | A = P(1 + R/1200)^(12T) |

### When Rate is Different Each Year
```
A = P × (1 + R₁/100) × (1 + R₂/100) × (1 + R₃/100)
```

### CI for Specific Years
```
CI for nth year = P × (1 + R/100)^(n-1) × (R/100)
Ratio: CI of nth year / CI of (n-1)th year = (1 + R/100)
```

---

## 📝 Effective Rate Shortcut (Using Successive %)

### 2-Year CI at R%
```
Effective CI% = 2R + R²/100
```
This means CI on 100 for 2 years at R% = 2R + R²/100

### Common Values (on Principal = 100)

| Rate | 2-yr CI | 3-yr CI |
|------|---------|---------|
| 5% | 10.25 | 15.7625 |
| 10% | 21 | 33.1 |
| 15% | 32.25 | 52.0875 |
| 20% | 44 | 72.8 |
| 25% | 56.25 | 95.3125 |

---

## 📝 Key Properties

| Property | Description |
|----------|-------------|
| CI > SI (for T > 1) | CI is always more than SI for same P, R, T (when T > 1) |
| CI for 1st year = SI for 1st year | For the first year, both are equal |
| CI grows exponentially | Amount forms a Geometric Progression |
| More frequent compounding → more CI | Quarterly > Half-yearly > Annually |

### Doubling Time (Rule of 72)
```
Approximate doubling time = 72 / R years
```
| Rate | Approx Doubles in |
|------|--------------------|
| 6% | 12 years |
| 8% | 9 years |
| 10% | 7.2 years |
| 12% | 6 years |
| 15% | 4.8 years |

---

## ⚡ Tricks & Shortcuts

> 💡 **Trick 1 – Successive Percentage**: For 2 years at 10%:
> - Effective rate = 10 + 10 + (10×10/100) = 21%
> - CI on ₹5000 = 21% of 5000 = ₹1050

> 💡 **Trick 2 – CI of Each Year**:
> - Year 1 CI = PR/100
> - Year 2 CI = Year 1 CI × (1 + R/100)
> - Year 3 CI = Year 2 CI × (1 + R/100)

> 💡 **Trick 3 – Half-yearly**: Replace R with R/2 and T with 2T.

> 💡 **Trick 4 – Rule of 72**: Quick mental math for doubling time. 72/R gives approximate years.

---

## 📖 Solved Examples

### Example 1: Basic CI
**Q**: Find CI on ₹8000 at 10% for 2 years (compounded annually).  
**Solution**:  
- Effective 2-yr rate = 21%
- CI = 21% of 8000 = **₹1680**
- Or: A = 8000 × (1.1)² = 8000 × 1.21 = 9680. CI = 9680-8000 = 1680 ✅

---

### Example 2: Half-Yearly Compounding
**Q**: Find CI on ₹10000 at 20% for 1 year, compounded half-yearly.  
**Solution**:  
- R = 20/2 = 10% per half-year, T = 2 half-years
- A = 10000 × (1.1)² = 10000 × 1.21 = 12100
- CI = **₹2100**

---

### Example 3: Different Rates
**Q**: Find CI on ₹5000 at 10% for 1st year and 20% for 2nd year.  
**Solution**:  
- A = 5000 × 1.1 × 1.2 = 5000 × 1.32 = 6600
- CI = **₹1600**

---

### Example 4: Finding Principal
**Q**: CI on a sum at 10% for 2 years is ₹1050. Find principal.  
**Solution**:  
- Effective 2-yr rate = 21%
- 21% of P = 1050 → P = 1050/0.21 = **₹5000**

---

### Example 5: Year-wise CI
**Q**: CI for 2nd year on ₹10000 at 10% is?  
**Solution**:  
- CI year 1 = 10% of 10000 = 1000
- CI year 2 = 1000 × (1 + 10/100) = 1000 × 1.1 = **₹1100**

---

### Example 6: CI vs SI Comparison
**Q**: What is the difference between CI and SI on ₹6000 at 5% for 2 years?  
**Solution**:  
- SI = (6000×5×2)/100 = 600
- CI = 6000 × [(1.05)² - 1] = 6000 × 0.1025 = 615
- Difference = **₹15**

---

## 🎯 Exam Tips
- Use the successive percentage trick for 2-year problems — much faster than the formula
- For 3 years, apply the successive percentage trick twice
- Half-yearly questions: just double T and halve R
- Rule of 72 is great for elimination in MCQs
