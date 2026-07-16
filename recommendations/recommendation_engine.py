def generate_recommendations(system_data):
    recommendations = []

    if system_data["cpu"] > 80:
        recommendations.append(
            "High CPU usage detected. Close unnecessary applications."
        )

    if system_data["memory"] > 80:
        recommendations.append(
            "High RAM usage detected. Consider closing unused programs."
        )

    if system_data["disk"] > 90:
        recommendations.append(
            "Disk usage is above 90%. Free some storage space."
        )

    battery = system_data["battery"]

    if isinstance(battery, (int, float)):
        if battery < 20:
            recommendations.append(
                "Battery is low. Enable power saving mode."
            )

    if len(recommendations) == 0:
        recommendations.append(
            "System is operating efficiently."
        )

    for process in system_data["processes"]:
     if process["cpu"] > 30:
        recommendations.append(
            f"{process['name']} is consuming high CPU resources."
        )

    return recommendations