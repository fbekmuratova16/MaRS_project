import numpy as np
import pickle
from sklearn.neighbors import BallTree
from pony.orm import select
from MARS.models import *
from os import path

dump_dir = 'C://'

class TreeIndex(object):

    def __init__(self, data, reindex=False):
        data_path = path.join(dump_dir, '%s.bin' % data.__name__)

        if reindex or not path.exists(data_path):
            a = []
            ids = []
            for fp, i in select((s.fingerprint, s.id) for s in data):
                by_x = np.unpackbits(np.fromstring(fp, dtype=np.uint8))
                a.append(by_x)
                ids.append(i)

            tree = BallTree(np.matrix(a), metric='jaccard')
            with open(data_path, 'wb') as f:
                pickle.dump((tree,ids), f)
        else:
            with open(data_path, 'rb') as f:
                tree, ids = pickle.load(f)

        self.__tree = tree
        self.__data = data
        self.__ids = ids

    def get_similar(self, structure):
        q1 = self.__data.get_fingerprints([structure])
        by_q = np.unpackbits(np.fromstring(q1[0], dtype=np.uint8))
        q = np.matrix([by_q])
        dist, ind = self.__tree.query(q, k=10)
        return dist, [self.__data[self.__ids[x]] for x in ind]