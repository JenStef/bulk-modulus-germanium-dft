# Bulk Modulus of Germanium Using Density Functional Theory

## Overview

This project investigates the structural and elastic properties of germanium using Density Functional Theory (DFT) calculations performed with Quantum ESPRESSO. The objective was to determine the equilibirum volume and bulk modulus of germanium by generating an energy-volume relationship and fitting the resulting data using an equation-of-state (EOS) approach.

This project demonstrates a complete computational materials workflow including convergence testing, structural relaxation, equation-of-state calculations, scientific data analysis, and visualization using Python.

===

## Objectives

- Perform convergence testing for plane-wave cutoff energy and k-point sampling.
- Obtain a fully relaed germanium crystal structure using DFT.
- Generate an energy-volume dataset through a series of compressed and expanded unit cells.
- Fit the energy-volume relationship using a cubic polynomial in t = V^(-1/3).
- Determine the equilibrium volume and bulk modulus.
- Compare computational results with literature values.

===

## Software and Tools

- Quantum ESPRESSO
- Python
- NumPy
- SciPy
- Pandas
- Matplotlib
- Linux
- Slurm Workload Manager

===

## Computational Workflow

### 1.  Convergence Testing

Convergence testing was performed to determine appropriate values for:

- Plane-wave cutoff energy (ecutwfc)
- K-point sampling density

Energy convergence criteria were estimated using the expected energy change associated with a 1% volume pertubation at literature values for the bulk modulus of germanium.

### 2. Variable-Cell Relaxation

A variable-cell relaxation ('vc-relax') calculation was performed to determine the equilibrium crystal structure and lattice parameters of germanium.

### 3. Equation of State Calculations

A series of calculations were performed for compressed and expanded unit cell volumes near equilibrium.

The resulting total energies and volumes were extracted and used to construct the energy-volume relationship.

### 4. EOS Analysis

The energy-volume data were fit using a cubic polynomial in:

t = V^(-1/3)

The fitted curve was used to determine:

- Equilibrium volume (V_0)
- Equilibrium Energy (E_0)
- Bulk Modulus (B)

### 5. Visualization

Python scripts were used to generate publication-style figures and analyze the fitted results.

===

## Repository Structure

bulk-modulus-ge-dft/
├── README.md
├── .gitignore
├── environment.yml
│
├── data/
│    ├── ge_convergence_results.csv
│    └── ge_energy_volume.csv
│
├── figures/
│    └── energy_vs_volume.png
│
├── hpc/
│    ├── submmit_convergence.sh
│    ├── submit_eos.sh
│    └── submit_vcrelax.sh
│
├── pseudos/
│    └── ge_pbe_v1.4.uspp.F.UPF
│
├── qe-inputs/
│    ├── convergence/
│    ├── eos/
│    └── vc-relax/
│
├── scripts/
│    ├── bulk_modulus_fit.py
│    └── convergence_energy_tolerance.py
│
└── report/
      └── Ge_BulkMod_Report.pdf

===

## Key Results

|      Property      |    Value   |
|--------------------|------------|
| Equilibrium Volume |  47.75 A^3 |
| Bulk Modulus       |     59 GPa |
| Equilibrium Energy | -427.31 Ry |

===

## Figure

### Energy vs. Volume Relationship

The figure below shows the calculated DFT energy-volume data and the fitted equation-of-state curve used to determine the equilibrium volume and bulk modulus.

![Energy vs. Volume] (figures/energy_vs_volume.png)

===

## Skills Demonstrated

- Density Functional Theory (DFT)
- Quantum ESPRESSO
- Convergence Testing
- Equation-of-State Analysis
- Computational Materials Science
- Scientific Programming with Python
- Data Analysis and Curve Fitting
- Scientific Visualization
- Linux and HPC Workflows
- Slurm Job Scheduling

===

## Computational Environment

Calculations are performed on a Linux-based high-performance computing cluster using the Slurm workload manager.

===

## Future Work

Potential extensions include:

- Birch-Murnaghan EOS Fitting
- Comparison of multiple exchange-correlation functionals
- Automated parsing of Quantum ESPRESSO outputs
- Additional validation against experimental and computational literature values

===

## References

- Quantum ESPRESSO Documentation
- Materials Project Database
- Literature values for germanium bulk modulus and equilibrium volume
