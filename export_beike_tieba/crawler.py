# coding=utf8
from __future__ import print_function
import requests

base_url = "http://tieba.baidu.com/f?kw=%E5%8C%97%E4%BA%AC%E7%A7%91%E6%8A%80%E5%A4%A7%E5%AD%A6&ie=utf-8&pn={offset}"

if __name__ == "__main__":
    for page in range(483, 1050):
        offset = (page-1) * 50
        url = base_url.format(offset=offset)
        print(page, url)
        resp = requests.get(url)
        with open("html/beike_tieba/%d.html" % page, "w") as f:
            f.write(resp.content.decode("utf-8"))
