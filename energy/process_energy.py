def classify_process_energy(cpu_usage):
    if cpu_usage >= 30:
        return "High"

    if cpu_usage >= 10:
        return "Medium"

    return "Low"