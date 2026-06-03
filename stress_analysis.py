import math

# ============================================================
# ============================================================

# -------------------------------------------------------
# Custom Domain Exception
# -------------------------------------------------------
class EngineeringError(ValueError):
    """Raised when engineering values violate physical constraints."""
    pass

# -------------------------------------------------------
# Input Helpers
# -------------------------------------------------------
def get_positive_float(prompt):
    """Get a validated positive float. Catches only ValueError."""
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("  Error: Invalid input — please enter a numeric value.")
            continue
        if value <= 0:
            print("  Error: Value must be greater than zero.")
            continue
        return value

def get_positive_int(prompt, minimum=1):
    """Get a validated positive integer. Catches only ValueError."""
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("  Error: Invalid input — please enter a whole number.")
            continue
        if value < minimum:
            print(f"  Error: Value must be at least {minimum}.")
            continue
        return value

# -------------------------------------------------------
# Engineering Calculations
# -------------------------------------------------------
def calc_area(diameter_m):
    """A = pi * d^2 / 4"""
    if diameter_m <= 0:
        raise EngineeringError("Diameter must be positive.")
    return (math.pi * diameter_m ** 2) / 4

def calc_stress(load_N, area_m2):
    """sigma = P / A"""
    if area_m2 <= 0:
        raise EngineeringError("Area must be positive.")
    try:
        return load_N / area_m2
    except ZeroDivisionError:
        raise EngineeringError("Area cannot be zero.")

def calc_fos(yield_Pa, stress_Pa):
    """FoS = yield_strength / working_stress"""
    if stress_Pa <= 0:
        raise EngineeringError("Working stress must be positive.")
    try:
        return yield_Pa / stress_Pa
    except ZeroDivisionError:
        raise EngineeringError("Working stress cannot be zero.")

def calc_strain(load_N, area_m2, E_Pa):
    """epsilon = P / (A * E)"""
    if area_m2 <= 0 or E_Pa <= 0:
        raise EngineeringError("Area and Young's modulus must be positive.")
    try:
        return load_N / (area_m2 * E_Pa)
    except ZeroDivisionError:
        raise EngineeringError("Area or Young's modulus cannot be zero.")

# -------------------------------------------------------
# Analysis Functions
# -------------------------------------------------------
def single_analysis(P, d_mm, yield_MPa, E_GPa, req_FoS):
    """Full stress analysis for a single diameter."""
    try:
        d_m       = d_mm / 1000
        yield_Pa  = yield_MPa * 1e6
        E_Pa      = E_GPa * 1e9
        A         = calc_area(d_m)
        stress_Pa = calc_stress(P, A)
        stress_MPa= stress_Pa / 1e6
        fos       = calc_fos(yield_Pa, stress_Pa)
        strain    = calc_strain(P, A, E_Pa)
        status    = "SAFE ✓" if fos >= req_FoS else "FAIL ✗"

        print(f"\n{'='*50}")
        print(f"  Area             : {A:.6f} m²")
        print(f"  Stress           : {stress_MPa:.2f} MPa")
        print(f"  Factor of Safety : {fos:.2f}")
        print(f"  Strain           : {strain:.6f}")
        print(f"  Design Status    : {status}")
        print(f"{'='*50}")

    except EngineeringError as e:
        print(f"  Engineering Error: {e}")
    except ArithmeticError as e:
        print(f"  Math Error: {e}")

def loop_analysis(P, yield_MPa, E_GPa, req_FoS, d_min, d_max, d_step):
    """Stress analysis for a range of diameters."""
    if d_max <= d_min:
        raise EngineeringError("Maximum diameter must be greater than minimum.")
    if d_step <= 0:
        raise EngineeringError("Step size must be positive.")

    yield_Pa = yield_MPa * 1e6
    E_Pa     = E_GPa * 1e9

    print(f"\n{'='*72}")
    print(f"{'Dia(mm)':<12}{'Area(m²)':<14}{'Stress(MPa)':<15}{'FoS':<10}{'Strain':<14}{'Status'}")
    print(f"{'-'*72}")

    d = d_min
    while d <= d_max + 1e-9:   # 1e-9 tolerance for float comparison
        try:
            d_m        = d / 1000
            A          = calc_area(d_m)
            stress_Pa  = calc_stress(P, A)
            stress_MPa = stress_Pa / 1e6
            fos        = calc_fos(yield_Pa, stress_Pa)
            strain     = calc_strain(P, A, E_Pa)
            status     = "SAFE ✓" if fos >= req_FoS else "FAIL ✗"
            print(f"{d:<12.1f}{A:<14.6f}{stress_MPa:<15.2f}{fos:<10.2f}{strain:<14.6f}{status}")
        except EngineeringError as e:
            print(f"  Skipping d={d:.1f}mm — {e}")
        d += d_step

    print(f"{'='*72}")

# -------------------------------------------------------
# Main Program
# -------------------------------------------------------
def main():
    print("=" * 55)
    print("   EXPERIMENT 01: Stress Analysis Tool")
    print("   AI in Mechanical Engineering — ONT406")
    print("   Sharda University")
    print("=" * 55)

    while True:
        print("\n--- MENU ---")
        print("1. Single Rod Analysis")
        print("2. Multi-Diameter Loop Analysis")
        print("3. Exit")

        choice = input("\nEnter your choice (1/2/3): ").strip()

        if choice == '1':
            print("\n--- Enter Rod Properties ---")
            P         = get_positive_float("  Applied Load P (N)        : ")
            d_mm      = get_positive_float("  Diameter (mm)             : ")
            yield_MPa = get_positive_float("  Yield Strength (MPa)      : ")
            E_GPa     = get_positive_float("  Young's Modulus (GPa)     : ")
            req_FoS   = get_positive_float("  Required Factor of Safety : ")
            single_analysis(P, d_mm, yield_MPa, E_GPa, req_FoS)

        elif choice == '2':
            print("\n--- Enter Analysis Parameters ---")
            try:
                P         = get_positive_float("  Applied Load P (N)        : ")
                yield_MPa = get_positive_float("  Yield Strength (MPa)      : ")
                E_GPa     = get_positive_float("  Young's Modulus (GPa)     : ")
                req_FoS   = get_positive_float("  Required Factor of Safety : ")
                d_min     = get_positive_float("  Minimum Diameter (mm)     : ")
                d_max     = get_positive_float("  Maximum Diameter (mm)     : ")
                d_step    = get_positive_float("  Step Size (mm)            : ")
                loop_analysis(P, yield_MPa, E_GPa, req_FoS, d_min, d_max, d_step)
            except EngineeringError as e:
                print(f"  Engineering Error: {e}")

        elif choice == '3':
            print("\nExiting. Goodbye!")
            break

        else:
            print("  Error: Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n  Program interrupted by user. Goodbye!")
