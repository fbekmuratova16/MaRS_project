import networkx as nx

G = nx.path_graph(3)

mapping = {0:'a',1:'b',2:'c'}

H=nx.relabel_nodes(G,mapping)
print(sorted(H.nodes()))
