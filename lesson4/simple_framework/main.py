#!/usr/bin/env python
# coding=utf8
""" 并行爬取北科计通学院新闻及其详情 """
from SimpleCrawler import *
import requests
from bs4 import BeautifulSoup


def worker(queue, task):
    """ 爬取新闻列表页 """
    url = task["url"] + "%d.html" % task["page"]
    print "downloading:", url
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, "html.parser")
    items = soup.find_all("div", {"class", "list_title"})

    for index, item in enumerate(items):
        detail_url = "http://nladuo.cn/scce_site/" + item.a['href']
        print "adding:", detail_url
        queue.put({
            "id": "detail_worker",
            "url": detail_url,
            "page": task["page"],
            "index": index,
            "title": item.get_text().replace("\n", "")
        })

    if task["page"] == 10:  # 添加结束信号
        queue.put({"id": "NO"})
    else:
        queue.put({
            "id": "worker",
            "url": "http://nladuo.cn/scce_site/",
            "page": task["page"]+1
        })


def detail_worker(queue, task):
    """ 爬取新闻详情页 """
    print "downloading:", task['url']
    resp = requests.get(task['url'])
    soup = BeautifulSoup(resp.content, "html.parser")
    click_num = soup.find("div", {"class", "artNum"}).get_text()
    print task["page"], task["index"], task['title'], click_num


if __name__ == '__main__':
    crawler = SimpleCrawler(5)
    crawler.add_task({
        "id": "worker",
        "url": "http://nladuo.cn/scce_site/",
        "page": 1
    })
    crawler.add_worker("worker", worker)
    crawler.add_worker("detail_worker", detail_worker)
    crawler.start()

