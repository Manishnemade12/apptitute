# Clocks — Angle Between Hands 🟢

## 📝 Key Formulas

### Speed of Hands
```
Hour hand: 0.5° per minute (360° in 12 hours)
Minute hand: 6° per minute (360° in 60 minutes)
Relative speed: 5.5° per minute (minute gains on hour)
```

### Angle Between Hands at H hours M minutes
```
Angle = |30H - 5.5M|
If result > 180°, subtract from 360° (take the smaller angle)
```

### When Do Hands Overlap?
```
30H = 5.5M → M = 60H/11
```
Hands overlap 11 times in 12 hours (not at 12 o'clock count depends on context).

### When Are Hands at Right Angle (90°)?
```
|30H - 5.5M| = 90° → Solve for M
```
Happens 22 times in 12 hours.

### When Are Hands Opposite (180°)?
```
|30H - 5.5M| = 180° → Solve for M
```
Happens 11 times in 12 hours.

---

## 📝 Clock Gain/Loss Problems
```
In a faulty clock gaining x minutes per hour:
Actual time elapsed = (60/(60+x)) × Shown time
```

---

## 📖 Solved Examples

### Example 1
**Q**: Angle at 3:30?  
**Solution**: |30×3 - 5.5×30| = |90-165| = **75°**

### Example 2
**Q**: At what time between 4 and 5 are hands at right angle?  
**Solution**: |30×4 - 5.5M| = 90. Cases: 120-5.5M=90 → M=30/5.5=**5.45 min**. OR 120-5.5M=-90 → M=210/5.5=**38.18 min**

### Example 3
**Q**: Angle at 7:20?  
**Solution**: |30×7 - 5.5×20| = |210-110| = **100°**

---

# Day of the Week Problems 🟢

## 📝 Key Facts
```
Normal year = 365 days = 52 weeks + 1 odd day
Leap year = 366 days = 52 weeks + 2 odd days
```

### Leap Year Rules
- Divisible by 4 → Leap (usually)
- Divisible by 100 → NOT leap
- Divisible by 400 → Leap

### Odd Days in a Century
| Century | Odd Days |
|---------|----------|
| 100 years | 5 odd days |
| 200 years | 3 odd days |
| 300 years | 1 odd day |
| 400 years | 0 odd days |

### Day Numbering
| Day | Number |
|-----|--------|
| Sunday | 0 |
| Monday | 1 |
| Tuesday | 2 |
| Wednesday | 3 |
| Thursday | 4 |
| Friday | 5 |
| Saturday | 6 |

---

## 📖 Solved Examples

### Example 1
**Q**: What day was Jan 1, 2000?  
**Solution**:  
- 1600 years = 0 odd days
- 300 years = 1 odd day
- 99 years = 24 leaps + 75 normal = 48+75 = 123 odd days = 17 weeks + 4 = 4 odd days
- Total = 0+1+4 = 5 odd days + Jan 1 = 6 → **Saturday**

### Example 2
**Q**: If Jan 1, 2023 is Sunday, what day is March 1, 2023?  
**Solution**: Jan(31-1=30) + Feb(28) = 58 days. 58/7 = 8 weeks + 2 odd days. Sunday + 2 = **Wednesday** (actually let me verify: 30+28=58, 58%7=2, Sun+2=Tue... 0+2=2=Tuesday)

---

## Quick Review
- Clock angle = |30H - 5.5M|
- Odd days: Normal year=1, Leap year=2
- 400 years = 0 odd days
