# Experiment 01: Core Python Concepts for Stress Analysis

---

## Aim
To implement control structures and modular functions in Python for fundamental mechanical engineering calculations such as stress analysis, Factor of Safety (FoS), and deformation evaluation.

---

## Concepts Covered
- Variables and data types for engineering quantities
- Control structures (if-else) for safety checks
- For loops for multiple design evaluations
- Functions for reusable engineering calculations
- Stress, Factor of Safety, Strain formulas

---

## Formulas Used

| Formula | Description |
|---|---|
| σ = P / A | Stress |
| FoS = σ_yield / σ_working | Factor of Safety |
| ε = P / (A × E) | Strain |
| A = π × d² / 4 | Cross-sectional Area |

---

## Software Required

| Software | Purpose | Download Link |
|---|---|---|
| Python 3.x | Programming language | https://www.python.org/downloads/ |
| VS Code | Code editor | https://code.visualstudio.com/ |
| Git | Version control | https://git-scm.com/ |

---

## Installation Steps

### Step 1: Install Python
```
1. Go to https://www.python.org/downloads/
2. Download Python 3.11 or above
3. During installation CHECK "Add Python to PATH"
4. Click Install Now
5. Verify: open terminal and type: python --version
```

### Step 2: Install VS Code
```
1. Go to https://code.visualstudio.com/
2. Download and install
3. Open VS Code → Extensions → Install "Python" extension
```

### Step 3: Install Required Libraries
Open terminal or command prompt and run:
```bash
pip install math
```
Note: `math` is a built-in Python library — no installation needed!

---

## How to Run

```bash
# Clone the repository
git clone https://github.com/2025514764himanshu-sudo1128/Core-Python-Stress-Analysis.git

# Navigate into folder
cd Core-Python-Stress-Analysis

# Run the program
python stress_analysis.py
```

---

## Expected Output
```
Area: 0.000314 m²
Stress: 31.83 MPa
Factor of Safety: 7.85
Design Status: SAFE
Strain: 0.000159

--- Stress for Multiple Diameters ---
Dia(mm)     Area(m²)      Stress(MPa)    FoS       Status
10          0.000079      127.32         1.96      FAIL
15          0.000177      56.59          4.42      SAFE
20          0.000314      31.83          7.85      SAFE
25          0.000491      20.37          12.27     SAFE
30          0.000707      14.15          17.68     SAFE
```

---

## Author
**Himanshu Kumar** (2025514764)
Department of Electrical, Electronics and Communication Engineering
Sharda University, Greater Noida
