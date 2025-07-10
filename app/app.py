import streamlit as st
import pandas as pd
import joblib
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.predict import predict_leads

st.title("🔮 Predictive Lead Conversion")
st.write("Upload lead metadata to predict conversion probability.")

uploaded_file = st.file_uploader("Upload CSV", type="csv")
if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.subheader("Uploaded Data")
    st.dataframe(data.head())

    if st.button("Predict Conversion"):
        predictions = predict_leads(data)
        data['Conversion Probability (%)'] = (predictions * 100).round(2)
        st.subheader("Prediction Results")
        st.dataframe(data)
