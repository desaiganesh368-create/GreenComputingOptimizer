import psutil


def get_battery_usage():
    battery = psutil.sensors_battery()

    if battery is not None:
        return battery.percent

    return "Battery Not Available"