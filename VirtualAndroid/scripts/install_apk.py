import subprocess

def install_apk(apk_path):
    try:
        cmd = ["adb", "install", apk_path]
        subprocess.run(cmd, check=True)
        print(f"APK installed successfully: {apk_path}")
    except Exception as e:
        print(f"Failed to install APK: {e}")

if __name__ == "__main__":
    install_apk("./sample_apps/Clock_7.10_(685617841)_APKPure.apk")
