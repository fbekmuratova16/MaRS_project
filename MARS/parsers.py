import argparse
from .CLI.main_structure_search import structure_reaction_search_core
from .CLI.main_structure_search import structure_molecule_search_core
from .CLI.main_substructure_search import substructure_search_core
from .CLI.main_similarity_search import similarity_search_core
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


def similarity_search(subparsers):
    parser = subparsers.add_parser('similar',
                                   help='Similarity search. This one searches similar Molecules,'
                                        ' using fingerprints and Tanimoto index',
                                   formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--input", "-i", default="input.rdf", type=argparse.FileType('r'),
                        help="RDF inputfile")
    parser.add_argument("--output", "-o", default="output.txt", type=argparse.FileType('w'),
                        help="Indexes of Similar Molecules in database")

    parser.set_defaults(func=similarity_search_core)


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
