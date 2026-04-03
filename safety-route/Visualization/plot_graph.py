# visualization/plot_graph.py

import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(G, nodes, path, danger_nodes):
    pos = nx.spring_layout(G, seed=42)

    colors = []

    for node in G.nodes():
        if node in danger_nodes:
            colors.append("red")  # danger
        elif path and node in path:
            colors.append("green")  # safe route
        elif nodes[node]["type"] == "shelter":
            colors.append("blue")  # shelter
        elif nodes[node]["type"] == "supply":
            colors.append("yellow")  # supply
        elif nodes[node]["type"] == "start":
            colors.append("purple")  # start
        elif nodes[node]["type"] == "destination":
            colors.append("black")  # destination
        else:
            colors.append("gray")  # normal

    plt.figure(figsize=(8, 6))

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color=colors,
        node_size=1200,
        font_size=10,
        font_weight="bold"
    )

    return plt