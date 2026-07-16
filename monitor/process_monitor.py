import psutil


def get_top_processes(limit=10):
    processes = []

    for process in psutil.process_iter(
        ['pid', 'name', 'cpu_percent', 'memory_percent']
    ):
        try:
            process_info = process.info

            processes.append({
                "pid": process_info["pid"],
                "name": process_info["name"],
                "cpu": round(process_info["cpu_percent"], 2),
                "memory": round(process_info["memory_percent"], 2)
            })

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess
        ):
            continue

    processes.sort(
        key=lambda x: x["cpu"],
        reverse=True
    )

    return processes[:limit]

    