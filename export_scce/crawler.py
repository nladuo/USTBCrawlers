# coding=utf8
from __future__ import print_function
import requests
from bs4 import BeautifulSoup
from urlparse import urlparse, parse_qs


def get_article_id(url):
    parsed_url = urlparse(url)
    return parse_qs(parsed_url.query)["articleId"][0]


def modified_and_save_base(html, page_num):
    soup = BeautifulSoup(html, "lxml")
    items = soup.find_all("div", {"class": "every_list"})

    del soup.find("base")["href"]

    for item in items:
        title_div = item.find("div", {"class": "list_title"})
        title = title_div.a.get_text()
        url = title_div.a["href"]
        title_div.a["href"] = "article/" + get_article_id(url) + ".html"

        time = item.find("div", {"class": "list_time"}).get_text()
        print(time, title, url)
        get_and_save_detail(url, get_article_id(url))  # 爬取详情页

    a_nexts = soup.find_all("a", {"name": "link_page_next"})

    # 设置页码
    if page_num == 1:
        a_nexts[0]["href"] = str(page_num + 1) + ".html"
    elif page_num == 10:
        a_nexts[0]["href"] = str(page_num - 1) + ".html"
    else:
        a_nexts[0]["href"] = str(page_num - 1) + ".html"
        a_nexts[1]["href"] = str(page_num + 1) + ".html"

    with open("html/%d.html" % page_num, "w") as f:
        f.write(str(soup))


def get_and_save_detail(url, ariticle_id):
    url = "http://scce.ustb.edu.cn/" + url
    while True:
        try:
            resp = requests.get(url)
            soup = BeautifulSoup(resp.content, "lxml")
            del soup.find("base")["href"]
            print(url)
            with open("html/article/%s.html" % ariticle_id, "w") as f:
                f.write(str(soup))
            break
        except:
            pass

base_url = "http://scce.ustb.edu.cn/more.action?categoryId=1&page=%d"

if __name__ == "__main__":
    for page in range(1, 11):
        url = base_url % page
        resp = requests.get(url)
        modified_and_save_base(resp.content, page)
