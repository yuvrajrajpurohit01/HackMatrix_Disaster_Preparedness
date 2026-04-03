import streamlit as st
import folium
from streamlit_folium import st_folium
from folium.plugins import HeatMap
import random
import math
import networkx as nx

from data.nodes import nodes
from data.edges import edges

st.set_page_config(page_title="DisasterSense", layout="wide")

st.title("🌍 DisasterSense - Smart Safety Routing System")

# ------------------ GRAPH BUILD ------------------
def build_graph():
    G = nx.Graph()
    G.add_edges_from(edges)
    return G

# ------------------ SIMULATION ------------------
def simulate_danger(nodes):
    all_nodes = list(nodes.keys())
    return random.sample(all_nodes, 3)

# ------------------ DISTANCE ------------------
def distance(p1, p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2) ** 0.5

# ------------------ NEAREST SHELTER ------------------
def find_nearest_shelter(start, nodes):
    start_pos = nodes[start]["pos"]
    shelters = [n for n in nodes if nodes[n]["type"] == "shelter"]
    nearest = min(shelters, key=lambda s: distance(start_pos, nodes[s]["pos"]))
    return nearest

# ------------------ CLEAN SAFE ROUTE ------------------
def find_clean_safe_route(G, start, end, danger_nodes):
    G_safe = G.copy()

    # Remove danger nodes except start/end
    filtered_danger = [d for d in danger_nodes if d != start and d != end]
    G_safe.remove_nodes_from(filtered_danger)

    try:
        return nx.shortest_path(G_safe, start, end)
    except:
        # fallback with weighted routing
        for u, v in G.edges():
            if u in danger_nodes or v in danger_nodes:
                G[u][v]['weight'] = 10
            else:
                G[u][v]['weight'] = 1

        try:
            return nx.shortest_path(G, start, end, weight='weight')
        except:
            return None

# ------------------ SIDEBAR ------------------
st.sidebar.title("⚙️ Control Panel")

start = st.sidebar.selectbox("Select Start Location", list(nodes.keys()))

mode = st.sidebar.radio("Select Mode", ["Auto Shelter", "Custom Destination"])

if mode == "Custom Destination":
    destination = st.sidebar.selectbox("Select Destination", list(nodes.keys()))
else:
    destination = None

# Danger simulation
if "danger_nodes" not in st.session_state:
    st.session_state.danger_nodes = simulate_danger(nodes)

if st.sidebar.button("🔄 Simulate Disaster"):
    st.session_state.danger_nodes = simulate_danger(nodes)

danger_nodes = st.session_state.danger_nodes

st.sidebar.write("🚨 Danger Zones:", danger_nodes)

# ------------------ LOGIC ------------------
G = build_graph()

if destination is None:
    destination = find_nearest_shelter(start, nodes)

path = find_clean_safe_route(G, start, destination, danger_nodes)

st.subheader(f"🎯 Destination: {destination} ({nodes[destination]['name']})")

# ------------------ MAP ------------------
m = folium.Map(location=nodes[start]["pos"], zoom_start=13)

# Highlight START
folium.Marker(
    nodes[start]["pos"],
    popup="START",
    icon=folium.Icon(color="green", icon="play")
).add_to(m)

# Highlight DESTINATION
folium.Marker(
    nodes[destination]["pos"],
    popup="DESTINATION",
    icon=folium.Icon(color="blue", icon="flag")
).add_to(m)

# Show only important nodes (reduce clutter)
for key, val in nodes.items():
    if key not in danger_nodes and (path is None or key not in path):
        continue

    lat, lon = val["pos"]

    icon_color = "gray"
    icon_type = "info-sign"

    if key in danger_nodes:
        icon_color = "red"
        icon_type = "remove"
    elif val["type"] == "shelter":
        icon_color = "blue"
        icon_type = "home"
    elif val["type"] == "supply":
        icon_color = "orange"
        icon_type = "plus"

    folium.Marker(
        [lat, lon],
        popup=f"{val['name']} ({val['type']})",
        icon=folium.Icon(color=icon_color, icon=icon_type)
    ).add_to(m)

# Draw CLEAN route
if path:
    route_coords = [nodes[n]["pos"] for n in path]

    folium.PolyLine(
        route_coords,
        color="green",
        weight=6,
        opacity=0.9
    ).add_to(m)

# Heatmap (danger)
heat_data = [nodes[n]["pos"] for n in danger_nodes]
HeatMap(heat_data).add_to(m)

# Show map
st_folium(m, width=1100, height=650)

# ------------------ ROUTE GUIDE ------------------
st.subheader("🧭 Route Guidance")

if path:
    for node in path:
        node_info = nodes[node]

        msg = f"➡️ Move to {node_info['name']}"

        if node_info["type"] == "shelter":
            msg += " 🏠"
        elif node_info["type"] == "supply":
            msg += " 🧃"
        elif node in danger_nodes:
            msg += " ⚠️"

        st.write(msg)
else:
    st.error("❌ No route available!")

# ------------------ LEGEND ------------------
st.subheader("📍 Map Legend")

st.markdown("""
🟢 Green → Safe Route  
🔴 Red → Danger Zone  
🔵 Blue → Shelter  
🟠 Orange → Supply  
""")