# LCM & HCF (Least Common Multiple & Highest Common Factor) 🔴

## 📌 Definitions

### HCF (Highest Common Factor) / GCD (Greatest Common Divisor)
The **largest number** that divides two or more numbers **exactly** (without remainder).

### LCM (Least Common Multiple)
The **smallest number** that is divisible by two or more given numbers.

---

## 📝 All Formulas

### Fundamental Relationship
```
Product of two numbers = LCM × HCF
a × b = LCM(a, b) × HCF(a, b)
```

### LCM & HCF of Fractions
```
LCM of fractions = LCM of Numerators / HCF of Denominators
HCF of fractions = HCF of Numerators / LCM of Denominators
```

### Properties of LCM
| Property | Formula |
|----------|---------|
| LCM is always ≥ the largest number | LCM(a, b) ≥ max(a, b) |
| LCM of co-primes | LCM(a, b) = a × b (when HCF = 1) |
| LCM(a, a) | = a |
| LCM(1, a) | = a |
| LCM(a, b, c) | Use prime factorization: take **highest** power of each prime |

### Properties of HCF
| Property | Formula |
|----------|---------|
| HCF is always ≤ the smallest number | HCF(a, b) ≤ min(a, b) |
| HCF of co-primes | HCF(a, b) = 1 |
| HCF(a, a) | = a |
| HCF(a, b, c) | Use prime factorization: take **lowest** power of each prime |

---

## 🔧 Methods to Find HCF

### Method 1: Prime Factorization
1. Find prime factors of each number
2. Take the **common primes** with the **lowest power**

**Example**: HCF of 36 and 48
- 36 = 2² × 3²
- 48 = 2⁴ × 3¹
- HCF = 2² × 3¹ = **12**

### Method 2: Division Method (Euclid's Algorithm)
1. Divide larger by smaller
2. Divide the divisor by the remainder
3. Repeat until remainder = 0
4. Last divisor = HCF

**Example**: HCF of 48 and 36
```
48 ÷ 36 = 1 remainder 12
36 ÷ 12 = 3 remainder 0
```
HCF = **12**

### Method 3: Successive Division (for 3+ numbers)
- Find HCF of first two, then HCF of that result with the third number, and so on.

---

## 🔧 Methods to Find LCM

### Method 1: Prime Factorization
1. Find prime factors of each number
2. Take **all primes** with the **highest power**

**Example**: LCM of 12, 15, 20
- 12 = 2² × 3
- 15 = 3 × 5
- 20 = 2² × 5
- LCM = 2² × 3 × 5 = **60**

### Method 2: Common Division Method
Divide all numbers together by common primes:
```
2 | 12  15  20
2 |  6  15  10
3 |  3  15   5
5 |  1   5   5
  |  1   1   1
```
LCM = 2 × 2 × 3 × 5 = **60**

---

## 🔑 Important Word Problem Patterns

### Pattern 1: Largest Number that Divides with Same Remainder
**Q Type**: "Find largest number that divides A, B, C leaving the **same** remainder."  
**Formula**: HCF of |A-B|, |B-C|, |A-C|

### Pattern 2: Largest Number with Different Remainders
**Q Type**: "Find largest number that divides A, B, C leaving remainders r₁, r₂, r₃."  
**Formula**: HCF of (A - r₁), (B - r₂), (C - r₃)

### Pattern 3: Smallest Number Divisible by All
**Q Type**: "Find smallest number divisible by A, B, C."  
**Formula**: LCM(A, B, C)

### Pattern 4: Smallest Number with Same Remainder
**Q Type**: "Find smallest number which when divided by A, B, C leaves remainder r in each case."  
**Formula**: LCM(A, B, C) + r

### Pattern 5: Smallest Number Leaving Different Remainders
**Q Type**: "Find smallest number which when divided by A, B, C leaves remainders r₁, r₂, r₃."  
**Check**: If (A - r₁) = (B - r₂) = (C - r₃) = k  
**Formula**: LCM(A, B, C) - k

### Pattern 6: Bells Ringing Together
**Q Type**: "Bells ring at intervals of A, B, C minutes. When will they ring together again?"  
**Formula**: LCM(A, B, C) minutes

---

## ⚡ Tricks & Shortcuts

> 💡 **Trick 1**: If ratio of two numbers is a:b and their HCF is h, then:
> - Numbers = ah and bh
> - LCM = abh (if a, b are co-prime)

> 💡 **Trick 2**: HCF(a, b) always divides LCM(a, b)

> 💡 **Trick 3**: For consecutive numbers, HCF is always **1** and LCM is their **product**.

> 💡 **Trick 4**: For consecutive even numbers (like 4, 6), HCF = 2.

> 💡 **Trick 5**: Quick LCM for 2 numbers = (a × b) / HCF(a, b)

---

## 📖 Solved Examples

### Example 1: Basic LCM & HCF
**Q**: Find LCM and HCF of 12 and 18.  
**Solution**:  
- 12 = 2² × 3
- 18 = 2 × 3²
- HCF = 2¹ × 3¹ = **6**
- LCM = 2² × 3² = **36**
- Verify: 12 × 18 = 216 = 6 × 36 ✅

---

### Example 2: LCM of Fractions
**Q**: Find LCM of 2/3, 4/5, and 1/6.  
**Solution**:  
- LCM of numerators (2, 4, 1) = 4
- HCF of denominators (3, 5, 6) = 1
- LCM = **4/1 = 4**

---

### Example 3: Ratio + HCF Problem
**Q**: Two numbers are in ratio 3:4 and their HCF is 5. Find LCM.  
**Solution**:  
- Numbers = 3 × 5 = 15 and 4 × 5 = 20
- LCM = (15 × 20) / 5 = **60**
- Or: LCM = 3 × 4 × 5 = **60** (since 3 and 4 are co-prime)

---

### Example 4: Bells Problem
**Q**: Three bells ring at intervals of 4, 7, and 14 minutes. If they ring together at 12:00, when do they ring together next?  
**Solution**:  
- LCM(4, 7, 14) = 28 minutes
- They ring together at **12:28 PM**

---

### Example 5: Largest Number Dividing with Same Remainder
**Q**: Find the largest number that divides 245, 1029, and 1525 leaving the same remainder.  
**Solution**:  
- |1029 - 245| = 784
- |1525 - 1029| = 496
- |1525 - 245| = 1280
- HCF(784, 496, 1280)
  - 784 = 2⁴ × 7²
  - 496 = 2⁴ × 31
  - 1280 = 2⁸ × 5
  - HCF = 2⁴ = **16**

---

### Example 6: Smallest Number with Remainder
**Q**: Find the smallest number which when divided by 6, 9, and 12 leaves remainder 1 in each case.  
**Solution**:  
- LCM(6, 9, 12) = 36
- Answer = 36 + 1 = **37**

---

### Example 7: Product Relationship
**Q**: LCM of two numbers is 180 and HCF is 6. If one number is 36, find the other.  
**Solution**:  
- a × b = LCM × HCF
- 36 × b = 180 × 6
- b = 1080 / 36 = **30**

---

## 🎯 Exam Strategy
- Always check if the answer × HCF = product of numbers (verification trick)
- In MCQs, LCM must be a multiple of all given numbers — use this to eliminate options fast
- For word problems, identify the pattern first (bells, divides, remainder) and apply the right formula
