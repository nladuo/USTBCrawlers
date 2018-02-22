#!/usr/bin/env python
# coding=utf8
""" 把一个任务分成两个任务 """
import multiprocessing
import requests
from bs4 import BeautifulSoup
import time


def crawl_one_page(page_num):
    resp = requests.get("http://nladuo.cn/scce_site/{page}.html".
                        format(page=page_num))
    soup = BeautifulSoup(resp.content, "html.parser")
    items = soup.find_all("div", {"class": "every_list"})

    for item in items:
        title_div = item.find("div", {"class": "list_title"})
        title = title_div.a.get_text()
        url = title_div.a["href"]
        date = item.find("div", {"class": "list_time"}).get_text()
        print date, title, url


def process(start, end):
    for i in range(start, end):
        print "crawling page %d ......." % i
        crawl_one_page(i)


if __name__ == '__main__':
    t0 = time.time()
    p = multiprocessing.Process(target=process, args=(1, 6))  # 任务1, 爬取1-5页
    p.start()

    p2 = multiprocessing.Process(target=process, args=(6, 11))  # 任务2, 爬取6-10页
    p2.start()

    p.join()
    p2.join()

    print "used:", (time.time() - t0)
