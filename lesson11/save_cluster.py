import pickle
import pymongo
from bson.objectid import ObjectId


def init_collection():
    client = pymongo.MongoClient(host="localhost", port=27017)
    db = client['tieba']
    return db["beike"]

if __name__ == "__main__":
    beike = init_collection()

    with open("km.pickle", "r") as f:
        print("loading km.pickle ...")
        km = pickle.load(f)

    with open("../lesson10/vectorizer.pickle", "r") as f:
        print("loading vectorizer.pickle ...")
        vectorizer = pickle.load(f)

    with open("../lesson10/segments.pickle", "r") as f:
        print("loading segments.pickle ...")
        segments = pickle.load(f)

        for key in segments:
            vec = vectorizer.transform([segments[key]])
            which_cluster = int(km.predict(vec[0])[0])
            print(key, which_cluster)

            beike.update({'_id': ObjectId(key)}, {
                '$set': {
                    'cluster': which_cluster
                }
            })
