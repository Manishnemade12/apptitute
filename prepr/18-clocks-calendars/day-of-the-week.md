# Day of the Week — Detailed 🟢

## 📝 Method: Odd Days
1. Count total odd days from reference
2. Find day using: 0=Sun, 1=Mon, 2=Tue, 3=Wed, 4=Thu, 5=Fri, 6=Sat

### Month-wise Days Table
| Month | Days | Odd days |
|-------|------|----------|
| Jan | 31 | 3 |
| Feb | 28/29 | 0/1 |
| Mar | 31 | 3 |
| Apr | 30 | 2 |
| May | 31 | 3 |
| Jun | 30 | 2 |
| Jul | 31 | 3 |
| Aug | 31 | 3 |
| Sep | 30 | 2 |
| Oct | 31 | 3 |
| Nov | 30 | 2 |
| Dec | 31 | 3 |

### Century Odd Days: 100yr=5, 200yr=3, 300yr=1, 400yr=0

---

## 📖 Example
**Q**: What day is 15 August 1947?  
**Solution**:  
- 1600 years → 0 odd days
- 300 years → 1 odd day
- 46 years → 11 leap + 35 normal = 22+35 = 57 → 57%7 = 1 odd day
- Jan-Jul 1947: 3+0+3+2+3+2+3 = 16 → 16%7 = 2 odd days
- 15 August: 15%7 = 1 odd day
- Total = 0+1+1+2+1 = 5 → **Friday**
