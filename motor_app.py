import streamlit as st
import joblib
import numpy as np

# Load your trained model
model = joblib.load("motor_maintenance_model.joblib")

st.title("⚙️ Motor Maintenance Prediction")

st.write("Enter motor parameters to predict if maintenance is needed.")

# Input fields
temp = st.number_input("Temperature (°C)", value=70.0)
vib = st.number_input("Vibration (m/s²)", value=0.5)
current = st.number_input("Current (A)", value=9.5)
rpm = st.number_input("RPM", value=1440.0)

if st.button("Predict"):
    # Prepare the data for the model
    data = np.array([[temp, vib, current, rpm]])
    prediction = model.predict(data)[0]
    result = "✅ No maintenance needed" if prediction == 0 else "⚠️ Maintenance is needed"
    st.success(f"Prediction: {result}")
