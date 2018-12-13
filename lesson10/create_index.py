from elasticsearch import Elasticsearch
import pymongo


def init_collection():
    client = pymongo.MongoClient(host="localhost", port=27017)
    db = client['tieba']
    return db["beike"]

es = Elasticsearch()
coll = init_collection()

# 初始化索引的Mappings设置，只有一个字段: 标题。
index_mappings = {
  "mappings": {
    "tiezi": {
      "properties": {
        "title": {
            "type": "text",
            "analyzer": "ik_max_word",
            "search_analyzer": "ik_max_word"
        },
      }
    },
  }
}

# es.indices.delete(index='tieba_index')

if es.indices.exists(index='tieba_index') is not True:
    print("create tieba_index")
    es.indices.create(index='tieba_index', body=index_mappings)


for tiezi in coll.find():
    _id = str(tiezi["_id"])
    doc = {
        "id": _id,
        "title": tiezi["title"]
    }
    print(doc)
    res = es.index(index="tieba_index", doc_type="tiezi", id=_id, body=doc)
    print(res)
