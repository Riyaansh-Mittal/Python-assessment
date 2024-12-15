# VirtualAndroid

VirtualAndroid is a project designed to emulate an Android environment using QEMU or KVM-QEMU. This emulator provides a lightweight way to test and debug Android applications locally.

## Features

- Run Android-x86 on your machine.
- Connect to the emulator via ADB for debugging and testing.
- Lightweight and customizable.

## Prerequisites

- QEMU or KVM-QEMU installed.
- Android-x86 ISO image.
- Python 3.x installed.
- ADB installed and configured.

## Installation

install requirements.txt
pip install -r requirements.txt

Install QEMU or KVM-QEMU:
-For Ubuntu:
  sudo apt-get install qemu-system-x86
  sudo apt-get install qemu-kvm

-For Windows:
  download QEMU from online

install adb by download android platform tools or in ubuntu: sudo apt install android-tools-adb android-tools-fastboot

run adb kill-server
adb start-server

Place your Android-x86 ISO file in the system_images directory.

# Usage
-Start the Android emulator:
  python scripts/start_android.py

-Verify the ADB connection:
  python scripts/check_adb_connection.py

-install apk
  python scripts/install_apk.py

-get system info:
  python scripts/get_system_info.py





