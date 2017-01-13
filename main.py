import argparse
from MARS.version import version
from MARS.parsers import structure_search_molecules
from MARS.parsers import structure_search_reactions
from MARS.parsers import similarity_search
from MARS.parsers import substructure_search
from importlib.util import find_spec
import importlib

def parse_args():
    parser = argparse.ArgumentParser(description="Molecules And Reactions Search", epilog="(c) KFU - 07-613 - 2016", prog='MARS')
    parser.add_argument("--version", "-v", action="version", version=version(), default=False)
    subparsers = parser.add_subparsers(title='subcommands', description='available utilities')

    structure_search_molecules(subparsers)
    structure_search_reactions(subparsers)
    substructure_search(subparsers)
    similarity_search(subparsers)
    #fill_database(subparsers)


    if find_spec('argcomplete'):
        argcomplete = importlib.import_module('argcomplete')
        argcomplete.autocomplete(parser)

    return parser

def main():
    parser = parse_args()
    args = parser.parse_args()
    if 'func' in args:
        args.func(**vars(args))
    else:
        parser.print_help()


if __name__ == '__main__':
    main()