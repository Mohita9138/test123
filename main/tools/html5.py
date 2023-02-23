import threading
from bs4 import BeautifulSoup
from main.tools import banner,template,waiting,writeup,colors,run_on_browser
import os
import requests
from bs4 import BeautifulSoup

def main():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("DOS ATTACK - BUG BOUNTY")
        list_vulns = ["WEB Messaging", "WEB Storage SQL Injection", "CORS Implementation", "Offline Web Applicatipn"]
        for i in range(len(list_vulns)):
            print(colors.options,f"{i}) {list_vulns[i]}".title(),colors.reset)
        vulns =  input(f"\n {colors.select}Select An Option ->{colors.reset}  ")
        while True:
            os.system("clear")
            banner.main()
            banner.attack("DOS ATTACK - BUG BOUNTY")
            if vulns == "0":
                os.system("clear")
                banner.main()
                banner.attack("WEb Messaging")
                # name,command,discription,writeups,link="",method="kali",github_install="",github_check=""
                ask = vuln_options()
                if ask == '1':
                    print(colors.options,"\nNo tools available for this Vulnerability type.\nIt is recommended to test manually for WEB Messaging to get better understanding & results.\nCheck out the writeup section to to learn about WEB Messaging",colors.reset)
                    waiting.waiting()
                elif ask == '2':
                    writeup.writeup({'HTML5 - Web messaging':'https://www.tutorialspoint.com/html5/html5_web_messaging.htm',
                    'Testing Web Messaging':'https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/11-Client-side_Testing/11-Testing_Web_Messaging',
                    'Web message manipulation':'https://portswigger.net/web-security/dom-based/web-message-manipulation',
                    'HTML5 Security: Cross Domain Messaging':'https://resources.infosecinstitute.com/topic/html5-security-cross-domain-messaging/',
                    'Testing for DOM XSS using web messages':'https://portswigger.net/burp/documentation/desktop/tools/dom-invader/web-messages'
                    
                    }, 'WEB Messaging')
                else:
                    return
            
            elif vulns =='1':
                os.system("clear")
                banner.main()
                banner.attack("WEB Storage SQL Injection")
                # name,command,discription,writeups,link="",method="kali",github_install="",github_check=""
                ask = vuln_options()
                if ask == '1':
                    print(colors.options,"\nNo tools available for this Vulnerability type.\nIt is recommended to test manually for WEB Storage SQL Injection to get better understanding & results.\nCheck out the writeup section to to learn about WEB Storage SQL Injection",colors.reset)
                    waiting.waiting()
                elif ask == '2':
                    writeup.writeup({'Testing Browser Storage':'https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/11-Client_Side_Testing/12-Testing_Browser_Storage',
                    'Testing for SQL Injection':'https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/05-Testing_for_SQL_Injection',
                    'Client-side SQL injection':'https://portswigger.net/kb/issues/00200332_client-side-sql-injection-stored-dom-based',
                    "Secure Implementation of HTML5's Web SQL Database":'https://code.google.com/archive/p/html5security/wikis/WebSQLDatabaseSecurity.wiki'
                    }, 'WEB Storage SQL Injection')
                else:
                    return
            
            elif vulns =='2':
                os.system("clear")
                banner.main()
                banner.attack("CORS Implementation")
                # name,command,discription,writeups,link="",method="kali",github_install="",github_check=""
                ask = vuln_options()
                if ask == '1':
                    print(colors.options,"\nNo tools available for this Vulnerability type.\nIt is recommended to test manually for CORS Implementation to get better understanding & results.\nCheck out the writeup section to to learn about CORS Implementation",colors.reset)
                    waiting.waiting()
                elif ask == '2':
                    writeup.writeup({'What is Web CORS in HTML5 ?':'https://www.geeksforgeeks.org/what-is-web-cors-in-html5/',
                    'Cross-origin resource sharing (CORS)':'https://portswigger.net/web-security/cors',
                    'Testing Cross Origin Resource Sharing':'https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/11-Client-side_Testing/07-Testing_Cross_Origin_Resource_Sharing',
                    'CORS Misconfiguration':'https://systemweakness.com/first-bug-bounty-program-found-cors-cross-origin-resource-sharing-misconfiguration-52c1bd3ebfe0',
                    'Advanced CORS Exploitation Techniques':'https://infosecwriteups.com/think-outside-the-scope-advanced-cors-exploitation-techniques-dad019c68397',
                    'Exploiting CORS misconfigurations for Bitcoins and bounties':'https://portswigger.net/research/exploiting-cors-misconfigurations-for-bitcoins-and-bounties',
                    'CORS - Misconfigurations & Bypass':'https://book.hacktricks.xyz/pentesting-web/cors-bypass',
                    'CORS Misconfiguration':'https://0xn3va.gitbook.io/cheat-sheets/web-application/cors-misconfiguration'
                    }, 'CORS Implementation')
                else:
                    return
            else:
                return
            

def vuln_options():
    print(f"{colors.options}1) Tools")
    print(f"2) Write-ups")
    print(f"3) Go Back..")
    ask=input(f"\n {colors.select}Select An Option ->{colors.reset}  ")
    return ask


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
        return f"{colors.red}Not Loaded Because No Internet Connection{colors.reset}"

if __name__=='__main__':
    main()