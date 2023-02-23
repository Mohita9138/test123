import os,subprocess
from main.tools import colors
def pip_install(name,run_arg):
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
            os.system(f"pip install {name}")
            # os.system("go install github.com/projectdiscovery/katana/cmd/katana@latest")
            # os.system(f'sudo cp ~/go/bin/{name} /usr/bin')
            download=input(f"{colors.blue}\nDo You Want To Run The Tool?(y/n): {colors.reset}")
            if download.lower()=="y" or download.lower()=="yes":
                os.system(f"{run_arg}")

pip_install("bopscrk","bopscrk -i")
