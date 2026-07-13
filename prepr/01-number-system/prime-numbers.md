# Prime Numbers, Factors & Multiples 🟡

## 📌 Definitions

### Prime Number
A number greater than 1 that has **exactly two factors**: 1 and itself.
- Examples: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47...

### Composite Number
A number that has **more than two factors**.
- Examples: 4, 6, 8, 9, 10, 12, 14, 15...

### Important Notes
- **1 is neither prime nor composite** (it has only one factor)
- **2 is the only even prime number**
- Every prime > 3 is of the form **6k ± 1** (but not every 6k ± 1 is prime)

---

## 📝 List of Prime Numbers

### Primes up to 100 (25 primes)
```
2,  3,  5,  7,  11, 13, 17, 19, 23, 29,
31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
73, 79, 83, 89, 97
```

### Quick Count
| Range | Count |
|-------|-------|
| 1 to 10 | 4 primes |
| 1 to 50 | 15 primes |
| 1 to 100 | 25 primes |
| 1 to 200 | 46 primes |
| 1 to 1000 | 168 primes |

---

## 🔧 How to Check if a Number is Prime

### Method: Trial Division
1. Find √N (approximate)
2. Check if N is divisible by any prime number ≤ √N
3. If not divisible by any → **N is prime**

**Example**: Is 131 prime?
- √131 ≈ 11.4
- Check primes ≤ 11: 2, 3, 5, 7, 11
- 131 ÷ 2 = not even ❌
- 131 ÷ 3 → 1+3+1 = 5 (not div by 3) ❌
- 131 ÷ 5 → doesn't end in 0/5 ❌
- 131 ÷ 7 = 18.7... ❌
- 131 ÷ 11 = 11.9... ❌
- **131 is prime** ✅

---

## 📝 Factors

### What is a Factor?
If a divides b exactly, then a is a **factor** of b.

### Finding All Factors of a Number
1. Express number in prime factorization form: N = p^a × q^b × r^c
2. **Number of factors** = (a+1)(b+1)(c+1)
3. **Sum of factors** = [(p^(a+1) - 1)/(p - 1)] × [(q^(b+1) - 1)/(q - 1)] × ...
4. **Product of all factors** = N^(number of factors / 2)

### Even & Odd Factors
- **Number of odd factors**: Ignore the power of 2 in factorization, then apply (a+1)(b+1)... for remaining primes
- **Number of even factors** = Total factors - Odd factors

### Perfect Square Factor Property
- A number is a **perfect square** if all powers in its prime factorization are **even**
- **Number of factors of a perfect square is always ODD**
- **Non-perfect squares always have EVEN number of factors**

---

## 📝 Multiples

### What is a Multiple?
b is a **multiple** of a if a divides b exactly.
- Multiples of 5: 5, 10, 15, 20, 25...

### Key Facts
- Every number is a multiple of 1 and itself
- 0 is a multiple of every number
- Multiples of a number are infinite

---

## 📝 Co-prime (Relatively Prime) Numbers
Two numbers are **co-prime** if their HCF = 1.

### Examples of Co-prime Pairs
- (2, 3), (4, 9), (8, 15), (13, 27)

### Important Properties
- Two consecutive numbers are always co-prime
- Two consecutive odd numbers are always co-prime  
- A prime number is co-prime with every number it doesn't divide
- 1 is co-prime with every number

---

## 📝 Twin Primes
Pairs of primes that differ by 2.
- (3, 5), (5, 7), (11, 13), (17, 19), (29, 31), (41, 43)...

---

## ⚡ Tricks & Shortcuts

> 💡 **Trick 1 – Quick Prime Check**: Every prime > 3 can be written as 6k ± 1. So to quickly eliminate, if a number is NOT of the form 6k ± 1, it's NOT prime (exception: 2 and 3).

> 💡 **Trick 2 – Factor Pairs**: List factors in pairs. For 36: (1,36), (2,18), (3,12), (4,9), (6,6). Stop when pairs repeat.

> 💡 **Trick 3 – Memorize Small Primes**: Know all primes up to 100 by heart. This saves time in exams.

> 💡 **Trick 4 – Sum of Reciprocals of Factors**: For N = p^a × q^b, Sum of reciprocals = (Sum of all factors) / N

---

## 📖 Solved Examples

### Example 1: Primality Check
**Q**: Is 247 prime?  
**Solution**:  
- √247 ≈ 15.7
- Check primes ≤ 15: 2, 3, 5, 7, 11, 13
- 247 ÷ 13 = 19 → **Divisible!**
- 247 = 13 × 19 → **Not prime** ❌

---

### Example 2: Number of Factors
**Q**: How many factors does 360 have?  
**Solution**:  
- 360 = 2³ × 3² × 5¹
- Number of factors = (3+1)(2+1)(1+1) = 4 × 3 × 2 = **24**

---

### Example 3: Sum of Factors
**Q**: Find the sum of all factors of 12.  
**Solution**:  
- 12 = 2² × 3¹
- Sum = [(2³ - 1)/(2 - 1)] × [(3² - 1)/(3 - 1)]
- = [7/1] × [8/2]
- = 7 × 4 = **28**
- Verify: Factors of 12 = 1, 2, 3, 4, 6, 12. Sum = 28 ✅

---

### Example 4: Odd Factors
**Q**: How many odd factors does 360 have?  
**Solution**:  
- 360 = 2³ × 3² × 5¹
- For odd factors, ignore 2³ → consider 3² × 5¹
- Odd factors = (2+1)(1+1) = **6**
- (They are: 1, 3, 5, 9, 15, 45)

---

### Example 5: Perfect Square Check
**Q**: Is 1764 a perfect square? How many factors does it have?  
**Solution**:  
- 1764 = 2² × 3² × 7²
- All powers are even → **Yes, perfect square** (42²)
- Factors = (2+1)(2+1)(2+1) = **27** (odd, as expected)

---

### Example 6: Co-prime Question
**Q**: How many numbers less than 100 are co-prime to 100?  
**Solution**:  
- 100 = 2² × 5²
- Using Euler's Totient: φ(100) = 100 × (1 - 1/2) × (1 - 1/5) = 100 × 1/2 × 4/5 = **40**

---

## 🎯 Exam Tips
- The "6k ± 1" check is the fastest way to eliminate non-primes in MCQs
- For factor-counting questions, always start with prime factorization
- Remember: Perfect squares have an **odd** number of factors — great for elimination in MCQs
