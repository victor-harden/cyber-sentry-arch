#!/usr/bin/env python3
"""
Cyber Sentry for Arch Linux
Checks installed packages against known vulnerabilities
"""

import subprocess
import requests
import json
from datetime import datetime

def get_installed_packages():
    result = subprocess.run(["pacman", "-Q"], capture_output=True, text=True)
    packages = {}
    for line in result.stdout.strip().split("\n"):
        if line:
            name, version = line.split()
            packages[name] = version
    return packages

def main():
    print(f"[{datetime.now()}] Scanning installed packages...")
    packages = get_installed_packages()
    print(f"Found {len(packages)} installed packages")
    print("\n[!] This is a basic skeleton. Extend with real vulnerability feeds.")
    print("Recommended sources: Arch Security Tracker + CISA KEV")

if __name__ == "__main__":
    main()
