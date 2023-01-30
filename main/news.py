from main.tools import banner
import requests
from bs4 import BeautifulSoup
def get_news(url="https://thehackernews.com/"):
    os.system("clear")
    banner.main()
    banner.attack("News")
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    titles = []
    discription_post=[]
    urls = []
    posts = soup.find("div", class_="blog-posts clear")
    for post in posts.find_all("h2"):
        title = post.text.strip()
        if title and '<img alt="external link"' not in str(post):
            titles.append(title)
            urls.append(post.find_parent('a')['href'])
    discriptions = soup.find_all("div", class_="home-desc")
    for discription in discriptions:
        discription=discription.text.strip()
        if title and '<img alt="external link"' not in str(discription):
            discription_post.append(discription)

    dates = []
    for date in soup.find_all("span", class_="h-datetime"):
        if '<img alt="external link"' not in str(date):
            dates.append(date.text.strip())

    for title, date, url,description in zip(titles, dates, urls,discription_post):
        print(f"\nTitle: {title} \ndescription: {description}  \nDate: {date} \nURL: {url}\n\n")
    input("Press ENTER to go back")
def main():
    os.system("clear")
    banner.main()
    banner.attack("News")
    ask=input("Do you want news Date wise?(y/n)")
    if ask.lower()=="y" or ask.lower()=="y":
        date_user=input("enter date:(YYYY-MM-DD)")
        get_news(f"https://thehackernews.com/search?updated-max={date_user}T17:23:00%2B05:30&max-results=10")
    else:
        get_news()
if __name__=="__main__":
    main()
