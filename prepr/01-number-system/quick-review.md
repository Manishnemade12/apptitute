# Quick Review: Number System 🔴

### Divisibility Rules
**Formulas**:
- 2: Last digit is even
- 3: Sum of digits is divisible by 3
- 4: Last two digits divisible by 4
- 5: Last digit is 0 or 5
- 8: Last 3 digits divisible by 8
- 9: Sum of digits is divisible by 9
- 11: Difference between sum of odd placed digits and even placed digits is 0 or multiple of 11.
**Trick**: To check divisibility by composite numbers (like 12), check divisibility for co-prime factors (3 and 4).

---
### LCM & HCF
**Formulas**:
- Product of two numbers = LCM * HCF
- LCM of fractions = LCM(Numerators) / HCF(Denominators)
- HCF of fractions = HCF(Numerators) / LCM(Denominators)
**Trick**: - To find largest number that divides A, B, C leaving remainders r1, r2, r3: Find HCF of (A-r1, B-r2, C-r3).
- To find smallest number divisible by A, B, C leaving remainder r in each case: Find LCM(A,B,C) + r.

---
### Prime Numbers, Factors, Multiples
**Formulas**:
- Prime number has exactly two factors: 1 and itself.
- Co-primes have HCF = 1.
**Trick**: To check if N is prime, find integer k > √N. Check divisibility of N by all prime numbers <= k.

---
### Remainder Theorem Basics
**Formulas**:
- Dividend = (Divisor × Quotient) + Remainder
- (a * b) % n = [(a % n) * (b % n)] % n
- Fermat's Little Theorem: a^(p-1) ≡ 1 (mod p) where p is prime.
**Trick**: Use negative remainders to simplify calculations. e.g., 34 % 7 can be written as -1.

---
### Unit Digit & Last Digit
**Formulas**:
- Cyclicity of 2, 3, 7, 8 is 4.
- Cyclicity of 4, 9 is 2.
- Cyclicity of 0, 1, 5, 6 is 1.
**Trick**: For x^y, find y % 4. If y%4 == 0, use power 4.

---
### Number of Factors
**Formulas**:
If N = p^a * q^b * r^c..., then Number of factors = (a+1)(b+1)(c+1)...
**Trick**: To find sum of factors: [ (p^(a+1)-1)/(p-1) ] * [ (q^(b+1)-1)/(q-1) ] ...

---
### Base Conversion
**Formulas**:
Decimal to Binary: Keep dividing by 2 and note remainders bottom to top.
Binary to Decimal: Multiply bits by powers of 2 from right to left.
**Trick**: Memorize powers of 2 up to 1024 for quick conversion.

---
