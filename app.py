import streamlit as st
from streamlit_option_menu import option_menu
import pyttsx3
import pickle
model = pickle.load(open("model.pkl", "rb"))

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    engine.say(text)
    engine.runAndWait()

# Page config
st.set_page_config(
    page_title="DisasterSense",
    page_icon="🚨",
    layout="wide"
)

# Custom CSS (Dark + Premium UI)
st.markdown("""
<style>
body {
    background-color: #0f172a;
}
.main {
    background-color: #0f172a;
}
h1, h2, h3 {
    color: #e2e8f0;
}
.stButton>button {
    background-color: #ef4444;
    color: white;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    selected = option_menu(
        "DisasterSense",
        ["Dashboard", "Risk Prediction", "Live Map", "Safe Route", "Offline Guide", "Voice AI"],
        icons=["house", "activity", "globe", "map", "book", "mic"],
        menu_icon="cast",
        default_index=0
    )

# ---------------- DASHBOARD ----------------
if selected == "Dashboard":
    st.title("🚨 DisasterSense Dashboard")
    st.subheader("AI Disaster Intelligence System")

    col1, col2, col3 = st.columns(3)

    col1.metric("Risk Level", "High", "+20%")
    col2.metric("Active Alerts", "5", "+2")
    col3.metric("Safe Zones Nearby", "3")

    st.markdown("### 📊 System Overview")
    st.info("AI is actively monitoring environmental and crowd data.")

# ---------------- RISK PREDICTION ----------------
elif selected == "Risk Prediction":
    st.title("🧠 AI Risk Prediction Engine")

    rainfall = st.number_input("Rainfall (mm)")
    temperature = st.number_input("Temperature (°C)")
    humidity = st.number_input("Humidity (%)")
    wind_speed = st.number_input("Wind Speed")
    river_level = st.number_input("River Level")
    earthquake = st.number_input("Earthquake Magnitude")

    if st.button("Predict Risk"):
        input_data = [[rainfall, temperature, humidity, wind_speed, river_level, earthquake]]
        prediction = model.predict(input_data)[0]

        if prediction == 0:
            st.success("🟢 Low Risk")
        elif prediction == 1:
            st.warning("🟡 Medium Risk")
        else:
            st.error("🔴 High Risk")

# ---------------- LIVE MAP ----------------
elif selected == "Live Map":
    import pydeck as pdk
    import pandas as pd

    st.title("🌍 Live Crowd Disaster Map")

    # Sample disaster points (you can later replace with real data)
    data = pd.DataFrame({
        'lat': [23.0225, 23.0300, 23.0150],
        'lon': [72.5714, 72.5800, 72.5600],
        'type': ['Fire', 'Flood', 'Accident']
    })

    layer = pdk.Layer(
        "ScatterplotLayer",
        data,
        get_position='[lon, lat]',
        get_radius=200,
        get_fill_color='[255, 0, 0, 160]',
        pickable=True
    )

    view_state = pdk.ViewState(
        latitude=23.0225,
        longitude=72.5714,
        zoom=12,
        pitch=0
    )

    st.pydeck_chart(pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        tooltip={"text": "{type}"}
    ))

    st.info("Red zones indicate reported disaster locations")

    st.markdown("### 🚨 Report New Incident")

lat = st.number_input("Latitude", value=23.02)
lon = st.number_input("Longitude", value=72.57)
dtype = st.selectbox("Disaster Type", ["Fire", "Flood", "Accident"])

if st.button("Submit Report"):
    st.success("Incident reported successfully!")

# ---------------- SAFE ROUTE ----------------
elif selected == "Safe Route":
    st.title("🧭 Smart Safe Route Generator")

    start = st.text_input("Current Location")
    destination = st.text_input("Safe Destination")

    if st.button("Generate Route"):
        st.success("✅ Safest route generated avoiding danger zones")

# ---------------- OFFLINE GUIDE ----------------
elif selected == "Offline Guide":
    st.title("📘 Offline Emergency Guide")

    guide = st.selectbox(
        "Select Emergency Type",
        ["Fire", "Flood", "Earthquake"]
    )

    if guide == "Fire":
        st.write("🔥 Stay low, avoid smoke, exit immediately.")
    elif guide == "Flood":
        st.write("🌊 Move to higher ground immediately.")
    elif guide == "Earthquake":
        st.write("🏢 Drop, Cover, Hold.")

# ---------------- VOICE AI ----------------
elif selected == "Voice AI":
    st.title("🎙️ Voice AI Assistant")

    user_input = st.text_input("Ask something (e.g., What to do in fire?)")

    if st.button("Get Help"):
        response = ""

        if "fire" in user_input.lower():
            response = "Stay low, avoid smoke, and exit immediately."
        elif "flood" in user_input.lower():
            response = "Move to higher ground and avoid water flow."
        elif "earthquake" in user_input.lower():
            response = "Drop, cover, and hold on."
        else:
            response = "I am here to help during emergencies."

        st.success(response)

        # 🔊 Speak response
        speak(response)