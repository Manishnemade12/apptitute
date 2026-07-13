# Average Speed Problems 🟡

## 📌 Concept
Average speed is **NOT** the simple average of speeds. It depends on total distance and total time.
```
Average Speed = Total Distance / Total Time
```

---

## 📝 All Formulas

### Case 1: Same Distance, Different Speeds
If a person travels distance d at speed x and returns at speed y:
```
Average Speed = 2xy / (x + y)    ← Harmonic Mean
```
**Note**: This is ALWAYS less than the simple average (x+y)/2.

### Case 2: Same Time, Different Speeds
If a person travels for time t at speed x and then time t at speed y:
```
Average Speed = (x + y) / 2    ← Arithmetic Mean
```

### Case 3: Different Distances, Different Speeds
If distances d₁, d₂ are covered at speeds v₁, v₂:
```
Average Speed = (d₁ + d₂) / (d₁/v₁ + d₂/v₂)
```

### Case 4: Three Different Speeds, Same Distance
Travels d at speeds x, y, z:
```
Average Speed = 3xyz / (xy + yz + xz)
```

---

## 📝 Key Properties

| Property | Description |
|----------|-------------|
| Average speed ≠ Average of speeds | Never just add and divide speeds |
| For same distance | Avg speed = Harmonic mean (always < arithmetic mean) |
| For same time | Avg speed = Arithmetic mean |
| If one speed is 0 | Avg speed = 0 (total distance/infinite time) |

---

## ⚡ Tricks & Shortcuts

> 💡 **Trick 1 – The 2xy/(x+y) Shortcut**: For round trip (same distance) — this formula is instant. No need to calculate time/distance separately.
> - Go 60, Come 40 → Avg = 2×60×40/100 = **48 kmph**

> 💡 **Trick 2 – The Ratio Method**: If speeds are in ratio a:b, and distances are equal:
> - Times are in ratio b:a (inverse)
> - Average speed = 2ab/(a+b) units

> 💡 **Trick 3 – Never Average Speeds**: The most common trap. 40 and 60 → avg is 48, NOT 50.

> 💡 **Trick 4 – Same Time Rare**: The "same time" case is rare in exams. Most problems are "same distance." Default to 2xy/(x+y) unless told otherwise.

---

## 📖 Solved Examples

### Example 1: Basic Round Trip
**Q**: A person goes to office at 30 kmph and returns at 20 kmph. Find average speed.  
**Solution**: Avg = 2×30×20 / (30+20) = 1200/50 = **24 kmph**

---

### Example 2: Same Time
**Q**: A train travels for 3 hours at 40 kmph and 3 hours at 60 kmph. Average speed?  
**Solution**:  
- Same time → Avg = (40+60)/2 = **50 kmph**
- Verify: Total distance = 120+180 = 300, Total time = 6, Avg = 300/6 = 50 ✅

---

### Example 3: Different Distances
**Q**: A car covers 200 km at 50 kmph and 300 km at 60 kmph. Find average speed.  
**Solution**:  
- Time₁ = 200/50 = 4 hrs
- Time₂ = 300/60 = 5 hrs
- Avg = (200+300)/(4+5) = 500/9 = **55.55 kmph**

---

### Example 4: Three Speeds, Same Distance
**Q**: A man travels equal distances at 10, 20, and 30 kmph. Average speed?  
**Solution**:  
- Avg = 3×10×20×30 / (10×20 + 20×30 + 30×10)
- = 18000 / (200 + 600 + 300) = 18000/1100
- = **16.36 kmph**

---

### Example 5: Word Problem
**Q**: A cyclist goes from A to B at 12 kmph. If he goes at 16 kmph, he reaches 30 min earlier. Find distance AB.  
**Solution**:  
- Time difference = 30 min = 1/2 hr
- D/12 - D/16 = 1/2
- (4D - 3D)/48 = 1/2
- D = **24 km**

---

### Example 6: Finding One Speed
**Q**: Average speed for a round trip is 48 kmph. If onward speed is 60 kmph, find return speed.  
**Solution**:  
- 48 = 2×60×y / (60+y)
- 48(60+y) = 120y
- 2880 + 48y = 120y
- 72y = 2880 → y = **40 kmph**

---

## 🎯 Exam Tips
- **Default to 2xy/(x+y)** for most problems (same distance is the most common case)
- The answer is always **less than the arithmetic mean** for same-distance problems
- Read carefully whether distance or time is the same — it changes the formula completely
