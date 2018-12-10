""" 分词 """
import pymongo
import jieba
import pickle


def init_collection():
    client = pymongo.MongoClient(host="localhost", port=27017)
    db = client['tieba']
    return db["beike"]

if __name__ == '__main__':
    beike = init_collection()
    items = beike.find({})
    segments = {}
    for item in items:
        key = str(item['_id'])
        val = " ".join(jieba.cut(item['title']))
        segments[key] = val
        print(key, val)
    print(items.count())

    with open("segments.pickle", "wb") as f:
        pickle.dump(segments, f)

