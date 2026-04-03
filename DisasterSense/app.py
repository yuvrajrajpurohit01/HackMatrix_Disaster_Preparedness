import streamlit as st
from streamlit_option_menu import option_menu
import pyttsx3
import pickle
import speech_recognition as sr
import pydeck as pdk
import pandas as pd
import requests
from streamlit_js_eval import get_geolocation

# ---------------- API KEY ----------------
OPENWEATHER_API_KEY = "4b15d57db43027b9d576072699a45af8"

# ---------------- MODEL ----------------
model = pickle.load(open("model.pkl", "rb"))

# ---------------- VOICE ----------------
def speak(text):
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 160)
        engine.say(text)
        engine.runAndWait()
    except:
        pass

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎤 Listening...")
        audio = r.listen(source)

    try:
        return r.recognize_google(audio)
    except:
        return "Could not understand"

# ---------------- INTENT ----------------
def detect_intent(text):
    text = text.lower()

    if any(w in text for w in ["fire", "smoke", "burn"]):
        return "fire"

    elif any(w in text for w in ["flood", "water", "rain"]):
        return "flood"

    elif any(w in text for w in ["earthquake", "quake", "shake"]):
        return "earthquake"

    elif any(w in text for w in ["weather", "temperature", "climate"]):
        return "weather"

    elif any(w in text for w in ["where am i", "location", "my position"]):
        return "location"

    elif any(w in text for w in ["route", "path", "direction"]):
        return "route"

    elif any(w in text for w in ["risk", "danger level", "safety"]):
        return "risk"

    elif any(w in text for w in ["help", "emergency", "what to do"]):
        return "help"

    elif any(w in text for w in ["status", "system", "working"]):
        return "status"

    elif any(w in text for w in ["hello", "hi", "hey"]):
        return "greeting"

    else:
        return "unknown"

# ---------------- WEATHER ----------------
def get_weather(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPENWEATHER_API_KEY}&units=metric"
    res = requests.get(url).json()

    if res.get("main"):
        return {
            "temp": res["main"]["temp"],
            "humidity": res["main"]["humidity"],
            "weather": res["weather"][0]["description"]
        }
    return None

# ---------------- PAGE ----------------
st.set_page_config(page_title="DisasterSense", layout="wide")
# ---------------- BACKGROUND IMAGE ----------------
st.markdown("""
<style>
.stApp {
    background-image: url("https://images.unsplash.com/photo-1581093588401-16f0b9c1cdd0");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}
    

.main {
    background: rgba(15, 23, 42, 0.85); /* dark overlay */
    padding: 20px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)


# ---------------- GPS ----------------
location = get_geolocation()

if location:
    user_lat = location["coords"]["latitude"]
    user_lon = location["coords"]["longitude"]
else:
    user_lat, user_lon = 23.0225, 72.5714

# ---------------- SIDEBAR ----------------
with st.sidebar:
    selected = option_menu(
        "DisasterSense",
        ["Dashboard", "Risk Prediction", "Live Map", "Safe Route", "Offline Guide", "Voice AI"],
        icons=["house", "activity", "globe", "map", "book", "mic"]
    )

# ---------------- DASHBOARD ----------------
if selected == "Dashboard":
    st.title("🚨 DisasterSense Dashboard")

    st.success(f"📍 Location: {user_lat}, {user_lon}")

    weather = get_weather(user_lat, user_lon)

    if weather:
        st.metric("Temperature", f"{weather['temp']} °C")
        st.metric("Humidity", f"{weather['humidity']}%")
        st.info(f"Condition: {weather['weather']}")

        if weather['humidity'] > 80:
            st.warning("⚠️ High Flood Risk!")

# ---------------- RISK ----------------
# ---------------- RISK PREDICTION ----------------
elif selected == "Risk Prediction":
    st.title("🧠 AI Risk Prediction System")

    rainfall = st.number_input("Rainfall (mm)")
    temperature = st.number_input("Temperature (°C)")
    humidity = st.number_input("Humidity (%)")
    wind = st.number_input("Wind Speed")
    river = st.number_input("River Level")
    quake = st.number_input("Earthquake Magnitude")

    # 🔄 Auto-fill weather
    if st.button("Auto Fill from Live Weather"):
        weather = get_weather(user_lat, user_lon)
        if weather:
            temperature = weather["temp"]
            humidity = weather["humidity"]
            st.success("✅ Weather data loaded!")

    # 🔮 Prediction
    if st.button("Predict Risk"):

        input_data = [rainfall, temperature, humidity, wind, river, quake]
        pred = model.predict([input_data])[0]

        # 🔢 Risk Score (custom logic)
        risk_score = (
            rainfall * 0.3 +
            humidity * 0.2 +
            wind * 0.1 +
            river * 0.3 +
            quake * 10
        )

        risk_score = min(100, round(risk_score, 2))

        # 🎯 Risk Level
        if pred == 0:
            level = "Low"
        elif pred == 1:
            level = "Medium"
        else:
            level = "High"

        # 📊 Display
        st.markdown(f"### 🚨 Risk Level: {level}")
        st.progress(risk_score / 100)
        st.metric("Risk Score", f"{risk_score}/100")

        # 🎯 Confidence Score
        confidence = 80 + (risk_score / 5)
        confidence = min(99, round(confidence, 2))
        st.metric("Model Confidence", f"{confidence}%")

        # 📊 Risk Factors
        st.markdown("### 📊 Risk Factors")

        if rainfall > 100:
            st.warning("🌧 High rainfall contributing to flood risk")

        if river > 5:
            st.warning("🌊 River level is critical")

        if quake > 5:
            st.warning("🌍 Earthquake magnitude is dangerous")

        if wind > 50:
            st.warning("💨 Strong winds increasing disaster spread")

        if humidity > 80:
            st.warning("💧 High humidity indicates possible flooding")

        # 🧠 Recommendations
        st.markdown("### 🧠 AI Recommendations")

        if level == "High":
            st.error("""
            - Evacuate immediately if in danger zone
            - Avoid rivers and low areas
            - Keep emergency kit ready
            """)

        elif level == "Medium":
            st.warning("""
            - Stay alert
            - Monitor weather updates
            - Prepare evacuation plan
            """)

        else:
            st.success("""
            - Situation is stable
            - Continue monitoring conditions
            """)
# ---------------- MAP ----------------
elif selected == "Live Map":
    st.title("🌍 Live Map")

    data = pd.DataFrame({
        'lat': [user_lat],
        'lon': [user_lon]
    })

    st.map(data)
    

# ---------------- ROUTE ----------------
elif selected == "Safe Route":
    st.title("🧭 Route (No API Mode)")

    start = st.text_input("Start Location", f"{user_lat},{user_lon}")
    end = st.text_input("Destination")

    if st.button("Generate Route"):
        if end:
            st.success("✅ Opening route in browser")

            st.markdown(
                f"[📍 Open Route in Google Maps](https://www.google.com/maps/dir/{start}/{end})"
            )
        else:
            st.error("Enter destination")

        

# ---------------- GUIDE ----------------
# ---------------- OFFLINE GUIDE ----------------
elif selected == "Offline Guide":
    st.title("📘 Smart Offline Emergency Guide")

    disaster = st.selectbox(
        "Select Emergency Type",
        ["Fire", "Flood", "Earthquake"]
    )

    st.markdown("## 🧭 Survival Phases")
    phase = st.radio("Choose Phase", ["Before", "During", "After"])

    # ---------------- FIRE ----------------
    if disaster == "Fire":

        if phase == "Before":
            st.markdown("""
            🔥 **Before Fire**
            - Install smoke alarms
            - Keep fire extinguisher ready
            - Identify exits in building
            - Avoid overloading electrical sockets
            """)

        elif phase == "During":
            st.markdown("""
            🔥 **During Fire**
            - Stay LOW to avoid smoke
            - Cover nose with cloth
            - Do NOT use elevators
            - Exit immediately
            """)

        else:
            st.markdown("""
            🔥 **After Fire**
            - Do not re-enter building
            - Check for injuries
            - Call emergency services
            """)

    # ---------------- FLOOD ----------------
    elif disaster == "Flood":

        if phase == "Before":
            st.markdown("""
            🌊 **Before Flood**
            - Store drinking water
            - Charge mobile phones
            - Move valuables to higher level
            - Prepare emergency kit
            """)

        elif phase == "During":
            st.markdown("""
            🌊 **During Flood**
            - Move to higher ground
            - Avoid walking in water
            - Switch off electricity
            - Listen to alerts
            """)

        else:
            st.markdown("""
            🌊 **After Flood**
            - Avoid contaminated water
            - Boil drinking water
            - Clean and disinfect home
            """)

    # ---------------- EARTHQUAKE ----------------
    elif disaster == "Earthquake":

        if phase == "Before":
            st.markdown("""
            🌍 **Before Earthquake**
            - Secure heavy furniture
            - Identify safe spots (under table)
            - Prepare emergency bag
            """)

        elif phase == "During":
            st.markdown("""
            🌍 **During Earthquake**
            - DROP, COVER, HOLD
            - Stay away from windows
            - Do NOT run outside
            """)

        else:
            st.markdown("""
            🌍 **After Earthquake**
            - Check injuries
            - Expect aftershocks
            - Avoid damaged buildings
            """)

    # ---------------- FOOD + WATER ----------------
    st.markdown("## 🍱 Food & Water Survival")

    st.markdown("""
    - Store at least 3 days of food
    - Prefer dry foods (biscuits, rice, nuts)
    - Keep bottled water (3 liters per person/day)
    - Use ORS packets
    - Avoid spoiled or flood-contaminated food
    """)

    # ---------------- EMERGENCY KIT ----------------
    st.markdown("## 🎒 Emergency Kit Checklist")

    st.markdown("""
    - 🔦 Flashlight + batteries  
    - 📱 Mobile + power bank  
    - 💊 First aid kit  
    - 🥫 Dry food packets  
    - 💧 Drinking water  
    - 📄 Important documents  
    - 🔔 Whistle for help  
    """)

    # ---------------- EVACUATION ----------------
    st.markdown("## 🧭 Evacuation Plan")

    st.markdown(f"""
    - Know nearest safe zones  
    - Keep transport ready  
    - Inform family before leaving  
    - Use **Safe Route module** for navigation  
    """)

    # ---------------- PRO TIPS ----------------
    st.markdown("## ⚠️ Survival Tips")

    st.info("""
    - Stay calm and think clearly  
    - Follow official instructions  
    - Avoid rumors  
    - Help others if safe  
    """)

# ---------------- VOICE ----------------
elif selected == "Voice AI":
    st.title("🎤 Voice Assistant")

    if "voice_text" not in st.session_state:
        st.session_state.voice_text = ""

    text = st.text_input("Command", st.session_state.voice_text)

    if st.button("Speak"):
        text = listen()
        st.session_state.voice_text = text
        st.success(text)

    if st.button("Execute"):
        intent = detect_intent(text)

        # 🔥 FIRE
        if intent == "fire":
            res = "Fire detected. Stay low, avoid smoke, and exit immediately."

        # 🌊 FLOOD
        elif intent == "flood":
            res = "Flood risk detected. Move to higher ground immediately."

        # 🌍 EARTHQUAKE
        elif intent == "earthquake":
            res = "Earthquake alert. Drop, cover, and hold tight."

        # 🌤 WEATHER
        elif intent == "weather":
            weather = get_weather(user_lat, user_lon)
            if weather:
                res = f"Current temperature is {weather['temp']} degree Celsius with {weather['weather']}"
            else:
                res = "Unable to fetch weather data"

        # 📍 LOCATION
        elif intent == "location":
            res = f"Your current location is latitude {user_lat} and longitude {user_lon}"

        # 🧭 ROUTE
        elif intent == "route":
            res = "Opening safest route on map"
            st.markdown(f"[Open Route](https://www.google.com/maps/dir/{user_lat},{user_lon})")

        # ⚠️ RISK
        elif intent == "risk":
            res = "Checking risk levels. Please use the risk prediction module for detailed analysis."

        # 🚨 HELP
        elif intent == "help":
            res = "In emergency, stay calm. Follow safety instructions based on disaster type."

        # ⚙️ STATUS
        elif intent == "status":
            res = "All systems are active and monitoring environment in real time."

        # 👋 GREETING
        elif intent == "greeting":
            res = "Hello! I am your disaster assistant. How can I help you?"

        else:
            res = "Sorry, I did not understand the command."

        st.success(res)
        speak(res)