#!/usr/bin/env python
# coding=utf8
""" 爬取北科贴吧帖子标题 """
import requests
import pymongo
from bs4 import BeautifulSoup
from SimpleCrawler import SimpleCrawler


def init_collection():
    client = pymongo.MongoClient(host="localhost", port=27017)
    db = client['tieba']
    return db["beike"]


def save_docs(docs):
    beike.insert(docs)


def worker(queue, task, lock):
    offset = (task["page"] - 1) * 50
    print "downloading: page %d" % task["page"]
    resp = requests.get("http://tieba.baidu.com/f?kw="
                        "%E5%8C%97%E4%BA%AC%E7%A7%91%E6%8A%80%E5%A4%A7%E5%AD%A6&ie=utf-8&pn=" + str(offset))
    soup = BeautifulSoup(resp.content, "html.parser")
    items = soup.find_all("a", {"class", "j_th_tit"})

    docs = []
    for index, item in enumerate(items):
        docs.append({"page": task["page"], "index": index, "title": item.get_text()})
        print task["page"], index, item.get_text()
    with lock:
        save_docs(docs)

    if task["page"] > 1000:
        queue.put({"id": "NO"})
    elif task["page"] % 10 == 0:
        start_page = task["page"] + 1
        end_page = task["page"] + 11
        for i in range(start_page, end_page):
            queue.put({"id": "worker", "page": i})


if __name__ == '__main__':
    beike = init_collection()
    crawler = SimpleCrawler(5)
    for i in range(1, 11):
        crawler.add_task({"id": "worker", "page": i})
    crawler.add_worker("worker", worker)
    crawler.start()
