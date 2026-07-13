# Remainder Theorem Basics 🟡

## 📌 Definition
When a number (Dividend) is divided by another (Divisor), we get:
```
Dividend = Divisor × Quotient + Remainder
```
Where: **0 ≤ Remainder < Divisor**

---

## 📝 All Formulas & Properties

### Basic Remainder Properties
```
(a + b) mod n = [(a mod n) + (b mod n)] mod n
(a - b) mod n = [(a mod n) - (b mod n)] mod n
(a × b) mod n = [(a mod n) × (b mod n)] mod n
(a^k) mod n   = [(a mod n)^k] mod n
```

### Negative Remainder Concept
If a mod n = r, then we can also write a mod n = **r - n** (negative remainder).  
This is extremely useful for simplifying calculations.

**Example**: 34 mod 7 = 6, but we can use -1 (since 6 - 7 = -1)

### Fermat's Little Theorem
If **p is prime** and **a is not divisible by p**, then:
```
a^(p-1) ≡ 1 (mod p)
```
**Example**: 2⁶ mod 7 = 64 mod 7 = 1 ✅ (since 7 is prime, 6 = 7-1)

### Euler's Theorem (Generalization)
If **a and n are co-prime**, then:
```
a^φ(n) ≡ 1 (mod n)
```
Where φ(n) = Euler's Totient Function

### Wilson's Theorem
If p is prime, then:
```
(p-1)! ≡ -1 (mod p)
```
**Example**: 6! mod 7 = 720 mod 7 = 6 = 7-1 = -1 (mod 7) ✅

---

## 📝 Important Remainder Patterns

### Remainder of aⁿ divided by (a - 1)
```
aⁿ mod (a-1) = 1 (always)
```
**Example**: 10ⁿ mod 9 = 1 → This is why digit sum rule works for divisibility by 9!

### Remainder of aⁿ divided by (a + 1)
```
aⁿ mod (a+1) = 1 if n is even
aⁿ mod (a+1) = a if n is odd (equivalent to -1)
```
**Example**: 10¹ mod 11 = 10 (-1), 10² mod 11 = 1, 10³ mod 11 = 10 (-1)...

### Remainder when dividing by 10, 100, 1000
```
N mod 10  = last digit of N
N mod 100 = last two digits of N
N mod 1000 = last three digits of N
```

---

## ⚡ Tricks & Shortcuts

> 💡 **Trick 1 – Negative Remainder**: Always look for negative remainders to make calculation easier.
> - 29 mod 5 = 4 → use -1 (since 29 = 30 - 1)
> - 98 mod 10 = 8 → use -2 (since 98 = 100 - 2)

> 💡 **Trick 2 – Break into Factors**: For a^n mod m, try to express a in terms of m.
> - 16^50 mod 17 = (17-1)^50 mod 17 = (-1)^50 mod 17 = **1**

> 💡 **Trick 3 – Cyclicity of Remainders**: Remainders repeat in cycles. Find the cycle and reduce the power.

> 💡 **Trick 4 – For large powers mod small prime**: Use Fermat's theorem to reduce the power first.
> - 2^100 mod 7: Since 7 is prime, 2^6 ≡ 1 (mod 7). So 2^100 = 2^(6×16 + 4) = (2^6)^16 × 2^4 ≡ 1 × 16 ≡ 2 (mod 7)

---

## 📖 Solved Examples

### Example 1: Basic Multiplication Remainder
**Q**: Find remainder when 15 × 17 × 19 is divided by 7.  
**Solution**:  
- 15 mod 7 = 1
- 17 mod 7 = 3
- 19 mod 7 = 5
- Product of remainders = 1 × 3 × 5 = 15
- 15 mod 7 = **1**

---

### Example 2: Using Negative Remainder
**Q**: Find remainder when 99 × 101 is divided by 10.  
**Solution**:  
- 99 mod 10 = -1
- 101 mod 10 = 1
- Product = (-1) × 1 = -1
- -1 mod 10 = **9**

---

### Example 3: Power Remainder using Fermat's
**Q**: Find remainder when 2^256 is divided by 17.  
**Solution**:  
- 17 is prime, so by Fermat's: 2^16 ≡ 1 (mod 17)
- 256 = 16 × 16
- 2^256 = (2^16)^16 ≡ 1^16 ≡ **1** (mod 17)

---

### Example 4: Remainder of Sum
**Q**: Find remainder when (55 + 66 + 77) is divided by 8.  
**Solution**:  
- 55 mod 8 = 7 (or -1)
- 66 mod 8 = 2
- 77 mod 8 = 5 (or -3)
- Sum = 7 + 2 + 5 = 14
- 14 mod 8 = **6**

---

### Example 5: Pattern-based
**Q**: Find remainder when 10^50 is divided by 9.  
**Solution**:  
Using aⁿ mod (a-1) = 1:
- 10^50 mod 9 = **1**

---

### Example 6: Complex Power
**Q**: Find remainder when 7^222 is divided by 5.  
**Solution**:  
- 7 mod 5 = 2
- So find 2^222 mod 5
- By Fermat's: 2^4 ≡ 1 (mod 5)
- 222 = 4 × 55 + 2
- 2^222 = (2^4)^55 × 2^2 ≡ 1 × 4 = **4**
- Or: remainder = -1 → 5-1 = **4**

---

### Example 7: Word Problem
**Q**: A number when divided by 5 gives remainder 3 and when divided by 7 gives remainder 4. What remainder does it give when divided by 35?  
**Solution**:  
- N = 5a + 3 and N = 7b + 4
- Try: N = 18 → 18/5 = 3R3 ✅, 18/7 = 2R4 ✅
- 18 mod 35 = **18**

---

## 🎯 Exam Strategy
- Fermat's Little Theorem is your **best friend** for large power remainder questions
- Always check if negative remainder simplifies the problem
- For mod operations, break complex expressions into simpler parts using the product/sum rules
