# Divisibility Rules 🔴

## 📌 What is Divisibility?
A number **a** is divisible by **b** if `a ÷ b` leaves **no remainder** (remainder = 0).  
Notation: b | a means "b divides a".

---

## 📝 Complete Divisibility Rules

### Divisibility by 2
- **Rule**: Last digit is **even** (0, 2, 4, 6, 8)
- Example: 4356 → last digit 6 (even) → ✅ Divisible

### Divisibility by 3
- **Rule**: **Sum of all digits** is divisible by 3
- Example: 8241 → 8+2+4+1 = 15 → 15 ÷ 3 = 5 → ✅ Divisible

### Divisibility by 4
- **Rule**: **Last two digits** form a number divisible by 4
- Example: 7324 → last two digits = 24 → 24 ÷ 4 = 6 → ✅ Divisible
- **Special**: If last two digits are 00, the number is divisible by 4

### Divisibility by 5
- **Rule**: Last digit is **0 or 5**
- Example: 2345 → last digit 5 → ✅ Divisible

### Divisibility by 6
- **Rule**: Number is divisible by **both 2 AND 3**
- Example: 1236 → Even (div by 2) ✅, 1+2+3+6=12 (div by 3) ✅ → ✅ Divisible by 6

### Divisibility by 7
- **Rule**: Double the last digit, subtract from remaining number. If result is divisible by 7, so is the original.
- Example: 343 → 34 - (3×2) = 34 - 6 = 28 → 28 ÷ 7 = 4 → ✅ Divisible
- **Alternate**: 1001 is divisible by 7. So any 6-digit number where first 3 digits = last 3 digits (like 142142) is divisible by 7.

### Divisibility by 8
- **Rule**: **Last three digits** form a number divisible by 8
- Example: 53104 → last three digits = 104 → 104 ÷ 8 = 13 → ✅ Divisible
- **Special**: If last three digits are 000, the number is divisible by 8

### Divisibility by 9
- **Rule**: **Sum of all digits** is divisible by 9
- Example: 729 → 7+2+9 = 18 → 18 ÷ 9 = 2 → ✅ Divisible

### Divisibility by 10
- **Rule**: Last digit is **0**
- Example: 5830 → last digit 0 → ✅ Divisible

### Divisibility by 11
- **Rule**: **Difference** between sum of digits at **odd positions** and sum of digits at **even positions** is 0 or a multiple of 11
- Positions are counted from the right (or left — result is same)
- Example: 121 → (1+1) - (2) = 0 → ✅ Divisible
- Example: 61809 → (6+8+9) - (1+0) = 23 - 1 = 22 → 22 ÷ 11 = 2 → ✅ Divisible

### Divisibility by 12
- **Rule**: Number is divisible by **both 3 AND 4**
- Example: 1452 → 1+4+5+2=12 (div by 3) ✅, last two digits 52 ÷ 4 = 13 (div by 4) ✅ → ✅ Divisible by 12

### Divisibility by 13
- **Rule**: Form alternating groups of 3 digits from right. Add odd-positioned groups, subtract even-positioned groups. If result is divisible by 13, so is the number.
- Example: 2911 → Groups: 2 | 911 → 911 - 2 = 909 → 909 ÷ 13 = 69.9... → ❌ Not divisible

### Divisibility by 15
- **Rule**: Number is divisible by **both 3 AND 5**

### Divisibility by 25
- **Rule**: **Last two digits** form a number divisible by 25 (00, 25, 50, 75)

---

## 🔑 Key Properties

| Property | Description |
|----------|-------------|
| **Composite Rule** | To check divisibility by a composite number, check for its **co-prime factors**. E.g., 12 = 3 × 4 (co-prime), so check 3 and 4 separately |
| **If a \| b and a \| c** | Then a \| (b + c) and a \| (b - c) |
| **If a \| b** | Then a \| (b × k) for any integer k |
| **Transitivity** | If a \| b and b \| c, then a \| c |

---

## ⚡ Tricks & Shortcuts

> 💡 **Trick 1 – Composite Number Shortcut**: For divisibility by composite numbers, always break into **co-prime** factors.
> - 6 = 2 × 3 → check 2 and 3
> - 12 = 3 × 4 → check 3 and 4 (NOT 2 and 6, because they share factor 2)
> - 15 = 3 × 5 → check 3 and 5
> - 18 = 2 × 9 → check 2 and 9

> 💡 **Trick 2 – Digit Sum Shortcut**: The digit sum trick for 3 and 9 can be applied **recursively**.
> - 8547 → 8+5+4+7 = 24 → 2+4 = 6 → div by 3? Yes. div by 9? No.

> 💡 **Trick 3 – Quick 11 Check**: Alternate + and - from the left digit.
> - 918082 → 9-1+8-0+8-2 = 22 → Divisible by 11 ✅

> 💡 **Trick 4 – For 7, 11, 13**: 1001 = 7 × 11 × 13. So any number of the form abcabc is always divisible by 7, 11, and 13.
> - 256256 = 256 × 1001 → divisible by 7, 11, and 13

---

## 📖 Solved Examples

### Example 1: Basic Divisibility Check
**Q**: Is 5765832 divisible by 4?  
**Solution**:  
Check last 2 digits: **32**  
32 ÷ 4 = 8 → ✅ **Divisible by 4**

---

### Example 2: Divisibility by 11
**Q**: Is 8294763 divisible by 11?  
**Solution**:  
Odd position digits (from right): 3, 7, 9, 8 → Sum = 27  
Even position digits (from right): 6, 4, 2 → Sum = 12  
Difference = 27 - 12 = **15** → Not 0 or multiple of 11 → ❌ **Not Divisible**

---

### Example 3: Finding Unknown Digit
**Q**: If 64x3 is divisible by 9, find the value of x.  
**Solution**:  
Sum of digits = 6 + 4 + x + 3 = 13 + x  
For divisibility by 9: 13 + x must be a multiple of 9  
Nearest multiple of 9 ≥ 13 is 18  
So 13 + x = 18 → **x = 5**

---

### Example 4: Composite Number Divisibility
**Q**: Is 7344 divisible by 12?  
**Solution**:  
12 = 3 × 4 (co-prime factors)  
- Divisibility by 3: 7+3+4+4 = 18 → 18 ÷ 3 = 6 ✅  
- Divisibility by 4: Last two digits = 44 → 44 ÷ 4 = 11 ✅  
Both pass → ✅ **Divisible by 12**

---

### Example 5: Word Problem
**Q**: What is the largest 4-digit number divisible by 88?  
**Solution**:  
Largest 4-digit number = 9999  
9999 ÷ 88 = 113 remainder 55  
Answer = 9999 - 55 = **9944**

---

### Example 6: Using the abcabc Trick
**Q**: 735735 is divisible by which of the following: 7, 11, 13, 15?  
**Solution**:  
735735 = 735 × 1001 = 735 × 7 × 11 × 13  
So divisible by **7, 11, and 13** ✅  
For 15: Need div by 3 and 5. 7+3+5+7+3+5 = 30 (div by 3 ✅), last digit 5 (div by 5 ✅) → **Also div by 15** ✅

---

## 🎯 Practice Tips
- Master rules for **2, 3, 4, 5, 8, 9, 11** — these come up the most
- For composite numbers, always identify co-prime factor pairs first
- The 1001 trick (7 × 11 × 13) is a **huge time saver** in MCQ exams
