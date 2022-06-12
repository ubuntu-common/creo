#!/usr/bin/env python3

from os import system as sh

with open("assets/art.dat", "r") as f:
    print(f.read())

print("    checking root...\n")
sh("sudo whoami")
print()

with open("/etc/os-release", "r") as f:
    osr = f.read()
    arch_id = osr.find("ID=arch")
    ubuntu_id = osr.find("ID=ubuntu")

if arch_id > 0:
    with open("assets/packages/arch.dat", "r") as f:
        packages = f.readlines()
        for package in packages:
            sh(f"sudo pacman -S --noconfirm --needed {package}")

elif ubuntu_id > 0:
    with open("assets/packages/ubuntu.dat", "r") as f:
        packages = f.readlines()
        for package in packages:
            sh(f"sudo apt install -y {package}")

with open("assets/massage.dat", "r") as f:
    print(f.read())
