from CGRtools.CGRreactor import CGRreactor
from CGRtools.files.SDFrw import SDFread
from networkx.algorithms import isomorphism
#a=list(SDFread(open('hasan.sdf')).read())

def Feruza_isomorph(a): # a - SDF file
    cgrr = CGRreactor()
    for x in a:
        iso = cgrr.spgraphmatcher(x, a[9])
        if iso.is_isomorphic():
            return ('isomorph')
        else:
            if iso.subgraph_is_isomorphic():
                return ('subgriso')