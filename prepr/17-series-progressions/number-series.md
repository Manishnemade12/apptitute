# Number Series & AP/GP 🟡

## 📌 Number Series
Find the pattern, predict next/missing term.

### Common Patterns
| Pattern | Example |
|---------|---------|
| +constant (AP) | 3, 7, 11, 15, **19** (+4) |
| ×constant (GP) | 2, 6, 18, 54, **162** (×3) |
| +increasing | 1, 2, 4, 7, 11, **16** (+1,+2,+3,+4,+5) |
| Squares | 1, 4, 9, 16, 25, **36** |
| Cubes | 1, 8, 27, 64, **125** |
| Fibonacci-type | 1, 1, 2, 3, 5, 8, **13** |
| Alternating | 2, 5, 3, 6, 4, **7** |
| Two interleaved | 1,10,2,20,3,**30** |

### Strategy
1. Check differences between consecutive terms
2. If differences are constant → AP
3. If differences form a pattern → second-level series
4. Check ratios → GP
5. Check squares/cubes

---

## 📝 Arithmetic Progression (AP)

### Formulas
```
nth term: aₙ = a + (n-1)d
Sum of n terms: Sₙ = n/2 × [2a + (n-1)d] = n/2 × (first + last)
```
Where a = first term, d = common difference.

### Properties
- Average of AP = (first + last)/2
- If a, b, c are in AP: b = (a+c)/2 (arithmetic mean)
- Sum of n terms of AP can be found if first, last, and n are known

---

## 📝 Geometric Progression (GP)

### Formulas
```
nth term: aₙ = a × r^(n-1)
Sum of n terms: Sₙ = a(rⁿ - 1)/(r - 1)    [r > 1]
                Sₙ = a(1 - rⁿ)/(1 - r)      [r < 1]
Sum of infinite GP (|r| < 1): S∞ = a/(1-r)
```
Where a = first term, r = common ratio.

### Properties
- If a, b, c are in GP: b² = ac (geometric mean)
- Ratio of consecutive terms is constant

---

## 📖 Solved Examples

### Example 1: AP
**Q**: Find 20th term of AP: 3, 7, 11, 15...  
**Solution**: a=3, d=4. a₂₀ = 3 + 19×4 = 3+76 = **79**

### Example 2: Sum of AP
**Q**: Sum of first 50 natural numbers?  
**Solution**: n/2 × (1+50) = 25 × 51 = **1275**

### Example 3: GP
**Q**: 3rd term of GP is 18, 6th term is 486. Find first term.  
**Solution**: ar²=18, ar⁵=486. r³=27, r=3. a=18/9=**2**

### Example 4: Infinite GP
**Q**: Sum of 1 + 1/2 + 1/4 + 1/8 + ...  
**Solution**: a=1, r=1/2. S = 1/(1-1/2) = **2**

### Example 5: Number Series
**Q**: 2, 6, 12, 20, 30, ?  
**Solution**: Differences: 4, 6, 8, 10, **12** → Next = 30+12 = **42**
Pattern: n(n+1) → 1×2, 2×3, 3×4, 4×5, 5×6, 6×7 = 42 ✅

---

## Quick Review
- AP: aₙ = a+(n-1)d | Sₙ = n/2(first+last)
- GP: aₙ = arⁿ⁻¹ | Sₙ = a(rⁿ-1)/(r-1) | S∞ = a/(1-r)
- Series: Check differences, then ratios, then squares/cubes
