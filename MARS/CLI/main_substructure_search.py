import sys
import traceback
from CGRtools.files.RDFrw import RDFread, RDFwrite


def substructure_search_core(**kwargs):
    inputdata = RDFread(kwargs['input'])
    outputdata = RDFwrite(kwargs['output'], extralabels=kwargs['save_extralabels'])

  #  worker = ?