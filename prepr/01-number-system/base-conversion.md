# Base Conversion (Number Base System) 🟢

## 📌 Concept
A **number base** (or radix) determines how many unique digits are used. Our everyday system is **Base 10 (Decimal)** which uses digits 0-9. Computers use **Base 2 (Binary)** with 0-1.

---

## 📝 Common Number Bases

| Base | Name | Digits Used | Usage |
|------|------|-------------|-------|
| 2 | Binary | 0, 1 | Computers |
| 8 | Octal | 0-7 | Programming |
| 10 | Decimal | 0-9 | Daily life |
| 16 | Hexadecimal | 0-9, A-F | Memory addresses |

---

## 📝 Conversion Formulas

### 1. Decimal to Any Base (Repeated Division)
**Method**: Divide the decimal number by the target base repeatedly. Write remainders **bottom to top**.

**Example**: Convert 25 to Binary (Base 2)
```
25 ÷ 2 = 12  remainder 1
12 ÷ 2 = 6   remainder 0
 6 ÷ 2 = 3   remainder 0
 3 ÷ 2 = 1   remainder 1
 1 ÷ 2 = 0   remainder 1
```
Read bottom to top: **11001₂**

### 2. Any Base to Decimal (Positional Value)
**Method**: Multiply each digit by base^position (position starts from 0 at right).

**Example**: Convert 11001₂ to Decimal
```
1×2⁴ + 1×2³ + 0×2² + 0×2¹ + 1×2⁰
= 16 + 8 + 0 + 0 + 1
= 25
```

### 3. Binary ↔ Octal (Shortcut)
Group binary digits in sets of **3** (from right) and convert each group.
```
Binary:  011  001  → Octal: 3  1 → 31₈
```

### 4. Binary ↔ Hexadecimal (Shortcut)
Group binary digits in sets of **4** (from right) and convert each group.
```
Binary: 0001  1001 → Hex: 1  9 → 19₁₆
```

---

## 📝 Powers of 2 (Must Memorize)

| 2^n | Value |
|-----|-------|
| 2⁰ | 1 |
| 2¹ | 2 |
| 2² | 4 |
| 2³ | 8 |
| 2⁴ | 16 |
| 2⁵ | 32 |
| 2⁶ | 64 |
| 2⁷ | 128 |
| 2⁸ | 256 |
| 2⁹ | 512 |
| 2¹⁰ | 1024 |

---

## 📝 Arithmetic in Different Bases

### Addition in Binary
```
0 + 0 = 0
0 + 1 = 1
1 + 0 = 1
1 + 1 = 10 (carry 1)
1 + 1 + 1 = 11 (carry 1, write 1)
```

**Example**: 1011 + 1101
```
  1 0 1 1
+ 1 1 0 1
---------
1 1 0 0 0
```
Result: **11000₂** = 24 (verify: 11+13 = 24 ✅)

### Subtraction in Binary
```
0 - 0 = 0
1 - 0 = 1
1 - 1 = 0
10 - 1 = 1 (borrow 1 from next position)
```

---

## 📝 Key Properties

| Property | Description |
|----------|-------------|
| Largest n-digit number in base b | b^n - 1 |
| Total n-digit numbers in base b | b^n - b^(n-1) |
| Largest 3-digit binary number | 111₂ = 7 |
| Largest 3-digit octal number | 777₈ = 511 |

---

## ⚡ Tricks & Shortcuts

> 💡 **Trick 1**: Memorize powers of 2 up to 2¹⁰ = 1024. Most conversion questions can be solved mentally with this knowledge.

> 💡 **Trick 2**: To quickly convert small decimals to binary, think of it as a sum of powers of 2.
> - 13 = 8 + 4 + 1 = 2³ + 2² + 2⁰ → **1101₂**

> 💡 **Trick 3**: A binary number with n digits has value between **2^(n-1)** and **2^n - 1**.
> - 5-digit binary → value between 16 and 31

> 💡 **Trick 4**: Hexadecimal A=10, B=11, C=12, D=13, E=14, F=15. Memorize this mapping.

---

## 📖 Solved Examples

### Example 1: Decimal to Binary
**Q**: Convert 45 to binary.  
**Solution**:  
- 45 = 32 + 8 + 4 + 1 = 2⁵ + 2³ + 2² + 2⁰
- Binary: **101101₂**
- Verify: 32+8+4+1 = 45 ✅

---

### Example 2: Binary to Decimal
**Q**: Convert 110110₂ to decimal.  
**Solution**:  
- 1×2⁵ + 1×2⁴ + 0×2³ + 1×2² + 1×2¹ + 0×2⁰
- = 32 + 16 + 0 + 4 + 2 + 0 = **54**

---

### Example 3: Decimal to Octal
**Q**: Convert 156 to Octal.  
**Solution**:  
```
156 ÷ 8 = 19  remainder 4
 19 ÷ 8 = 2   remainder 3
  2 ÷ 8 = 0   remainder 2
```
Answer: **234₈**  
Verify: 2×64 + 3×8 + 4 = 128+24+4 = 156 ✅

---

### Example 4: Hexadecimal to Decimal
**Q**: Convert 2A3₁₆ to decimal.  
**Solution**:  
- 2×16² + A×16¹ + 3×16⁰
- = 2×256 + 10×16 + 3×1
- = 512 + 160 + 3 = **675**

---

### Example 5: Binary to Octal
**Q**: Convert 10110111₂ to Octal.  
**Solution**:  
Group in 3s from right: 010 | 110 | 111
- 010 = 2, 110 = 6, 111 = 7
- Answer: **267₈**

---

### Example 6: Largest Number Problem
**Q**: What is the largest 4-digit number in base 5?  
**Solution**:  
- Largest 4-digit in base 5 = 4444₅
- = 4×5³ + 4×5² + 4×5¹ + 4×5⁰
- = 500 + 100 + 20 + 4 = **624**
- Or use formula: 5⁴ - 1 = 625 - 1 = **624**

---

## 🎯 Exam Tips
- Base conversion questions are straightforward — just practice the division method
- For binary, the "sum of powers of 2" method is faster than repeated division
- These questions are rare in exams (🟢 priority) but are **easy marks** when they appear
