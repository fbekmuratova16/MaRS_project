# -*- coding: utf-8 -*-

import sys
import traceback
from CGRtools.files.RDFrw import RDFread, RDFwrite
from itertools import count
import itertools
from MARS.models import Molecules
from pony.orm import db_session
from MARS.models import Reactions
from MARS.models import ReactionsMolecules


def fill_database_core(**kwargs):
    it = iter(RDFread(kwargs['input']))
    chunksize = kwargs['chunksize']

    for x in itertools.zip_longest(*[it]*chunksize):
        if None in x:
            y = []
            for i in x:
                if i is None:
                    break
                y.append(i)
            x = y

        print(x)

        substrats_list = []
        products_list = []

        for i in x:
            for j in i['substrats']:
                substrats_list.append(j)
            for u in i['products']:
                products_list.append(u)

        print(substrats_list)
        print(products_list)

        substrats_fp = Molecules.get_fingerprints(substrats_list)
        products_fp = Molecules.get_fingerprints(products_list)

        with db_session():
            for i in range(0,len(substrats_list)):
                substrat_fear = Molecules.get_fear(substrats_list[i])
                if not Molecules.exists(fear=substrat_fear):
                    Molecules(substrats_list[i],substrats_fp[i])

            for i in range(0,len(products_list)):
                product_fear = Molecules.get_fear(products_list[i])
                if not Molecules.exists(fear=product_fear ):
                    Molecules(products_list[i], products_fp[i])

            for reaction in x:
                react_fear = Reactions.get_fear(reaction)
                if not Reactions.exists(fear=react_fear):
                    Reactions(reaction)






