import sys
import traceback
from CGRtools.files.RDFrw import RDFread, RDFwrite


def structure_reaction_search_core(**kwargs):
    inputdata = RDFread(kwargs['input'])
    outputdata = RDFwrite(kwargs['output'])
    search_type = kwargs['enclosure']
    if search_type == False:
        print("We are going to use simple hash-search now:")
    else:
        print("We are going to use advanced enclosure-search now:")


  #  worker = ?

def structure_molecule_search_core(**kwargs):
    inputdata = RDFread(kwargs['input'])
    outputdata = RDFwrite(kwargs['output'])
    if kwargs['product'] == False and kwargs['reagent'] == False:
        product = None
    elif kwargs['product'] == True and kwargs['reagent'] == True:
        print('No,No,No')
    elif kwargs['product'] == True:
        product = True
    elif kwargs['reagent'] == True:
        product = False

    print(product)





