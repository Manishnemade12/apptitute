# Word Arrangement Problems 🟡

## 📌 Concept
Arranging the letters of a given word — with or without constraints.

---

## 📝 Formulas

### All Letters Different
```
n letters → n! arrangements
```

### With Repeated Letters
```
n letters with p₁ alike, p₂ alike... → n! / (p₁! × p₂! × ...)
```

### Vowels Together
Treat all vowels as **one unit**. Arrange units, then arrange vowels internally.
```
(n - v + 1)! × v! / (repeats)
```
Where v = number of vowels.

### Vowels Never Together
```
Total arrangements - Vowels together
```

### Starting with Specific Letter
Fix the first position, arrange remaining (n-1)!

### Alphabetical Rank
Count how many words come before the given word in dictionary order.

---

## 📖 Solved Examples

### Example 1: All Different
**Q**: Arrangements of CRAFT?  
**Solution**: 5! = **120**

---

### Example 2: Repeated Letters
**Q**: Arrangements of BANANA?  
**Solution**: 6!/(3!×2!) = 720/12 = **60**

---

### Example 3: Vowels Together
**Q**: Arrangements of GARDEN with vowels together?  
**Solution**:  
- Vowels: A, E → treat as [AE]. Consonants: G, R, D, N
- Units: G, R, D, N, [AE] → 5! = 120
- Vowels internally: 2! = 2
- Total = **240**

---

### Example 4: Starting with Vowel
**Q**: How many words from ORANGE start with a vowel?  
**Solution**: Vowels O, A, E → 3 choices for first letter, remaining 5! = 120 each → 3 × 120 = **360**

---

## Quick Review
```
All different: n!
Repeated: n!/(p₁!×p₂!...)
Vowels together: Treat as block → (units)! × (vowels)!
No two vowels together: Total - Vowels together
```
