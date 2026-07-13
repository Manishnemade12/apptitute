# Permutation & Combination — Basic Concepts 🟡

## 📌 Definitions
- **Permutation (nPr)**: Arrangement of objects where **order matters**
- **Combination (nCr)**: Selection of objects where **order doesn't matter**

---

## 📝 All Formulas

### Permutation
```
nPr = n! / (n-r)!
```
Number of ways to **arrange** r items from n items.

### Combination
```
nCr = n! / [r! × (n-r)!] = nPr / r!
```
Number of ways to **select** r items from n items.

### Factorial
```
n! = n × (n-1) × (n-2) × ... × 1
0! = 1, 1! = 1
```

### Key Identities
| Identity | Formula |
|----------|---------|
| nC0 = nCn = 1 | Selecting none or all |
| nC1 = n | Selecting one |
| nCr = nC(n-r) | Symmetry |
| nCr + nC(r-1) = (n+1)Cr | Pascal's rule |
| nPn = n! | Arranging all n items |

---

## 📝 Important Formulas

### Arrangements with Repetition
- n items, all **different**: n! arrangements
- n items with **p alike, q alike**: n! / (p! × q!)
- Arrangement of n items where **repetition allowed**: nʳ

### Circular Permutation
```
(n-1)! arrangements (fixing one position)
If clockwise = anticlockwise (e.g., necklace): (n-1)!/2
```

---

## ⚡ Tricks & Shortcuts

> 💡 **"Arrange" = Permutation, "Select/Choose" = Combination**

> 💡 **Complement Method**: "At least one" = Total - None

> 💡 **Group Together**: If items must be together, treat them as one unit

> 💡 **Gap Method**: For "no two together", place the restricted items in gaps between other items

---

## 📖 Solved Examples

### Example 1: Basic Permutation
**Q**: How many 3-letter words from {A,B,C,D,E} (no repetition)?  
**Solution**: 5P3 = 5×4×3 = **60**

---

### Example 2: Basic Combination
**Q**: Choose 3 from 8 people.  
**Solution**: 8C3 = (8×7×6)/(3×2×1) = **56**

---

### Example 3: Word with Repeated Letters
**Q**: Arrangements of MISSISSIPPI?  
**Solution**: 11! / (4!×4!×2!) = 11! / (24×24×2) = **34650**

---

### Example 4: Circular
**Q**: 6 people around a round table.  
**Solution**: (6-1)! = 5! = **120**

---

### Example 5: At Least One
**Q**: From 5 men and 4 women, select 5 such that at least one woman is included.  
**Solution**: Total - All men = 9C5 - 5C5 = 126 - 1 = **125**

---

## 🎯 Exam Tips
- "Order matters" → Permutation, "Order doesn't matter" → Combination
- For word arrangement, always check for repeated letters
- "At least one" → use complement (Total - None)
