""" 多进程爬取北科计通学院新闻 """
import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool
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
        print(date, title, url)

if __name__ == '__main__':
    t0 = time.time()
    p = Pool(5)
    for page in range(1, 11):  # 1-10页
        p.apply_async(crawl_one_page, args=(page,))

    # 关闭进程池, 等待子进程结束
    p.close()
    p.join()

    print("used:", (time.time() - t0))
