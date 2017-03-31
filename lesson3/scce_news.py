#!/usr/bin/env python
# coding=utf8
""" 多进程爬取北科计通学院新闻 """
import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool


def crawl_webpage(page_num):
    resp = requests.get("http://scce.ustb.edu.cn/more.action?categoryId=1&page=%d" % page_num)
    soup = BeautifulSoup(resp.content, "html.parser")
    items = soup.find_all("div", {"class", "list_title"})

    for index, item in enumerate(items):
        print page_num, index, item.get_text().replace("\n", "")
    print ""


if __name__ == '__main__':
    p = Pool(5)
    for page in range(1, 11):  # 1-10页
        p.apply_async(crawl_webpage, args=(page,))

    # 关闭进程池, 等待子进程结束
    p.close()
    p.join()
