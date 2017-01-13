import numpy as np
from sklearn.neighbors import DistanceMetric, BallTree

s = [b'\x30\x31\x30\x30\x31\x30\x31\x30', b'\x31\x30\x31\x30\x31\x30\x31\x30',
     b'\x30\x31\x30\x30\x30\x30\x30\x30', b'\x30\x31\x30\x30\x31\x30\x31\x30',
     b'\x31\x30\x31\x30\x30\x30\x30\x31', b'\x30\x30\x31\x30\x30\x30\x31\x30',
     b'\x30\x31\x30\x30\x30\x30\x31\x30', b'\x31\x30\x30\x30\x31\x30\x30\x31',
     b'\x31\x30\x30\x30\x30\x30\x30\x31', b'\x31\x30\x30\x31\x30\x30\x31\x30']
q = b'\x31\x30\x31\x31\x31\x30\x31\x30'
npq = np.fromstring(q, dtype = np.uint8)
by_q = np.unpackbits(npq)
q1 = np.matrix(by_q)

def npmatrix(fp):
    a = []
    for i in fp:
        npX = np.fromstring(i, dtype = np.uint8)
        by_x = np.unpackbits(npX)
        a.append(by_x)
    b = np.matrix(a)
    return b

tree = BallTree(npmatrix(s), metric='jaccard')
dist, ind = tree.query(q1, k=3)
print(dist, ind)