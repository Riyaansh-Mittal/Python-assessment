import subprocess

def get_system_info():
    try:
        os_version = subprocess.check_output(["adb", "shell", "getprop ro.build.version.release"]).decode("utf-8").strip()
        device_model = subprocess.check_output(["adb", "shell", "getprop ro.product.model"]).decode("utf-8").strip()
        memory_info = subprocess.check_output(["adb", "shell", "cat /proc/meminfo"]).decode("utf-8").strip()

        system_info = f"""
        OS Version: {os_version}
        Device Model: {device_model}
        Memory Info:
        {memory_info}
        """
        print(system_info)
        with open("system_info.log", "w") as log_file:
            log_file.write(system_info)
        print("System information logged to system_info.log.")
    except Exception as e:
        print(f"Failed to retrieve system information: {e}")

if __name__ == "__main__":
    get_system_info()
