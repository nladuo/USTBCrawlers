""" 爬取北科计通学院新闻 """
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    resp = requests.get("http://nladuo.cn/scce_site/")
    # print resp.content
    soup = BeautifulSoup(resp.content, "lxml")
    items = soup.find_all("div", {"class": "every_list"})

    for item in items:
        title_div = item.find("div", {"class": "list_title"})
        title = title_div.a.get_text()
        url = title_div.a["href"]
        time = item.find("div", {"class": "list_time"}).get_text()
        print(time, title, url)
