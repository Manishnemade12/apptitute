# Successive Percentage Change 🔴

## 📌 Concept
When **two or more percentage changes** are applied **one after another** on the same quantity, the net effect is NOT simply the sum of the percentages. We use the **successive change formula**.

---

## 📝 All Formulas

### Two Successive Changes: x% and y%
```
Net % change = x + y + (xy / 100)
```

**Rules**:
- If increase → use **+ve** value
- If decrease → use **-ve** value

### Three Successive Changes: x%, y%, z%
First find net of x and y, then apply z on the result:
```
Step 1: Net₁ = x + y + (xy/100)
Step 2: Final = Net₁ + z + (Net₁ × z / 100)
```

### General Multiplier Approach (Fastest)
For successive changes of x% and y%:
```
Final Value = Original × [(100+x)/100] × [(100+y)/100]
```
For decrease, x or y will be negative.

---

## 📝 Special Cases

### Same % increase and decrease (x% up, then x% down)
```
Net change = -(x²/100) %    ← Always a DECREASE
```

| x% up then x% down | Net Change |
|---------------------|------------|
| 10% ↑ then 10% ↓ | **1% decrease** |
| 20% ↑ then 20% ↓ | **4% decrease** |
| 25% ↑ then 25% ↓ | **6.25% decrease** |
| 30% ↑ then 30% ↓ | **9% decrease** |
| 50% ↑ then 50% ↓ | **25% decrease** |

### Two Equal Increases of x%
```
Net change = 2x + (x²/100) %
```

### Two Equal Decreases of x%
```
Net change = -2x + (x²/100) %
```

### Area Change (Length × Breadth)
If length increases by x% and breadth increases by y%:
```
% change in area = x + y + (xy/100)
```
(Same formula! Because Area = L × B)

---

## 📝 Properties

| Property | Description |
|----------|-------------|
| Order doesn't matter | x% then y% = y% then x% (same net result) |
| Not additive | 10% + 10% ≠ 20% (it's 21%) |
| Always net loss | Same % up then down always gives net decrease |
| Multiplicative | Final = Original × (1+x/100) × (1+y/100) |

---

## ⚡ Tricks & Shortcuts

> 💡 **Trick 1 – Quick Net for Common Pairs**:
> - 10% + 10% = 21%
> - 20% + 20% = 44%
> - 10% - 10% = -1%
> - 20% - 20% = -4%
> - 25% - 20% = 25 - 20 + (-500/100) = 0% → **No change!**

> 💡 **Trick 2 – Assume 100**: For word problems, always start with value = 100. Apply each percentage step by step.
> - 20% increase then 10% decrease: 100 → 120 → 108 → Net = **8% increase**

> 💡 **Trick 3 – Area Shortcut**: When both dimensions change, use the formula directly. Don't calculate new dimensions separately.

> 💡 **Trick 4 – Voter/Election Problems**: If x% of A goes to B, the net change between them is 2x% of A (one loses, other gains).

---

## 📖 Solved Examples

### Example 1: Basic Successive Change
**Q**: A price increases by 20% and then by 10%. What is the net percentage increase?  
**Solution**:  
- Net = 20 + 10 + (20×10/100) = 30 + 2 = **32%**
- Verify: 100 → 120 → 132 ✅

---

### Example 2: Increase then Decrease
**Q**: Salary increased by 25% and then decreased by 20%. Find net change.  
**Solution**:  
- Net = 25 + (-20) + (25 × (-20)/100)
- = 25 - 20 - 5 = **0% (No change!)**
- Verify: 100 → 125 → 100 ✅

---

### Example 3: Same % Up and Down
**Q**: Population increases by 10% in the first year and decreases by 10% in the second. What is the net change?  
**Solution**:  
- Net = -(10²/100) = -100/100 = **1% decrease**
- Verify: 100 → 110 → 99 ✅

---

### Example 4: Three Successive Changes
**Q**: Price increases by 10%, then 20%, then decreases by 10%. Find net change.  
**Solution**:  
- Step 1: Net of 10% and 20% = 10 + 20 + (200/100) = 32%
- Step 2: Net of 32% and -10% = 32 - 10 + (32×(-10)/100) = 22 - 3.2 = **18.8%**
- Verify: 100 → 110 → 132 → 118.8 ✅

---

### Example 5: Area Problem
**Q**: If the length of a rectangle is increased by 20% and breadth is decreased by 10%, find the % change in area.  
**Solution**:  
- % change = 20 + (-10) + (20 × (-10)/100)
- = 20 - 10 - 2 = **8% increase**

---

### Example 6: Side of a Square
**Q**: If each side of a square is increased by 30%, by what % does the area increase?  
**Solution**:  
- Both length and breadth increase by 30%
- Net = 30 + 30 + (30×30/100) = 60 + 9 = **69%**

---

### Example 7: Real-World Problem
**Q**: The price of petrol increases by 25%. By what % must a person reduce consumption so that expenditure increases by only 10%?  
**Solution**:  
Let reduction = x%  
- 25 + (-x) + (25 × (-x)/100) = 10
- 25 - x - 0.25x = 10
- 1.25x = 15
- x = **12%**

---

## 🎯 Exam Tips
- The formula x + y + (xy/100) is the **most used formula** in percentage — memorize it cold
- Common trap: 20% up then 20% down ≠ 0. It's always a decrease!
- For area/volume problems, this same formula applies — recognize the pattern
