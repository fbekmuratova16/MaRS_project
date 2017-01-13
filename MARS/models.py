
from pony.orm import Database, PrimaryKey, Required, Set, Json, buffer, left_join
from CGRtools.FEAR import FEAR
from networkx.readwrite.json_graph import node_link_data, node_link_graph
from MODtools.descriptors.fragmentor import Fragmentor
from CGRtools.CGRcore import CGRcore
from functools import reduce


db = Database()
fear = FEAR()
cgr_core=CGRcore()
fragmentor_mol = Fragmentor()
fragmentor_rct = Fragmentor()


class Molecules(db.Entity):
    id = PrimaryKey(int, auto=True)
    data = Required(Json)
    fear = Required(str, unique=True)
    fingerprint = Required(buffer)
    reactions = Set('ReactionsMolecules')

    def __init__(self, molecule, fingerprint=None):
        fear_str = self.get_fear(molecule)
        data = node_link_data(molecule)

        if fingerprint is None:
            fingerprint = self.get_fingerprints([molecule])[0]

        super(self, Molecules).__init__(data=data, fear=fear_str, fingerprint=fingerprint)

    @staticmethod
    def get_molecule(molecule):
        return Molecules.get(fear=fear.getreactionhash(Molecules))

    @staticmethod
    def get_fingerprints(molecules):
        matrix = fragmentor_mol.get(molecules)['X']
        # todo: zulfia
   #     return fingerprints

    @staticmethod
    def get_fear(molecule):
        return fear.getreactionhash(molecule)


class Reactions(db.Entity):
    id = PrimaryKey(int, auto=True)
    fear = Required(str, unique=True)
    fingerprint = Required(buffer)
    molecules = Set('ReactionsMolecules', cascade_delete=True)

    #Таблица реакиц это просто запись, что там нужно делать, к ней нужно подключить таблицу молекул, а была ли такая молекула в таблице молекул
    # если нет то добавить с марингом и изоморфным вложение и указанием роли. ИМ чтобы выяснить. МАР - словарь превратить в словарь цифр, пар столько сколько и атомов лист имеет четкое число элементов.
    #добавление объектов мэни ту мэни в пони
    def __init__(self, fingerprint=None,):
        pass

    @staticmethod
    def get_fingerprints(reactions, get_cgr=False):
        cgrs = []
        matrix = fragmentor_rct.get(cgrs)['X']
        # todo: zulfia
  #      return (fingerprints, cgrs) if get_cgr else fingerprints

    @staticmethod
    def get_reaction(reaction):
        cgr = cgr_core.getCGR(reaction)
        return Reactions.get(fear=fear.getreactionhash(cgr))

    @staticmethod
    def get_reactions_by_molecule(molecule, product=None):
        if product is None:
            q = left_join(
                r for m in Molecules if m.fear == fear.getreactionhash(molecule) for rs in m.reactions for r in
                rs.reactions)
        else:
            q = left_join(r for m in Molecules if m.fear == fear.getreactionhash(molecule) for rs in m.reactions if
                          rs.product == product for r in rs.reactions)
        return list(q)

    @staticmethod
    def get_reactions_by_molecules(product=None, reagent=None):
        d = dict()
        if product is not None:
            for i in product:
                d[i] = set()
            for m, r in left_join(
                    (m.fear, r) for m in Molecules if m.fear in [fear.getreactionhash(x) for x in product] for rs in
                    m.reactions if rs.product for r in rs.reactions):
                d[m].add(r)

        if reagent is not None:
            for i in reagent:
                d[i] = set()
            for m, r in left_join(
                    (m.fear, r) for m in Molecules if m.fear in [fear.getreactionhash(x) for x in reagent] for rs in
                    m.reactions if not rs.product for r in rs.reactions):
                d[m].add(r)

        return reduce(set.intersection, d.values())


class ReactionsMolecules(db.Entity):
    id = PrimaryKey(int, auto=True)
    molecule = Required(Molecules)
    reaction = Required(Reactions)
    product = Required(bool)
    mapping = Required(Json)


db.bind("sqlite", ":memory:")
db.generate_mapping(create_tables=True)


