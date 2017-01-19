import CGRtools.files.RDFrw as RDFrw
rdffile = open('Your_rdf_file.rdf','r')
reacttuple = RDFrw.RDFread(rdffile)
reactlist = reacttuple.read()

react0 = reactlist[0]
react0s = react0.substrats
react0p = react0.products

# v.2: 18/01/2017/17:30

tempreaction = react0
tempfear = get_fear(tempreaction)
query0 = select(r.id for r in Reactions if tempfear = r.fear)[:]
     # проверка на наличие переданной реакции в БД
if query0.len() = 0:
     # Если такой реакции нет в БД
     super(self, Reactions).__init__(fear=fear_str, fingerprint=fingerprint)

     for molecs in tempreaction.substarts:
         tempfearm1 = get_fear(molecs)
         query1 = Molecules.get(fear = tempfearm1)
         # существуют ли исходные в-ва реакции в БД. Проверка по строковому представлению молекулы

         if not query1:
             fear_str = get_fear(molecs)
             data = node_link_data(molecs)
             if fingerprint is None:
                 fingerprint = self.get_fingerprints([molecs])[0]

         ms = Molecules(data = data, fear = fear_str, fingerprint =
fingerprint)
         rm = ReactionsMolecules(molecule = ms, reaction = self, product
= False, mapping = dict([]))


     for molecp in tempreaction.products:
         tempfearm2 = get_fear(molecp)
         query2 = Molecules.get(fear = tempfearm2)
         # существуют ли образующиеся в-ва реакции в БД. Проверка по строковому представлению молекулы

         if not query2:
             fear_str = get_fear(molecp)
             data = node_link_data(molecp)
             if fingerprint is None:
                 fingerprint = self.get_fingerprints([molecp])[0]

         mp = Molecules(data = data, fear = fear_str, fingerprint =
fingerprint)
         rm = ReactionsMolecules(molecule = mp, reaction = self, product
= True, mapping = dict([]))

commit()