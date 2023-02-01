from main.tools import run_on_browser,colors
def writeup(writeup_dist,name):
    while True:
        os.system("clear")
        banner.main()
        banner.attack(name)
        #convert dict keys in list(type casting)
        key=list(writeup_dist.keys())
        key.append("go back")
        for i in range(len(key)):
            print(f"{colors.options}{i}) {key[i]}{colors.reset}")
        option = input("\n {colors.select}Select an option -> {colors.reset} ")
        #1-9=int kdsjfhgkjds=int X to type cast safely 
        try:
            threading.Thread(target=run_on_browser.main, args=(writeup_dist[key[int(option)]],)).start()
            #a={"a":1,"b":2}
            # print(2)
        except:
            return