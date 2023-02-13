from main.tools import banner,waiting,writeup,colors
import os
import subprocess

class template:
    def __init__(self,name,command,discription,writeups,link="",method="kali",github_install="",github_check=""):
        self.name=name
        self.command=command
        self.method=method
        self.discription=discription
        self.writeup=writeups
        self.link=link
        self.github_install=github_install
        self.github_check=github_check
        while True:
            os.system("clear")
            banner.main()
            banner.attack(self.name)
            banner.description(self.discription)
            ask=tool_writeups()
            if ask=="1":
                if method=="kali":
                    check_installed(self.name,self.command)
                    waiting.waiting()
                elif method=="go":
                    which_check(self.name,self.link,self.command)
                    waiting.waiting()
                elif method=="github":
                    if os.path.exists(f"Tools/{self.github_check}"):
                        print(f"{colors.green}[+] It Is Installed{colors.reset}")
                        run=input(f"{colors.blue}[+] Do You Want To Run?(y/n):{colors.reset}")
                        if run.lower()=="yes" or run.lower()=="y":
                            os.system(self.command)
                    else:
                        print(f"{colors.red}[-]Not Installed{colors.reset}")
                        installed=input(f"{colors.blue}[+] Do You Want To Install")
                        if installed.lower()=="y" or installed.lower()=="yes":
                            os.system(f"cd Tools && {self.github_install}")
                            run=input(f"{colors.blue}[+] Do You Want To Run?(y/n):{colors.reset}")
                            if run.lower()=="yes" or run.lower()=="y":
                                os.system(f"cd Tools && {self.command}")
                    waiting.waiting()
            elif ask=="2":
                writeup.writeup(self.writeup,self.name)
            else:
                return


def tool_writeups():
    print(f"{colors.options}1) TOOL(About,Installation)")
    print(f"2) Write Ups")
    print(f"3) Go Back..")
    ask=input(f"\n {colors.select}Select An Option ->{colors.reset}  ")
    return ask

def check_installed(name, run_arg):
    proc = subprocess.Popen([f"dpkg -s {name} 2>/dev/null"], stdout=subprocess.PIPE, shell=True)
    (there, notthere) = proc.communicate()
    if "install ok installed" not in there.decode():
        print(f"\n{colors.red}[+] Not Installed")
        print(f"{colors.red}\n[+] It Is Not Installed In Your Kali{colors.reset}")
        install = input(f"{colors.blue}Do You Want To Install The Tool?(y/n):{colors.reset}")
        if install.lower()=="yes" or install.lower()=="y":
            os.system(f"apt install {name} -y")
            download = input(f"{colors.blue}Do You Want To Run The Tool?(y/n):{colors.reset}")
            if download == "y" or download == "Y" or download == "Yes" or download == "yes":
                os.system(f"{run_arg}")
    else:
        print(f"{colors.green}[+] Installed")
        print(f"[+] It Is Installed In Your Kali{colors.reset}")
        download = input(f"{colors.blue}Do You Want To Run The Tool?(y/n):{colors.reset}")
        if download == "y" or download == "Y" or download == "Yes" or download == "yes":
            os.system(f"{run_arg}")


def which_check(name,link,run_arg):
    proc = subprocess.Popen([f"which {name}"],stdout=subprocess.PIPE,shell=True)
    (there,nothere)=proc.communicate()
    if there:
        print(f"\n{colors.green}[+] Installed")
        print(f"[+] It Is Installed In Your Kali{colors.reset}\n")
        download=input(f"{colors.blue}\nDo You Want To Run The Tool?(y/n): {colors.reset} ")
        if download.lower()=="y" or download.lower()=="yes":
            os.system(f"{run_arg}")
    else:
        print(f"{colors.red}\n[+] It Is Not Installed In Your Kali{colors.reset}")    
        download=input(f"{colors.blue}[+] Do You Want To Install It?(y/n):{colors.reset} ")
        if download.lower()=="y" or download.lower()=="yes":
            os.system(f"go install {link}")
            # os.system("go install github.com/projectdiscovery/katana/cmd/katana@latest")
            os.system(f'sudo cp ~/go/bin/{name} /usr/bin')
            download=input(f"{colors.blue}\nDo You Want To Run The Tool?(y/n): {colors.reset}")
            if download.lower()=="y" or download.lower()=="yes":
                os.system(f"{run_arg}")

