#!/usr/bin/python3
import os
import subprocess
from main.tools import banner

def main():
    os.system("clear")
    banner.main()
    banner.attack("Setup")
    os.system("pip install -r requirements.txt")
    create_symlink()
def create_symlink():
    script_path = os.path.abspath("cyberonix.py")
    link_path = os.path.join("/usr/local/bin", "cyberonix")
    subprocess.run(["ln", "-s", script_path, link_path])
    finish()
def finish():
    os.system("clear")
    banner.main()
    banner.attack("Setup Completed")
    os.system("cyberonix")

if __name__ == "__main__":
    main()

