#!/usr/bin/env python
# coding=utf8
""" 爬取多个页面 """
import requests
from bs4 import BeautifulSoup


def crawl_one_page(page_num):
    resp = requests.get("http://scce.ustb.edu.cn/more.action?categoryId=1&page={page}".
                        format(page=page_num))
    soup = BeautifulSoup(resp.content)
    items = soup.find_all("div", {"class": "every_list"})

    for item in items:
        title_div = item.find("div", {"class": "list_title"})
        title = title_div.a.get_text()
        url = title_div.a["href"]
        time = item.find("div", {"class": "list_time"}).get_text()
        print time, title, url

if __name__ == '__main__':
    for i in range(1, 11):
        print "crawling page %d ......." % i
        crawl_one_page(1)
