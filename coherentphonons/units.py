from scipy.constants import hbar, elementary_charge, atomic_mass, physical_constants, electron_volt

length_scale = 1e-10 # physical_constants['Bohr radius'][0]
mass_scale = atomic_mass

# print("\"Lattice Hartree\" units")
# print("hbar = 1")
# print("e = 1")
# print(f"Length scale = {length_scale} m")
# print("amu = 1")


# atomic_mass *= 100
energy = hbar**2 / (mass_scale * length_scale ** 2)

time_in_ps = (hbar / energy) / 1e-12
freq_in_thz = 1 / time_in_ps

efield_in_vperm = energy / (length_scale * elementary_charge)

# print(f"Energy in eV = {energy / electron_volt:0.06e}")
# print(f"Time in s = {hbar / energy:0.06e}")
# print(f"Freq in 1/s = {energy / hbar:0.06e}")
# print(f"Efield in V/m = {energy / (length_scale * elementary_charge):0.06e}")
# print(f"Dipole moment in C m = {elementary_charge * length_scale:0.06e}")
# print(f"Force in N = {energy / length_scale:0.06e}")