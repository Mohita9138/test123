import banner
import os
import subprocess
import threading
import time
import requests
from bs4 import BeautifulSoup
import run_on_browser
try:
    def check_installed(name,needargs=False):
        proc = subprocess.Popen([f"dpkg -s {name}"], stdout=subprocess.PIPE, shell=True)
        #there keyfor success output and noththere for error output
        (there, notthere) = proc.communicate()
        if "install ok installed" not in there.decode():
                    print("[-] not installed")
                    print("[+] it is not installed in your Kali")
                    download=input("[+] Do you want to install it?(y/n)")
                    if download=="y" or download=="Y" or download=="Yes" or download=="yes":
                        os.system(f"apt install {name} -y")
                        if needargs:
                            download=input("Do you want to run the tool?(y/n)")
                            if download=="y" or download=="Y" or download=="Yes" or download=="yes":
                                #when tool is of cli no need of thread
                                thread_run(name,needargs)
                        else:
                            download=input("Do you want to run the tool?(y/n)")
                            if download=="y" or download=="Y" or download=="Yes" or download=="yes":
                                #when tool is of gui it needs thread
                                threading.Thread(target=thread_run, args=(name,)).start()
        else:
                    print("[+] Installed")
                    print("[+] it is installed in your kali")
                    if needargs:
                            download=input("Do you want to run the tool?(y/n)")
                            if download=="y" or download=="Y" or download=="Yes" or download=="yes":
                                #when tool is of cli no need of thread
                                thread_run(name,needargs)
                    else:
                            download=input("Do you want to run the tool?(y/n)")
                            if download=="y" or download=="Y" or download=="Yes" or download=="yes":
                                #when tool is of gui it needs thread
                                threading.Thread(target=thread_run, args=(name,)).start()
    
    def thread_run(command,needargs=False):
        if needargs=="no-help":
            #it will run only help because it is in cli
            os.system(f"{command}")
        elif needargs:
            os.system(f"{command} -h")
        else:
            #for gui all errors/output will go in null 
            os.system(f"{command} > /dev/null 2>&1")

    def github_getting_text(link,selector,indexvalue):
        print("Please Wait....\r",end="")
        URL = link
        try:
            r = requests.get(URL)
            soup = BeautifulSoup(r.content, 'html5lib')
            paras = soup.select(selector)
            #check index value from test file
            return paras[indexvalue].text
        except:
            return "Not loaded because no internet connection"

    def main():
        while True:
            os.system("clear")
            banner.main()
            banner.attack("WEB Application Analysis")
            list_attacks=["Burp Suite","Owasp ZAP","Nikto","Wapiti","Nessus","dirb","skipfish","Nuclei","go back"]
            for i in range(len(list_attacks)):
                print(f"{i}) {list_attacks[i]}")

            option = input("\n Select an option ->  ")
            if option=="0":
                print("\n[+] Burp Suite")
                os.system("clear")
                burp_suite()
            elif option=="1":
                print("\n[+] Owasp ZAP")
                os.system("clear")
                Owasp_ZAP()
            elif option=="2":
                print("\n[+] Nikto")
                os.system("clear")
                Nikto()
            elif option=="3":
                print("\n[+] Wapiti")
                os.system("clear")
                Wapiti()
            elif option=="4":
                print("\n[+] Nessus")
                os.system("clear")
                Nessus()
            elif option=="5":
                print("\n[+] dirb")
                os.system("clear")
                dirb()
            elif option=="6":
                print("\n[+] skipfish")
                os.system("clear")
                skipfish()
            elif option=="7":
                print("\n[+] Nuclei")
                os.system("clear")
                Nuclei()
            else:
                return
    def burp_suite():
        while True:
            os.system("clear")
            banner.main()
            banner.attack("Burp Suite")
            banner.description("Burp Suite is an integrated platform for performing security testing of web applications. Its various tools work seamlessly together to support the entire testing process, from initialmapping and analysis of an application's attack surface, through to finding and exploiting security vulnerabilities. Burp gives you full control, letting you combine advanced manual techniques with state-of-the-art automation, to make your work faster, more effective, and more fun.")
            ask=tool_writeups()
            if ask=="1":
                ask_install=input("[+] Do you want to install burp Suit or not?(y/n)")
                if ask_install=="y" or ask_install=="Y" or ask_install=="Yes" or ask_install=="yes":
                    professional=input("[+] Do you want it's professional?(Y/N)")
                    if professional=="y" or professional=="Y" or professional=="Yes" or professional=="yes":
                        #clone repo
                        os.system("git clone https://github.com/hardikhacker/Burp-Suite")
                        os.system("cd Burp-Suite && chmod +x * && ./Kali_Linux_Setup.sh")
                    else:
                        #check for installation
                        check_installed("burpsuite")
                        waiting()
            elif ask=="2":
                #first argument for dictionary(key=title,value=url) second argument for banner 
                writeup({"Top 10 tips for burpsuite":"https://medium.com/r3d-buck3t/top-10-tips-for-burp-suite-72212d22328f","Setting up burbsuite":"https://thexssrat.medium.com/setting-up-burp-suite-b0a6767d3408","Burp Suite: Do I need the professional edition?":"https://thexssrat.medium.com/burp-suite-do-i-need-the-professional-edition-bf8c87ce236e","Burp Suite Extensions to help you Pentest":"https://medium.com/codex/burp-suite-extensions-to-help-you-pentest-97f22a7d7d4d","FIND MORE resources here":"https://medium.com/search?q=burpsuite"},"Brup Suit Writeup")
            else:
                return

    def Owasp_ZAP():
        while True:
            os.system("clear")
            banner.main()
            banner.attack("Owasp ZAP")
            banner.description("The OWASP Zed Attack Proxy (ZAP) is an easy to use integrated penetration testing tool for finding vulnerabilities in web applications.\nIt is designed to be used by people with a wide range of security experience and as such is ideal for developers and functional testers who are new to penetration testing as well as being a useful addition to an experienced pen testers toolbox. https://www.owasp.org/index.php/ZAP")
            ask=tool_writeups()
            if ask=="1":
                print("[+] Download/usage")
                print("\n Preinstalled in Repository")
                print("\n Go to Application section and search for `zap`")
                check_installed("zaproxy")
                waiting()
            elif ask=="2":
                writeup({"How to setup OWASP ZAP to scan your web application for security vulnerabilities":"https://www.linkedin.com/pulse/how-setup-owasp-zap-scan-your-web-application-security-botla/","Authenticated Scan using OWASP-ZAP":"https://medium.com/@secureica/authenticated-scan-using-owasp-zap-f0a71dafe41","OWASP ZAP: 6 Key Capabilities and a Quick Tutorial":"https://www.hackerone.com/knowledge-center/owasp-zap-6-key-capabilities-and-quick-tutorial","Initial Setup":"https://infosecgirls.gitbook.io/infosecgirls-training/v/appsec/initial-setup-with-owasp-zap/untitled","Setup OWASP ZAP":"https://infosecgirls.gitbook.io/infosecgirls-training/v/appsec/initial-setup-with-owasp-zap/setup-owasp-zap"},"Owasp ZAP writeup")
            else:
                return

    def Nikto():
        while True:
            os.system("clear")
            banner.main()
            banner.attack("Nikto")
            github=github_getting_text("https://github.com/sullo/nikto/wiki/Overview-&-Description",'div[class="markdown-body"]',0)
            banner.description(github)
            print("\n")
            ask=tool_writeups()
            if ask=="1":
                print("[+] Download/usage")
                github=github_getting_text("https://github.com/sullo/nikto",'pre[class="notranslate"]',1)
                print(github)
                print("\n Preinstalled in Repository")
                check_installed("nikto",True)
                waiting()
            elif ask=="2":
                writeup({"What is nikto and its usages":"https://www.geeksforgeeks.org/what-is-nikto-and-its-usages/","Nikto website vulnerability scanner":"https://securitytrails.com/blog/nikto-website-vulnerability-scanner","Nikto webserver scanner":"https://geekflare.com/nikto-webserver-scanner/","What is Nikto Tool in Kali and how to use it?":"https://www.cyber-today.com/what-is-nikto-tool-in-kali-and-how-to-use-it/","Basic Testing":"https://github.com/sullo/nikto/wiki/Basic-Testing"},"Nikto writeup")
            else:
                return
    def Wapiti():
        while True:
            os.system("clear")
            banner.main()
            banner.attack("Wapiti")
            github=github_getting_text("https://github.com/wapiti-scanner/wapiti",'p[dir="auto"]',6)
            banner.description(github)
            print("\n")
            ask=tool_writeups()
            if ask=="1":
                print("\n Preinstalled in Repository")
                check_installed("wapiti",True)
                waiting()
            elif ask=="2":
                writeup({"wapiti free web application vulnerability scanner":"https://pentestit.medium.com/wapiti-free-web-application-vulnerability-scanner-ce7712adf644","Official docs":"https://github.com/wapiti-scanner/wapiti","wapiti tutorial":"https://www.kalilinux.in/2021/01/wapiti-tutorial.html","complete guide to using wapiti web vulnerability scanner to keep your web applications websites secure":"https://linuxsecurity.com/features/complete-guide-to-using-wapiti-web-vulnerability-scanner-to-keep-your-web-applications-websites-secure"},"Wapiti writeup")
            else:
                return
    def Nessus():
        while True:
            os.system("clear")
            banner.main()
            banner.attack("Nessus")
            github=github_getting_text("https://www.techtarget.com/searchnetworking/definition/Nessus",'section[id="content-body"]',0)
            banner.description(github)
            ask=tool_writeups()
            if ask=="1":
                print("\n Only config availabe in Repository")
                print("Checking if nessus available in you kali or not .......")
                proc = subprocess.Popen([f"dpkg -s Nessus"], stdout=subprocess.PIPE, shell=True)
                (there, notthere) = proc.communicate()
                if "install ok installed" not in there.decode():
                            print("[-] not installed")
                            print("[+] it is not installed in your Kali")
                            download=input("[+] Do you want to install it?(y/n)")
                            if download=="y" or download=="Y" or download=="Yes" or download=="yes":
                                os.system("curl --request GET --url 'https://www.tenable.com/downloads/api/v2/pages/nessus/files/Nessus-10.4.2-debian9_amd64.deb' --output 'Nessus-10.4.2-debian9_amd64.deb'")
                                os.system(f"dpkg -i Nessus-10.4.2-debian9_amd64.deb")
                                use=input("[+] Do you want to start it's services?(y/n)")
                                if use=="y" or use=="Y" or use=="Yes" or use=="yes":
                                    os.system("systemctl start nessusd.service")
                                    print("[+] Service started....")
                                    print("[+] YOU CAN CHECK IT'S WRITE UPS FOR MORE INFO")
                                    use=input("[+] Do you want to configure Nessus?(y/n)")
                                    if use=="y" or use=="Y" or use=="Yes" or use=="yes":
                                        threading.Thread(target=run_on_browser.main, args=("https://kali:8834/",)).start()
                else:
                    print("[+] It is installed in you pc......")
                    use=input("[+] Do you want to start it's services?(y/n)")
                    if use=="y" or use=="Y" or use=="Yes" or use=="yes":
                                    os.system("systemctl start nessusd.service")
                                    print("[+] Service started....")
                                    print("[+] YOU CAN CHECK IT'S WRITE UPS FOR MORE INFO")
                                    use=input("[+] Do you want to configure Nessus?(y/n)")
                                    if use=="y" or use=="Y" or use=="Yes" or use=="yes":
                                        threading.Thread(target=run_on_browser.main, args=("https://kali:8834/",)).start()
                waiting()
                #check_installed("wapiti",True)
                
            elif ask=="2":
                writeup({"How To: Run Your First Vulnerability Scan with Nessus":"https://www.tenable.com/blog/how-to-run-your-first-vulnerability-scan-with-nessus","A brief introduction to the Nessus vulnerability scanner":"https://resources.infosecinstitute.com/topic/a-brief-introduction-to-the-nessus-vulnerability-scanner/","Beginner’s Guide to Nessus":"https://www.hackingarticles.in/beginners-guide-to-nessus/","Nessus Ubuntu Installation and Tutorial":"https://linuxhint.com/nessus-ubuntu-installation-tutorial/"},"Nessus writeup")
            else:
                return

    def dirb():
        while True:
            os.system("clear")
            banner.main()
            banner.attack("Dirb")
            banner.description("DIRB IS a Web Content Scanner. It looks for existing (and/or hidden) Web Objects. It basically works by launching a dictionary basesd attack against a web server and analizing the response")
            ask=tool_writeups()
            if ask=="1":
                print("[+] Download/usage")
                github=github_getting_text("https://www.kali.org/tools/dirb/#tool-documentation",'pre',0)
                print(github)
                print("\n Preinstalled in Repository")
                check_installed("dirb","no-help")
                waiting()
            elif ask=="2":
                writeup({"Dirb — A web content scanner":"https://medium.com/tech-zoom/dirb-a-web-content-scanner-bc9cba624c86","Footprinting and Reconnaissance with DIRB Tool (For Security Researcher and Bug Bounty Hunters":"https://www.openbugbounty.org/blog/mas00712/footprinting-and-reconnaissance-with-dirb-tool-for-security-researcher-and-bug-bounty-hunters/","Comprehensive Guide on Dirb Tool":"https://www.hackingarticles.in/comprehensive-guide-on-dirb-tool/"},"Nessus writeup")
            else:
                return

    def skipfish():
        while True:
            os.system("clear")
            banner.main()
            banner.attack("skipfish")
            banner.description("Skipfish is an active web application security reconnaissance tool. It prepares an interactive sitemap for the targeted site by carrying out a recursive crawl and dictionary-based probes. The resulting map is then annotated with the output from a number of active (but hopefully non-disruptive) security checks. The final report generated by the tool is meant to serve as a foundation for professional web application security assessments.")
            ask=tool_writeups()
            if ask=="1":
                print("[+] Download/usage")
                print("\n Preinstalled in Repository")
                check_installed("skipfish",True)
                waiting()
            elif ask=="2":
                writeup({"Skipfish in Kali Linux":"https://www.javatpoint.com/skipfish-in-kali-linux","Skipfish – Penetration Testing tool in Kali Linux":"https://www.geeksforgeeks.org/skipfish-penetration-testing-tool-in-kali-linux/","skipfish (1) - Linux Man Pages":"https://www.systutorials.com/docs/linux/man/1-skipfish/","Skipfish – Web Application Security Scanner for XSS, SQL Injection, Shell injection":"https://gbhackers.com/skipfish-web-application-security-scanner/"},"skipfish writeup")
            else:
                return
    def Nuclei():
        while True:
            os.system("clear")
            banner.main()
            banner.attack("Nuclei")
            github=github_getting_text("https://github.com/projectdiscovery/nuclei",'p[dir="auto"]',3)
            banner.description(github)
            ask=tool_writeups()
            if ask=="1":
                print("[+] Download/usage")
                print("\n Preinstalled in Repository")
                check_installed("skipfish",True)
                waiting()
            elif ask=="2":
                writeup({"Nuclei - Automated Vulnerability Scanning Tool":"https://allabouttesting.org/nuclei-automated-vulnerability-scanning-tool/","Nuclei – Fast and Customizable Vulnerability Scanner":"https://www.geeksforgeeks.org/nuclei-fast-and-customizable-vulnerability-scanner/","Gauing+Nuclei for Instant Bounties":"https://infosecwriteups.com/gauing-nuclei-for-instant-bounties-7a8a07979fff ","DevSecOps 101 Part 3: Scanning Live Web Applications with Nuclei":"https://escape.tech/blog/devsecops-part-iii-scanning-live-web-applications"},"Nuclei writeup")
            else:
                return
    def tool_writeups():
        print("1) TOOL(about,installation)")
        print("2) Write ups")
        print("3) go back..")
        ask=input("Select an option ->  ")
        return ask
    def writeup(writeup_dist,name):
        while True:
            os.system("clear")
            banner.main()
            banner.attack(name)
            #convert dict keys in list(type casting)
            key=list(writeup_dist.keys())
            key.append("go back")
            for i in range(len(key)):
                print(f"{i}) {key[i]}")
            option = input("\n Select an option ->  ")
            #1-9=int kdsjfhgkjds=int X to type cast safely 
            try:
                threading.Thread(target=run_on_browser.main, args=(writeup_dist[key[int(option)]],)).start()
                
            except:
                return
    def waiting():
            input("\n[+]press ENTER to go back ")
except:
    print("thanks ...")

if __name__ == "__main__": 
    main()