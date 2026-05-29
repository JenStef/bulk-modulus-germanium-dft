# Constants
B0_GPa = 58
V0_Ang3 = 45.69 # Primitive cell V0 for Ge atom from Materials Project
delta = (1.0-(0.99**3))

# Conversion factor GPa * Ang^3 to eV
conv = 0.0062415

# Delta E = (B0 * V0 / 2) * delta^2
delta_E_eV = (B0_GPa * V0_Ang3 / 2) * (delta**2) * conv

print(f"{delta_E_eV=}")
