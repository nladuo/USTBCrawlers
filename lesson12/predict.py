""" 获取贴子帖子的相关贴子 """
import requests
import pymongo
from bs4 import BeautifulSoup
import pickle
import operator
from sklearn.metrics.pairwise import cosine_similarity
import jieba


def init_collection():
    client = pymongo.MongoClient(host="localhost", port=27017)
    db = client['tieba']
    return db["beike"]


def get_title(href):
    resp = requests.get(href)
    soup = BeautifulSoup(resp.content, "html.parser")
    return soup.find("h1", {"class": "core_title_txt"}).get_text()


if __name__ == "__main__":
    beike = init_collection()

    title = get_title("http://tieba.baidu.com/p/5077010001")
    print("title:", title)

    segment = " ".join(jieba.cut(title))

    with open("../lesson11/km.pickle", "r") as f:
        print("loading km.pickle ...")
        km = pickle.load(f)

    with open("../lesson10/vectorizer.pickle", "r") as f:
        print("loading vectorizer.pickle ...")
        vectorizer = pickle.load(f)

    # 获取cluster
    vec = vectorizer.transform([segment])
    which_cluster = int(km.predict(vec[0])[0])

    # 找出所有该cluster的帖子
    tiezis = beike.find({"cluster": which_cluster})
    print("cluster count:", tiezis.count())

    sim_tiezis = []
    for tiezi in tiezis:
        tiezi_seg = " ".join(jieba.cut(tiezi["title"]))
        tiezi_vec = vectorizer.transform([tiezi_seg])
        similarity = cosine_similarity(vec[0], tiezi_vec[0])[0][0]
        if similarity > 0:
            # print tiezi["title"], similarity
            sim_tiezis.append({"title": tiezi["title"], "similarity": similarity})

    sim_tiezis.sort(key=operator.itemgetter("similarity"), reverse=True)

    print("Result: ")
    if len(sim_tiezis) == 0:
        print("No similar tiezi!!")
    elif len(sim_tiezis) < 20:
        for tiezi in sim_tiezis:
            print(tiezi["title"], tiezi["similarity"])
    else:
        for tiezi in sim_tiezis[:20]:
            print(tiezi["title"], tiezi["similarity"])

