#!/usr/bin/python3
import banner
import tools
import os
import subprocess
import Cheat_sheet
import news
import time

try:
    def exit_program():
        os.system("clear")
        banner.main()
        print("[+] Thanks visit again")
        exit()
    def update():
        os.system("clear")
        banner.main()
        banner.attack("Update")
        print("[+] Checking for updates.......")
        process = subprocess.Popen("git checkout . && git pull ",shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        (use,nouse)=process.communicate()
        if not nouse:
            if "Already up to date" in use.decode():
                print("[+] it is updated")
            elif "not a git repository" in use.decode():
                print("[-] IT is not a github repository")
            elif "Updating" in use.decode():
                print("[+] updating...")
                print(use.decode())
                print("\u001b[32m[+] Cyberonix is UPDATED to latest version")
            else:
                print("[-] Something went wrong....")
                print(use.decode())
        else:
            print("[-] something went wrong")
            print(nouse)
        for i in range(5):
            print(f"[!] Redirecting in ...{5-i}sec\r",end="")
            time.sleep(i)

    def main():
        update()
        os.system("chmod +x *")
        proc = subprocess.Popen([f"id"], stdout=subprocess.PIPE, shell=True)
        #there keyfor success output and noththere for error output
        (there, notthere) = proc.communicate()
        there=there.decode()
        if "root" not in there:
            os.system("sudo python main.py")
            exit()
        while True:
            os.system("clear")
            banner.main()
            list_attacks=["TOOLS","CHEATSHEET","NEWS","exit"]
            for i in range(len(list_attacks)):
                print(f"{i}) {list_attacks[i]}")
            option=input("\n Select an option ->  ")
            if option=="0":
                os.system("clear")
                tools.main()
            elif option=="1":
                os.system("clear")
                Cheat_sheet.main()
            elif option=="2":
                os.system("clear")
                news.main()
            else:
                exit_program()
    #to run file separately
    if __name__ == "__main__": 
        main()
except KeyboardInterrupt:
    exit_program()