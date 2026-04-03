
# DisasterSense: AI-Powered Disaster Intelligence System

## 1. Introduction

DisasterSense is an intelligent disaster management system designed to predict, monitor, and respond to natural and human-made disasters in real time. The system integrates machine learning, geolocation, voice interaction, and visualization tools to provide users with actionable insights and safety recommendations.

The application is built using Streamlit and provides a modular interface for risk prediction, live mapping, route planning, voice assistance, and offline emergency guidance.

---

## 2. Objectives

- To predict disaster risk using environmental parameters
- To provide real-time situational awareness using APIs
- To assist users with voice-based interaction
- To generate safe evacuation routes avoiding danger zones
- To offer comprehensive offline survival guidance
- To visualize disaster-related data using interactive charts and maps

---

## 3. System Architecture

The system consists of the following modules:

1. Dashboard
2. Risk Prediction Engine
3. Live Map Visualization
4. Safe Route Generator
5. Offline Emergency Guide
6. Voice AI Assistant

Each module operates independently but shares common data such as user location and environmental inputs.

---

## 4. Technologies Used

### Frontend
- Streamlit: Used to build the interactive web interface

### Backend
- Python: Core programming language

### Libraries
- streamlit: UI framework
- streamlit-option-menu: Sidebar navigation
- pyttsx3: Text-to-speech engine
- speech_recognition: Voice input processing
- pydeck: Map visualization
- pandas: Data handling
- requests: API communication
- pickle: Model loading
- streamlit-js-eval: Browser-based geolocation

---

## 5. Module Descriptions

### 5.1 Dashboard

Displays:
- User’s current GPS location
- Real-time weather data (temperature, humidity, condition)
- Alerts based on environmental thresholds

Uses:
- `get_geolocation()` for location detection
- `get_weather()` for API-based weather data

---

### 5.2 Risk Prediction Module

#### Input Parameters:
- Rainfall
- Temperature
- Humidity
- Wind Speed
- River Level
- Earthquake Magnitude

#### Processing:
- Data is passed into a pre-trained machine learning model (`model.pkl`)
- A custom risk score is calculated using weighted contributions

#### Output:
- Risk Level (Low, Medium, High)
- Risk Score (0–100)
- Confidence Score
- Risk Factor Analysis
- Recommendations

#### Visualization:
- Bar charts for input parameters
- Bar charts for risk contribution
- Line chart for trend simulation

---

### 5.3 Live Map Module

Displays:
- User location using latitude and longitude
- Danger zones marked dynamically

Uses:
- `pydeck` and `st.map()` for visualization
- Data stored in session state for real-time updates

---

### 5.4 Safe Route Module

#### Functionality:
- Generates navigation routes using browser-based map links
- Avoids danger zones using spatial logic

#### Logic:
- Checks if user location is near a danger zone
- If yes, generates a detour point
- Creates a modified route avoiding unsafe areas

#### Output:
- Safe route link using Google Maps URL

---

### 5.5 Offline Emergency Guide

Provides:
- Disaster-specific instructions (Fire, Flood, Earthquake)
- Divided into:
  - Before
  - During
  - After

Includes:
- Food and water preservation guidelines
- Emergency kit checklist
- Evacuation planning
- General survival tips

This module works without internet access.

---

### 5.6 Voice AI Assistant

#### Features:
- Accepts voice input using microphone
- Converts speech to text
- Detects user intent
- Responds with text and speech

#### Supported Commands:
- Fire alerts
- Flood alerts
- Earthquake alerts
- Weather queries
- Location queries
- Route navigation
- System status
- Emergency help

#### Components:
- `speech_recognition` for input
- `pyttsx3` for output
- `detect_intent()` for command classification

---

## 6. API Integration

### OpenWeather API

Used for:
- Real-time temperature
- Humidity
- Weather conditions

Endpoint:

---

## 7. Machine Learning Model

- Loaded using `pickle`
- Accepts numerical environmental inputs
- Outputs categorical risk levels

---

## 8. Data Flow

1. User provides input or voice command
2. System processes input using logic or ML model
3. APIs fetch real-time environmental data
4. Results are visualized using charts/maps
5. System provides recommendations and alerts

---

## 9. UI/UX Features

- Glassmorphism design
- Animated background
- Notification panel
- Blinking alert system
- Interactive charts and maps

---

## 10. Installation

### Step 1: Install dependencies

---

## 11. Limitations

- Route optimization is heuristic-based (not real-time traffic aware)
- Requires internet for weather API and maps
- Voice recognition accuracy depends on microphone quality
- ML model accuracy depends on training data

---

## 12. Future Enhancements

- Integration with real-time disaster APIs
- Live camera-based fire detection using computer vision
- Advanced route optimization using GIS systems
- Mobile application version
- Multi-language voice support
- AI chatbot integration

---

## 13. Conclusion

DisasterSense demonstrates a complete disaster intelligence system combining machine learning, real-time data, and user interaction. It enhances situational awareness, improves decision-making, and provides practical safety solutions.

This system can be further extended into a scalable real-world disaster management platform.
