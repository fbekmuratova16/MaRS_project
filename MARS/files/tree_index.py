import numpy as np
import pickle
from sklearn.neighbors import DistanceMetric, BallTree
from models import Molecules, Reactions
from Similarity_search import *
# создать класс, который будет создавать индексы для молекул. Если реиндекс = False, значит индекс есть, дерево не пересоздаем
# если реиндекс = True, значит этого индекса нет, дерево нужно обновить.

class TreeIndex(Molecules.fingerprint, Reactions.fingerprint):
    def __init__(self, reindex = False):
        if reindex == True:
            pass
        else:
            file_mol = open('C:\tree_mol.bin', 'wb')
            tree = BallTree(npmatrix(s), metric='jaccard')
            output_mol = pickle.dump(treem, file_mol)
            file_mol.close()