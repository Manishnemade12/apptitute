# Change in Average 🔴

## 📌 Concept
These problems involve how the average changes when a new member is **added**, **removed**, or **replaced** in a group.

---

## 📝 All Formulas

### Adding a New Member
When a new member with value V is added to a group of n members with average A:
```
New Average = (n×A + V) / (n + 1)
V = New Average + n × (New Average - Old Average)
V = New Average + n × Change in Average
```

### Removing a Member
When a member with value V is removed from a group of n members with average A:
```
New Average = (n×A - V) / (n - 1)
V = Old Average - (n-1) × (New Average - Old Average)
```

### Replacing a Member
When old value V₁ is replaced by new value V₂ in a group of n members:
```
Change in Average = (V₂ - V₁) / n
New Average = Old Average + (V₂ - V₁) / n
V₂ = V₁ + n × Change in Average
```

### Adding/Removing Multiple Members
Adding k members with sum S to a group of n with average A:
```
New Average = (n×A + S) / (n + k)
```

---

## 📝 Common Problem Patterns

### Pattern 1: Age/Weight of New Person
"Average age of n people is A. A new person joins. Average becomes A'."
```
New person's age = A' + n × (A' - A)
                 = A' × (n+1) - A × n
```

### Pattern 2: Replacement
"Average weight of n people is A. If a person weighing W₁ is replaced by another, average changes by x."
```
Weight of new person = W₁ + n × x
(x is +ve if avg increases, -ve if decreases)
```

### Pattern 3: Wrong Entry Corrected
"Average was A, but one value was wrongly taken as X instead of Y."
```
Correct Average = A + (Y - X) / n
```

### Pattern 4: Runs / Cricket Average
"After k innings, average increases by x."
```
Runs in k-th inning = New Average + (k-1) × x
```

---

## ⚡ Tricks & Shortcuts

> 💡 **Trick 1 – Distribution of Change**: When a new person joins and average increases by x:
> - The new person "gives" x to each of the existing n members AND has (New Average) for themselves
> - So: New person = New Average + n × x

> 💡 **Trick 2 – Replacement Quick Formula**: New = Old + n × (change in average). That's it.

> 💡 **Trick 3 – Wrong Entry**: Just add/subtract the correction. If value should be 36 instead of 26: add (36-26)/n = 10/n to the average.

> 💡 **Trick 4 – Cricket Shortcut**: Runs scored = New avg + (innings - 1) × increase in avg.

---

## 📖 Solved Examples

### Example 1: New Member Added
**Q**: Average age of 10 students is 14. A new student joins, average becomes 15. Find age of new student.  
**Solution**:  
- New student age = 15 + 10 × (15-14) = 15 + 10 = **25**
- Verify: Old sum = 140, New sum = 140+25 = 165, 165/11 = 15 ✅

---

### Example 2: Member Removed
**Q**: Average of 8 numbers is 27. One number 35 is removed. New average?  
**Solution**:  
- Sum = 8 × 27 = 216
- New sum = 216 - 35 = 181
- New average = 181/7 = **25.86**

---

### Example 3: Replacement
**Q**: Average weight of 20 students is 45 kg. If a student of 55 kg is replaced by a new student, average drops to 44.5 kg. Weight of new student?  
**Solution**:  
- Change = 44.5 - 45 = -0.5
- New weight = 55 + 20 × (-0.5) = 55 - 10 = **45 kg**

---

### Example 4: Cricket Average
**Q**: A batsman has average 36 after 25 innings. How many runs should he score in the 26th inning to raise average to 38?  
**Solution**:  
- Runs = 38 + 25 × (38-36) = 38 + 50 = **88**
- Verify: Old sum = 900, New sum = 900+88 = 988, 988/26 = 38 ✅

---

### Example 5: Wrong Entry
**Q**: Average marks of 30 students was found to be 72. Later, one student's marks were misread as 84 instead of 48. Find correct average.  
**Solution**:  
- Correct average = 72 + (48-84)/30 = 72 - 36/30 = 72 - 1.2 = **70.8**

---

### Example 6: Multiple Additions
**Q**: Average weight of 15 people is 50 kg. 3 people with weights 62, 58, and 70 kg join. New average?  
**Solution**:  
- Old sum = 750
- New sum = 750 + 62 + 58 + 70 = 940
- New avg = 940/18 = **52.22 kg**

---

### Example 7: Teacher's Age Problem
**Q**: Average age of 30 students is 15. When teacher's age is included, average increases by 1. Teacher's age?  
**Solution**:  
- Teacher's age = (15+1) + 30 × 1 = 16 + 30 = **46**

---

## 🎯 Exam Tips
- The "New person's value = New avg + n × change" formula solves 90% of these problems
- For replacement: New = Old + n × change (simplest formula ever)
- Cricket/batting average problems are the same as "adding a new member"
- Always verify with Sum = Avg × Count
