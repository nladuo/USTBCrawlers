from sklearn.cluster import KMeans
import cPickle as pickle
from time import time
import numpy as np


if __name__ == "__main__":

    with open("../lesson10/dataset.pickle", "rb") as f:
        X = np.load(f)
        print "shape of dataset:", X.shape

    with open("../lesson10/segments.pickle", "rb") as f:
        segments = pickle.load(f)

    km = KMeans(init='k-means++', n_clusters=200, verbose=1)
    t0 = time()
    km.fit(X)
    print "done in %0.3fs" % (time() - t0)

    with open("km.pickle", "wb") as f:
        pickle.dump(km, f, pickle.HIGHEST_PROTOCOL)
