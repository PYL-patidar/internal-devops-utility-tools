## This is for putting my actual logic of utility -> system server metrics

import psutil


def get_system_metrics():
    cpu_percentage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/")

    cpu_threshold = 10

    status = "High CPU" if cpu_percentage > cpu_threshold else "Healthy"

    return {"cpu_percentage":cpu_percentage,
            "memory":memory,
            "disk_usage":disk,
            "status":status
            }


