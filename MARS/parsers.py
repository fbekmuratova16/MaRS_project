# -*- coding: utf-8 -*-

import argparse
from .CLI.main_structure_search import structure_reaction_search_core
from .CLI.main_structure_search import structure_molecule_search_core
from .CLI.main_substructure_search import substructure_search_core
from .CLI.main_similarity_search import similarity_search_reactions_core
from .CLI.main_similarity_search import similarity_search_molecules_core
from .CLI.main_fill_database import fill_database_core


def structure_search_molecules(subparsers):
    parser = subparsers.add_parser('struct_mol', help='Simple structure search of given Molecule',
                                   formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--input", "-i", default="input.rdf", type=argparse.FileType('r'),
                        help="RDF inputfile")
    parser.add_argument("--output", "-o", default="output.rdf", type=argparse.FileType('w'),
                        help="RDF file containing needed reations")
    parser.add_argument("--product","-pr",action = 'store_true', help = "Use this if you are"
                                    " looking for reactions, in which your molecule is a product(DO NOT WRITE ANY ARGS)")

    parser.add_argument("--reagent", "-re", action = 'store_true', help="Use this if you are"
                                    " looking for reactions, in which your molecule is a reagent(DO NOT WRITE ANY ARGS)")

    parser.set_defaults(func=structure_molecule_search_core)


def structure_search_reactions(subparsers):
    parser = subparsers.add_parser('struct_react', help='Simple structure search of given Reaction',
                                   formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--input", "-i", default="input.rdf", type=argparse.FileType('r'),
                        help="RDF inputfile")
    parser.add_argument("--output", "-o", default="output.rdf", type=argparse.FileType('w'),
                        help="RDF file containing needed reactions")
    parser.add_argument("--enclosure", '-en',action = 'store_true',help = 'Use this if you want '
                                    'to use advanced non-hash reaction search ' )

    parser.set_defaults(func=structure_reaction_search_core)


def similarity_search_reactions(subparsers):
    parser = subparsers.add_parser('similar_react',
                                   help='Reactions similarity search. This one searches similar Reactions,'
                                        ' using fingerprints and Tanimoto index',
                                   formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--input", "-i", default="input.rdf", type=argparse.FileType('r'),
                        help="RDF inputfile")
    parser.add_argument("--output", "-o", default="output.rdf", type=argparse.FileType('w'),
                        help="RDFile containing similar reactions with Tanimoto Index as property.")
    parser.add_argument("--treepath","-tp", default="C://", type=str, help='Path to BallTree')
    parser.add_argument("--rebuild",'-rb', action='store_true', help='Use this if want to rebuild your BallTree')
    parser.add_argument("--number","-n", type=int, default=10, help='Number of similar reactions, that you want to get')

    parser.set_defaults(func=similarity_search_reactions_core)

def similarity_search_molecules(subparsers):
    parser = subparsers.add_parser('similar_mol',
                                   help='Molecules similarity search. This one searches similar Molecules,'
                                        ' using fingerprints and Tanimoto index',
                                   formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--input", "-i", default="input.sdf", type=argparse.FileType('r'),
                        help="SDF inputfile")
    parser.add_argument("--output", "-o", default="output.sdf", type=argparse.FileType('w'),
                        help="SDFile containing similar molecules with Tanimoto Index as property.")
    parser.add_argument("--treepath", "-tp", default="C://", type=str, help='Path to BallTree')
    parser.add_argument("--rebuild", '-rb', action='store_true', help='Use this if want to rebuild your BallTree')
    parser.add_argument("--number", "-n", type=int, default=10,
                        help='Number of similar molecules, that you want to get')

    parser.set_defaults(func=similarity_search_molecules_core)


def substructure_search(subparsers):
    parser = subparsers.add_parser('substruct',
                                   help=' Subsctructure search.This one searches Molecules with'
                                        ' certain fragment in their structure ',
                                   formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--input", "-i", default="input.rdf", type=argparse.FileType('r'),
                        help="RDF inputfile")
    parser.add_argument("--output", "-o", default="output.txt", type=argparse.FileType('w'),
                        help="Indexes of Molecules with needed fragment in database")

    parser.set_defaults(func=substructure_search_core)


def fill_database(subparsers):
    parser = subparsers.add_parser('dbfill',
                                   help=' This utility fills database with new entities ',
                                   formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--input", "-i", default="input.rdf", type=argparse.FileType('r'),
                        help="RDF inputfile")
    parser.add_argument("--chunksize","-cs",type=int, default =100, help='RDFread portion size')

    parser.set_defaults(func=fill_database_core)
