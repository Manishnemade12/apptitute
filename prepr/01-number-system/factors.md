# Number of Factors 🟢

## 📌 Concept
Given a number N, we can find the total count of factors, the sum of factors, the product of factors, and more — all using its **prime factorization**.

---

## 📝 Prime Factorization Form
Any natural number N can be written as:
```
N = p₁^a × p₂^b × p₃^c × ...
```
Where p₁, p₂, p₃... are distinct prime factors and a, b, c... are their powers.

**Example**: 360 = 2³ × 3² × 5¹

---

## 📝 All Formulas

### 1. Number of Factors (Divisors)
```
τ(N) = (a+1)(b+1)(c+1)...
```

| Example | Factorization | Number of Factors |
|---------|--------------|-------------------|
| 12 | 2² × 3¹ | (2+1)(1+1) = 6 |
| 36 | 2² × 3² | (2+1)(2+1) = 9 |
| 100 | 2² × 5² | (2+1)(2+1) = 9 |
| 360 | 2³ × 3² × 5¹ | (3+1)(2+1)(1+1) = 24 |

### 2. Sum of All Factors
```
σ(N) = [(p₁^(a+1) - 1)/(p₁ - 1)] × [(p₂^(b+1) - 1)/(p₂ - 1)] × ...
```

**Example**: Sum of factors of 12 = 2² × 3¹
- = [(2³-1)/(2-1)] × [(3²-1)/(3-1)]
- = [7/1] × [8/2]
- = 7 × 4 = **28**
- Verify: 1+2+3+4+6+12 = 28 ✅

### 3. Product of All Factors
```
Product = N^(number of factors / 2)
```

**Example**: Product of factors of 12
- Number of factors = 6
- Product = 12^(6/2) = 12³ = **1728**
- Verify: 1×2×3×4×6×12 = 1728 ✅

### 4. Number of Odd Factors
Ignore the factor of 2 completely:
```
If N = 2^a × p₂^b × p₃^c × ...
Odd factors = (b+1)(c+1)... (skip the 2's power)
```

### 5. Number of Even Factors
```
Even factors = Total factors - Odd factors
```
OR:
```
Even factors = a × (b+1)(c+1)...   (2's power contributes a, not a+1)
```

### 6. Sum of Odd Factors
Replace 2^a with 2^0 = 1 in the sum formula:
```
Sum of odd factors = 1 × [(p₂^(b+1)-1)/(p₂-1)] × ...
```

### 7. Sum of Even Factors
```
Sum of even factors = Total sum - Sum of odd factors
```

---

## 📝 Special Types of Factors

### Perfect Square Factors
For a factor to be a perfect square, all prime powers in that factor must be **even**.
```
If N = p₁^a × p₂^b × p₃^c
Number of perfect square factors = (⌊a/2⌋+1)(⌊b/2⌋+1)(⌊c/2⌋+1)
```

**Example**: 360 = 2³ × 3² × 5¹
- Powers available: 2→{0,2}, 3→{0,2}, 5→{0}
- Perfect square factors = (2)(2)(1) = **4**
- They are: 1, 4, 9, 36

### Factor Pairs
```
Number of factor pairs = Total factors / 2
(For perfect squares, one factor pairs with itself, so pairs = (Total-1)/2 + 1)
```

---

## 📝 Key Properties

| Property | Description |
|----------|-------------|
| Perfect square | Has **odd** number of factors |
| Non-perfect square | Has **even** number of factors |
| Prime number p | Has exactly **2** factors: 1 and p |
| p^n (prime power) | Has exactly **n+1** factors |
| 1 | Has exactly **1** factor |

---

## ⚡ Tricks & Shortcuts

> 💡 **Trick 1**: To find the smallest number with exactly n factors:
> - Express n as a product of numbers in descending order
> - Assign the largest powers to the smallest primes
> - Example: Smallest number with 12 factors → 12 = 4×3 or 3×2×2 → 2³×3²×5¹ = 360? No, try: 12 = 6×2 → 2⁵×3¹ = 96. Compare: 12 = 4×3 → 2³×3² = 72. **72 is smallest!**

> 💡 **Trick 2**: If you only need to check "how many factors" in MCQ, check if all answer options are achievable from the prime factorization pattern.

> 💡 **Trick 3**: Number of ways to express N as product of 2 co-prime factors = 2^(k-1) where k = number of distinct prime factors.

---

## 📖 Solved Examples

### Example 1: Basic Factor Count
**Q**: Find the number of factors of 720.  
**Solution**:  
- 720 = 2⁴ × 3² × 5¹
- Factors = (4+1)(2+1)(1+1) = 5 × 3 × 2 = **30**

---

### Example 2: Sum of Factors
**Q**: Find the sum of all factors of 60.  
**Solution**:  
- 60 = 2² × 3 × 5
- Sum = [(2³-1)/1] × [(3²-1)/2] × [(5²-1)/4]
- = 7 × 4 × 6 = **168**

---

### Example 3: Odd Factors
**Q**: How many odd factors does 240 have?  
**Solution**:  
- 240 = 2⁴ × 3 × 5
- Ignore 2⁴ → 3¹ × 5¹
- Odd factors = (1+1)(1+1) = **4**
- (They are: 1, 3, 5, 15)

---

### Example 4: Even Factors
**Q**: How many even factors does 240 have?  
**Solution**:  
- Total factors = (4+1)(1+1)(1+1) = 20
- Odd factors = 4
- Even factors = 20 - 4 = **16**

---

### Example 5: Perfect Square Factors
**Q**: How many factors of 1800 are perfect squares?  
**Solution**:  
- 1800 = 2³ × 3² × 5²
- For perfect square: even powers only
  - 2 can have power 0 or 2 → 2 choices
  - 3 can have power 0 or 2 → 2 choices
  - 5 can have power 0 or 2 → 2 choices
- Total = 2 × 2 × 2 = **8**

---

### Example 6: Smallest Number with Given Factors
**Q**: What is the smallest number that has exactly 10 factors?  
**Solution**:  
- 10 = 10 → p⁹ → 2⁹ = 512
- 10 = 5 × 2 → p⁴ × q¹ → 2⁴ × 3 = 48
- 10 = 2 × 5 → p¹ × q⁴ → 2 × 3⁴ = 162
- Smallest = **48**

---

## 🎯 Exam Tips
- Always start by finding the prime factorization — everything else follows from it
- For MCQs, check if the answer needs to be odd (perfect square indicator)
- Remember: the product formula N^(d/2) is rarely asked but helps verify answers
