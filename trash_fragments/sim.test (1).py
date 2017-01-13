
# coding: utf-8

# In[ ]:




# In[58]:

# import numpy as np

# def create_array_mol(fingerprint_mol):
#     nparray_mol = np.fromstring(fingerprint_mol, dtype = np.uint64) 
#     return nparray_mol

# fingerprint_mol = b'111110101010101'
# create_array_mol(fingerprint_mol)


# In[80]:

import numpy as np
from math import *
from sklearn.neighbors import NearestNeighbors
from sklearn.neighbors import KNeighborsClassifier
# cimport numpy as np
# cimport cython 
# from libc.stdint cimport uint64_t

fingerprint_mol = b'10101001'


nparray_mol = np.fromstring(fingerprint_mol, dtype = np.uint8)

def tanimoto(x,y):
    for x in range(len(nparray_mol)):
        for y in range(1, len(nparray_mol)):
            NNEQ = len(set.intersection([nparray_mol[x], nparray_mol[y]]))
            NNZ = len(set.union([nparray_mol[x], nparray_mol[y]]))
            return NNEQ/NNZ
    
nbrs = KNeighborsClassifier(n_neighbors=10, algorithm='ball_tree', leaf_size=50, metric=tanimoto)
nbrs.fit(nparray_mol[x], nparray_mol[y])
distances, indices = nbrs.kneighbors(nparray_mol[x], nparray_mol[y])
print(nbrs)


# In[77]:




# In[ ]:



