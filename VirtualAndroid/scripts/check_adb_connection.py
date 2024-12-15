import subprocess

def check_adb_connection():
    try:
        output = subprocess.check_output(["adb", "devices"]).decode("utf-8")
        print(output)
        if "emulator" in output:
            print("ADB is connected to the virtual Android system.")
        else:
            print("No emulator found. Ensure the virtual Android system is running.")
    except Exception as e:
        print(f"Error checking ADB connection: {e}")

if __name__ == "__main__":
    check_adb_connection()
