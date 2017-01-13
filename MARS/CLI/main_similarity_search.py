import sys
import traceback
from CGRtools.files.RDFrw import RDFread, RDFwrite
from MARS.files import Similarity_search

def similarity_search_core(**kwargs):
    inputdata = RDFread(kwargs['input'])
    outputdata = RDFwrite(kwargs['output'])

    #worker =