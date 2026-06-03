# Experiment 01 — Code Explanation
# Core Python Concepts for Stress Analysis

---

## What is this program doing?

This program simulates what a **Mechanical Engineer calculates on paper**
but automates it using Python. Given a rod under load, it calculates:
- How much stress is acting on it
- Whether it is safe or will fail
- How much it deforms (strain)
- And repeats this for multiple rod sizes using a loop

---

## Line by Line Explanation

---

### Line 1
```python
import math
```
**What it does:**
`math` is a built-in Python library that gives you access to
mathematical constants and functions like π (pi), square root, etc.

**Why we need it:**
The formula for area uses π: A = π × d² / 4
Without `import math`, Python doesn't know what π is.

**Real life analogy:**
Like picking up a calculator before solving a math problem.

---

### Lines 5-10 (Given Data)
```python
P = 10000           # Applied Load (N)
d = 0.02            # Diameter (m)
yield_strength = 250e6   # Yield Strength (Pa)
E = 200e9           # Young's Modulus (Pa)
required_FoS = 2    # Minimum FoS
```
**What it does:**
Stores the known engineering values as variables.

**Important notation:**
- `250e6` means 250 × 10⁶ = 250,000,000 Pa = 250 MPa
- `200e9` means 200 × 10⁹ = 200,000,000,000 Pa = 200 GPa
- This is called **scientific notation** — much cleaner than writing all zeros

**Why convert MPa to Pa?**
All formulas in SI system use Pascals (Pa). If you mix units,
you get wrong answers. Always convert to base SI units first.

---

### Lines 13-14 (Area Calculation)
```python
A = (math.pi * d**2) / 4
print(f"Area: {A:.6f} m²")
```
**What it does:**
Calculates the cross-sectional area of the circular rod.

**Formula:** A = π × d² / 4

**Breaking it down:**
- `math.pi` = 3.14159...
- `d**2` means d² (d squared) — `**` is the power operator in Python
- The result is divided by 4

**The f-string:**
`f"Area: {A:.6f} m²"` means:
- `f"..."` = formatted string (allows variables inside)
- `{A:.6f}` = print variable A with 6 decimal places
- `.6f` = 6 decimal places, float format

---

### Lines 17-19 (Stress Calculation)
```python
stress = P / A
stress_MPa = stress / 1e6
print(f"Stress: {stress_MPa:.2f} MPa")
```
**What it does:**
Applies the stress formula σ = P / A

**Why divide by 1e6?**
The answer comes out in Pascals (Pa).
Engineers prefer MPa for readability.
1 MPa = 1,000,000 Pa = 1e6 Pa
So dividing by 1e6 converts Pa → MPa.

---

### Lines 22-23 (Factor of Safety)
```python
FoS = yield_strength / stress
print(f"Factor of Safety: {FoS:.2f}")
```
**What it does:**
FoS tells us how many times stronger the material is
compared to the actual stress on it.

**Example:**
If FoS = 7.85, the material can handle 7.85× more stress
before it starts to permanently deform (yield).

**Engineering rule:**
- FoS = 1 → Right at the limit (dangerous)
- FoS = 2 → Twice as strong as needed (safe)
- FoS > 2 → Very safe design

---

### Lines 26-31 (Safety Check — if-else)
```python
if FoS >= required_FoS:
    status = "SAFE"
else:
    status = "FAIL"
print(f"Design Status: {status}")
```
**What it does:**
Decision making — exactly like an engineer deciding
whether to approve or reject a design.

**How if-else works:**
```
if (condition is TRUE):
    do this
else:
    do that instead
```

**The `>=` operator:**
Means "greater than or equal to".
If FoS is 7.85 and required is 2, then 7.85 >= 2 is TRUE → SAFE.

---

### Lines 34-39 (Function for Strain)
```python
def calc_strain(P, A, E):
    """Calculate strain: ε = P / (A × E)"""
    return P / (A * E)

strain = calc_strain(P, A, E)
print(f"Strain: {strain:.6f}")
```
**What it does:**
Defines a reusable function to calculate strain.

**What is a function?**
A named block of code that:
- Takes inputs (called parameters): P, A, E
- Does a calculation
- Returns the result

**Why use functions?**
If you need to calculate strain 100 times with different values,
you just call `calc_strain(...)` each time instead of rewriting
the formula every time.

**The docstring:**
`"""Calculate strain: ε = P / (A × E)"""`
This is documentation inside the function — good practice!

**What is strain physically?**
Strain is how much the material stretches per unit length.
Strain = 0.000159 means the rod stretches 0.0159% of its length.

---

### Lines 42-52 (For Loop — Multiple Diameters)
```python
for d_mm in [10, 15, 20, 25, 30]:
    d_m = d_mm / 1000
    area = (math.pi * d_m**2) / 4
    sigma = P / area
    sigma_MPa = sigma / 1e6
    fos = yield_strength / sigma
    result = "SAFE" if fos >= required_FoS else "FAIL"
    print(f"{d_mm:<12}{area:<14.6f}{sigma_MPa:<15.2f}{fos:<10.2f}{result}")
```
**What it does:**
Repeats the entire stress calculation for 5 different diameters
automatically — without writing the code 5 times.

**How the for loop works:**
```
for each value in the list [10, 15, 20, 25, 30]:
    run all the indented code below
    using that value as d_mm
```

The loop runs 5 times total — once for d_mm=10, once for d_mm=15, etc.

**Unit conversion inside loop:**
`d_m = d_mm / 1000` converts mm → m (10mm → 0.01m)
Always needed because formulas use meters.

**The inline if-else (ternary operator):**
`result = "SAFE" if fos >= required_FoS else "FAIL"`
This is a shorter way of writing if-else on one line.

**The print formatting:**
`{d_mm:<12}` means: print d_mm, left-aligned, in 12 character width.
This makes the output appear as a neat table.

---

## Key Engineering Insights

**Why does stress DECREASE as diameter increases?**
Larger diameter → larger area → same force spread over more area
→ less stress per unit area. This is why thick rods are stronger.

**Why does FoS INCREASE as diameter increases?**
More area → less stress → further from yield point → higher safety margin.

**Real world application:**
This exact calculation is done when designing:
- Bolts and fasteners
- Structural columns
- Pressure vessel walls
- Bridge cables

---

## Common Mistakes to Avoid

| Mistake | Wrong | Correct |
|---|---|---|
| Unit mismatch | d = 20 (mm) | d = 0.02 (m) |
| Forgetting π | A = d**2 / 4 | A = math.pi * d**2 / 4 |
| Wrong power | d*2 | d**2 |
| Not importing | math.pi without import | import math first |
