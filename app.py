import streamlit as st
import requests

st.title("Invoice Classifier")

text = st.text_input("Enter Invoice Text")

if st.button("Predict"):

    response = requests.post(
        "http://127.0.0.1:5000/predict",
        json={"text": text}
    )

    data = response.json()

    st.success(f"Category: {data['category']}")

    st.write(f"Confidence: {data['confidence']}%")

    st.write(f"Model Accuracy: {data['model_accuracy']}")