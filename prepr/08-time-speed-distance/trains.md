# Train-based Problems 🔴

## 📌 Concept
Train problems are **relative speed + length** problems. The key difference is that a train has a **measurable length**, which must be accounted for.

---

## 📝 All Formulas

### Train Crossing a Stationary Object
| Object | Distance to Cover | Formula |
|--------|-------------------|---------|
| Pole/Person/Signal | Length of Train | T = L_train / Speed |
| Platform/Bridge | Length of Train + Length of Platform | T = (L_train + L_platform) / Speed |
| Tunnel | Length of Train + Length of Tunnel | Same as bridge |

### Train Crossing a Moving Object
| Scenario | Relative Speed | Distance |
|----------|---------------|----------|
| Another train (opposite direction) | S₁ + S₂ | L₁ + L₂ |
| Another train (same direction) | S₁ - S₂ | L₁ + L₂ |
| Man walking (opposite direction) | S_train + S_man | L_train |
| Man walking (same direction) | S_train - S_man | L_train |

### General Formula
```
Time = (Total Distance to Cover) / (Relative Speed)
```

---

## 📝 Key Properties

| Property | Description |
|----------|-------------|
| Crossing a pole | Distance = Length of train only |
| Crossing a platform | Distance = Length of train + Length of platform |
| Two trains crossing each other | Distance = Sum of both lengths |
| Convert to same units | Always use m/s with meters, or km/hr with km |

---

## ⚡ Tricks & Shortcuts

> 💡 **Trick 1 – Two Equations**: If a train crosses a pole in t₁ seconds and a platform of length L in t₂ seconds:
> - Speed = L / (t₂ - t₁) and Length of train = Speed × t₁

> 💡 **Trick 2 – Always Convert to m/s**: For train problems, meters and seconds are the natural units.

> 💡 **Trick 3 – Opposite vs Same**: Opposite → add speeds (quick crossing), Same → subtract speeds (slow crossing).

---

## 📖 Solved Examples

### Example 1: Crossing a Pole
**Q**: A 300m train at 72 kmph crosses a pole. Time?  
**Solution**: Speed = 72 × 5/18 = 20 m/s. Time = 300/20 = **15 seconds**

---

### Example 2: Crossing a Platform
**Q**: A 200m train at 54 kmph crosses a 400m bridge. Time?  
**Solution**: Speed = 15 m/s. Distance = 200+400 = 600. Time = 600/15 = **40 seconds**

---

### Example 3: Two Trains Opposite Direction
**Q**: Trains of 150m and 250m at 60 and 40 kmph cross each other. Time?  
**Solution**:  
- Relative speed = 100 kmph = 100 × 5/18 = 250/9 m/s
- Distance = 400m
- Time = 400 / (250/9) = 400 × 9/250 = **14.4 seconds**

---

### Example 4: Two Trains Same Direction
**Q**: A 200m train at 72 kmph overtakes a 300m train at 54 kmph. Time?  
**Solution**:  
- Relative speed = 18 kmph = 5 m/s
- Distance = 500m
- Time = 500/5 = **100 seconds**

---

### Example 5: Finding Length
**Q**: A train crosses a pole in 10 sec and a 200m platform in 20 sec. Find length and speed.  
**Solution**:  
- Speed = 200/(20-10) = 20 m/s = **72 kmph**
- Length = 20 × 10 = **200m**

---

## 🎯 Exam Tips
- Convert everything to m/s and meters FIRST
- For pole: only train length. For platform: both lengths. For another train: both lengths.
- These problems are very common — practice the two-equation method
