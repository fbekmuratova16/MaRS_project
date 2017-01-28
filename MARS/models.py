# -*- coding: utf-8 -*-
from pony.orm import Database, PrimaryKey, Required, Set, Json, buffer, left_join, sql_debug, select, commit
from CGRtools.FEAR import FEAR
from networkx.readwrite.json_graph import node_link_data, node_link_graph
from MODtools.descriptors.fragmentor import Fragmentor
from CGRtools.CGRcore import CGRcore
from functools import reduce
from CGRtools.files.SDFrw import MoleculeContainer
from CGRtools.files.RDFrw import RDFread, ReactionContainer
import networkx as nx
from .files.Zulfia import get_bitstring

db = Database()
fear = FEAR()
cgr_core=CGRcore()
fragmentor_mol = Fragmentor()
fragmentor_rct = Fragmentor()

class Molecules(db.Entity):
    id = PrimaryKey(int, auto=True)
    data = Required(Json)
    fear = Required(str, unique=True)
    fingerprint = Required(bytes)
    reactions = Set('ReactionsMolecules')

    def __init__(self, molecule, fingerprint=None):
        fear_str = self.get_fear(molecule)
        data = node_link_data(molecule)

        if fingerprint is None:
            fingerprint = self.get_fingerprints([molecule])[0]

        super(Molecules,self).__init__(data=data, fear=fear_str, fingerprint=fingerprint.bytes)

    @staticmethod
    def get_molecule(molecule):
        return Molecules.get(fear=fear.get_cgr_string(Molecules))

    @staticmethod
    def get_fingerprints(molecules):
        dataframe = fragmentor_mol.get(molecules)['X']
        return get_bitstring(dataframe)

    @staticmethod
    def get_fear(molecule):
        return fear.get_cgr_string(molecule)

    @property
    def structure(self):
        molcont = node_link_graph(self.data)
        molcont.__class__ = MoleculeContainer
        return molcont


class Reactions(db.Entity):
    id = PrimaryKey(int, auto=True)
    fear = Required(str, unique=True)
    fingerprint = Required(bytes) #Boris: changed buffer to bytes
    molecules = Set('ReactionsMolecules', cascade_delete=True)

    #Таблица реакиц это просто запись, что там нужно делать, к ней нужно подключить таблицу молекул, а была ли такая молекула в таблице молекул
    # если нет то добавить с марингом и изоморфным вложение и указанием роли. ИМ чтобы выяснить. МАР - словарь превратить в словарь цифр, пар столько сколько и атомов лист имеет четкое число элементов.
    #добавление объектов мэни ту мэни в пони
    def __init__(self, reaction, fingerprint=None):
        tempfear = Reactions.get_fear(reaction)
        # Boris: deleted entity check, cause it's supposed to be done outside of the class
        if fingerprint is None:  # Boris: added situation when FP is None
            fingerprint = self.get_fingerprints([reaction])[0]

        super(Reactions,self).__init__(fear=tempfear, fingerprint=fingerprint.bytes) # Boris: swapped Reactions and self

        for molecs in reaction.substrats:
            tempfearm1 = Molecules.get_fear(molecs)
            molecule = Molecules.get(fear=tempfearm1)
                
            # существуют ли исходные в-ва реакции в БД
            if not molecule:
                molecule=Molecules(molecs)

            # Boris: No object link rm is required to create new entity
            ReactionsMolecules(molecule=molecule, reaction=self, product=False, mapping=dict([]))

        for molecp in reaction.products:
            tempfearm2=Molecules.get_fear(molecp)
            molecule=Molecules.get(fear=tempfearm2)
                
            # существуют ли исходные в-ва реакции в БД
            if not molecule:
                 molecule=Molecules(molecp)

            # Boris: No object link rm is required to create new entity
            ReactionsMolecules(molecule=molecule, reaction=self, product=True, mapping=dict([]))

    @staticmethod
    def get_fingerprints(reactions, get_cgr=False):
        cgrs = []
        for reaction in reactions:
            cgr = cgr_core.getCGR(reaction)
            cgrs.append(cgr)

        dataframe = fragmentor_rct.get(cgrs)['X']

        return (get_bitstring(dataframe), cgrs) if get_cgr else get_bitstring(dataframe)

    @staticmethod
    def get_reaction(reaction):
        cgr = cgr_core.getCGR(reaction)
        return Reactions.get(fear=fear.get_cgr_string(cgr))

    @staticmethod
    def get_reactions_by_molecule(molecule, product=None):
        if product is None:
            q = left_join(
                rs.reaction for m in Molecules if m.fear == fear.get_cgr_string(molecule) for rs in m.reactions)
        else:
            q = left_join(rs.reaction for m in Molecules if m.fear == fear.get_cgr_string(molecule) for rs in m.reactions if
                          rs.product == product)
        return list(q)

    @staticmethod
    def get_reactions_by_molecules(molecule, product=None, reagent=None):
        d = dict()
        if product is not None:
            for i in product:
                d[fear.get_cgr_string(molecule)] = set()
            for m, r in left_join(
                    (m.fear, r) for m in Molecules if m.fear in [fear.get_cgr_string(x) for x in product] for rs in
                    m.reactions if rs.product for r in rs.reactions):
                d[m].add(r)

        if reagent is not None:
            for i in reagent:
                d[fear.get_cgr_string(molecule)] = set()
            for m, r in left_join(
                    (m.fear, r) for m in Molecules if m.fear in [fear.get_cgr_string(x) for x in reagent] for rs in
                    m.reactions if not rs.product for r in rs.reactions):
                d[m].add(r)

        return reduce(set.intersection, d.values())

    @staticmethod
    def get_fear(reaction):
        return fear.get_cgr_string(cgr_core.getCGR(reaction))

    @property
    def structure(self):
        products = []
        substrats = []
        for mr in self.molecules:
            molcont = nx.relabel_nodes(mr.molecule.structure, dict(mr.mapping))
            if mr.product:
                products.append(molcont)
            else:
                substrats.append(molcont)
        return ReactionContainer(products=products, substrats=substrats)


class ReactionsMolecules(db.Entity):
    id = PrimaryKey(int, auto=True)
    molecule = Required(Molecules)
    reaction = Required(Reactions)
    product = Required(bool)
    mapping = Required(Json)


db.bind("sqlite", "datatest.db")
db.generate_mapping(create_tables=True)
sql_debug(True)

