#!/usr/bin/env python
# coding=utf8
""" 把一个任务分成两个任务——例子2 """
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


if __name__ == '__main__':
    t0 = time.time()

    p = None  # 进程1
    p2 = None  # 进程2

    for i in range(1, 11):
        if i % 2 == 1:  # 把偶数任务分配给进程1
            p = multiprocessing.Process(target=crawl_one_page, args=(i,))
            p.start()
        else:           # 把奇数任务分配给进程2
            p2 = multiprocessing.Process(target=crawl_one_page, args=(i,))
            p2.start()

        if i % 2 == 0:  # 保证只有两个进程, 等待两个进程完成
            p.join()
            p2.join()

    print "used:", (time.time() - t0)
