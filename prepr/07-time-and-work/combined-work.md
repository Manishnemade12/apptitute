# Combined Work (A+B, A+B+C) 🔴

## 📌 Concept
When multiple people (or machines) work together, their efficiencies **add up**. This section covers all patterns of combined work problems.

---

## 📝 All Formulas

### Two People Working Together
```
1/A + 1/B = 1/T
T = (A × B) / (A + B)
```

### Three People Working Together
```
1/A + 1/B + 1/C = 1/T
```

### Finding Individual from Combined
If A+B take p days, B+C take q days, A+C take r days:
```
1/A + 1/B + 1/C = (1/2) × (1/p + 1/q + 1/r)
```
Then:
```
1/A = (1/A + 1/B + 1/C) - 1/q   [subtract B+C]
1/B = (1/A + 1/B + 1/C) - 1/r   [subtract A+C]
1/C = (1/A + 1/B + 1/C) - 1/p   [subtract A+B]
```

### Alternate Day Work
If A works on day 1, B on day 2, A on day 3, B on day 4...:
- Work done in 2 days = A's 1 day + B's 1 day
- Find how many complete 2-day cycles fit, then handle remaining

---

## 📝 Common Patterns

### Pattern 1: A and B together, then one leaves
"A and B work for d days, then B leaves. A finishes remaining in x days."
- Work done by (A+B) in d days + Work done by A in x days = Total Work

### Pattern 2: Finding how long one person worked
"A and B start together. Total work done in T days. B left after d days."
- B worked d days, A worked T days

### Pattern 3: People join midway
"A starts alone. After d days, B joins."
- Total = A's solo work + (A+B)'s joint work

---

## ⚡ Tricks & Shortcuts

> 💡 **Trick 1 – LCM Method for Combined**: 
> A=10, B=15, C=20 → Total Work = LCM(10,15,20) = 60
> Eff: A=6, B=4, C=3 → Together = 13/day → Time = 60/13 ≈ 4.6 days

> 💡 **Trick 2 – Alternate Day Pattern**: Calculate 2-day output, divide total work, handle the fractional day.

> 💡 **Trick 3 – Someone Leaves**: Track work done in phases. Phase 1: all together. Phase 2: remaining people.

---

## 📖 Solved Examples

### Example 1: Three People Together
**Q**: A=10 days, B=12 days, C=15 days. All together?  
**Solution**:  
- Total Work = LCM(10,12,15) = 60
- A=6, B=5, C=4 → Together = 15/day
- Time = 60/15 = **4 days**

---

### Example 2: One Person Leaves
**Q**: A=12 days, B=16 days. They work together for 4 days, then B leaves. How many more days for A to finish?  
**Solution**:  
- Total Work = LCM(12,16) = 48
- A=4, B=3 → Together = 7/day
- In 4 days: 28 done. Remaining = 20
- A alone: 20/4 = **5 more days**

---

### Example 3: Alternate Days
**Q**: A=10 days, B=15 days. They work on alternate days starting with A. Total days?  
**Solution**:  
- Total Work = LCM(10,15) = 30
- A=3/day, B=2/day → In 2 days = 5 done
- Full cycles: 30/5 = 6 cycles = **12 days**

---

### Example 4: Finding Individual
**Q**: A+B = 8 days, B+C = 12 days, A+C = 10 days. Find A alone.  
**Solution**:  
- Total Work = LCM(8,12,10) = 120
- A+B = 15/day, B+C = 10/day, A+C = 12/day
- 2(A+B+C) = 37 → A+B+C = 18.5/day
- A = 18.5 - 10 = 8.5/day → A alone = 120/8.5 ≈ **14.1 days**

---

### Example 5: Person Joins Midway
**Q**: A takes 20 days. After 5 days, B joins and they finish in 3 more days. How long does B take alone?  
**Solution**:  
- Total Work = 20 units (A's eff = 1/day)
- A works 8 days = 8 units. B works 3 days.
- A in last 3 days = 3 units
- B in 3 days = 20 - 8 = 12... Wait: A works 5 days alone = 5. Then A+B work 3 days = Total 20.
- A+B in 3 days = 15. A alone = 3. B alone in 3 days = 12. B per day = 4 → B alone = 20/4 = **5 days**... That seems too fast. Let me redo.
- Actually: A's eff = 1 unit/day. In 5 days A does 5. Remaining = 15.
- A+B do 15 in 3 days → (A+B) = 5/day. A = 1. B = 4/day → B alone = 20/4 = **5 days**

---

## 🎯 Exam Tips
- LCM method makes combined work easy — never use fractions
- Track phases carefully when people join or leave
- Alternate day problems: calculate 2-day output, then do division
