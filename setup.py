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
    proc = subprocess.Popen([f"pwd"], stdout=subprocess.PIPE, shell=True)
    #there keyfor success output and noththere for error output
    (there, notthere) = proc.communicate()
    there=there.decode()
    there=there.split()
    f = open("run.sh", "w")
    f.write("#!/bin/bash")
    f.write("\n")
    f.write(f'python3 {there[0]}/cyber.py "$@"')
    f.close()
    os.system("chmod +x *")
    os.system("sudo cp run.sh /usr/bin/cyberonix")
    finish()
def finish():
    os.system("clear")
    banner.main()
    banner.attack("Setup Completed")
    os.system("cyberonix")

if __name__ == "__main__":
    main()

