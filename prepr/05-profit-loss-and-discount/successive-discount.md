# Successive Discount 🔴

## 📌 What is Discount?
Discount is the **reduction** given on the **Marked Price (MP)** to arrive at the **Selling Price (SP)**.
```
Discount = MP - SP
Discount % = (Discount / MP) × 100
SP = MP × (100 - Discount%) / 100
```

---

## 📝 Successive Discount Formula

When **two discounts** d₁% and d₂% are given one after another:
```
Net Single Discount = d₁ + d₂ - (d₁ × d₂ / 100)
```
**Note**: This is similar to successive percentage change but with a MINUS sign (because both are decreases).

### For Three Successive Discounts
```
Step 1: Net of d₁ and d₂ = d₁ + d₂ - (d₁d₂/100)
Step 2: Apply d₃ on the result from Step 1
```

### Multiplier Approach (Fastest)
```
SP = MP × [(100-d₁)/100] × [(100-d₂)/100]
```
For three discounts:
```
SP = MP × [(100-d₁)/100] × [(100-d₂)/100] × [(100-d₃)/100]
```

---

## 📝 Key Properties

| Property | Description |
|----------|-------------|
| Order doesn't matter | d₁ then d₂ = d₂ then d₁ (same net effect) |
| Two successive discounts ≠ single sum | 20% + 10% ≠ 30% (it's 28%) |
| Net discount < sum of individual discounts | Always |
| A single discount of x% > two discounts of x/2% each | E.g., 20% > 10%+10% (20% vs 19%) |

---

## 📝 Comparison: Which Discount Scheme is Better for Buyer?

| Scheme | Net Discount |
|--------|-------------|
| Single 30% | 30% |
| 20% + 10% | 28% |
| 15% + 15% | 27.75% |
| 10% + 10% + 10% | 27.1% |
| 25% + 5% | 28.75% |

**Rule**: The more "spread out" the discounts are, the **less** the net discount. A single large discount is always better for the buyer.

---

## ⚡ Tricks & Shortcuts

> 💡 **Trick 1 – Apply on 100**: Assume MP = 100 and apply discounts step by step.
> - 20% and 10%: 100 → 80 → 72. Net discount = 28%.

> 💡 **Trick 2 – Use the Formula**: d₁ + d₂ - d₁d₂/100. For 20 and 10:
> - 20 + 10 - 200/100 = 28%

> 💡 **Trick 3 – Fraction Multiplier**: Convert to fractions.
> - 20% off = ×4/5, 25% off = ×3/4, 10% off = ×9/10
> - 20% then 25% off: SP = MP × 4/5 × 3/4 = MP × 3/5 = 40% off

---

## 📖 Solved Examples

### Example 1: Two Successive Discounts
**Q**: A shop offers successive discounts of 20% and 10% on a shirt marked ₹500. Find SP.  
**Solution**:  
- SP = 500 × 80/100 × 90/100 = 500 × 0.72 = **₹360**
- Or: Net discount = 20 + 10 - 2 = 28%. SP = 500 × 72/100 = ₹360 ✅

---

### Example 2: Finding Equivalent Single Discount
**Q**: What single discount is equivalent to successive discounts of 30% and 20%?  
**Solution**: Net = 30 + 20 - (30×20/100) = 50 - 6 = **44%**

---

### Example 3: Three Successive Discounts
**Q**: Successive discounts of 10%, 20%, and 30% on an item worth ₹1000.  
**Solution**:  
- SP = 1000 × 90/100 × 80/100 × 70/100
- = 1000 × 0.9 × 0.8 × 0.7
- = 1000 × 0.504 = **₹504**

---

### Example 4: Comparing Discount Schemes
**Q**: Which is better for the buyer: 40% single discount or 30% + 10% successive?  
**Solution**:  
- Single 40% → pays 60%
- 30% + 10% → Net = 30 + 10 - 3 = 37% → pays 63%
- **40% single is better** (buyer pays less)

---

### Example 5: Finding Required Second Discount
**Q**: A shopkeeper gives 20% discount. To clear stock, he gives another discount. If total discount is 32%, what is the second discount?  
**Solution**:  
- 20 + d₂ - (20×d₂/100) = 32
- d₂ - 0.2d₂ = 12
- 0.8d₂ = 12 → d₂ = **15%**

---

## 🎯 Exam Tips
- Use the formula or "assume 100" method — both are equally fast
- Remember: two successive discounts always give LESS discount than their sum
- For MCQs comparing schemes, calculate net discount and compare
