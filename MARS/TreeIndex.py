import numpy as np
import pickle
from sklearn.neighbors import BallTree
from pony.orm import select
from MARS.models import *
from os import path

fp = select( f.fingerprint for f in Molecules and Reactions)
id_s = select( i.id for i in Molecules and Reactions)
dump_dir = 'C://'

class TreeIndex(object):

    def npmatrix(fp):
        a = []
        for i in fp:
            npX = np.fromstring(i, dtype=np.uint8)
            by_x = np.unpackbits(npX)
            a.append(by_x)
        b = np.matrix(a)
        return b

    def __init__(self, data, reindex=False):
        data_path = path.join(dump_dir, '%s.bin' % data.__name__)
        if reindex or path.exists(data_path):
            with open(data_path, 'wb') as f:
                tree = BallTree(b, metric='jaccard')
                pickle.dump(tree, f)
        else:
            with open(data_path, 'rb') as f:
                tree = pickle.load(f)

        self.__tree = tree
        self.__data = data

    def get_similar(self, structure):
        q1 = self.__data.get_fingerprints([structure])
        npq = np.fromstring(q1[0], dtype=np.uint8)
        by_q = np.unpackbits(npq)
        q = np.matrix(by_q)
        dist, ind = self.__tree.query(q, k=10)
        return dist, ind