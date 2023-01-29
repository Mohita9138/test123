import configparser
import tweepy
import os
from main.tools import banner
new_count=0
def main():
    os.system("clear")
    banner.main()
    banner.attack("News")
    check_existence()

def check_existence():
    path = 'config.ini'
    
    # Check whether a path pointing to a file
    isFile = os.path.isfile(path)
    if isFile:
        print("[+] PRESS ENTER to continue\n[+] PRESS SPACE for exit ")
        fatch_tweet()
    else:
        making_config()
def making_config():
    os.system("clear")
    banner.main()
    banner.attack("News")
    banner.description("Please enter your twitter API\nTo get your Twitter API key, secret key, access token, and access secret, you will need to create a Twitter Developer account and a Project. Once you have created a project, you can then create a Twitter developer application and generate the necessary keys and tokens. It is important to note that these keys and tokens should be kept private and not shared with anyone.\nFor more refrance click here:\nhttps://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api")
    config = configparser.ConfigParser()
    config.add_section('twitter')
    api_key=input("[+]input api key / CONSUMER KEY:")
    config.set('twitter', 'api_key', api_key)
    api_key_secret=input("[+]input api key secret / CONSUMER SECRET:")
    config.set('twitter', 'api_key_secret', api_key_secret)
    access_token=input("[+]input access token / ACCESS_TOKEN:")
    config.set('twitter', 'access_token', access_token)
    access_token_secret=input("[+]input access token secret / ACCESS SECRET:")
    config.set('twitter', 'access_token_secret', access_token_secret)
    # Write the new structure to the new file
    with open("config.ini", 'w') as configfile:
        config.write(configfile)
    fatch_tweet()


def fatch_tweet():
    config = configparser.ConfigParser()
    config.read('config.ini')
    # Read the values
    new_count=10
    api_key = config['twitter']['api_key']
    api_key_secret = config['twitter']['api_key_secret']
    access_token = config['twitter']['access_token']
    access_token_secret = config['twitter']['access_token_secret']
    try:
        auth = tweepy.OAuthHandler(api_key, api_key_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        while True:
            os.system("clear")
            banner.main()
            banner.attack("News")
            tweets = api.user_timeline(screen_name="newsycombinator",count=new_count,tweet_mode='extended')
            count=0
            for i in tweets:
                count+=1
                print(f"[+] News {count}.\n{i.full_text}\n")
                print("\u001b[37m---------------------------------------------------------------------------\n")
            user_want=input("[+] PRESS ENTER to go back\n[+] write more and press enter to get more news\n")
            if user_want.lower()=="more":
                new_count+=10
            else:
                break
    except:
        os.system("clear")
        banner.main()
        banner.attack("News")
        print("[-] SOMETHING WENT WRONG !!\nplease check your credintial in config.ini file")
        update=input("Do you want to change config.ini here?(y/n)")
        if update.lower()=="y" or update.lower()=="yes":
            making_config()
if __name__=="__main__":
    check_existence()
