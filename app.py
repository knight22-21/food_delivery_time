from tensorflow.keras.models import load_model
from tensorflow.keras.layers import LSTM, Dense
import streamlit as st
import numpy as np

# Load Model
model = load_model("lstm_model.h5")

st.title("Food Delivery Time Prediction 🚀")

a = st.number_input("Age of Delivery Partner", min_value=18, max_value=65, step=1)
b = st.slider("Ratings of Previous Deliveries", min_value=1.0, max_value=5.0, step=0.1)
c = st.number_input("Total Distance (in km)", min_value=1, max_value=50, step=1)

if st.button("Predict Delivery Time"):
    features = np.array([[[a], [b], [c]]])  # Reshape for LSTM
    prediction = model.predict(features)
    st.write(f"Predicted Delivery Time in Minutes = {round(prediction[0][0], 2)}")
