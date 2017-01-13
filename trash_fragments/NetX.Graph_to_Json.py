import networkx as nx
from networkx.readwrite import json_graph

G = nx.Graph([(1,2)])

json1 = json_graph.node_link_data(G)
graph1 = json_graph.node_link_graph(json1)
print(json1)
print(type(graph1))