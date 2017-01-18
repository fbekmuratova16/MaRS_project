import numpy as np
from sklearn.neighbors import DistanceMetric, BallTree
from models import Molecules, Reactions


s = select( m for m in Molecules).order_by(Molecules.fingerprint)[:]
s = select( m for m in Reactions).order_by(Reactions.fingerprint)[:]

def npmatrix(fp):
    a = []
    for i in fp:
        npX = np.fromstring(i, dtype = np.uint8)
        by_x = np.unpackbits(npX)
        a.append(by_x)
    b = np.matrix(a)
    return b

def get_similar():
tree = BallTree(npmatrix(s), metric='jaccard')
dist, ind = tree.query(q, k=10)
print(dist, ind)