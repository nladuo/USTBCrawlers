#!/usr/bin/env python
# coding=utf8
""" 获取贴子帖子的相关贴子 """
import requests
import pymongo
from bs4 import BeautifulSoup


def get_title(href):
    resp = requests.get(href)
    soup = BeautifulSoup(resp.content, "html.parser")
    return soup.find("h1", {"class": "core_title_txt"}).get_text()


if __name__ == "__main__":
    title = get_title("http://tieba.baidu.com/p/5049046087")
    print "title:", title

