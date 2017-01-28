import sys
import traceback
from CGRtools.files.RDFrw import RDFread, RDFwrite, ReactionContainer
from CGRtools.files.SDFrw import SDFread, SDFwrite, MoleculeContainer
from MARS.files.TreeIndex import TreeIndex
from MARS.models import Reactions, Molecules
from pony.orm import db_session
from networkx.readwrite import json_graph


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
    molecules = SDFread(kwargs['input'])
    outputdata = RDFwrite(kwargs['output'])
    product = kwargs['product']
    if kwargs['product'] == False and kwargs['reagent'] == False:
        product = None
    elif kwargs['product'] == True and kwargs['reagent'] == True:
        print('No,No,No')
    elif kwargs['product'] == True:
        product = True
    elif kwargs['reagent'] == True:
        product = False
    with db_session():
        for molecule in molecules:
            required_reacts = Reactions.get_reactions_by_molecule(molecule,product)
            print(required_reacts)
            for reaction in required_reacts:
                react_cont = reaction.structure
                print(react_cont)
                outputdata.write(react_cont)








