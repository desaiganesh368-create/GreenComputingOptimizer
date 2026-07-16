def calculate_carbon_emission(power_consumption):
    EMISSION_FACTOR = 0.82

    energy_consumption_kwh = power_consumption / 1000

    carbon_emission = energy_consumption_kwh * EMISSION_FACTOR

    return round(carbon_emission, 4)