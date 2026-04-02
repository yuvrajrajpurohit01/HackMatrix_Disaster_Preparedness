# DisasterSense – Disaster Preparedness App

> From prediction to protection — helping people stay safe before, during, and after disasters.

---

## Overview

DisasterSense is a next-generation AI-powered disaster intelligence system designed to help people respond faster and smarter during emergencies. It combines early risk prediction, real-time crowd updates, safe routing, offline emergency guidance, and voice assistance into one unified platform.

The goal is to reduce panic, improve decision-making, and save lives in disaster-prone regions.

---

## Problem Statement

Natural disasters such as floods, heatwaves, earthquakes, and wildfires are increasing every year. When they strike, people often receive delayed alerts, no local guidance, and no clear action plan.

For example, imagine waking up at 2 AM to rising floodwater. You receive a generic message like “Stay safe,” but there is no map, no route, and no step-by-step guidance. This is the reality for millions of people every disaster season.

Families, students, travelers, and entire communities are affected. In those critical moments, the absence of real-time local information leads to panic and unsafe decisions, turning a manageable situation into a life-threatening one.

---

## Why It Matters

Delayed information causes panic, injuries, and loss of life.  
The first few hours of a disaster are often the most dangerous, not only because of the disaster itself, but because people do not know what is happening around them.

There is a serious need for a fast, intelligent, and accessible emergency system that can guide users with clarity when it matters most.

---

## Existing Solutions and Gaps

Current solutions include government SMS alerts, weather apps, news channels, NDMA portals, and map services. Each of these tools solves only one small part of the problem.

Their limitations are clear: they are not real-time or hyper-local, they do not use AI-based prediction, they do not include user-generated updates, they do not give step-by-step emergency guidance, and many do not work offline.

The gap is not just a missing feature — it is a missing category. There is no single unified platform that combines AI prediction, crowd intelligence, smart routing, and offline support. DisasterSense bridges that gap.

---

## Proposed Solution

DisasterSense is not just an alert app. It is a full-stack AI disaster intelligence system that thinks ahead of the disaster, communicates during it, and guides people through it, even without internet.

It predicts risk before the event, updates users in real time as conditions change, and provides safe actions when the situation becomes critical.

### Key Features
- AI Risk Prediction Engine
- Live Crowd Disaster Map
- Smart Safe Route Generator
- Offline Emergency Guide
- Voice AI Assistant

---

## How It Works

A user opens DisasterSense in the morning, and the app silently analyzes their location along with live data. If it detects a high-risk situation, it instantly suggests a safe route and the nearest shelter.

As conditions worsen, nearby users upload live updates. The AI classifies incidents and updates the map automatically, so routes adjust around danger zones.

When the network goes down, the offline guide and voice assistant continue to support the user with step-by-step instructions until they reach safety.

---

## Main Features

### 1. AI Risk Prediction
The system analyzes weather data, historical disaster patterns, and local conditions to estimate risk levels for the user's exact location.

### 2. Live Crowd Disaster Map
Users can submit photos or reports. The system classifies incidents such as floods, fires, road blocks, or shelters and places them on a live map.

### 3. Smart Safe Route Generator
The app calculates the safest evacuation route by avoiding danger zones and updating the path in real time.

### 4. Offline Emergency Guide
When internet access is lost, the app still provides safety instructions, emergency steps, and basic survival guidance.

### 5. Voice AI Assistant
Users can speak naturally during panic situations, and the app responds with instant guidance and emergency steps.

---

## System Architecture

DisasterSense follows a structured flow where user inputs are processed through the frontend and backend, integrated with real-time APIs and AI logic to analyze risks and deliver instant alerts, safe routes, and emergency guidance.

### Architecture Flow
User Layer → Application Layer → Backend Layer → AI/ML Layer → Data Layer → External APIs

### Layers
- **User Layer:** Mobile app, web dashboard, and voice assistant
- **Application Layer:** Real-time map, alert display, and incident reporting
- **Backend Layer:** User management, alert processing, route generation, and data aggregation
- **AI/ML Layer:** Risk prediction, image analysis, and NLP modules
- **Data Layer:** User reports and historical data storage
- **External APIs:** Weather data, maps, routing, and emergency service integration

---

## Working Process

```text
App opens
→ Location detected instantly
→ Real-time conditions analyzed
→ Risk alert with time estimate displayed

As the situation evolves
→ Users upload live reports
→ Map updates with danger zones
→ Safe route automatically adjusts

When conditions become critical
→ Voice guidance activated
→ Emergency Mode enabled with one tap
→ Location shared with trusted contacts

In case of network failure
→ Offline guide continues to provide support
```
## 🛠️ Implementation Plan

- Design a simple and intuitive user interface with location detection  
- Integrate weather and environmental APIs to collect real-time data  
- Develop the backend system to process incoming data and store information efficiently  
- Build the AI model to predict potential disaster risks in real time  
- Visualize risk levels and alerts on an interactive map  
- Enable live crowd reporting for dynamic disaster updates  
- Integrate SOS and emergency response features with real-time location sharing  
- Test, optimize, and refine the system for accuracy, speed, and reliability  

---

## 🧰 Tech Stack

### Frontend
- HTML  
- CSS  
- JavaScript  

Used to build a simple, responsive, and user-friendly interface.

---

### Backend
- Node.js  
- Express.js  

Handles server logic, API requests, and data processing.

---

### Database
- Firebase  
- MongoDB  

Stores real-time data and enables instant updates.

---

### APIs and Tools
- GeoLocation API — Detects the user’s current location for personalized alerts  
- OpenWeather API — Provides real-time weather data for risk analysis  
- Google Maps API — Displays maps and helps generate safe routes  

---

### AI and Logic
- Python  
- Scikit-learn — Basic risk prediction model  
- Pandas — Data handling  
- Rule-based logic — Fast decision making  

---

## 📊 Expected Outcome

DisasterSense delivers a real-time, location-specific alert system that combines AI risk predictions with live community updates. Users receive early warnings, continuously updated danger maps, and dynamically generated safe routes, along with an offline emergency guide for uninterrupted support.

---

## 👥 Benefits to Users

- Critical time to act with advance warnings  
- Crowd-verified real-time conditions  
- Step-by-step voice-guided assistance  
- Continuous support even without internet  

---

## 🌍 Real-World Impact

- Saves lives with early warnings  
- Reduces panic through clear guidance  
- Improves real-time community awareness  
- Works even without internet  
- Scalable for large-scale disaster management  

---

## 🔮 Future Scope

### Future Improvements
- Integration with government systems and official APIs (IMD, NDMA)  
- Satellite imagery and drone-feed integration for aerial monitoring  
- Advanced AI models for earlier and more accurate risk prediction  
- Multilingual voice support (Hindi and regional languages)  
- Wearable SOS device integration for instant emergency alerts  

---

### 📈 Scalability
- Deployable across cities, states, and countries globally  
- Works in low or no network conditions  
- Adaptable to multiple disaster types and environments  
- Easily integrable with national disaster management systems  

---

## 🏁 Final Summary

DisasterSense is a next-generation, AI-powered disaster intelligence system that combines prediction, real-time awareness, and continuous guidance into one unified platform. It addresses a critical real-world gap with a scalable and production-ready approach, making it capable of evolving from a hackathon solution into essential public safety infrastructure.

---

## 👨‍💻 Team Hackover

- Gokul Karthic  
- Aditya Raj  
- Ashwani Pandey  
- Yuvraj Rajpurohit  
