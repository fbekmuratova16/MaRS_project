import numpy as np

def Alina_simsearch(fingerprint,tanimoto):
    fingerprint = b'1010101'

    def create_array_mol(fp):
        nparray_mol = np.fromstring(fp, dtype = np.uint8)
        return nparray_mol

    for x in fingerprint:
        create_array_mol(x)

    def Tanimoto (moli, molj):
        return (moli & molj).count(1) / (moli | molj).count(1)

    for moli in nparray_mol:
        for molj in nparray_mol:
            Tanimoto(moli, molj)

    index_distance_dictionary = {}

    return index_distance_dictionary

