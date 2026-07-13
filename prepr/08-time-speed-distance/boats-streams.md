# Boats and Streams 🔴

## 📌 Concept
A boat moving in **still water** has speed **u**. A stream has speed **v**. The effective speed of the boat changes depending on direction.

---

## 📝 All Formulas

### Core Speeds
```
Downstream Speed (D) = u + v    (boat goes WITH the stream)
Upstream Speed (U)   = u - v    (boat goes AGAINST the stream)
```

### Finding Boat and Stream Speed
```
Speed of boat in still water (u) = (D + U) / 2
Speed of stream (v)              = (D - U) / 2
```

### Time for a Journey
```
Time Downstream = Distance / (u + v)
Time Upstream   = Distance / (u - v)
```

### Round Trip (Same Distance d, both ways)
```
Total Time = d/(u+v) + d/(u-v) = 2ud / (u² - v²)
Average Speed = (u² - v²) / u
```

---

## 📝 Key Properties

| Property | Description |
|----------|-------------|
| Downstream is always faster | D > U always (since v > 0) |
| In still water, v = 0 | D = U = u |
| If u < v | Boat cannot go upstream (gets carried away) |
| Downstream time < Upstream time | For same distance |

---

## 📝 Special Problem Types

### Type 1: Man Drops Something in River
- Object floats at stream speed v
- Man continues for time t, then turns back
- Time to catch object: Distance between them / Relative speed approaching

### Type 2: Same Distance Up and Down
```
If upstream time = T₁, downstream time = T₂
u/v = (T₁ + T₂) / (T₁ - T₂)
```

---

## ⚡ Tricks & Shortcuts

> 💡 **Trick 1 – D and U**: Downstream = ADD, Upstream = SUBTRACT. Simple!

> 💡 **Trick 2 – Find u and v from D and U**: u = (D+U)/2, v = (D-U)/2. Average and half-difference.

> 💡 **Trick 3 – Time Ratio**: If speed downstream:upstream = a:b, then time downstream:upstream = b:a (inverse).

> 💡 **Trick 4 – Round Trip Average Speed**: Not 2uv/(u+v)! It's (u²-v²)/u for boats (because D and U are not u and v directly, they include stream).
> - Actually for round trip same distance: Avg = 2DU/(D+U) where D=u+v, U=u-v → = 2(u+v)(u-v)/2u = (u²-v²)/u

---

## 📖 Solved Examples

### Example 1: Basic
**Q**: Boat speed = 10 kmph, stream = 2 kmph. Time to go 36 km downstream?  
**Solution**: D = 10+2 = 12. Time = 36/12 = **3 hrs**

---

### Example 2: Finding Speeds
**Q**: Downstream speed = 18 kmph, upstream = 12 kmph. Find boat and stream speed.  
**Solution**:  
- u = (18+12)/2 = **15 kmph**
- v = (18-12)/2 = **3 kmph**

---

### Example 3: Round Trip
**Q**: Boat speed = 8 kmph in still water, stream = 2 kmph. Time for 30 km round trip?  
**Solution**:  
- D = 10, U = 6
- Time = 30/10 + 30/6 = 3 + 5 = **8 hrs**

---

### Example 4: Finding Stream Speed
**Q**: A man rows 48 km upstream in 8 hrs and 48 km downstream in 6 hrs. Find stream speed.  
**Solution**:  
- U = 48/8 = 6 kmph, D = 48/6 = 8 kmph
- v = (8-6)/2 = **1 kmph**

---

### Example 5: Time Ratio
**Q**: Ratio of upstream to downstream speed is 2:3. If stream speed is 3 kmph, find boat speed.  
**Solution**:  
- U:D = 2:3. Let U = 2k, D = 3k
- v = (D-U)/2 = k/2 = 3 → k = 6
- u = (D+U)/2 = 5k/2 = 15 → **u = 15 kmph**

---

## 🎯 Exam Tips
- Always identify downstream (with stream) and upstream (against stream)
- The u and v extraction from D and U is the most useful calculation
- Round trip problems: calculate each leg separately, then add times
