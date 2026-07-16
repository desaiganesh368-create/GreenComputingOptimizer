def calculate_eco_score(
    cpu_usage,
    memory_usage,
    power_usage,
    carbon_emission
):
    score = 100

    if cpu_usage > 80:
        score -= 25
    elif cpu_usage > 60:
        score -= 15
    elif cpu_usage > 40:
        score -= 5

    if memory_usage > 80:
        score -= 20
    elif memory_usage > 60:
        score -= 10
    elif memory_usage > 40:
        score -= 5

    if power_usage > 80:
        score -= 20
    elif power_usage > 60:
        score -= 10

    if carbon_emission > 0.06:
        score -= 20
    elif carbon_emission > 0.04:
        score -= 10

    if score < 0:
        score = 0

    return score

def get_eco_status(score):
    if score >= 90:
        return "Excellent"

    if score >= 75:
        return "Good"

    if score >= 60:
        return "Moderate"

    if score >= 40:
        return "Poor"

    return "Critical"