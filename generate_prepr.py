import os
import re

base_dir = r"c:\Users\manis\Desktop\opensource\apptitute\prepr"

topics_data = [
    {
        "id": "1",
        "name": "Number System",
        "priority": "🔴",
        "subtopics": {
            "divisibility-rules": {
                "title": "Divisibility Rules",
                "formulas": "- 2: Last digit is even\n- 3: Sum of digits is divisible by 3\n- 4: Last two digits divisible by 4\n- 5: Last digit is 0 or 5\n- 8: Last 3 digits divisible by 8\n- 9: Sum of digits is divisible by 9\n- 11: Difference between sum of odd placed digits and even placed digits is 0 or multiple of 11.",
                "tricks": "To check divisibility by composite numbers (like 12), check divisibility for co-prime factors (3 and 4).",
                "examples": "**Q**: Is 14532 divisible by 4?\n**Ans**: Yes, because last 2 digits '32' is divisible by 4.\n\n**Q**: Is 2728 divisible by 11?\n**Ans**: (2+2) - (7+8) = 4 - 15 = -11. Divisible by 11."
            },
            "lcm-hcf": {
                "title": "LCM & HCF",
                "formulas": "- Product of two numbers = LCM * HCF\n- LCM of fractions = LCM(Numerators) / HCF(Denominators)\n- HCF of fractions = HCF(Numerators) / LCM(Denominators)",
                "tricks": "- To find largest number that divides A, B, C leaving remainders r1, r2, r3: Find HCF of (A-r1, B-r2, C-r3).\n- To find smallest number divisible by A, B, C leaving remainder r in each case: Find LCM(A,B,C) + r.",
                "examples": "**Q**: Find LCM of 12 and 15.\n**Ans**: 60.\n\n**Q**: Two numbers are in ratio 3:4 and their HCF is 4. Find LCM.\n**Ans**: Numbers are 12 and 16. LCM = 48."
            },
            "prime-numbers": {
                "title": "Prime Numbers, Factors, Multiples",
                "formulas": "- Prime number has exactly two factors: 1 and itself.\n- Co-primes have HCF = 1.",
                "tricks": "To check if N is prime, find integer k > √N. Check divisibility of N by all prime numbers <= k.",
                "examples": "**Q**: Is 137 prime?\n**Ans**: √137 < 12. Primes <= 11 are 2, 3, 5, 7, 11. 137 is not divisible by any of these. So, yes."
            },
            "remainder-theorem": {
                "title": "Remainder Theorem Basics",
                "formulas": "- Dividend = (Divisor × Quotient) + Remainder\n- (a * b) % n = [(a % n) * (b % n)] % n\n- Fermat's Little Theorem: a^(p-1) ≡ 1 (mod p) where p is prime.",
                "tricks": "Use negative remainders to simplify calculations. e.g., 34 % 7 can be written as -1.",
                "examples": "**Q**: Find remainder when 15 x 17 is divided by 7.\n**Ans**: (15%7) x (17%7) = 1 x 3 = 3."
            },
            "unit-digit": {
                "title": "Unit Digit & Last Digit",
                "formulas": "- Cyclicity of 2, 3, 7, 8 is 4.\n- Cyclicity of 4, 9 is 2.\n- Cyclicity of 0, 1, 5, 6 is 1.",
                "tricks": "For x^y, find y % 4. If y%4 == 0, use power 4.",
                "examples": "**Q**: Find unit digit of 3^45.\n**Ans**: 45 % 4 = 1. 3^1 = 3."
            },
             "factors": {
                "title": "Number of Factors",
                "formulas": "If N = p^a * q^b * r^c..., then Number of factors = (a+1)(b+1)(c+1)...",
                "tricks": "To find sum of factors: [ (p^(a+1)-1)/(p-1) ] * [ (q^(b+1)-1)/(q-1) ] ...",
                "examples": "**Q**: Number of factors of 100?\n**Ans**: 100 = 2^2 * 5^2. Factors = (2+1)*(2+1) = 9."
            },
             "base-conversion": {
                "title": "Base Conversion",
                "formulas": "Decimal to Binary: Keep dividing by 2 and note remainders bottom to top.\nBinary to Decimal: Multiply bits by powers of 2 from right to left.",
                "tricks": "Memorize powers of 2 up to 1024 for quick conversion.",
                "examples": "**Q**: Convert 13 to binary.\n**Ans**: 1101."
            }
        }
    },
    {
        "id": "2",
        "name": "Percentage",
        "priority": "🔴",
        "subtopics": {
            "basic-conversion": {
                "title": "Basic Percentage Conversion",
                "formulas": "Fraction to %: Multiply by 100\n% to Fraction: Divide by 100",
                "tricks": "Memorize fraction equivalents: 1/2=50%, 1/3=33.33%, 1/4=25%, 1/5=20%, 1/6=16.66%, 1/7=14.28%, 1/8=12.5%, 1/9=11.11%, 1/11=9.09%.",
                "examples": "**Q**: What is 16.66% of 36?\n**Ans**: 1/6 * 36 = 6."
            },
            "increase-decrease": {
                "title": "Percentage Increase/Decrease",
                "formulas": "Percentage change = (Difference / Initial Value) * 100",
                "tricks": "If A is x% more than B, then B is (x/(100+x))*100 % less than A.",
                "examples": "**Q**: If price increases by 25%, by what % should consumption decrease to keep expenditure same?\n**Ans**: (25/125)*100 = 20%."
            },
             "successive-change": {
                "title": "Successive Percentage Change",
                "formulas": "Net % change = x + y + (xy/100)",
                "tricks": "If both are increase, x and y are positive. If one is decrease, make it negative.",
                "examples": "**Q**: Salary increased by 10% then decreased by 10%.\n**Ans**: 10 - 10 - (10*10/100) = -1% (1% decrease)."
            },
            "word-problems": {
                "title": "Word Problems",
                "formulas": "Population after n years = P * (1 + R/100)^n\nMarks: Pass mark = (Marks scored + Marks failed by) OR (Marks scored - Marks above passing)",
                "tricks": "Use 100 as initial value for easy calculation.",
                "examples": "**Q**: Candidate gets 20% marks and fails by 30 marks. Another gets 32% and passes by 42 marks. Find max marks.\n**Ans**: Difference = 12% = 72 marks. Max marks = (72/12)*100 = 600."
            }
        }
    },
    {
        "id": "3",
        "name": "Ratio and Proportion",
        "priority": "🔴",
        "subtopics": {
            "basic-ratio": {
                "title": "Basic Ratio Simplification",
                "formulas": "A ratio a:b is a fraction a/b.",
                "tricks": "If A:B = m:n and B:C = p:q, then A:B:C = (m*p) : (n*p) : (n*q).",
                "examples": "**Q**: A:B=2:3, B:C=4:5. Find A:B:C.\n**Ans**: 8:12:15."
            },
            "dividing-number": {
                "title": "Dividing a number in given ratio",
                "formulas": "If sum S is divided into a:b, then parts are S * (a/(a+b)) and S * (b/(a+b)).",
                "tricks": "Find the value of 1 'unit' by dividing total sum by total ratio parts.",
                "examples": "**Q**: Divide 1000 in ratio 3:2.\n**Ans**: Total parts = 5. 1 part = 200. Parts are 600 and 400."
            },
            "proportion": {
                "title": "Proportion",
                "formulas": "If a:b :: c:d, then a*d = b*c (Product of extremes = Product of means).\nThird proportion of a, b is b^2/a.\nMean proportion of a, b is √(a*b).",
                "tricks": "Direct variation: a1/b1 = a2/b2. Inverse variation: a1*b1 = a2*b2.",
                "examples": "**Q**: Find fourth proportional to 4, 9, 12.\n**Ans**: 4*x = 9*12 -> x = 27."
            }
        }
    },
    {
        "id": "4",
        "name": "Average",
        "priority": "🔴",
        "subtopics": {
            "simple-average": {
                "title": "Simple Average",
                "formulas": "Average = Sum of observations / Number of observations",
                "tricks": "If every observation is increased by x, the new average also increases by x.",
                "examples": "**Q**: Average of first 5 natural numbers?\n**Ans**: (1+2+3+4+5)/5 = 3. Trick: For AP, Average = (First + Last)/2 = (1+5)/2 = 3."
            },
            "weighted-average": {
                "title": "Weighted Average",
                "formulas": "Weighted Avg = (n1*A1 + n2*A2) / (n1 + n2)",
                "tricks": "Can use mixture & alligation method to solve quickly.",
                "examples": "**Q**: Class A has 30 students avg 40. Class B has 20 students avg 50.\n**Ans**: (30*40 + 20*50) / 50 = 2200/50 = 44."
            },
             "average-speed": {
                "title": "Average Speed Problems",
                "formulas": "Average Speed = Total Distance / Total Time\nIf distance is same (A to B and B to A with speeds x and y): Avg Speed = 2xy / (x+y)",
                "tricks": "Never average the speeds directly if time taken is different.",
                "examples": "**Q**: Go at 40 kmph, return at 60 kmph.\n**Ans**: Avg speed = 2*40*60 / (40+60) = 4800/100 = 48 kmph."
            },
            "change-in-average": {
                "title": "Change in Average",
                "formulas": "New Value = Old Average + Number of obs * Change in average",
                "tricks": "If a person is replaced and avg increases by x, New person = Old person + (n * x).",
                "examples": "**Q**: Avg age of 10 students is 15. Teacher included, avg becomes 16.\n**Ans**: Teacher's age = 16 + (10 * 1) = 26."
            }
        }
    },
    {
        "id": "5",
        "name": "Profit, Loss and Discount",
        "priority": "🔴",
        "subtopics": {
            "basic-profit-loss": {
                "title": "Basic Profit/Loss %",
                "formulas": "Profit = SP - CP\nLoss = CP - SP\nProfit/Loss % = (Profit or Loss / CP) * 100",
                "tricks": "Always calculate % on CP unless stated otherwise.",
                "examples": "**Q**: CP=100, SP=120. Profit %?\n**Ans**: (20/100)*100 = 20%."
            },
            "cp-sp-relations": {
                "title": "CP/SP Relations",
                "formulas": "SP = CP * (100 + Profit%)/100\nSP = CP * (100 - Loss%)/100",
                "tricks": "If SP of x articles = CP of y articles, Profit% = (y-x)/x * 100.",
                "examples": "**Q**: CP of 10 pens = SP of 8 pens. Profit%?\n**Ans**: (10-8)/8 * 100 = 25%."
            },
             "successive-discount": {
                "title": "Successive Discount",
                "formulas": "Net discount for x% and y% = x + y - (xy/100)",
                "tricks": "Calculate on 100. 100 -> -x% -> -y%.",
                "examples": "**Q**: Two successive discounts of 20% and 10%.\n**Ans**: 20 + 10 - 2 = 28%."
            },
            "marked-price": {
                "title": "Marked Price Problems",
                "formulas": "SP = MP - Discount\nDiscount% = (Discount / MP) * 100\nMP/CP = (100 + Profit%) / (100 - Discount%)",
                "tricks": "Use the MP/CP ratio formula for lightning fast answers.",
                "examples": "**Q**: Shopkeeper gives 10% discount and earns 20% profit. If CP is 300, find MP.\n**Ans**: MP/300 = 120/90 = 4/3. MP = 400."
            },
             "dishonest-dealer": {
                "title": "Dishonest Dealer",
                "formulas": "Profit % = (Error / (True Value - Error)) * 100",
                "tricks": "Think of it as: Goods given vs Goods paid for.",
                "examples": "**Q**: Dealer sells at CP but uses 900g weight instead of 1kg.\n**Ans**: Profit % = (100 / 900) * 100 = 11.11%."
            }
        }
    },
    {
        "id": "6",
        "name": "Simple and Compound Interest",
        "priority": "🔴",
        "subtopics": {
            "si-basics": {
                "title": "SI Formula-based",
                "formulas": "SI = (P * R * T) / 100\nAmount = P + SI = P * (1 + RT/100)",
                "tricks": "SI is same for every year.",
                "examples": "**Q**: P=1000, R=10%, T=2. SI?\n**Ans**: (1000*10*2)/100 = 200."
            },
            "ci-basics": {
                "title": "CI Formula-based",
                "formulas": "Amount = P * (1 + R/100)^T\nCI = Amount - P",
                "tricks": "Use effective rate % (Successive percentage). For 2 years at 10%, effective CI% = 10+10+(10*10)/100 = 21%.",
                "examples": "**Q**: P=1000, R=10%, T=2. CI?\n**Ans**: 21% of 1000 = 210."
            },
            "si-ci-difference": {
                "title": "SI vs CI Difference",
                "formulas": "2 years diff = P * (R/100)^2\n3 years diff = P * (R/100)^2 * (3 + R/100)",
                "tricks": "Memorize these formulas, they appear in 90% tests.",
                "examples": "**Q**: Diff b/w CI and SI on 5000 at 10% for 2 yrs.\n**Ans**: 5000 * (10/100)^2 = 50."
            }
        }
    },
     {
        "id": "7",
        "name": "Time and Work",
        "priority": "🔴",
        "subtopics": {
            "work-efficiency": {
                "title": "Basic Work-Efficiency",
                "formulas": "Work = Time * Efficiency",
                "tricks": "Always assume Total Work = LCM of given days.",
                "examples": "**Q**: A takes 10 days, B takes 15 days. Together?\n**Ans**: Total Work=30. A's eff=3, B's eff=2. Time = 30/(3+2) = 6 days."
            },
             "combined-work": {
                "title": "Combined Work",
                "formulas": "1/A + 1/B = 1/T",
                "tricks": "For two people: (A*B)/(A+B) days.",
                "examples": "**Q**: A=20, B=30. Together?\n**Ans**: (20*30)/(50) = 12 days."
            },
            "pipes-cisterns": {
                "title": "Pipes and Cisterns",
                "formulas": "Same as Time & Work. Outlet pipes have negative efficiency.",
                "tricks": "Take negative efficiency for leaks.",
                "examples": "**Q**: Pipe A fills in 10hr. Leak empties in 15hr. Total time?\n**Ans**: Work=30. A eff=+3, Leak=-2. Net eff=1. Time=30/1 = 30hrs."
            },
             "work-equivalence": {
                "title": "Work Equivalence",
                "formulas": "(M1 * D1 * H1) / W1 = (M2 * D2 * H2) / W2",
                "tricks": "MDH / W rule.",
                "examples": "**Q**: 10 men do a work in 20 days. How many men for 10 days?\n**Ans**: 10*20 = x*10 => x = 20 men."
            }
        }
    },
    {
        "id": "8",
        "name": "Time, Speed & Distance",
        "priority": "🔴",
        "subtopics": {
             "basic-sdt": {
                "title": "Basic Speed Distance Time",
                "formulas": "Distance = Speed * Time",
                "tricks": "kmph to m/s: Multiply by 5/18.\nm/s to kmph: Multiply by 18/5.",
                "examples": "**Q**: Convert 72 kmph to m/s.\n**Ans**: 72 * 5/18 = 20 m/s."
             },
             "relative-speed": {
                "title": "Relative Speed",
                "formulas": "Opposite direction: Add speeds (S1 + S2)\nSame direction: Subtract speeds (S1 - S2)",
                "tricks": "Used when two bodies are in motion.",
                "examples": "**Q**: Two trains going towards each other at 50 and 40 kmph. Relative speed?\n**Ans**: 90 kmph."
             },
             "trains": {
                "title": "Train-based Problems",
                "formulas": "Time = (Length of Train + Length of Platform) / Speed\nFor standing man/pole, Length of Platform = 0.",
                "tricks": "Convert all units to m/s and meters before calculating.",
                "examples": "**Q**: Train 200m long at 72kmph crosses a 100m bridge. Time?\n**Ans**: Speed=20m/s. Distance=300m. Time = 300/20 = 15s."
             },
             "boats-streams": {
                "title": "Boats and Streams",
                "formulas": "Downstream Speed (D) = Boat(u) + Stream(v)\nUpstream Speed (U) = Boat(u) - Stream(v)\nu = (D+U)/2, v = (D-U)/2",
                "tricks": "D is always greater than U.",
                "examples": "**Q**: Boat speed 10, Stream speed 2. Downstream time for 36km?\n**Ans**: D = 12 kmph. Time = 36/12 = 3 hrs."
             }
        }
    }
]

# Provide fallback for remaining topics so we cover all 19
other_topics = [
    ("9", "Ages", "🟡", ["Present age problems", "Ratio based age problems"]),
    ("10", "Mixtures & Alligation", "🟡", ["Basic alligation rule", "Mixing quantities"]),
    ("11", "Permutation & Combination", "🟡", ["Basic concepts", "Word arrangement"]),
    ("12", "Probability", "🟡", ["Basic probability", "Conditional probability"]),
    ("13", "Simplification & Approximation", "🔴", ["BODMAS", "Surds & Indices"]),
    ("14", "Algebra", "🟢", ["Linear equations", "Quadratic equations"]),
    ("15", "Geometry & Mensuration", "🟡", ["Area & perimeter", "Volume & surface area"]),
    ("16", "Data Interpretation", "🔴", ["Table DI", "Bar Pie chart"]),
    ("17", "Series & Progressions", "🟡", ["Number series", "AP and GP"]),
    ("18", "Clocks & Calendars", "🟢", ["Angle between hands", "Day of the week"]),
    ("19", "Logarithm", "🟢", ["Basic log rules"])
]

# Ensure the base directory exists
os.makedirs(base_dir, exist_ok=True)

# Generate detailed topics
for topic in topics_data:
    folder_name = f"{topic['id'].zfill(2)}-{re.sub(r'[^a-zA-Z0-9]', '-', topic['name'].lower())}"
    folder_path = os.path.join(base_dir, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    
    quick_review_content = f"# Quick Review: {topic['name']} {topic['priority']}\n\n"
    
    for sub_id, sub_data in topic['subtopics'].items():
        file_path = os.path.join(folder_path, f"{sub_id}.md")
        
        # Subtopic file content
        content = f"# {sub_data['title']}\n\n"
        content += f"## Formulas\n{sub_data['formulas']}\n\n"
        content += f"## Tricks & Shortcuts\n> 💡 {sub_data['tricks']}\n\n"
        content += f"## Examples\n{sub_data['examples']}\n"
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        # Append to quick review
        quick_review_content += f"### {sub_data['title']}\n**Formulas**:\n{sub_data['formulas']}\n**Trick**: {sub_data['tricks']}\n\n---\n"
        
    # Write quick review file
    qr_path = os.path.join(folder_path, "quick-review.md")
    with open(qr_path, 'w', encoding='utf-8') as f:
        f.write(quick_review_content)

# Generate generic/fallback for remaining topics
for (t_id, t_name, priority, subtopics) in other_topics:
    folder_name = f"{t_id.zfill(2)}-{re.sub(r'[^a-zA-Z0-9]', '-', t_name.lower())}"
    folder_path = os.path.join(base_dir, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    
    quick_review_content = f"# Quick Review: {t_name} {priority}\n\n"
    
    for sub in subtopics:
        sub_id = re.sub(r'[^a-zA-Z0-9]', '-', sub.lower())
        file_path = os.path.join(folder_path, f"{sub_id}.md")
        
        content = f"# {sub}\n\n"
        content += f"## Formulas\n- Standard formulas for {sub} (To be updated)\n\n"
        content += f"## Tricks & Shortcuts\n> 💡 Standard trick for {sub} (To be updated)\n\n"
        content += f"## Examples\n**Q**: Example question for {sub}\n**Ans**: Example answer.\n"
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        quick_review_content += f"### {sub}\n**Formulas**: Standard formulas (To be updated)\n**Trick**: (To be updated)\n\n---\n"
        
    qr_path = os.path.join(folder_path, "quick-review.md")
    with open(qr_path, 'w', encoding='utf-8') as f:
        f.write(quick_review_content)

print(f"Successfully generated all preparation folders and files at {base_dir}!")
