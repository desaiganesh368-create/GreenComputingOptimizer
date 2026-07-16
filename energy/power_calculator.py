def calculate_power_consumption(cpu_usage, memory_usage):
    BASE_POWER = 20
    CPU_FACTOR = 0.5
    MEMORY_FACTOR = 0.2

    estimated_power = (
        BASE_POWER
        + (cpu_usage * CPU_FACTOR)
        + (memory_usage * MEMORY_FACTOR)
    )

    return round(estimated_power, 2)