import banner
import os
import subprocess
import threading
import time


def clear():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')
    pass


def waiting():
    input("\n[+]press ENTER to go back ")


def check_installed(name, needargs=False):
    proc = subprocess.Popen([f"dpkg -s {name}"], stdout=subprocess.PIPE, shell=True)
    # there keyfor success output and noththere for error output
    (there, notthere) = proc.communicate()
    if "install ok installed" not in there.decode():
        print("[-] not installed")
        print("[+] it is not installed in your Kali")
        download = input("[+] Do you want to install it?(y/n)")
        if download == "y" or download == "Y" or download == "Yes" or download == "yes":
            os.system(f"apt install {name} -y")
            if needargs:
                download = input("Do you want to run the tool?(y/n)")
                if download == "y" or download == "Y" or download == "Yes" or download == "yes":
                    # when tool is of cli no need of thread
                    thread_run(name, needargs)
            else:
                download = input("Do you want to run the tool?(y/n)")
                if download == "y" or download == "Y" or download == "Yes" or download == "yes":
                    # when tool is of gui it needs thread
                    threading.Thread(target=thread_run, args=(name,)).start()
    else:
        print("[+] installed")
        print("[+] it is installed in your kali")
        if needargs:
            download = input("Do you want to run the tool?(y/n)")
            if download == "y" or download == "Y" or download == "Yes" or download == "yes":
                # when tool is of cli no need of thread
                thread_run(name, needargs)
        else:
            download = input("Do you want to run the tool?(y/n)")
            if download == "y" or download == "Y" or download == "Yes" or download == "yes":
                # when tool is of gui it needs thread
                threading.Thread(target=thread_run, args=(name,)).start()


def writeup(writeup_dist, name):
    while True:
        clear()
        banner.main()
        banner.attack(name)
        # convert dict keys in list(type casting)
        key = list(writeup_dist.keys())
        key.append("go back")
        for i in range(len(key)):
            print(f"{i}) {key[i]}")
        option = input("\n Select an option ->  ")
        # 1-9=int kdsjfhgkjds=int X to type cast safely
        try:
            threading.Thread(target=run_on_browser, args=(writeup_dist[key[int(option)]],)).start()
            # a={"a":1,"b":2}
            # print(2)
        except:
            return


def run_on_browser(URL):
    # print("[+] Opening url")
    print("[+] Opening Article")
    proc = subprocess.Popen([f"pwd"], stdout=subprocess.PIPE, shell=True)
    # there keyfor success output and noththere for error output
    (there, notthere) = proc.communicate()
    there = there.decode()
    there = there.split("/")
    if "root" in there:
        os.system(f"firefox {URL} 2>/dev/null")
    else:
        # this is to get desktop enviroment
        proc = subprocess.Popen([f"echo $DESKTOP_SESSION"], stdout=subprocess.PIPE, shell=True)
        (envo, noenvo) = proc.communicate()
        # this is to get username
        proc = subprocess.Popen([f"cat /etc/passwd | grep {there[2]}"], stdout=subprocess.PIPE, shell=True)
        (uid, notuid) = proc.communicate()
        uid = uid.decode()
        uid = uid.split(":")
        os.system(f"sudo chown root:root /run/user/{uid[2]}/gdm/Xauthority > /dev/null 2>&1")
        # os.system(f"firefox {URL} 2>/dev/null")
        os.system(f"sudo chown root:root /home/{there[2]}/.Xauthority > /dev/null 2>&1")
        os.system(f"firefox {URL} 2>/dev/null")


def thread_run(command, needargs=False):
    if needargs == "no-help":
        # it will run only help because it is in cli
        os.system(f"{command}")
    elif needargs:
        os.system(f"{command} -h")
    else:
        # for gui all errors/output will go in null
        os.system(f"{command} > /dev/null 2>&1")


def first_list():
    print("1) TOOL(about,installation)")
    print("2) Write ups")
    print("3) go back..")
    option = input("Select an option ->  ")
    return option


def root():
    clear()
    banner.main()
    banner.attack("Password Hacking")
    list_root_attacks = ["Brute Force Attacks", "Dictionary Attacks", "Rainbow Table Attack", "Wordlist Generator",
                         "Phishing Attacks", "Keylogger Attacks", "go back"]
    for i in range(len(list_root_attacks)):
        print(f"{i}) {list_root_attacks[i]}")
    pass
    option = input("Select an option ->  ")
    return option


def main():
    while True:
        clear()
        banner.main()
        banner.attack("Password Hacking")
        option = root()
        if option == "0":
            while True:
                print("\n[+] Brute Force Attacks")
                clear()
                banner.main()
                banner.attack("Brute Force")
                banner.description("A brute force attack is a method of attempting to gain unauthorized access to a "
                                "computer or network by systematically trying every possible combination of characters "
                                "or words in order to discover a valid password or key. In a 'pure' brute force "
                                "attack, all possible combinations are tried one after another until the correct one "
                                "is found. This can be a time-consuming process, but it is often effective because "
                                "many people use easily-guessed passwords.")
                ask = Brute_Force_Tools()
                if ask == "0":
                    Hashcat()
                    pass
                elif ask == "1":
                    John_The_Ripper()
                    pass
                elif ask == "2":
                    Hydra()
                    pass
                elif ask == "3":
                    Johnny()
                    pass
                elif ask == "4":
                    CrackStation()
                    pass
                elif ask == "5":
                    CyberChef()
                    pass
                elif ask == "6":
                    pass
                else:
                    break

        elif option == "1":
            while True:
                print("\n[+] Dictionary Attacks")
                clear()
                banner.main()
                banner.attack("Dictionary Attacks")
                banner.description("A dictionary attack is a type of brute force attack that involves trying every word "
                                "in a predefined list (a dictionary) as a password. This method is more efficient than "
                                "a traditional brute force attack, where every possible combination of characters is "
                                "tried, because most people use common words or phrases as passwords. The attacker can "
                                "also use a list of commonly used passwords or publicly available information about "
                                "the target (such as their name, birthdate, etc.) to create a custom dictionary.")
                ask = Dictionary_Attack_Tools()

                if ask == "0":
                    Hashcat()
                    pass
                elif ask == "1":
                    John_The_Ripper()
                    pass
                elif ask == "2":
                    Hydra()
                    pass
                elif ask == "3":
                    Medusa()
                    pass
                elif ask == "4":
                    Ncrack()
                    pass
                elif ask == "5":
                    Johnny()
                    pass
                elif ask == "6":
                    CrackStation()
                    pass
                elif ask == "7":
                    CyberChef()
                    pass
                elif ask == "8":
                    pass
                else:
                    print("Invalid Command")
                clear()

        elif option == "2":
            while True:
                print("\n[+] Rainbow Table Attack")
                clear()
                banner.main()
                banner.attack("Rainbow Table Attack")
                banner.description("A rainbow table attack is a method of cracking password hashes by using precomputed "
                                "tables of hash values, which can be faster than traditional brute force attack. It is "
                                "particularly effective against hash functions that are fast to compute and vulnerable "
                                "to collisions, but less effective against stronger hash functions.")
                ask = Rainbow_Table_Tools()
                if ask == "0":
                    RainbowCrack()
                    pass
                elif ask == "1":
                    ophCrack()
                    pass
                else:
                    break

        elif option == "3":
            while True:
                print("\n[+] Wordlist Generator")
                clear()
                banner.main()
                banner.attack("Wordlist Generator")
                banner.description("A wordlist generator is a tool that generates a list of words or phrases that can be "
                                "used in a dictionary attack. The list can be generated from a predefined dictionary, "
                                "real-world data such as web pages, or by using a combination of commonly used words "
                                "or patterns. This list of words is then used to try as potential passwords in a "
                                "dictionary attack, which can be more efficient than a traditional brute force attack "
                                "as it tries only words that are likely to be used as passwords.")
                ask = Wordlist_Generator_Tools()
                if ask == "0":
                    Crunch()
                    pass
                elif ask == "1":
                    Cupp()
                    pass
                elif ask == "2":
                    bopscrk()
                    pass
                else:
                    break

        elif option == "4":
            while True:
                print("\n[+] Phishing Attacks")
                clear()
                banner.main()
                banner.attack("Phishing Attacks")
                banner.description("A phishing attack is a type of cyber attack in which an attacker uses fraudulent "
                                "emails, websites, or other means of communication to trick a victim into providing "
                                "sensitive information such as login credentials, personal information, or financial "
                                "details. The attacker often poses as a trustworthy entity and attempts to convince "
                                "the victim to click on a link, download an attachment, or enter information into a "
                                "fake website. The goal of a phishing attack is to steal sensitive information or "
                                "install malware on the victim's device.")
                ask = Phishing_Attacks_Tools()
                if ask == "0":
                    SET()
                    pass
                elif ask == "1":
                    HiddenEye()
                    pass
                elif ask == "2":
                    r3bu5()
                    pass
                elif ask == "3":
                    zphisher()
                    pass
                elif ask == "4":
                    Shellphish()
                    pass
                elif ask == "5":
                    Gophish()
                    pass
                elif ask == "6":
                    Smikta()
                    pass
                else:
                    break

        elif option == "5":
            while True:
                print("\n[+] Keylogger Attacks")
                clear()
                banner.main()
                banner.attack("Keylogger Attacks")
                banner.description("A keylogger attack is a type of cyber attack in which an attacker uses malicious "
                                "software, called a keylogger, to record every keystroke made by a victim on their "
                                "computer or mobile device. This includes passwords, credit card numbers, "
                                "personal information, and other sensitive data. The keylogger can also take "
                                "screenshots of the victim's screen, record their internet browsing history, "
                                "and even capture audio and video. The attacker can use this information to steal "
                                "personal identities, login credentials, and financial information, or to gain access "
                                "to sensitive systems. Keyloggers can be installed through malware, email attachments, "
                                "or social engineering tactics like phishing.")
                ask = Keylogger_Attacks_Tools()
                if ask == "0":
                    ZLogger()
                    pass
                else:
                    break
        else:
            return


# Sub Root Function Tools0


def Brute_Force_Tools():
    clear()
    banner.main()
    banner.attack("Brute Force Tools")
    list_root_attacks = ["Hashcat", "John The Ripper", "Hydra", "Johnny (GUI John)",
                         "CrackStation (Website)", "CyberChef (Website)", "go back"]
    for i in range(len(list_root_attacks)):
        print(f"{i}) {list_root_attacks[i]}")
    pass
    option = input("Select an option ->  ")
    return option
    pass


def Dictionary_Attack_Tools():
    clear()
    banner.main()
    banner.attack("Dictionary Force Tools")
    list_root_attacks = ["Hashcat", "John The Ripper", "Hydra", "Medusa", "Nrack", "Johnny (GUI John)",
                         "CrackStation (Website)", "CyberChef (Website)", "go back"]
    for i in range(len(list_root_attacks)):
        print(f"{i}) {list_root_attacks[i]}")
    pass
    option = input("Select an option ->  ")
    return option
    pass


def Rainbow_Table_Tools():
    clear()
    banner.main()
    banner.attack("Rainbow Table Tools")
    list_root_attacks = ["RainbowCrack", "ophCrack", "go back"]
    for i in range(len(list_root_attacks)):
        print(f"{i}) {list_root_attacks[i]}")
    pass
    option = input("Select an option ->  ")
    return option
    pass


def Wordlist_Generator_Tools():
    clear()
    banner.main()
    banner.attack("Wordlist Generator Tools")
    list_root_attacks = ["Crunch", "Cupp", "bopscrk", "go back"]
    for i in range(len(list_root_attacks)):
        print(f"{i}) {list_root_attacks[i]}")
    pass
    option = input("Select an option ->  ")
    return option
    pass


def Phishing_Attacks_Tools():
    clear()
    banner.main()
    banner.attack("Phishing Attacks Tools")
    list_root_attacks = ["Social-Engineer Toolkit (SET)", "HiddenEye", "r3bu5", "zphisher", "Shellphish",
                         "Gophish (GUI)", "Smikta (Website)", "go back"]
    for i in range(len(list_root_attacks)):
        print(f"{i}) {list_root_attacks[i]}")
    pass
    option = input("Select an option ->  ")
    return option
    pass


def Keylogger_Attacks_Tools():
    clear()
    banner.main()
    banner.attack("Keylogger Attack Tools")
    list_root_attacks = ["ZLogger", "go back"]
    for i in range(len(list_root_attacks)):
        print(f"{i}) {list_root_attacks[i]}")
    pass
    option = input("Select an option ->  ")
    return option
    pass


# Bruteforce Tools

def Hashcat():
    while True:
        clear()
        banner.main()
        banner.attack("Hashcat")

        banner.description("Hashcat is an open-source password cracking tool that can perform dictionary, brute force "
                           "and combination attacks, it uses the power of GPUs to accelerate the cracking process, "
                           "supports a wide variety of hashing algorithms and it can run on Windows, Linux and macOS. "
                           "It's widely used for password recovery, security testing and penetration testing.")
        ask = first_list()
        if ask == "1":
            ask_install = input("[+] Do you want to install hashcat or not?(y/n)")
            if ask_install == "y" or ask_install == "Y" or ask_install == "Yes" or ask_install == "yes":
                # check for installation
                check_installed("hashcat", True)
        elif ask == "2":

            # first argument for dictionary(key=title,value=url) second argument for banner
            writeup(
                {
                    "Hashcat tutorial for beginners": "https://resources.infosecinstitute.com/topic/hashcat-tutorial-beginners/",
                    "How to Crack Passwords Using Hashcat Tool?": "https://geekflare.com/password-cracking-with-hashcat/"}
                , "Hashcat Writeup")

        else:
            return

        waiting()
    pass


def John_The_Ripper():
    while True:
        clear()
        banner.main()
        banner.attack("John The Ripper")
        banner.description("John the Ripper is a free and open-source password cracking software tool. It can be run "
                           "on a variety of operating systems, including Windows, macOS, and Linux. It uses a "
                           "combination of wordlists and rules to try and guess the password for a given hash or "
                           "file, and can support a variety of different hash types, including those used for Unix "
                           "and Windows passwords. John the Ripper is commonly used by security professionals and "
                           "system administrators to audit the security of their systems and detect weak or easily "
                           "guessable passwords.")
        ask = first_list()
        if ask == "1":
            ask_install = input("[+] Do you want to install John The Ripper or not?(y/n)")
            if ask_install == "y" or ask_install == "Y" or ask_install == "Yes" or ask_install == "yes":
                # check for installation
                check_installed("john", True)
        elif ask == "2":

            # first argument for dictionary(key=title,value=url) second argument for banner
            writeup(
                {
                    "Open-wall John": "https://www.openwall.com/john/",
                    "Password Cracking With John The Ripper": "https://www.section.io/engineering-education/password-cracking-with-john-the-ripper/",
                    "Tips and Tutorials of John": "https://www.varonis.com/blog/john-the-ripper"}
                , "Hashcat Writeup")
        else:
            return
        waiting()
    pass


def Hydra():
    while True:
        clear()
        banner.main()
        banner.attack("Hydra")
        banner.description("Hydra is a password cracking tool that performs brute-force and dictionary attacks on "
                           "network protocols such as Telnet, FTP, HTTP, and SSH. It is used to test the security of "
                           "remote systems by attempting to log in with multiple username and password combinations. "
                           "It can run on multiple operating systems and is commonly used by security professionals "
                           "and penetration testers.")
        ask = first_list()
        if ask == "1":
            ask_install = input("[+] Do you want to install Hydra or not?(y/n)")
            if ask_install == "y" or ask_install == "Y" or ask_install == "Yes" or ask_install == "yes":
                # check for installation
                check_installed("hydra", True)
        elif ask == "2":

            # first argument for dictionary(key=title,value=url) second argument for banner
            writeup(
                {
                    "How to use the hydra for password cracking": "https://www.techtarget.com/searchsecurity/tutorial/How-to-use-the-Hydra-password-cracking-tool",
                    "Hydra Tool For Brute- force attack": "https://systemweakness.com/hydra-tool-for-brute-force-attack-72653db7abe9?gi=efe05fea34af"}
                , "Hydra Writeup")
        else:
            return

        waiting()
    pass


def Johnny():
    while True:
        clear()
        banner.main()
        banner.attack("Johnny")
        banner.description("Johnny is a GUI (Graphical User Interface) for the John the Ripper password cracking "
                           "tool. It provides a user-friendly interface for managing and running John the Ripper's "
                           "cracking tasks, rather than using command line commands. It is designed to make the "
                           "process of cracking passwords more efficient and user-friendly. It can run on Windows, "
                           "Linux and MacOS.")
        ask = first_list()
        if ask == "1":
            ask_install = input("[+] Do you want to install Johnny or not?(y/n)")
            if ask_install == "y" or ask_install == "Y" or ask_install == "Yes" or ask_install == "yes":
                # check for installation
                check_installed("johnny")
        elif ask == "2":
            # first argument for dictionary(key=title,value=url) second argument for banner
            writeup(
                {
                    "How to use the Johnny GUI for password cracking": "https://andregodinho1.medium.com/how-to-use-johnny-an-advanced-password-cracker-recovery-gui-soft-61736c8cb1ca",
                    "Password cracking with Johnny": "https://www.youtube.com/watch?v=Wrg6XZu6Luw"}
                , "Johnny Writeup")
        else:
            return
        waiting()
    pass


def CrackStation():
    while True:
        clear()
        banner.main()
        banner.attack("CrackStation")
        banner.description("CrackStation is a website that provides a service to check if a given password has been "
                           "previously compromised in a data breach. It uses a precomputed hash database of billions "
                           "of real-world passwords to check if a given password is in the list. It's designed to "
                           "help users and organizations check the security of their passwords and identify weak or "
                           "easily guessable passwords that should be changed.")
        ask = first_list()
        if ask == "1":
            run_on_browser("https://crackstation.net/")
            pass
        elif ask == "2":
            # first argument for dictionary(key=title,value=url) second argument for banner
            writeup(
                {
                    "Salted Password Hashing - Doing it Right": "https://crackstation.net/hashing-security.htm",
                    "CrackStation's Password Cracking Dictionary": "https://crackstation.net/crackstation-wordlist-password-cracking-dictionary.htm",
                    "Wordlist Download": "https://crackstation.net/crackstation-wordlist-password-cracking-dictionary.htm"}
                , "Crackstation Writeup")
        else:
            return
        waiting()
    pass


def CyberChef():
    while True:
        clear()
        banner.main()
        banner.attack("CyberChef")
        banner.description("Cyber Chef is a web-based tool developed by the US Cyber Command, that allows users to "
                           "perform digital forensic and incident response tasks, such as data carving, decoding, "
                           "and exfiltration using pre-built 'recipes' or custom workflows using a visual, "
                           "drag-and-drop interface. It can process various types of data and run on different "
                           "platforms. It is generally used by security professionals to quickly process large "
                           "amounts of data, extract useful information and identify potential malicious activity.")
        ask = first_list()
        if ask == "1":
            run_on_browser("https://gchq.github.io/CyberChef/")
            pass
        elif ask == "2":
            # first argument for dictionary(key=title,value=url) second argument for banner
            writeup(
                {
                    "CyberChef - A must have security tool": "https://www.youtube.com/watch?v=rT_CjwKN380",
                    "CyberChef – Data decoding made easy": "https://www.csnp.org/post/cyberchef-data-decoding-made-easy"}
                , "CyberChef Writeup")
        else:
            return
        waiting()
    pass


# Dictionary Tools
def Medusa():
    while True:
        clear()
        banner.main()
        banner.attack("Medusa")
        banner.description("Medusa is a password cracking tool that is used to perform brute-force attacks on login "
                           "credentials. It is a command-line tool that can be used to test the security of login "
                           "systems by trying a large number of possible username and password combinations. Medusa "
                           "is capable of testing various protocols such as HTTP, HTTPS, FTP, SSH, and more. It is "
                           "mainly used by penetration testers and security professionals to identify weak passwords "
                           "in a network and help improve the overall security of an organization. However, "
                           "like other password cracking tools, it can also be used by malicious actors for illegal "
                           "activities.")
        ask = first_list()
        if ask == "1":
            ask_install = input("[+] Do you want to install medusa or not?(y/n)")
            if ask_install == "y" or ask_install == "Y" or ask_install == "Yes" or ask_install == "yes":
                # check for installation
                check_installed("medusa", True)

        elif ask == "2":

            # first argument for dictionary(key=title,value=url) second argument for banner
            writeup(
                {
                    "A Detailed Guide on Medusa": "https://www.hackingarticles.in/a-detailed-guide-on-medusa/",
                    "Bruteforce Password Cracking with Medusa": "https://www.yeahhub.com/bruteforce-password-cracking-medusa-kali-linux/"}
                , "Medusa Writeup")
        else:
            return
        waiting()
    pass


def Ncrack():
    while True:
        clear()
        banner.main()
        banner.attack("Ncrack")
        banner.description("Ncrack is a network authentication cracking tool. It is designed to perform efficient "
                           "brute-force and dictionary attacks against a variety of different network protocols, "
                           "including Telnet, FTP, HTTP, HTTPS, SMB, and RDP. It can be used to test the security of "
                           "networks and remote systems by attempting to log in with a large number of different "
                           "username and password combinations.Ncrack is similar to other password cracking tools "
                           "such as John the Ripper and Hydra, but it is specifically designed to work with network "
                           "protocols. It can run on Windows, Linux, and macOS and is often used by security "
                           "professionals and penetration testers to test the security of networks and web "
                           "applications")
        ask = first_list()
        if ask == "1":
            ask_install = input("[+] Do you want to install Ncrack or not?(y/n)")
            if ask_install == "y" or ask_install == "Y" or ask_install == "Yes" or ask_install == "yes":
                # check for installation
                check_installed("ncrack", True)

        elif ask == "2":

            # first argument for dictionary(key=title,value=url) second argument for banner
            writeup(
                {
                    "Comprehensive Guide on Ncrack – A Brute Forcing Tool": "https://www.hackingarticles.in/comprehensive-guide-on-ncrack-a-brute-forcing-tool/",
                    "Ncrack – Network Authentication and Password Cracking Tool": "https://secnhack.in/ncrack-network-authentication-and-password-cracking-tool/"}
                , "Ncrack Writeup")
        else:
            return
        waiting()
    pass


# Rainbow Attacks
def RainbowCrack():
    while True:
        clear()
        banner.main()
        banner.attack("RainbowCrack")
        banner.description("RainbowCrack is a password cracking tool that uses a large precomputed table of hash "
                           "values to speed up the process of cracking passwords. It is commonly used to crack "
                           "Windows LM hashes and NTLM hashes, as well as other types of hashes such as those used in "
                           "Linux and Unix-based systems. The tool is named after the 'rainbow table' data structure "
                           "it uses to efficiently store the precomputed hash values.")
        ask = first_list()
        if ask == "1":
            ask_install = input("[+] Do you want to install RainbowCrack or not?(y/n)")
            if ask_install == "y" or ask_install == "Y" or ask_install == "Yes" or ask_install == "yes":
                output = subprocess.check_output("which rcrack", shell=True)
                if "rcrack" not in output.decode():
                    print("[-] not installed")
                    download = input("[+] Do you want to install it?(y/n)")
                    if download == "y" or download == "Y" or download == "Yes" or download == "yes":
                        os.system("sudo apt install rcrack")
                        download = input("Do you want to run the tool?(y/n)")
                        if download == "y" or download == "Y" or download == "Yes" or download == "yes":
                            # when tool is of gui it needs thread
                            os.system("rcrack")
                else:
                    print("[+] it is installed !!")
                    download = input("Do you want to run the tool?(y/n)")
                    if download == "y" or download == "Y" or download == "Yes" or download == "yes":
                        # when tool is of gui it needs thread
                        os.system("rcrack")
                    pass

        elif ask == "2":

            # first argument for dictionary(key=title,value=url) second argument for banner
            writeup(
                {
                    "How to use rainbow-crack tool": "https://null-byte.wonderhowto.com/how-to/rainbow-tables-create-use-them-crack-passwords-0131470/",
                    "Rainbow Tables & Rainbow-crack Cracking Passwords": "https://www.kalilinux.in/2021/03/rainbow-tables-rainbowcrack-kali-linux.html"}
                , "rainbow crack Writeup")
        else:
            return
        waiting()
    pass


def ophCrack():
    while True:
        clear()
        banner.main()
        banner.attack("Oph Crack")
        banner.description("Ophcrack is a free, open-source password cracking tool specifically designed to crack "
                           "Windows login passwords. It uses rainbow tables, a precomputed table of hash values, "
                           "to crack passwords quickly. It can also recover LM and NTLM hashes, and it supports a "
                           "variety of hash algorithms such as LM, NTLM, and MD5. The tool is available as a bootable "
                           "CD or USB drive and can be used to recover lost or forgotten Windows passwords.")
        ask = first_list()
        if ask == "1":
            ask_install = input("[+] Do you want to install ophcrack or not?(y/n)")
            if ask_install == "y" or ask_install == "Y" or ask_install == "Yes" or ask_install == "yes":
                # check for installation
                check_installed("ophcrack")

        elif ask == "2":

            # first argument for dictionary(key=title,value=url) second argument for banner
            writeup(
                {
                    "Crack Windows Passwords With Ophcrack and Rainbow Tables": "https://www.wikihow.com/Crack-Windows-Passwords-With-Ophcrack-and-Rainbow-Tables/"}
                , "oph crack Writeup")
        else:
            return
        waiting()
    pass


# Wordlist Generator Tools
def Crunch():
    while True:
        clear()
        banner.main()
        banner.attack("Crunch")
        banner.description("Crunch is a wordlist generator tool that can be used to generate a list of all possible "
                           "combinations of characters for a given set of parameters. It can be used to generate a "
                           "wordlist for password cracking, testing password policies and other security related "
                           "tasks. It is a simple command line tool that can be used to generate wordlists with "
                           "different character sets, lengths, patterns and other parameters. It can also use a "
                           "standard or a custom character set to generate the wordlist and can be used to generate a "
                           "wordlist of any size.")
        ask = first_list()
        if ask == "1":
            ask_install = input("[+] Do you want to install Crunch or not?(y/n)")
            if ask_install == "y" or ask_install == "Y" or ask_install == "Yes" or ask_install == "yes":
                # check for installation
                check_installed("crunch", True)

        elif ask == "2":

            # first argument for dictionary(key=title,value=url) second argument for banner
            writeup(
                {
                    "Create Wordlist Using Crunch": "https://null-byte.wonderhowto.com/how-to/tutorial-create-wordlists-with-crunch-0165931/",
                    "Crunch Password List Generation": "https://www.hackingtutorials.org/general-tutorials/crunch-password-list-generation/",
                    "Complete Guide on Crunch Tool": "https://secnhack.in/complete-guide-on-crunch-tool/",

                }
                , "Crunch Writeup")
        else:
            return
        waiting()
    pass


def Cupp():
    while True:
        clear()
        banner.main()
        banner.attack("Cupp")
        banner.description("CUPP (Common User Passwords Profiler) is a tool that generates a custom wordlist based on "
                           "personal information about a target. It can be used to generate a wordlist based on "
                           "information such as the target's name, birthdate, address, and other personal details. "
                           "CUPP can be used to perform a dictionary attack on a password hash, trying all the "
                           "generated words as passwords, in order to crack the password. CUPP is written in Python "
                           "and it's open source.")
        ask = first_list()
        if ask == "1":
            ask_install = input("[+] Do you want to install Cupp or not?(y/n)")
            if ask_install == "y" or ask_install == "Y" or ask_install == "Yes" or ask_install == "yes":
                # check for installation
                check_installed("cupp", True)

        elif ask == "2":

            # first argument for dictionary(key=title,value=url) second argument for banner
            writeup(
                {
                    "Cybrary CUPP Tool": "https://www.cybrary.it/blog/0p3n/using-cupp-tool-generate-powerful-password-lists/",
                    "How To Create Password List Using CUPP Tool": "https://programmercave0.github.io/blog/2019/10/10/How-to-create-Password-list-using-CUPP-tool-on-ubuntu",
                    "CUPP Tool Password Generator)": "https://www.geeksforgeeks.org/cupp-common-user-passwords-profiler/",

                }
                , "cupp Writeup")
        else:
            return
        waiting()
    pass


def bopscrk():
    while True:
        clear()
        banner.main()
        banner.attack("bopscrk")
        banner.description("Bopscrk (Before Outset Password Cracking is a tool to generate smart and powerful "
                           "wordlists for targeted attacks. It is part of Black Arch Linux for as long as we can "
                           "remember. It introduces personal information related to the target and combines every "
                           "word and transforms it into possible passwords. It also contains a lyric pass module "
                           "which allows it to search lyrics related to the favourite artist of the target and then "
                           "include them into the wordlists.")
        ask = first_list()
        if ask == "1":
            ask_install = input("[+] Do you want to install bopscrk or not?(y/n)")
            if ask_install == "y" or ask_install == "Y" or ask_install == "Yes" or ask_install == "yes":
                # install bopscrk using pip
                output = subprocess.check_output("which bopscrk", shell=True)
                if "bopscrk" not in output.decode():
                    print("[-] not installed")
                    download = input("[+] Do you want to install it?(y/n)")
                    if download == "y" or download == "Y" or download == "Yes" or download == "yes":
                        os.system("sudo pip3 install bopscrk")
                        download = input("Do you want to run the tool?(y/n)")
                        if download == "y" or download == "Y" or download == "Yes" or download == "yes":
                            # when tool is of gui it needs thread
                            os.system("bopscrk -h")
                else:
                    print("[+] it is installed !!")
                    download = input("Do you want to run the tool?(y/n)")
                    if download == "y" or download == "Y" or download == "Yes" or download == "yes":
                        # when tool is of gui it needs thread
                        os.system("bopscrk -h")
                    pass
        elif ask == "2":

            # first argument for dictionary(key=title,value=url) second argument for banner
            writeup(
                {
                    "Create Wordlist Like Pro by Zsecurity": "https://zsecurity.org/create-password-wordlists-like-a-pro-2/",
                    "Wordlist For Pentester": "https://www.hackingarticles.in/wordlists-for-pentester/"
                }
                , "cupp Writeup")
        else:
            return
        waiting()
    pass


# Phishing Tools
def SET():
    while True:
        clear()
        banner.main()
        banner.attack("Social Engineering Toolkit")
        banner.description("The Social Engineering Toolkit (SET) is an open-source penetration testing framework that "
                           "is used to perform various social engineering attacks. It is designed to be used for the "
                           "purposes of penetration testing and vulnerability assessments, and it can be used to "
                           "perform attacks such as phishing, website attacks, and other forms of social engineering. "
                           "The toolkit is written in Python and is available for Windows, Linux, and Mac OS X. It "
                           "can be used to test the security of an organization's employees and to evaluate the "
                           "effectiveness of security awareness training programs.")
        ask = first_list()
        if ask == "1":
            ask_install = input("[+] Do you want to install setoolkit or not?(y/n)")
            if ask_install == "y" or ask_install == "Y" or ask_install == "Yes" or ask_install == "yes":
                # install bopscrk using pip
                output = subprocess.check_output("which setoolkit", shell=True)
                if "setoolkit" not in output.decode():
                    print("[-] not installed")
                    download = input("[+] Do you want to install it?(y/n)")
                    if download == "y" or download == "Y" or download == "Yes" or download == "yes":
                        os.system("sudo apt install set")
                        download = input("Do you want to run the tool?(y/n)")
                        if download == "y" or download == "Y" or download == "Yes" or download == "yes":
                            # when tool is of gui it needs thread
                            os.system("setoolkit")
                else:
                    print("[+] it is installed !!")
                    download = input("Do you want to run the tool?(y/n)")
                    if download == "y" or download == "Y" or download == "Yes" or download == "yes":
                        # when tool is of gui it needs thread
                        os.system("setoolkit")
                    pass
        elif ask == "2":

            # first argument for dictionary(key=title,value=url) second argument for banner
            writeup(
                {
                    "Phishing using SET": "https://www.golinuxcloud.com/social-engineering-toolkit-phishing/",
                    "Phishing using SET by Hengky Sanjaya": "https://medium.com/hengky-sanjaya-blog/social-engineering-toolkit-set-23be8b66aa18"
                }
                , "set Writeup")
        else:
            return
        waiting()
    pass


def HiddenEye():
    while True:
        clear()
        banner.main()
        banner.attack("HiddenEye")
        banner.description("HiddenEye is a modern phishing tool with advanced functionality. It is written in Python "
                           "and can be run on Windows, Linux, and Mac OS X. It allows you to perform various phishing"
                           "attacks.")
        ask = first_list()
        if ask == "1":
            ask_install = input("[+] Do you want to install Hiddeneye or not?(y/n)")
            if ask_install == "y" or ask_install == "Y" or ask_install == "Yes" or ask_install == "yes":
                # install HiddenEye
                if os.path.exists("HiddenEye"):
                    print("[+] Tool is already exits !!")
                    pass
                else:
                    os.system("git clone https://github.com/Morsmalleo/HiddenEye && cd HiddenEye && pip3 "
                              "install -r requirements.txt")
                    pass
                download = input("Do you want to run the tool?(y/n)")
                if download == "y" or download == "Y" or download == "Yes" or download == "yes":
                    os.system("cd HiddenEye && python HiddenEye.py && cd ..")
            else:
                pass
        elif ask == "2":

            # first argument for dictionary(key=title,value=url) second argument for banner
            writeup(
                {
                    "HiddenEye by JohnJHacking": "https://johnjhacking.com/blog/hiddeneye/",
                    "HiddenEye by Zsecurity": "https://zsecurity.org/hiddeneye-with-ngrok-all-in-one-phishing-solution/",
                    "HiddenEye by Null-Byte": "https://null-byte.wonderhowto.com/forum/phish-with-hiddeneye-tool-with-advanced-feature-0323221/"
                }
                , "HiddenEye Writeup")
        else:
            return
        waiting()
    pass


def r3bu5():
    while True:
        clear()
        banner.main()
        banner.attack("r3bu5")
        banner.description("It is a Phishing tool that has latest and updated login pages, Mask URL support, "
                           "Beginners Friendly, Multiple tunneling options")
        ask = first_list()
        if ask == "1":
            ask_install = input("[+] Do you want to install r3bu5 or not?(y/n)")
            if ask_install == "y" or ask_install == "Y" or ask_install == "Yes" or ask_install == "yes":
                # install r3bu5
                if os.path.exists("r3bu5"):
                    print("[+] Tool is already exits !!")
                    pass
                else:
                    os.system("git clone https://github.com/k46-db0y/r3bu5 && cd r3bu5 && chmod +x r3bu5.sh")
                    pass
                download = input("Do you want to run the tool?(y/n)")
                if download == "y" or download == "Y" or download == "Yes" or download == "yes":
                    os.system("cd r3bu5 && bash r3bu5.sh  && cd ..")
            else:
                pass
        elif ask == "2":

            # first argument for dictionary(key=title,value=url) second argument for banner
            writeup(
                {
                    "Github Repo of r3bu5": " https://github.com/k46-db0y/r3bu5"
                }
                , "r3bu5 Writeup")
        else:
            return
        waiting()
    pass


def zphisher():
    while True:
        clear()
        banner.main()
        banner.attack("zphisher")
        banner.description("Zphisher is an open-source phishing tool that automates the process of creating and "
                           "deploying phishing pages. It allows users to easily create phishing pages for various "
                           "popular websites, such as Google, Facebook, and LinkedIn, and can be used to perform "
                           "phishing attacks on targeted individuals or organizations. It can also be used to test "
                           "the security awareness of an organization's employees. Zphisher is written in Shell "
                           "Script and it's available for Linux and Termux.")
        ask = first_list()
        if ask == "1":
            ask_install = input("[+] Do you want to install zphisher or not?(y/n)")
            if ask_install == "y" or ask_install == "Y" or ask_install == "Yes" or ask_install == "yes":
                # install zphisher
                if os.path.exists("zphisher"):
                    print("[+] Tool is already exits !!")
                    pass
                else:
                    os.system("git clone https://github.com/htr-tech/zphisher && cd zphisher && chmod +x zphisher.sh")
                    pass
                download = input("Do you want to run the tool?(y/n)")
                if download == "y" or download == "Y" or download == "Yes" or download == "yes":
                    os.system("cd zphisher && ./zphisher.sh && cd ..")
            else:
                pass
        elif ask == "2":

            # first argument for dictionary(key=title,value=url) second argument for banner
            writeup(
                {
                    "Zphisher phishing tool by reconshell": "https://reconshell.com/zphisher-an-automated-phishing-tool/",
                    "Zphisher phishing tool by vulners": "https://vulners.com/kitploit/KITPLOIT:1994086289094110137"
                }
                , "zphisher Writeup")
        else:
            return
        waiting()
    pass


def Shellphish():
    while True:
        clear()
        banner.main()
        banner.attack("Shellphish")
        banner.description("Shellphish is a tool used for phishing attacks, specifically for the purpose of stealing "
                           "login credentials. It automates the process of creating phishing pages for various "
                           "websites, such as social media platforms and email services. The tool is typically used "
                           "by ethical hackers and penetration testers to test the security of a system, but can also "
                           "be used by malicious actors for illegal activities.")
        ask = first_list()
        if ask == "1":
            ask_install = input("[+] Do you want to install Shellphish or not?(y/n)")
            if ask_install == "y" or ask_install == "Y" or ask_install == "Yes" or ask_install == "yes":
                # install Shellphish
                if os.path.exists("ShellPhish"):
                    print("[+] Tool is already exits !!")
                    pass
                else:
                    os.system("git clone https://github.com/AbirHasan2005/ShellPhish && cd ShellPhish && chmod +x"
                              " shellphish.sh")
                    pass
                download = input("Do you want to run the tool?(y/n)")
                if download == "y" or download == "Y" or download == "Yes" or download == "yes":
                    os.system("cd ShellPhish && ./shellphish.sh && cd .. ")
            else:
                pass
        elif ask == "2":

            # first argument for dictionary(key=title,value=url) second argument for banner
            writeup(
                {
                    "Shellphish Tool Writeup": "https://www.kalilinux.in/2019/04/shellphish-phishing-page-creator.html"
                }
                , "Shellphish Writeup")
        else:
            return
        waiting()
    pass


def Gophish():
    while True:
        clear()
        banner.main()
        banner.attack("Gophish")
        banner.description("Gophish is an open-source tool for conducting phishing campaigns. It allows users to "
                           "create, send and track phishing campaigns, including the ability to create custom "
                           "phishing templates and landing pages, as well as track user interactions with the "
                           "phishing emails. Gophish is often used by penetration testers and security professionals "
                           "to test the security of an organization's email system and educate employees on how to "
                           "spot and avoid phishing attempts. However, like other phishing tools, it can also be used "
                           "by malicious actors for illegal activities.")
        ask = first_list()
        if ask == "1":
            ask_install = input("[+] Do you want to install Gophish or not?(y/n)")
            if ask_install == "y" or ask_install == "Y" or ask_install == "Yes" or ask_install == "yes":
                # install Gophish
                print("[+] Downloading.......")
                time.sleep(5)

                # if [ -d 'Gophish' ]; then echo 'Already Exists'; else sudo mkdir Gophish && cd Gophish && sudo wget
                # https://github.com/gophish/gophish/releases/download/v0.12.1/gophish-v0.12.1-linux-64bit.zip
                # 2>/dev/null && sudo unzip gophish-v0.12.1-linux-64bit.zip >/dev/null && sudo chmod +x gophish && (
                # sudo ./gophish 2>/dev/null &) && cd .. ; fi

                os.system("mkdir Gophish && cd Gophish && wget "
                          "https://github.com/gophish/gophish/releases/download/v0.12.1/gophish-v0.12.1-linux-64bit"
                          ".zip && unzip gophish-v0.12.1-linux-64bit.zip > /dev/null 2>&1 && chmod +x gophish && "
                          "./gophish && cd ..")

                # output = subprocess.Popen(["./gophish"], shell=True, stdout=subprocess.DEVNULL,
                #                           stderr=subprocess.DEVNULL)
                run_on_browser("https://127.0.0.1:3333/")

            else:
                pass
        elif ask == "2":

            # first argument for dictionary(key=title,value=url) second argument for banner
            writeup(
                {
                    "Shellphish Tool Writeup": "https://www.kalilinux.in/2019/04/shellphish-phishing-page-creator.html"
                }
                , "Gophish Writeup")
        else:
            return
        waiting()
    pass


def Smikta():
    while True:
        clear()
        banner.main()
        banner.attack("Smikta")
        banner.description("The website offers a variety of pre-made phishing pages for popular websites such as"
                           "Facebook, Gmail, and Instagram, which can be used to steal login credentials. It also"
                           "provides tutorials on how to use these pages and other hacking techniques.")
        ask = first_list()
        if ask == "1":
            run_on_browser("https://smikta.info/")
            pass
        elif ask == "2":
            # first argument for dictionary(key=title,value=url) second argument for banner
            writeup(
                {
                    "Smikta Tutorial": "https://www.youtube.com/watch?v=lf9RrTcGwFU"}
                , "Smikta Writeup")
        else:
            return
        waiting()
    pass


# Keylogger Tool
def ZLogger():
    while True:
        clear()
        banner.main()
        banner.attack("ZLogger")
        banner.description("zLogger is a Remote persistent keylogger it is written in python, and can generate "
                           "executables that run on Windows and Linux, once executed on a system it’ll run the "
                           "background, record every key-strike and report to the email specified when the keylogger "
                           "was generated.")
        ask = first_list()
        if ask == "1":
            ask_install = input("[+] Do you want to install ZLogger or not?(y/n)")
            if ask_install == "y" or ask_install == "Y" or ask_install == "Yes" or ask_install == "yes":
                # install ZLogger
                if os.path.exists("ZLogger"):
                    print("[+] Tool is already exits !!")
                    pass
                else:
                    os.system("git clone https://github.com/z00z/ZLogger && cd ZLogger && pip install pynput")
                    pass
                download = input("Do you want to run the tool?(y/n)")
                if download == "y" or download == "Y" or download == "Yes" or download == "yes":
                    os.system("cd ZLogger && python zlogger.py -h && cd ..")
            else:
                pass
        elif ask == "2":

            # first argument for dictionary(key=title,value=url) second argument for banner
            writeup(
                {
                    "ZLogger Tool in Medium": "https://medium.com/purple-team/make-a-keylogger-using-the-zlogger-tool-9945bc87922",
                    "ZLogger by Zsecurity": "https://zsecurity.org/hiddeneye-with-ngrok-all-in-one-phishing-solution/",
                    "ZLogger in Null-Byte": "https://null-byte.wonderhowto.com/forum/phish-with-hiddeneye-tool-with-advanced-feature-0323221/"
                }
                , "ZLogger Writeup")
        else:
            return
        waiting()


if __name__ == "__main__":
    main()
