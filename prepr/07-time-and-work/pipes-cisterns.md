# Pipes and Cisterns 🔴

## 📌 Concept
Pipes and Cisterns is **Time & Work with positive and negative efficiencies**.
- **Inlet pipe**: Fills the tank → **positive** efficiency
- **Outlet pipe / Leak**: Empties the tank → **negative** efficiency

---

## 📝 All Formulas

### Basic Concepts
```
If pipe A fills in 'a' hours → A's efficiency = +1/a (or +Total/a using LCM)
If pipe B empties in 'b' hours → B's efficiency = -1/b (or -Total/b)
Net efficiency = Sum of all (positive and negative)
Time to fill = Total Work / Net Efficiency
```

### Two Inlet Pipes
```
Together fill in: T = (a × b) / (a + b) hours
```

### One Inlet + One Outlet
```
If inlet fills in 'a' hrs, outlet empties in 'b' hrs (b > a for filling):
Time to fill = (a × b) / (b - a) hours
```

### Net Effect
```
If filling rate > emptying rate → Tank eventually fills
If emptying rate > filling rate → Tank eventually empties
If filling rate = emptying rate → Tank never fills (or stays same)
```

---

## 📝 Key Properties

| Property | Description |
|----------|-------------|
| Inlet = positive work | Adds water/content |
| Outlet/Leak = negative work | Removes water/content |
| Net rate = Sum of all rates | Inlets positive, outlets negative |
| Without leak fills in a, with leak fills in b | Leak rate = 1/a - 1/b |

---

## 📝 Leak Problems
"Without leak, pipe fills in 'a' hrs. With leak, it fills in 'b' hrs (b > a)."
```
Leak empties in = (a × b) / (b - a) hours
```

---

## ⚡ Tricks & Shortcuts

> 💡 **Trick 1 – LCM Method**: Same as Time & Work. Outlet gets negative efficiency.
> - A fills in 10 hr, leak in 15 hr → Work = 30. A=+3, Leak=-2 → Net=1 → 30 hrs.

> 💡 **Trick 2 – Pipes Opened Sequentially**: Track phases of operation.
> - Phase 1: Only A open → calculate work done
> - Phase 2: A + B open → calculate remaining work

> 💡 **Trick 3 – Part Filling**: "How much is filled in x hours?" = x × (Net efficiency) / Total Work

---

## 📖 Solved Examples

### Example 1: Two Inlet Pipes
**Q**: Pipe A fills a tank in 12 hrs, Pipe B in 18 hrs. Together?  
**Solution**:  
- Work = LCM(12,18) = 36. A=3, B=2 → Together=5
- Time = 36/5 = **7.2 hrs** = 7 hrs 12 min

---

### Example 2: Inlet + Outlet
**Q**: Pipe A fills in 10 hrs. Pipe B empties in 15 hrs. Both open, time to fill?  
**Solution**:  
- Work = 30. A=+3, B=-2 → Net=1
- Time = 30/1 = **30 hrs**

---

### Example 3: Leak Problem
**Q**: A pipe fills a tank in 6 hrs. Due to a leak, it takes 8 hrs. How long to empty by leak alone?  
**Solution**:  
- Leak empties in = (6×8)/(8-6) = 48/2 = **24 hrs**

---

### Example 4: Sequential Opening
**Q**: A fills in 10 hrs. B fills in 15 hrs. A opened first for 3 hrs, then both opened. Total time?  
**Solution**:  
- Work = 30. A=3, B=2
- Phase 1: A alone 3 hrs → 9 done. Remaining = 21
- Phase 2: A+B = 5/hr → 21/5 = 4.2 hrs
- Total = 3 + 4.2 = **7.2 hrs**

---

### Example 5: Three Pipes
**Q**: A fills in 10 hrs, B fills in 20 hrs, C empties in 40 hrs. All open, time to fill?  
**Solution**:  
- Work = 40. A=4, B=2, C=-1 → Net=5
- Time = 40/5 = **8 hrs**

---

### Example 6: Part Filled
**Q**: A fills in 12 hrs, B empties in 18 hrs. How much tank is filled in 9 hrs?  
**Solution**:  
- Work = 36. A=3, B=-2 → Net=1/hr
- In 9 hrs = 9 units done. Fraction = 9/36 = **1/4** of the tank

---

## 🎯 Exam Tips
- Pipes & Cisterns = Time & Work with negative workers — same LCM method
- Leak problems appear very frequently — memorize the leak formula
- Always check: is the tank filling or emptying? (Net positive or negative)
