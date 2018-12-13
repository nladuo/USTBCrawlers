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
    print("downloading: page %d" % task["page"])
    # 1. 下载页面
    resp = requests.get("http://tieba.baidu.com/f?kw="
                        "%E5%8C%97%E4%BA%AC%E7%A7%91%E6%8A%80%E5%A4%A7%E5%AD%A6&ie=utf-8&pn=" + str(offset))
    soup = BeautifulSoup(resp.content, "html.parser")

    # 2. 解析页面
    items = soup.find_all("a", {"class", "j_th_tit"})

    docs = []
    for index, item in enumerate(items):
        docs.append({
            "page": task["page"],
            "index": index,
            "title": item.get_text(),
            "href": "http://tieba.baidu.com" + item.attrs["href"]
        })
        print(task["page"], index, item.get_text())
    # 3. 保存数据
    with lock:
        save_docs(docs)

    # 4. 添加新任务
    if (task["page"] + 10) > 1000:
        queue.put({"id": "NO"})
    else:
        queue.put({"id": "worker", "page": task["page"] + 10})

beike = init_collection()

if __name__ == '__main__':
    crawler = SimpleCrawler(5)
    crawler.add_worker("worker", worker)
    for i in range(1, 11):
        crawler.add_task({"id": "worker", "page": i})
    crawler.start()
