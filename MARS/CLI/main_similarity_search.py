import sys
import traceback
from CGRtools.files.RDFrw import RDFread, RDFwrite
from CGRtools.files.SDFrw import SDFread, SDFwrite, MoleculeContainer
from MARS.files.TreeIndex import TreeIndex
from MARS.models import Reactions, Molecules
from pony.orm import db_session
from networkx.readwrite import json_graph



def similarity_search_reactions_core(**kwargs):
    outputdata = RDFwrite(kwargs['output'])
    reactions = RDFread(kwargs['input'])
    num = kwargs['number']
    rebuild = kwargs['rebuild']

    with db_session():
        x = TreeIndex(Reactions, reindex=rebuild)
        for reaction_container in reactions:
            print(TreeIndex.get_similar(x,reaction_container))


def similarity_search_molecules_core(**kwargs):
    molecules = SDFread(kwargs['input'])
    outputdata = SDFwrite(kwargs['output'])
    num = kwargs['number']
    rebuild = kwargs['rebuild']
    with db_session():
        x = TreeIndex(Molecules, reindex=rebuild)
        for molecule_container in molecules:
            a,b = TreeIndex.get_similar(x, molecule_container,num)
            arc = []
            for i in b:
                mol_cont = json_graph.node_link_graph(i.data)
                mol_cont.__class__ = MoleculeContainer
                outputdata.write(mol_cont)







    #