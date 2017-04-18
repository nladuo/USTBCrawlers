#!/usr/bin/env python
# coding=utf-8
""" 向量化 """
from sklearn.feature_extraction.text import TfidfVectorizer
import cPickle as pickle
import numpy as np

if __name__ == '__main__':
    with open("segments.pickle", "r") as f:
        segments = pickle.load(f)

    vectorizer = TfidfVectorizer()
    contents = segments.values()

    # 转换模型
    model = vectorizer.fit(contents)
    print len(model.vocabulary_)

    # 转化向量
    X = vectorizer.transform(contents)
    with open("dataset.dat", "w") as f:
        print "saving dataset....."
        np.save(f, X)

    # 保存模型
    with open("vectorizer.pickle", "w") as f:
        print "saving vectorizer model....."
        pickle.dump(model, f)
