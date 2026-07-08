import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("cargo_delay_model.pkl")

st.set_page_config(page_title="Cargo Delivery Delay Prediction", layout="centered")

st.title("🚚 Cargo Delivery Delay Prediction System")

st.write("Enter Shipment Details")

# --------------------------
# Dropdown Inputs
# --------------------------

route = st.selectbox(
    "Route",
    [
        "Chennai-Bangalore",
        "Chennai-Madurai",
        "Chennai-Coimbatore",
        "Chennai-Trichy",
        "Chennai-Salem"
    ]
)

weather = st.selectbox(
    "Weather Condition",
    [
        "Sunny",
        "Rain",
        "Fog",
        "Cloudy",
        "Storm"
    ]
)

vehicle = st.selectbox(
    "Vehicle Type",
    [
        "Truck",
        "Van",
        "Mini Truck",
        "Bike"
    ]
)

region = st.selectbox(
    "Region",
    [
        "North",
        "South",
        "East",
        "West",
        "Central"
    ]
)

delivery_partner = st.selectbox(
    "Delivery Partner",
    [
        "Delhivery",
        "BlueDart",
        "DHL",
        "FedEx",
        "DTDC"
    ]
)

delivery_mode = st.selectbox(
    "Delivery Mode",
    [
        "Standard",
        "Express",
        "Same Day"
    ]
)

package_type = st.selectbox(
    "Package Type",
    [
        "Electronics",
        "Food",
        "Clothes",
        "Furniture",
        "Documents"
    ]
)

distance = st.number_input(
    "Distance (km)",
    min_value=1.0,
    value=100.0
)

weight = st.number_input(
    "Package Weight (kg)",
    min_value=0.1,
    value=5.0
)

rating = st.slider(
    "Delivery Rating",
    1,
    5,
    4
)

cost = st.number_input(
    "Delivery Cost",
    min_value=100.0,
    value=1000.0
)

# --------------------------
# Encoding
# --------------------------

route_map = {
    "Chennai-Bangalore":0,
    "Chennai-Madurai":1,
    "Chennai-Coimbatore":2,
    "Chennai-Trichy":3,
    "Chennai-Salem":4
}

weather_map = {
    "Sunny":0,
    "Rain":1,
    "Fog":2,
    "Cloudy":3,
    "Storm":4
}

vehicle_map = {
    "Truck":0,
    "Van":1,
    "Mini Truck":2,
    "Bike":3
}

region_map = {
    "North":0,
    "South":1,
    "East":2,
    "West":3,
    "Central":4
}

partner_map = {
    "Delhivery":0,
    "BlueDart":1,
    "DHL":2,
    "FedEx":3,
    "DTDC":4
}

mode_map = {
    "Standard":0,
    "Express":1,
    "Same Day":2
}

package_map = {
    "Electronics":0,
    "Food":1,
    "Clothes":2,
    "Furniture":3,
    "Documents":4
}

# --------------------------
# Prediction
# --------------------------

if st.button("Predict Delay"):

    input_data = pd.DataFrame([{
        "delivery_partner": partner_map[delivery_partner],
        "package_type": package_map[package_type],
        "vehicle_type": vehicle_map[vehicle],
        "delivery_mode": mode_map[delivery_mode],
        "region": region_map[region],
        "weather_condition": weather_map[weather],
        "distance_km": distance,
        "package_weight_kg": weight,
        "delivery_rating": rating,
        "delivery_cost": cost,
        "route": route_map[route]
    }])

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0][1] * 100

    st.markdown("---")

    st.subheader("Prediction Result")

    st.write(f"### Delay Probability : {probability:.2f}%")

    if prediction == 1:
        st.error("🚨 Shipment Will Be Delayed")
    else:
        st.success("✅ Shipment Will Arrive On Time")

    if probability >= 5:
        st.error("🔴 HIGH RISK")
    elif probability >= 3:
        st.warning("🟡 MEDIUM RISK")
    else:
        st.success("🟢 LOW RISK")

# ===================================================
# SIDEBAR
# ===================================================

st.sidebar.title("🚚 Cargo Delivery Delay Prediction")

# ------------------------------
# Project Information
# ------------------------------

st.sidebar.header("📌 Project Information")

st.sidebar.write("**Project Name**")
st.sidebar.write("Cargo Delivery Delay Prediction System")

st.sidebar.write("**Objective**")
st.sidebar.write(
    "Predict whether a shipment will be delayed using Machine Learning."
)

st.sidebar.write("**Technologies Used**")
st.sidebar.write("""
- Python
- Streamlit
- Machine Learning
- Pandas
- Joblib
""")

st.sidebar.write("**Output**")
st.sidebar.write("""
✅ Delay Prediction

📊 Delay Probability

🚨 Risk Level
""")

st.sidebar.markdown("---")

# ------------------------------
# Developer Information
# ------------------------------

st.sidebar.header("👩‍💻 Developer")

st.sidebar.write("**Name**")
st.sidebar.write("Kalaiyarasi T")

st.sidebar.write("**Department**")
st.sidebar.write("B.Tech Information Technology")

st.sidebar.write("**Role**")
st.sidebar.write("AI & ML Intern")

st.sidebar.write("**Email**")
st.sidebar.markdown("kalaiyarasikalaiyarasi171@gmail.com)")

st.sidebar.write("**LinkedIn**")
st.sidebar.markdown("https://www.linkedin.com/in/kalaiyarasi-t-3aa72b359?utm_source=share_via&utm_content=profile&utm_medium=member_android")

st.sidebar.markdown("---")

st.sidebar.success("Developed by Kalaiyarasi")