#!/usr/bin/env python
# coding=utf8
""" 把一个任务分成两个任务 """
import multiprocessing
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


def process(start, end):
    for i in range(start, end):
        print "crawling page %d ......." % i
        crawl_one_page(1)


if __name__ == '__main__':
    p = multiprocessing.Process(target=process, args=(1, 6))  # 任务1, 爬取1-5页
    p.start()

    p2 = multiprocessing.Process(target=process, args=(6, 11))  # 任务2, 爬取6-10页
    p2.start()
