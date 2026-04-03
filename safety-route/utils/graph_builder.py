# utils/graph_builder.py

import networkx as nx
from data.edges import edges

def build_graph():
    G = nx.Graph()
    G.add_edges_from(edges)
    return G