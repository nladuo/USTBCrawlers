#!/usr/bin/env python
# coding=utf8
""" 爬取北科计通学院新闻 """
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    resp = requests.get("http://scce.ustb.edu.cn/more.action?categoryId=1")
    # print resp.content
    soup = BeautifulSoup(resp.content)
    items = soup.find_all("div", {"class": "every_list"})

    for item in items:
        title_div = item.find("div", {"class": "list_title"})
        title = title_div.a.get_text()
        url = title_div.a["href"]
        time = item.find("div", {"class": "list_time"}).get_text()
        print time, title, url
