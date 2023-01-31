from main.tools import banner,run_on_browser,waiting
import os
import subprocess
import threading
import time
import requests
from bs4 import BeautifulSoup


def check_installed(name, needargs=False):
    proc = subprocess.Popen(
        [f"dpkg -s {name}"], stdout=subprocess.PIPE, shell=True)
    # there keyfor success output and noththere for error output
    (there, notthere) = proc.communicate()
    if "install ok installed" not in there.decode():
        print("[-] not installed")
        print("[+] it is not installed in your Kali")
        download = input("[+] Do you want to install it?(y/n)")
        if download[0].lower() == "y":
            os.system(f"apt install {name} -y")
            if needargs:
                download = input("Do you want to run the tool?(y/n)")
                if download[0].lower() == "y":
                    # when tool is of cli no need of thread
                    thread_run(name, needargs)
            else:
                download = input("Do you want to run the tool?(y/n)")
                if download[0].lower() == "y":
                    # when tool is of gui it needs thread
                    threading.Thread(target=thread_run, args=(name,)).start()
    else:
        print("[+] Installed")
        print("[+] It is installed in your kali")
        if needargs:
            download = input("Do you want to run the tool?(y/n)")
            if download[0].lower() == "y":
                # when tool is of cli no need of thread
                thread_run(name, needargs)
        else:
            download = input("Do you want to run the tool?(y/n)")
            if download[0].lower() == "y":
                # when tool is of gui it needs thread
                threading.Thread(target=thread_run, args=(name,)).start()
                if name == 'kismet':
                    print(f"[+] {name} is started at address: http://localhost:2501 (or the address of this system) for the Kismet UI")
                    KURL = "http://localhost:2501" 
                    threading.Thread(target=run_on_browser, args=(KURL,)).start()
                    # os.system(f"firefox http://localhost:2501 2>/dev/null")

def thread_run(command, needargs=False):
    print("\n")
    if needargs == "no-help":
        # it will run only help because it is in cli
        os.system(f"{command}")
    elif needargs == '-h':
        os.system(f"{command} -h")
    elif needargs == '--help':
        os.system(f"{command} --help")
    else:
        # for gui all errors/output will go in null
        # time.sleep(1)
        # subprocess.Popen(["xdotool", "key", "ctrl+shift+t"])
        os.system(f"{command} > /dev/null 2>&1")

# def run_on_browser(URL):
#     print("[+] Opening Article")
#     os.system(f"firefox {URL} 2>/dev/null")
#     time.sleep(3)

def run_on_browser(URL):
    proc = subprocess.Popen([f"pwd"], stdout=subprocess.PIPE, shell=True)
    # there keyfor success output and noththere for error output
    (there, notthere) = proc.communicate()
    there = there.decode()
    there = there.split("/")
    if "root" in there:
        os.system(f"firefox {URL} 2>/dev/null")
        time.sleep(3)
    else:
        # this is to get desktop enviroment
        proc = subprocess.Popen([f"echo $DESKTOP_SESSION"], stdout=subprocess.PIPE, shell=True)
        (envo, noenvo) = proc.communicate()
        # this is to get username
        proc = subprocess.Popen([f"cat /etc/passwd | grep {there[2]}"], stdout=subprocess.PIPE, shell=True)
        (uid, notuid) = proc.communicate()
        uid = uid.decode()
        uid = uid.split(":")
        if envo == "GNOME":
            os.system(f"sudo chown root:root /run/user/{uid[2]}/gdm/Xauthority")
            os.system(f"firefox {URL} 2>/dev/null")

        else:
            os.system(f"sudo chown root:root /home/{there[2]}/.Xauthority")
            os.system(f"firefox {URL} 2>/dev/null")

        


def github_getting_text(link, selector, indexvalue):
    print("Please Wait....\r", end="")
    URL = link
    try:
        r = requests.get(URL)
        soup = BeautifulSoup(r.content, 'html5lib')
        paras = soup.select(selector)
        # check index value from test file
        return paras[indexvalue].text
    except Exception as e:
        print(e)
        return "Not loaded because no internet connection"


def main():
    os.system("clear")
    banner.main()
    banner.attack("Wireless Hacking")
    list_attacks = ["Kismet", "Wifite", "Fern Wifi Cracker",
                    "Aircrack-ng", "Fluxion", "Wifiphisher", "Bettercap", "go back"]
    for i in range(len(list_attacks)):
        print(f"{i}) {list_attacks[i]}")

    option = input("\n Select an option ->  ")
    if option == "0":
        print("\n[+] Kismet")
        os.system("clear")
        Kismet()
    elif option == "1":
        print("\n[+] Wifite")
        os.system("clear")
        Wifite()
    elif option == "2":
        print("\n[+] Fern Wifi Cracker")
        os.system("clear")
        Fern_wifi()
    elif option == "3":
        print("\n[+] Aircrack-ng")
        os.system("clear")
        Aircrack()
    elif option == "4":
        print("\n[+] Fluxion")
        os.system("clear")
        Fluxion()
    elif option == "5":
        print("\n[+] Wifiphisher")
        os.system("clear")
        Wifiphisher()
    elif option == "6":
        print("\n[+] Bettercap")
        os.system("clear")
        Bettercap()
    else:
        return


def Kismet():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("Kismet")
        github = github_getting_text(
            "https://github.com/kismetwireless/kismet-docs/blob/master/readme/000-intro.md", 'p[dir="auto"]', 0)
        banner.description(github)
        ask = tool_options()
        if ask == "1":
            # print("[+] Download/usage")
            # github = github_getting_text("https://www.kali.org/tools/kismet/", 'div[id="packages-info"]', 1)
            # print(github)
            print("\n Preinstalled in Repository")
            check_installed("kismet")
            waiting.waiting()
        elif ask == "2":
            # first argument for dictionary(key=title,value=url) second argument for banner
            writeup({"Kismet -- WiFi Sniffer": "https://www.kalilinux.in/2019/02/kismet-wifi-sniffer.html", "Use Kismet to Watch Wi-Fi User Activity": "https://null-byte.wonderhowto.com/how-to/use-kismet-watch-wi-fi-user-activity-through-walls-0182214/",
                    "HACKING WIFI USING KISMET": "https://www.bookofnetwork.com/hacking-tutorials/Kismet-Wireless", "How To Use Kismet Kali Linux?": "https://www.systranbox.com/how-to-use-kismet-kali-linux/"}, "Kismet Writeups")
        else:
            return

def Wifite():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("Wifite")
        banner.description(" > Wifite is a tool to audit WEP or WPA encrypted wireless networks. It uses aircrack-ng, pyrit, reaver, tshark tools to perform the audit.\n > This tool is customizable to be automated with only a few arguments and can be trusted to run without supervision.")
        ask = tool_options()
        if ask == "1":
            print("[+] Download/usage")
            github = github_getting_text("https://www.kali.org/tools/wifite/", 'pre', 1)
            print(github)
            print("\n Preinstalled in Repository")
            check_installed("wifite", "-h")
        elif ask == "2":
            writeup({"Wifite walkthrough Part-1": "https://resources.infosecinstitute.com/topic/wifite-walkthrough-part-1/", "Wifite walkthrough Part-2": "https://resources.infosecinstitute.com/topic/wifite-walkthrough-part-2/",
                    "Wireless pentesting with Wifite": "https://www.hackingarticles.in/wireless-penetration-testing-wifite/", "Wifite - Automated Wifi hacking tool": "https://kalitut.com/wifite-automated-wi-fi-hacking-tool/"}, "Wifite writeups")
        else:
            return

def Fern_wifi():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("Fern Wifi Cracker")
        github = github_getting_text(
            "https://github.com/savio-code/fern-wifi-cracker", 'p[dir="auto"]', 0)
        banner.description(github)
        print("\n")
        ask = tool_options()
        if ask == "1":
            # print("[+] Download/usage")
            # github = github_getting_text("https://github.com/savio-code/fern-wifi-cracker", 'selector', index)
            # print(github)
            print("\n Preinstalled in Repository")
            check_installed("fern-wifi-cracker")
            waiting.waiting()
        elif ask == "2":
            writeup({"What is Fern Wifi Cracker": "https://www.kalilinux.in/2020/09/fern-wifi-cracker.html", "Hacking Wifi networks using Fern Wifi Cracker": "https://www.studocu.com/en-au/document/western-sydney-university/it-product-support-and-services/fern-wifi-cracker-hacking-wifi-networks-using-fern-wifi-cracker-easily/10772514",
                    "Wireless penetration testing - Fern ": "https://www.hackingarticles.in/wireless-penetration-testing-fern/", "Cracking wifi passwords using Fern": "https://hacking84.rssing.com/chan-13108703/article238.html"}, "Fern Wifi Cracker writeups")
        else:
            return

def Aircrack():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("Aircrack-ng")
        github = github_getting_text("https://github.com/aircrack-ng/aircrack-ng", 'p[dir="auto"]', 1)
        github += github_getting_text("https://github.com/aircrack-ng/aircrack-ng", 'ul[dir="auto"]', 0)
        banner.description(github)
        print("\n")
        ask = tool_options()
        if ask == "1":
            print("[+] Download/usage")
            github = github_getting_text("https://www.kali.org/tools/aircrack-ng/", 'pre', 38)
            print(github)
            print("\n Preinstalled in Repository")
            check_installed("aircrack-ng", "--help")
            waiting.waiting()
        elif ask == "2":
            writeup({"How to use Aircrack-ng": "https://linuxhint.com/how_to_aircrack_ng/", "Aircrack-ng Practical Demonstration Tutorial": "https://techofide.com/blogs/how-to-use-aircrack-ng-aircrack-ng-tutorial-practical-demonstration/",
                    "Hacking the wireless network in 5 simple steps": "https://www.hackingloops.com/how-to-use-aircrack-kali/", "Crack WPA/WPA2 WiFi Passwords using Aircrack-ng & Kali Linux": "https://nooblinux.com/crack-wpa-wpa2-wifi-passwords-using-aircrack-ng-kali-linux/"}, "Aircrack-ng Writeups")
        else:
            return

def Fluxion():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("Fluxion")
        github = github_getting_text(
            "https://github.com/FluxionNetwork/fluxion", 'p[dir="auto"]', 1)
        banner.description(github)
        ask = tool_options()
        if ask == "1":
            print("Checking Fluxion is installed or not......")
            if not os.path.isdir("fluxion"):
                print("[-] Fluxion is not installed")
                download = input("[+] Do you want to install it?(y/n)")
                if download[0].lower() == "y":
                    print("[+] Installing .......")
                    os.system(
                        "git clone https://www.github.com/FluxionNetwork/fluxion.git")
                    print(
                        f"\nFluxion is installed at ' {os.getcwd()} ' path\n")
                    use = input("[+] Do you want to start Fluxion? (y/n)")
                    if use[0].lower() == "y":
                        os.system(
                            "cd fluxion && chmod +x fluxion.sh && ./fluxion.sh")
            else:
                print("[+] Fluxion is already Installed !!")
                use = input("[+] Do you want to start Fluxion? (y/n)")
                if use[0].lower() == "y":
                    os.system(
                        "cd fluxion && chmod +x fluxion.sh && ./fluxion.sh")

        elif ask == "2":
            writeup({"Fluxion kali linux tutorial": "https://linuxhint.com/fluxion-kali-linux-tutorial/", "Fluxion - Wifi security auditing tool": "https://www.hackingloops.com/fluxion/", "Fluxion -- Crack WiFi Passwords in Minutes": "https://www.kalilinux.in/2020/07/fluxion-kali-linux-crack-wifi.html",
                    "Cracking WPA/WPA2 Passwords in Minutes with Fluxion": "https://gbhackers.com/cracking-wpawpa2-passwords-fluxion/amp/", "Wireless Penetration Testing: Fluxion": "https://www.hackingarticles.in/wireless-penetration-testing-fluxion/", "Fluxion in Kali Linux usage": "https://www.cyberpratibha.com/blog/fluxion-wpa-wpa2-hacking/"}, "Fluxion writeups")
        else:
            return


def Wifiphisher():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("Wifiphisher")
        github = github_getting_text(
            "https://github.com/wifiphisher/wifiphisher", 'p[dir="auto"]', 2)
        banner.description(github)
        print("\n")
        ask = tool_options()
        if ask == "1":
            print("\n")
            print("[+] Download/usage")
            github = github_getting_text("https://github.com/wifiphisher/wifiphisher", 'p[dir="auto"]', 25)
            print(github)
            github = github_getting_text("https://github.com/wifiphisher/wifiphisher", 'p[dir="auto"]', 26)
            print(github)
            print("\n Preinstalled in Repository")
            check_installed("wifiphisher", '-h')
            waiting.waiting()
        elif ask == "2":
            writeup({"WiFi Exploitation with WifiPhisher": "https://www.hackingarticles.in/wifi-exploitation-wifiphisher/", "wifiphisher Description": "https://en.kali.tools/?p=90", "Read Team engagement on Wifi with Wifiphisher": "https://whitehatinstitute.com/conduct-red-team-engagements-on-wifi-with-wifiphisher/", "Wireless Hacking with WifiPhisher":
                    "https://cntemngwa.medium.com/wireless-hacking-with-wifiphisher-d4b857414146", "WifiPhisher – WiFi Crack and Phishing Framework": "https://latesthackingnews.com/2018/10/02/wifiphisher-wifi-crack-and-phishing-framework/", "Wifiphisher Evil Twin Attack": "https://kalitut.com/wifiphisher-evil-twin-attack/"}, "Wifiphisher Writeups")
        else:
            return


def Bettercap():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("Bettercap")
        github = github_getting_text(
            "https://github.com/bettercap/bettercap", 'p[dir="auto"]', 3)
        banner.description(github)
        ask = tool_options()
        if ask == "1":
            print("\n")
            print("[+] Download/usage")
            github = github_getting_text("https://www.kali.org/tools/bettercap/", 'pre', 1)
            print(github)
            print("\n Preinstalled in Repository")
            check_installed("bettercap", '-h')
            waiting.waiting()
        elif ask == "2":
            writeup({"Better official Docs": "https://www.bettercap.org/usage/", "Sniffing using bettercap in Linux": "https://www.geeksforgeeks.org/sniffing-using-bettercap-in-linux/", "Wireless Penetration Testing: Bettercap": "https://www.hackingarticles.in/wireless-penetration-testing-bettercap/",
                    "Hack Wi-Fi Networks with Bettercap": "https://null-byte.wonderhowto.com/how-to/hack-wi-fi-networks-with-bettercap-0194422/", "Bettercap Description": "https://en.kali.tools/?p=140", "Bluetooth Low Energy recon using Bettercap": "https://medium.com/@mks_01/bluetooth-low-energy-recon-using-bettercap-a53bb1b46e93"}, "Bettercap Writeups")
        else:
            return


def tool_options():
    print("1) TOOL(about,installation)")
    print("2) Write ups")
    print("3) go back..")
    ask = input("Select an option ->  ")
    return ask


def writeup(writeup_dict, name):
    while True:
        os.system("clear")
        banner.main()
        banner.attack(name)
        # convert dict keys in list(type casting)
        key = list(writeup_dict.keys())
        key.append("go back")
        for i in range(len(key)):
            print(f"{i}) {key[i]}")
        option = input("\n Select an option ->  ")
        # 1-9=int kdsjfhgkjds=int X to type cast safely
        try:
            threading.Thread(target=run_on_browser, args=(writeup_dict[key[int(option)]],)).start()
            # a={"a":1,"b":2}
            # print(2)
        except:
            return

if __name__ == "__main__":
    main()
