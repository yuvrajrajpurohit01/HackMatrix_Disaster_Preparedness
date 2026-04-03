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
## Requirements

Make sure the following are installed on your system:

- Python (3.8 or above)
- pip (Python package manager)
- Git (optional, for cloning repository)

### Python Libraries

Install all required dependencies using:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install streamlit folium streamlit-folium networkx matplotlib
```

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yuvrajrajpurohit01/HackMatrix_Disaster_Preparedness.git
```

---

### 2. Navigate to the Project Folder

```bash
cd safety-route
```

---

### 3. Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate   (Windows)
```

---

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 5. Run the Application

```bash
streamlit run app.py
```

---

## Working Process

1. The user selects a starting location from the interface  
2. The system simulates or detects danger zones  
3. A graph is constructed using predefined nodes and edges  
4. Danger nodes are removed from the graph dynamically  
5. The system computes the safest route using shortest path logic  
6. If no safe route exists:
   - A weighted fallback path is calculated  
7. The route is displayed on an interactive map  
8. Step-by-step navigation guidance is provided to the user  

---

## Output

- Interactive map with safe route visualization  
- Highlighted danger zones, shelters, and supply areas  
- Dynamic route updates based on changing conditions  
- Step-by-step navigation guidance  
