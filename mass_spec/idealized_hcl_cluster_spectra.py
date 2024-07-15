from scipy.special import comb
import matplotlib.pyplot as plt
import constants as ct


def get_mz_spectrum(cluster_size):
    mz_spectrum = []
    for n_cl37 in range(cluster_size+1):
        # binomial distribution
        rel_abundance = comb(cluster_size, n_cl37, exact=True) *\
                        ct.CL37_REL_ABUNDANCE ** n_cl37 *\
                        ct.CL35_REL_ABUNDANCE ** (cluster_size - n_cl37)
        mass = n_cl37 * ct.CL37_MASS +\
               (cluster_size - n_cl37) * ct.CL35_MASS +\
               cluster_size * ct.H1_MASS
        mz_spectrum.append((mass, rel_abundance))
    return mz_spectrum


def get_time_of_flight_spectrum(spectrum):
    tof_spectrum = {}
    for mass, rel_abundance in spectrum.items():
        mass *= ct.DALTON_TO_KG_CONVERSION_FACTOR
        time = ct.D * (mass / (ct.U * ct.CHARGE_OF_ELECTRON)) ** (1 / 2)
        tof_spectrum[time] = rel_abundance
    return tof_spectrum


spectrum = {}

for cluster_size in range(1, ct.MAX_CLUSTER_SIZE+1):
    mz_spectrum = get_mz_spectrum(cluster_size)
    for mass, rel_abundance in mz_spectrum:
        if mass in spectrum.keys():
            spectrum[mass] += rel_abundance
        else:
            spectrum[mass] = rel_abundance
normalization_factor = sum(spectrum.values())
for mass, rel_abundance in spectrum.items():
    spectrum[mass] /= normalization_factor
    # convert to relative abundance to %
    spectrum[mass] *= 100

plt.rcParams.update({'font.size': 16})

# m/z ratio spectrum plot
plt.figure(figsize=(12, 8))
plt.stem(spectrum.keys(), spectrum.values())
plt.ylabel("Relative Abundance (%)")
plt.xlabel("m/z (Th)")
plt.ylim((0, 20))
plt.xlim((0, 170))
for mass, rel_abundance in spectrum.items():
    plt.annotate(f"{mass:.2f}", xy=(mass, rel_abundance), xytext=(0,5),
                 textcoords="offset points",ha="left")

# time of flight spectrum plot
tof_spectrum = get_time_of_flight_spectrum(spectrum)

plt.figure(figsize=(12, 8))
plt.stem(tof_spectrum.keys(), tof_spectrum.values())
plt.ylabel("Relative Abundance (%)")
plt.xlabel("Time (s)")
plt.ylim((0, 20))
plt.xlim((0, 4.5e-5))
for time, rel_abundance in tof_spectrum.items():
    plt.annotate(f"{time/1e-5:.2f}", xy=(time, rel_abundance), xytext=(0,5),
                 textcoords="offset points",ha="left")
plt.show()
