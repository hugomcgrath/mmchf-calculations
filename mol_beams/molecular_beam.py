import constants as ct
import numpy as np


def get_average_speed(temperature):
    average_speed = ((8 * ct.R * temperature) / (np.pi * ct.CH4_MOLAR_MASS)) ** (1 / 2)
    return average_speed

def get_pressure():
    p = ct.K * ct.T1 /\
        (np.sqrt(2) * np.pi * ct.CH4_KINETIC_DIAMETER ** 2 *\
         ct.DISTANCE_TO_DETECTOR)
    return p

def get_mean_free_path():
    return 1 / (np.sqrt(2) * np.pi * ct.CH4_KINETIC_DIAMETER ** 2 *\
           ct.MAX_NUMBER_DENSITY_GMC)

def get_time(mean_free_path, average_speed):
    return mean_free_path / average_speed

average_speed_low_pressure = get_average_speed(ct.T1)
T2 = ct.P2 * ct.T1 / ct.P1
average_speed_high_pressure = get_average_speed(T2)
print(f"Average speed at p = 0.1 bar: {average_speed_low_pressure:.2f} m s^-1")
print(f"Average speed at p = 1 bar: {average_speed_high_pressure:.2f} m s^-1")

p = get_pressure()
print(f"To get mean free path of 1 m we must reduce pressure to:")
print(f"p = {p:.2e} Pa")

mean_free_path_gmc = get_mean_free_path()
print(f"The mean free path in a GMC is: {mean_free_path_gmc/1000:.2f} km")

t1 = get_time(mean_free_path_gmc, average_speed_low_pressure)
print(f"Average time before impact at room temperature: {t1/60:.2f} min")

average_speed_space = get_average_speed(ct.T_GMC)
t2 = get_time(mean_free_path_gmc, average_speed_space)
print(f"Average time before impact at space temperature: {t2/60/60:.2f} h")