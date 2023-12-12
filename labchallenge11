import psutil


def get_system_time_info():
    """
    Fetch various system time information using psutil.

    Returns:
        dict: Dictionary containing various system time information.
    """

    info = {}
    cpu_times = psutil.cpu_times()
    info["user_normal_time"] = cpu_times.user
    info["kernel_time"] = cpu_times.system
    info["idle_time"] = cpu_times.idle
    info["user_priority_time"] = cpu_times.nice
    info["iowait_time"] = cpu_times.iowait
    info["irq_time"] = cpu_times.irq
    info["softirq_time"] = cpu_times.softirq
    info["guest_time"] = cpu_times.guest
    info["guest_nice_time"] = cpu_times.guest_nice

    return info


if __name__ == "__main__":
    system_info = get_system_time_info()
    print("System Time Information:")
    for key, value in system_info.items():
        print(f"{key}: {value}")
