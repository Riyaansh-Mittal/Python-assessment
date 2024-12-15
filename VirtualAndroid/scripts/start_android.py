import os
import subprocess

def start_android_emulator(iso_file_path):
    """
    Start the Android emulator using a single ISO file.
    """
    # Ensure the ISO file exists
    if not os.path.exists(iso_file_path):
        print(f"Error: ISO file not found at {iso_file_path}")
        return

    # QEMU command to launch the Android emulator
    qemu_command = [
        'qemu-system-x86_64',
        '-accel', 'tcg',  # Use software-based acceleration for Windows
        '-boot', 'd',  # Boot from the ISO file
        '-cdrom', iso_file_path,  # Path to the Android ISO file
        '-m', '512',  # Allocate 512MB of RAM
        '-smp', '4',  # Use 4 CPU cores (you can adjust based on your system)
        '-vga', 'virtio',  # Virtual VGA device
        '-usb',  # Enable USB devices
        '-device', 'usb-tablet',  # Use USB tablet for mouse support
        '-device', 'usb-kbd',  # USB keyboard
        '-net', 'nic',  # Network interface card
        '-net', 'user,hostfwd=tcp::5555-:5555',  # Network settings for ADB access
        '-serial', 'mon:stdio'
    ]


    # Launch the emulator
    try:
        print("Starting the Android emulator...")
        subprocess.run(qemu_command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to start the emulator: {e}")
    except FileNotFoundError:
        print("Error: QEMU is not installed or not in PATH. Install it to proceed.")

if __name__ == "__main__":
    iso_file_path = "system_images/android-x86_64-9.0-r2.iso"
    start_android_emulator(iso_file_path)
