import constants as ct


def get_time_resolution():
    delta_m = 1 * ct.DALTON_TO_KG_CONVERSION_FACTOR
    m = ct.DESIRED_RESOLUTION * delta_m
    time_resolution = (ct.D / ct.U ** (1 / 2)) *\
                      (((m + delta_m) / ct.CHARGE_OF_ELECTRON) ** (1 / 2) -\
                       (m / ct.CHARGE_OF_ELECTRON) ** (1 / 2))
    return time_resolution


tof_time_step = get_time_resolution()
print(f"Desired resolving power: {ct.DESIRED_RESOLUTION}")
print(f"Time step: {tof_time_step:.2e} s")
