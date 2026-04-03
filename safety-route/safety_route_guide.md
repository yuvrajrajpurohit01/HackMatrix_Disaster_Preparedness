# Safety Route Module – DisasterSense

The Safety Route Module is the core intelligence layer of DisasterSense that computes the safest possible path during emergencies by dynamically avoiding danger zones and guiding users to safety.

---

## Overview

In disaster situations, traditional navigation systems fail because they do not consider real-time risk.  
This module addresses that limitation using graph-based routing and dynamic risk filtering.

It ensures:
- Safe navigation even in uncertain conditions  
- Automatic rerouting when danger zones appear  
- Intelligent fallback when no fully safe path exists  

---

## Key Features

### Smart Safe Routing
- Removes danger zones from the graph
- Computes shortest safe path using NetworkX
- Ensures start and destination are always reachable

### Adaptive Pathfinding
- If no safe path exists:
  - Switches to weighted routing
  - Minimizes exposure to dangerous areas

### Nearest Shelter Detection
- Automatically finds closest shelter using distance calculation
- Supports emergency evacuation scenarios

### Real-Time Simulation
- Dynamically generates disaster zones
- Updates routes instantly based on new risks

### Clean Visualization
- Map-based routing using Folium
- Color-coded markers for:
  - Danger Zones  
  - Shelters  
  - Supplies  
  - Safe Route  

---

## Tech Stack

- Python  
- NetworkX – Graph-based routing  
- Streamlit – UI framework  
- Folium – Map visualization  
- Random / Math – Simulation and distance logic  

---

## Module Structure

```
safety-route/
│
├── app.py                  # Main Streamlit application
│
├── data/
│   ├── nodes.py            # Locations with coordinates and types
│   ├── edges.py            # Graph connections
│
├── utils/
│   ├── graph_builder.py    # Graph creation
│   ├── simulation.py       # Disaster simulation
│   ├── shelter_finder.py   # Nearest shelter logic
│
├── requirements.txt        # Project dependencies
```
# Safety Route Module – DisasterSense

The Safety Route Module is the core intelligence layer of DisasterSense that computes the safest possible path during emergencies by dynamically avoiding danger zones and guiding users to safety.

---

## Overview

In disaster situations, traditional navigation systems fail because they do not consider real-time risk.  
This module addresses that limitation using graph-based routing and dynamic risk filtering.

It ensures:
- Safe navigation even in uncertain conditions  
- Automatic rerouting when danger zones appear  
- Intelligent fallback when no fully safe path exists  

---

## Key Features

### Smart Safe Routing
- Removes danger zones from the graph  
- Computes shortest safe path using NetworkX  
- Ensures start and destination are always reachable  

### Adaptive Pathfinding
- If no safe path exists:
  - Switches to weighted routing  
  - Minimizes exposure to dangerous areas  

### Nearest Shelter Detection
- Automatically finds closest shelter using distance calculation  
- Supports emergency evacuation scenarios  

### Real-Time Simulation
- Dynamically generates disaster zones  
- Updates routes instantly based on new risks  

### Clean Visualization
- Map-based routing using Folium  
- Color-coded markers for:
  - Danger Zones  
  - Shelters  
  - Supplies  
  - Safe Route  

---

## Tech Stack

- Python  
- NetworkX – Graph-based routing  
- Streamlit – UI framework  
- Fol
