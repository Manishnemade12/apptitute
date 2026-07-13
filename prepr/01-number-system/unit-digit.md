# Unit Digit & Last Digit Problems 🟡

## 📌 Concept
The **unit digit** (last digit) of a number is the digit in the **ones place**.  
Many exam questions ask: "Find the unit digit of A^B" or "What is the last digit of a large expression?"

The key insight: **Only the unit digit of the base matters**, and unit digits follow a **cyclicity pattern**.

---

## 📝 Cyclicity Table (Core Formula)

Every digit (0–9) repeats its unit digit in a cycle when raised to powers:

| Digit | Cycle of Unit Digits | Cyclicity |
|-------|---------------------|-----------|
| **0** | 0, 0, 0, 0... | 1 |
| **1** | 1, 1, 1, 1... | 1 |
| **2** | 2, 4, 8, 6, 2, 4, 8, 6... | **4** |
| **3** | 3, 9, 7, 1, 3, 9, 7, 1... | **4** |
| **4** | 4, 6, 4, 6... | **2** |
| **5** | 5, 5, 5, 5... | 1 |
| **6** | 6, 6, 6, 6... | 1 |
| **7** | 7, 9, 3, 1, 7, 9, 3, 1... | **4** |
| **8** | 8, 4, 2, 6, 8, 4, 2, 6... | **4** |
| **9** | 9, 1, 9, 1... | **2** |

### Summary
| Cyclicity | Digits |
|-----------|--------|
| **1** (always same) | 0, 1, 5, 6 |
| **2** (alternates) | 4, 9 |
| **4** (four-cycle) | 2, 3, 7, 8 |

---

## 🔧 Step-by-Step Method

### To find unit digit of a^n:
1. Take the **unit digit** of a
2. Check the **cyclicity** of that digit
3. Find **n mod cyclicity**
4. If remainder = 0, use the **last value** in the cycle (i.e., use cyclicity itself as the power)
5. Calculate unit digit of (unit digit of a)^(remainder)

---

## 📝 Special Properties

### Property 1: Unit digits 0, 1, 5, 6
Any power of these digits gives the **same unit digit**.
- 5^1 = 5, 5^2 = 25, 5^3 = 125 → always **5**
- 6^1 = 6, 6^2 = 36, 6^3 = 216 → always **6**

### Property 2: Unit digits 4 and 9
- **Even power** → unit digit 6 (for 4) or 1 (for 9)
- **Odd power** → unit digit 4 (for 4) or 9 (for 9)

### Property 3: Products
The unit digit of a product depends only on the unit digits of the factors:
- Unit digit of (23 × 47) = Unit digit of (3 × 7) = Unit digit of 21 = **1**

### Property 4: Powers of Powers
For a^(b^c), compute (b^c) mod cyclicity first.

---

## ⚡ Tricks & Shortcuts

> 💡 **Trick 1 – The "4 Rule"**: For digits with cyclicity 4 (2, 3, 7, 8):
> - Power mod 4 = 1 → use 1st value in cycle
> - Power mod 4 = 2 → use 2nd value
> - Power mod 4 = 3 → use 3rd value
> - Power mod 4 = 0 → use 4th value

> 💡 **Trick 2 – Even/Odd Shortcut for 4 and 9**:
> - 4^(even) → 6, 4^(odd) → 4
> - 9^(even) → 1, 9^(odd) → 9

> 💡 **Trick 3 – Big Product Shortcut**: For products, just multiply unit digits step by step, keeping only the last digit each time.

> 💡 **Trick 4 – a^a pattern**: For the series 1^1 + 2^2 + 3^3 + ... find each unit digit individually and add.

---

## 📖 Solved Examples

### Example 1: Basic Unit Digit
**Q**: Find the unit digit of 7^253.  
**Solution**:  
- Unit digit of base = 7 (cyclicity = 4)
- 253 mod 4 = 1
- 1st value in cycle of 7: **7**
- Unit digit = **7**

---

### Example 2: Cyclicity 2
**Q**: Find the unit digit of 4^372.  
**Solution**:  
- Cyclicity of 4 = 2
- 372 is even
- 4^(even) → unit digit = **6**

---

### Example 3: Power of Zero
**Q**: Find the unit digit of 9^100.  
**Solution**:  
- Cyclicity of 9 = 2
- 100 is even
- 9^(even) → unit digit = **1**

---

### Example 4: Product Expression
**Q**: Find the unit digit of 23^14 × 87^22 × 64^8.  
**Solution**:  
- 23^14 → unit digit of 3, cyclicity 4, 14 mod 4 = 2, cycle: 3,9,7,1 → **9**
- 87^22 → unit digit of 7, cyclicity 4, 22 mod 4 = 2, cycle: 7,9,3,1 → **9**
- 64^8 → unit digit of 4, cyclicity 2, 8 is even → **6**
- Product: 9 × 9 × 6 = 81 × 6 = 486 → unit digit = **6**

---

### Example 5: Sum Expression
**Q**: Find the unit digit of 1! + 2! + 3! + 4! + ... + 100!  
**Solution**:  
- 1! = 1, 2! = 2, 3! = 6, 4! = 24 → unit digit 4
- 5! = 120 → unit digit 0
- 6!, 7!, ..., 100! all have unit digit **0** (since they contain 5 × 2)
- Sum of unit digits = 1 + 2 + 6 + 4 + 0 + 0 + ... = 13
- Unit digit = **3**

---

### Example 6: Power of a Power
**Q**: Find the unit digit of 2^(3^4).  
**Solution**:  
- 3^4 = 81
- Find unit digit of 2^81
- Cyclicity of 2 = 4
- 81 mod 4 = 1
- Cycle of 2: 2, 4, 8, 6 → 1st position = **2**

---

### Example 7: Difference Problem
**Q**: Find the unit digit of 7^91 - 3^53.  
**Solution**:  
- 7^91: cyclicity 4, 91 mod 4 = 3, cycle: 7,9,3,1 → unit digit = **3**
- 3^53: cyclicity 4, 53 mod 4 = 1, cycle: 3,9,7,1 → unit digit = **3**
- 3 - 3 = **0**

---

## 🎯 Exam Tips
- Memorize the cyclicity table — it's the foundation of all unit digit problems
- For factorials ≥ 5!, the unit digit is always **0** (since 5! = 120)
- In MCQs, unit digit questions are free marks if you know cyclicity — solve in under 30 seconds
