import sys
import traceback
from CGRtools.files.RDFrw import RDFread, RDFwrite
from itertools import count
import itertools
from MARS.models import Molecules


def fill_database_core(**kwargs):
    it = iter(RDFread(kwargs['input']))
    chunksize = kwargs['chunksize']

    for x in itertools.zip_longest(*[it]*chunksize):
        if x.count(None) != 0:
            y = list(x)
            n = y.count(None)
            for i in range (0,n):
                y.remove(None)
            x = tuple(y)
        print(x)
        substrats_list = []
        products_list = []
        for i in x:
            substrats = i['substrats']
            substrats_list.append(substrats)
            products = i['products']
            products_list.append(products)
            sustrats_fp = Molecules.get_fingerprints(substrats_list)
            products_fp = Molecules.get_fingerprints(products_list)


        print(substrats_list)
        print(products_list)






