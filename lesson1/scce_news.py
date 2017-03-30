#!/usr/bin/env python
#coding=utf8
''' 爬取北科计通学院新闻 '''
import requests
from bs4 import BeautifulSoup

resp = requests.get("http://scce.ustb.edu.cn/more.action?categoryId=1")
soup = BeautifulSoup(resp.content)
items = soup.find_all("div", {"class", "list_title"})

for index, item in enumerate(items):
    print index, item.get_text().replace("\n", "")
