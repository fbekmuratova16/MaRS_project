import sys
import traceback
from CGRtools.files.RDFrw import RDFread, RDFwrite
from itertools import count
import itertools


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

