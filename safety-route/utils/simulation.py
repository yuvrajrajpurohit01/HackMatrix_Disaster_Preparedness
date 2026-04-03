# utils/simulation.py

import random

def simulate_danger(nodes):
    all_nodes = list(nodes.keys())
    return random.sample(all_nodes, 2)