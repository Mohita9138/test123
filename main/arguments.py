import dns.resolver, requests, socket, os, time
import random
from selenium import webdriver
from ipwhois import IPWhois
from main.tools import colors, banner


def getip(domain_name):
    ip_address = socket.gethostbyname(domain_name)
    banner.main()
    banner.attack("Get Ip")
    print(
        f"{colors.green}The IP address of {domain_name} is {ip_address}{colors.reset}"
    )


def ipinformation(ip):
    banner.main()
    banner.attack("Get Ip Infomation")
    print("waiting..\r", end="")
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)

    data = response.json()
    for key, value in data.items():
        print(f"{colors.blue}[+] {key}\t --> \t{colors.green}{value}{colors.reset}")


def dnsrecords(domain, names):
    banner.main()
    banner.attack("DNS Records")
    names = names.upper()
    names = names.split(",")
    for name in names:
        try:
            answers = dns.resolver.resolve(domain, name)
            for answer in answers:
                print(
                    f"{colors.blue}[+] {name}\t -->\t{colors.green}{answer}{colors.reset}"
                )
        except dns.rdatatype.UnknownRdatatype:
            print(f"{colors.red}[-] Wrong Record Input{colors.reset}")
        except dns.resolver.NoAnswer:
            print(f"{colors.red}[-] No {name} Record Found{colors.reset}")
        except dns.resolver.NXDOMAIN:
            print(f"{colors.red}[-] Host {domain} Not Found{colors.reset}")


def checking(result_str):
    print(f"{colors.green}Checking for password{colors.reset}")
    passwords = [
        "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/xato-net-10-million-passwords.txt",
        "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt",
        "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-100000.txt",
        "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/xato-net-10-million-passwords-1000000.txt",
    ]
    for link in range(len(passwords)):
        pass_check(passwords[link], result_str, link)


def pass_check(url, password, number):
    print(f"{colors.blue}Test {number}{colors.reset}")
    raw = requests.get(url)
    lists = raw.text.split("\n")
    for i in lists:
        if password == i:
            print(f"{colors.red}FAILED{colors.reset}")
    else:
        print(f"{colors.green}PASSED{colors.reset}")


def exit_program():
    print("\033[38;5;105m", "[+] Thanks visit again".title())
    exit()


def asnrecord(path="", url="", output=""):
    banner.main()
    banner.attack("ASN")
    if path != "":
        try:
            f = open(path, "r")
            urls = f.read()
            urls = urls.split("\n")
            for url in urls:
                if url != "":
                    try:
                        ipwhois = IPWhois(url)
                        result = ipwhois.lookup_rdap()
                        if output != "":
                            outputfunc(output, f"{url}\t --> {result['asn']}")
                        print(
                            f"{colors.blue}[+] {url}\t --> {colors.green}{result['asn']}{colors.reset}"
                        )
                    except KeyboardInterrupt:
                        exit_program()
                    except:
                        if output != "":
                            outputfunc(output, f"{url}\t --> Something Went Wrong")
                        print(
                            f"{colors.red}[+] {url}\t --> {colors.red}Something Went Wrong{colors.reset}"
                        )
        except Exception as err:
            print(
                f"{colors.red}[-] Something Went Wrong\n[!] {err}\n[!] Check Your File location"
            )
    else:
        try:
            ipwhois = IPWhois(url)
            result = ipwhois.lookup_rdap()
            if output != "":
                outputfunc(output, f"{url}\t --> {result['asn']}")
            print(
                f"{colors.blue}[+] {url}\t --> {colors.green}{result['asn']}{colors.reset}"
            )
        except KeyboardInterrupt:
            exit_program()
        except:
            if output != "":
                outputfunc(output, f"{url}\t --> Something Went Wrong")
            print(
                f"{colors.red}[+] {url}\t --> {colors.red}Something Went Wrong{colors.reset}"
            )


def outputfunc(addr, line):
    f = open(addr, "a")
    f.write(line)
    f.write("\n")
    f.close()


def http_status_code(path="", url="", output=""):
    banner.main()
    banner.attack("HTTP Status Code")
    if path != "":
        try:
            f = open(path, "r")
            urls = f.read()
            urls = urls.split("\n")
            for url in urls:
                if url != "":
                    try:
                        headers = {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
                        }
                        response = requests.get(url, headers=headers, timeout=20)
                        status = str(response.status_code)
                        if status[0] == "1":
                            print(
                                f"{colors.blue}[+] {url}\t --> {colors.light_blue}{status}{colors.reset}"
                            )
                        elif status[0] == "2":
                            print(
                                f"{colors.blue}[+] {url}\t --> {colors.green}{status}{colors.reset}"
                            )
                        elif status[0] == "3":
                            print(
                                f"{colors.blue}[+] {url}\t --> {colors.yellow}{status}{colors.reset}"
                            )
                        elif status[0] == "4":
                            print(
                                f"{colors.blue}[+] {url}\t --> {colors.red}{status}{colors.reset}"
                            )
                        elif status[0] == "5":
                            print(
                                f"{colors.blue}[+] {url}\t --> {colors.purple}{status}{colors.reset}"
                            )
                        else:
                            print(
                                f"{colors.blue}[+] {url}\t --> {colors.green}{status}{colors.reset}"
                            )
                        if output != "":
                            outputfunc(output, f"{url}\t --> {status}")
                    except Exception as err:
                        if "timed out" in str(err):
                            err = "Connection Time Outed"
                        else:
                            err = "Something Went Wrong"
                        if output != "":
                            outputfunc(output, f"{url}\t --> {err}")
                        print(
                            f"{colors.red}[+] {url}\t --> {colors.red}{err}{colors.reset}"
                        )
                time.sleep(0.5)
        except Exception as err:
            print(f"{colors.red}[-] Something Went Wrong\n[!] {err}")
    else:
        try:
            response = requests.get(url)
            status = str(response.status_code)
            if output != "":
                outputfunc(output, f"{url}\t --> {status}")
            if status[0] == "1":
                print(
                    f"{colors.blue}[+] {url}\t --> {colors.light_blue}{status}{colors.reset}"
                )
            elif status[0] == "2":
                print(
                    f"{colors.blue}[+] {url}\t --> {colors.green}{status}{colors.reset}"
                )
            elif status[0] == "3":
                print(
                    f"{colors.blue}[+] {url}\t --> {colors.yellow}{status}{colors.reset}"
                )
            elif status[0] == "4":
                print(
                    f"{colors.blue}[+] {url}\t --> {colors.red}{status}{colors.reset}"
                )
            elif status[0] == "5":
                print(
                    f"{colors.blue}[+] {url}\t --> {colors.purple}{status}{colors.reset}"
                )
            else:
                print(
                    f"{colors.blue}[+] {url}\t --> {colors.green}{status}{colors.reset}"
                )
        except:
            print(
                f"{colors.red}[+] {url}\t --> {colors.red}Something Went Wrong{colors.reset}"
            )


def password_gen(
    upper=True, lower=True, digit=True, punctuation=True, length="8", check=True
):
    banner.main()
    banner.attack("Password Generators")
    ascii_lowercase = "abcdefghijklmnopqrstuvwxyz"
    ascii_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    string_digits = "0123456789"
    string_punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    main_password = ""
    if upper:
        main_password += ascii_uppercase
    if lower:
        main_password += ascii_lowercase
    if digit:
        main_password += string_digits
    if punctuation:
        main_password += string_punctuation
    result_str = "".join(random.choice(main_password) for i in range(int(length)))
    print(
        f"{colors.blue}[+] Your Passwrod Is: {colors.green}{result_str}{colors.reset}"
    )
    if check:
        checking(result_str)
def remove_dublicates(location,output=''):
    f=open(location,'r')
    lines=f.read()
    lines=lines.split('\n')
    readed=[]
    for line in lines:
        if line not in readed:
            readed.append(line)
    f.close()
    if output=='':
        if not os.path.isdir("duplicate"):
            os.system("mkdir duplicate")
        location=location.split('.')
        location=location[0].split('/')
        fn=open(f"duplicate/{location[(len(location)-1)]}_removed.txt",'a')
        for read in readed:
            fn.write(read)
            fn.write('\n')
        fn.close()
    else:
        location=location.split('.')
        location=location[0].split('/')
        fn=open(f'{output}',"a")
        for read in readed:
            fn.write(read)
            fn.write('\n')
        fn.close()


        

def screenshot(path="", url=""):
    banner.main()
    banner.attack("Screenshotting")
    if path != "":
        try:
            f = open(path, "r")
            urls = f.read()
            urls = urls.split("\n")
            for url in urls:
                if url != "":
                    driver_path = "main/tools/.driver/geckodriver"
                    firefox_options = webdriver.FirefoxOptions()
                    firefox_options.headless = True
                    driver = webdriver.Firefox(
                        executable_path=driver_path, options=firefox_options
                    )
                    try:
                        driver.get(url)
                        url_new = url.split("//")
                        path = os.getcwd()
                        screenshot_filename = f"{path}/Screenshot/{url_new[1]}.png"
                        if not os.path.isdir("Screenshot"):
                            os.system("mkdir Screenshot")
                        driver.save_screenshot(screenshot_filename)
                        print(
                            f"{colors.blue}[+] {url}\t --> {colors.green}Screenshot saved to {screenshot_filename}{colors.reset}"
                        )
                        driver.quit()
                    except KeyboardInterrupt:
                        exit_program()
                    except:
                        print(
                            f"{colors.red}[+] {url}\t --> {colors.red}Something Went Wrong{colors.reset}"
                        )
        except Exception as err:
            print(
                f"{colors.red}[-] Something Went Wrong\n[!] {err}\n[!] Check Your File location"
            )
    else:
        driver_path = "main/tools/.driver/geckodriver"
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.headless = True
        driver = webdriver.Firefox(executable_path=driver_path, options=firefox_options)
        try:
            driver.get(url)
            url_new = url.split("//")
            path = os.getcwd()
            screenshot_filename = f'{path}/Screenshot/{url_new[1].replace("/","_")}.png'
            if not os.path.isdir("Screenshot"):
                os.system("mkdir Screenshot")
            driver.save_screenshot(screenshot_filename)
            print(
                f"{colors.blue}[+] {url}\t --> {colors.green}Screenshot saved to {screenshot_filename}{colors.reset}"
            )
            driver.quit()
        except KeyboardInterrupt:
            exit_program()
        except:
            print(
                f"{colors.red}[+] {url}\t --> {colors.red}Something Went Wrong{colors.reset}"
            )
