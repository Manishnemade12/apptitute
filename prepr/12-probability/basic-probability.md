# Basic Probability (Cards, Dice, Coins) 🟡

## 📌 Definition
```
Probability P(E) = Favourable Outcomes / Total Outcomes
0 ≤ P(E) ≤ 1
P(E) + P(not E) = 1
```

---

## 📝 Standard Sample Spaces

### Coin
- 1 coin: {H, T} → 2 outcomes
- 2 coins: {HH, HT, TH, TT} → 4 outcomes
- n coins: 2ⁿ outcomes

### Dice
- 1 die: {1,2,3,4,5,6} → 6 outcomes
- 2 dice: 36 outcomes
- n dice: 6ⁿ outcomes

### Cards (Standard Deck of 52)
| Category | Count |
|----------|-------|
| Total cards | 52 |
| Suits | 4 (♠♥♦♣) |
| Cards per suit | 13 |
| Red cards (♥♦) | 26 |
| Black cards (♠♣) | 26 |
| Face cards (J,Q,K) | 12 (3 per suit) |
| Aces | 4 |

---

## 📝 Key Formulas

| Rule | Formula |
|------|---------|
| AND (both events) | P(A∩B) = P(A) × P(B) [if independent] |
| OR (either event) | P(A∪B) = P(A) + P(B) - P(A∩B) |
| Complement | P(not A) = 1 - P(A) |
| Conditional | P(A\|B) = P(A∩B) / P(B) |

---

## 📖 Solved Examples

### Example 1: Single Die
**Q**: Probability of getting a prime number on a die.  
**Solution**: Primes = {2,3,5} → P = 3/6 = **1/2**

---

### Example 2: Two Dice Sum
**Q**: P(sum = 7) with two dice?  
**Solution**: Favorable = {(1,6),(2,5),(3,4),(4,3),(5,2),(6,1)} = 6 → P = 6/36 = **1/6**

---

### Example 3: Cards
**Q**: P(drawing a King or a Heart)?  
**Solution**: Kings=4, Hearts=13, King of Hearts=1 → P = (4+13-1)/52 = **16/52 = 4/13**

---

### Example 4: Two Coins
**Q**: P(at least one head) with 2 coins?  
**Solution**: 1 - P(no heads) = 1 - 1/4 = **3/4**

---

### Example 5: Without Replacement
**Q**: 2 cards drawn without replacement. P(both Aces)?  
**Solution**: (4/52) × (3/51) = 12/2652 = **1/221**

---

## 🎯 Exam Tips
- "At least one" → use complement: 1 - P(none)
- "And" → multiply | "Or" → add (subtract overlap)
- Cards deck structure is must-know
