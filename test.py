import sys
import traceback
from CGRtools.files.RDFrw import RDFread, RDFwrite


file1 = open('DA_new.rdf','r')
a = RDFread(file1)
print(a)