# ⚡ Quick Review: Number System 🔴

> Use this file for **last-minute revision** before your exam. All key formulas and tricks in one place.

---

## Divisibility Rules
| Divisor | Rule |
|---------|------|
| 2 | Last digit even |
| 3 | Digit sum divisible by 3 |
| 4 | Last 2 digits divisible by 4 |
| 5 | Last digit 0 or 5 |
| 6 | Div by both 2 AND 3 |
| 7 | Double last digit, subtract from rest |
| 8 | Last 3 digits divisible by 8 |
| 9 | Digit sum divisible by 9 |
| 11 | (Sum odd-position digits) - (Sum even-position digits) = 0 or ×11 |
| 12 | Div by both 3 AND 4 |

**Key Trick**: abcabc = abc × 1001 = abc × 7 × 11 × 13

---

## LCM & HCF
- **Product of 2 numbers = LCM × HCF**
- HCF: Take **lowest** powers of common primes
- LCM: Take **highest** powers of all primes
- LCM of fractions = LCM(num) / HCF(den)
- HCF of fractions = HCF(num) / LCM(den)

**Word Problem Patterns**:
| Pattern | Formula |
|---------|---------|
| Largest no. dividing A,B,C leaving same remainder | HCF of \|A-B\|, \|B-C\|, \|A-C\| |
| Largest dividing A,B,C leaving r₁,r₂,r₃ | HCF of (A-r₁), (B-r₂), (C-r₃) |
| Smallest divisible by A,B,C | LCM(A,B,C) |
| Smallest div by A,B,C leaving remainder r | LCM + r |
| Bells ringing together | LCM of intervals |

---

## Prime Numbers & Factors
- 2 is the only even prime
- Every prime > 3 is of form 6k ± 1
- Check prime: test divisibility by all primes ≤ √N

**Factor Formulas (N = p^a × q^b × r^c)**:
| What | Formula |
|------|---------|
| Number of factors | (a+1)(b+1)(c+1) |
| Sum of factors | [(p^(a+1)-1)/(p-1)] × ... |
| Product of factors | N^(total/2) |
| Odd factors | Skip 2's power, apply formula |
| Even factors | Total - Odd |
| Perfect square factors | (⌊a/2⌋+1)(⌊b/2⌋+1)... |

**Key**: Perfect squares have ODD number of factors

---

## Remainder Theorem
- **(a×b) mod n = [(a mod n) × (b mod n)] mod n**
- Same for +, -
- **Fermat's**: a^(p-1) ≡ 1 (mod p) when p is prime
- 10^n mod 9 = 1 (always)
- 10^n mod 11 = 1 (even n), 10 (odd n)

**Key Trick**: Use negative remainders → 29 mod 5 = -1

---

## Unit Digit / Cyclicity

| Cyclicity | Digits |
|-----------|--------|
| 1 (always same) | 0, 1, 5, 6 |
| 2 (even/odd) | 4, 9 |
| 4 (four-cycle) | 2, 3, 7, 8 |

**Cycles**: 2→{2,4,8,6}, 3→{3,9,7,1}, 7→{7,9,3,1}, 8→{8,4,2,6}

**Method**: Unit digit of a^n → (unit digit of a)^(n mod cyclicity)

**Key**: n! for n ≥ 5 always has unit digit **0**

---

## Base Conversion
- Decimal → Binary: Divide by 2, remainders bottom-to-top
- Binary → Decimal: Multiply by 2^position, sum up
- Binary → Octal: Group 3 bits
- Binary → Hex: Group 4 bits
- Largest n-digit number in base b = b^n - 1

**Powers of 2**: 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024
