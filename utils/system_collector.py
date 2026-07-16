from monitor.cpu_monitor import get_cpu_usage
from monitor.memory_monitor import get_memory_usage
from monitor.disk_monitor import get_disk_usage
from monitor.battery_monitor import get_battery_usage
from monitor.process_monitor import get_top_processes


def collect_system_data():
    system_data = {
        "cpu": get_cpu_usage(),
        "memory": get_memory_usage(),
        "disk": get_disk_usage(),
        "battery": get_battery_usage(),
        "processes": get_top_processes()
    }

    return system_data