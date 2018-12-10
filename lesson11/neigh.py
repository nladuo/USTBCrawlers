from sklearn.preprocessing import normalize
from sklearn.neighbors import NearestNeighbors
import numpy as np
import pymongo

with open("../lesson10/dataset.pickle", "rb") as f:
    X = np.load(f)
    print("shape of dataset:", X.shape)

# 归一化: 归一化后相似度就是向量的点乘
X_normalized = normalize(X, norm='l2', axis=1)


# 最近邻查找
neigh = NearestNeighbors(n_neighbors=30, algorithm='kd_tree')

neigh.fit(X_normalized.toarray())


def init_collection():
    client = pymongo.MongoClient(host="localhost", port=27017)
    db = client['tieba']
    return db["beike"]

# 更新到数据库
beike = init_collection()
items = beike.find({})
segments = {}
for item in items:
    key = str(item['_id'])
