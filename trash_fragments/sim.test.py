
# coding: utf-8

# In[ ]:

# import numpy as np
# fingerprint_mol = b''
# nparray_mol = np.fromstring(fingerprint_mol, dtype = np.uint8) 
# print (nparray_mol)
# return nparray_mol


# In[58]:

# import numpy as np

# def create_array_mol(fingerprint_mol):
#     nparray_mol = np.fromstring(fingerprint_mol, dtype = np.uint64) 
#     return nparray_mol

# fingerprint_mol = b'111110101010101'
# create_array_mol(fingerprint_mol)


# In[76]:

import numpy as np

fingerprint_mol = b'1010101'

def create_array_mol(fp_mol):
    nparray_mol = np.fromstring(fp_mol, dtype = np.uint8) 
    return nparray_mol

for x in fingerprint_mol:
    create_array_mol(x)

def Tanimoto (moli, molj):
    return (moli & molj).count(1) / (moli | molj).count(1)

for moli in nparray_mol:
    for molj in nparray_mol:
        Tanimoto(moli, molj)


# In[77]:

import sklearn.pairwise.distance_metrics
__doc__


# In[ ]:



