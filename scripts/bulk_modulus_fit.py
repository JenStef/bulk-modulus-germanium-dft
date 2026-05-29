#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from matplotlib.ticker import ScalarFormatter
from matplotlib.ticker import FuncFormatter

# --------------------------------
# Global plot style (publication style)
# --------------------------------
plt.rcParams.update({
    "font.size": 8,
    "axes.labelsize": 10,
    "axes.titlesize": 12,
    "legend.fontsize": 8,
    "figure.figsize": (6.5,4),
    "lines.linewidth": 2,
})

# -----------------------------
# 1. Read data
# -----------------------------
data = pd.read_csv("E_V_data.csv")

V = data["V (A)"].to_numpy()
E = data["E (Ry)"].to_numpy()

# -----------------------------
# 2. Transform variable
# t = V^(-1/3)
# -----------------------------
t = V**(-1/3)

# -----------------------------
# 3. Fit cubic polynomial in t
# E(t) = c3 t^3 + c2 t^2 + c1 t + c0
# -----------------------------
c3, c2, c1, c0 = np.polyfit(t, E, 3)

# Predicted energies at original points
E_pred = c3*t**3 + c2*t**2 + c1*t + c0

# -----------------------------
# 4. Compute R^2
# -----------------------------
ss_res = np.sum((E - E_pred)**2)
ss_tot = np.sum((E - np.mean(E))**2)
r2 = 1 - ss_res / ss_tot

# -----------------------------
# 5. Find stationary points from dE/dt = 0
# 3 c3 t^2 + 2 c2 t + c1 = 0
# -----------------------------
roots = np.roots([3*c3, 2*c2, c1])

# Keep only real roots
real_roots = roots[np.isreal(roots)].real

# Keep positive roots only, since t = V^(-1/3) must be positive
physical_roots = real_roots[real_roots > 0]

if len(physical_roots) == 0:
    raise ValueError("No positive real stationary point found.")

# -----------------------------
# 6. Choose the minimum using second derivative
# d2E/dt2 = 2 c2 + 6 c3 t
# -----------------------------
def second_derivative(tt):
    return 2*c2 + 6*c3*tt

min_candidates = [tt for tt in physical_roots if second_derivative(tt) > 0]

if len(min_candidates) == 0:
    raise ValueError("No minimum found among physical stationary points.")

t0 = min_candidates[0]

# Minimum energy
E0 = c3*t0**3 + c2*t0**2 + c1*t0 + c0

# Convert back to equilibrium volume
V0 = t0**(-3)

# -----------------------------
# 7. Conversions
# 2.17987e-18 J = 1 Ry
# 1e-10 m = 1 Ang
# Ry Ang^2 / Ang ^5 = Ry / Ang^3
# -----------------------------
Ang_m = 1 * 10**-10
Ry_J = 2.17987 * 10**-18
Pa_GPa = 1 * 10**9

J_m3 = Ry_J / (Ang_m)**3

# print(f"Pa conversion factor = {J_m3:.5e}")

# -----------------------------
# 7. Bulk modulus
# B = (t0^5 / 9) * (d2E/dt2 at t0)
# J = N * m
# Pa = N / m^2
# GPa = Pa^9
# -----------------------------
d2E_dt2_t0 = second_derivative(t0)
B = (t0**5 / 9) * d2E_dt2_t0
B_Pa = B * J_m3
B_GPa = B_Pa / Pa_GPa

# -----------------------------
# 8. Print results
# -----------------------------
print("Cubic fit in t = V^(-1/3):")
print(f"E(t) = {c0:.8e} + {c1:.8e} t + {c2:.8e} t^2 + {c3:.8e} t^3")
print(f"R^2 = {r2:.8f}")
print()
print(f"t0 = {t0:.8f}")
print(f"V0 = {V0:.8f}")
print(f"E0 = {E0:.8f}")
print(f"d2E/dt2 at t0 = {d2E_dt2_t0:.8f}")
print(f"Bulk modulus B (GPa) = {B_GPa:.8f}")
print(f"Bulk modulus B (Ry/A^3) = {B:.8f}")

# -----------------------------
# 9. Smooth curve for plotting
# -----------------------------
t_fit = np.linspace(t.min(), t.max(), 400)
E_fit = c3*t_fit**3 + c2*t_fit**2 + c1*t_fit + c0
V_fit = t_fit**(-3)

# Sort by V so the plotted curve looks correct
sort_idx = np.argsort(V_fit)
V_fit_sorted = V_fit[sort_idx]
E_fit_sorted = E_fit[sort_idx]

# -----------------------------
# 10. Plot E vs V
# -----------------------------
fig, ax = plt.subplots(figsize=(6, 4))

ax.scatter(V, E, label="Data")
ax.plot(V_fit_sorted, E_fit_sorted, label=r"Cubic fit in $t=V^{-1/3}$")
ax.scatter(V0, E0, label="Minimum")

# Axis labels and title
ax.set_xlabel("Volume (A^3)")
ax.set_ylabel("Energy (Ry)")
ax.set_title(r"E(V) fit using cubic polynomial in $t=V^{-1/3}$")

# Manual scientific notation formatting
#ax.xaxis.set_major_formatter(FormatStrFormatter('%.2e'))
#ax.yaxis.set_major_formatter(FormatStrFormatter('%.5e'))

# Optional: make axis number size larger
#ax.tick_params(axis='both', labelsize=12)

ax.legend()
plt.tight_layout()
# Optional save
plt.savefig("energy_vs_volume.png", dpi=300)
plt.show()


# In[ ]:




