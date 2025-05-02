import streamlit as st
import requests

st.title("Predicción de Diabetes")

# Entradas del usuario
pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=1)
glucose = st.number_input("Glucose", min_value=0.0, max_value=300.0, value=120.0)
blood_pressure = st.number_input("Blood Pressure", min_value=0.0, max_value=200.0, value=70.0)
skin_thickness = st.number_input("Skin Thickness", min_value=0.0, max_value=100.0, value=20.0)
insulin = st.number_input("Insulin", min_value=0.0, max_value=900.0, value=79.0)
bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=20.0)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.5, value=0.5)
age = st.number_input("Age", min_value=0, max_value=100, value=33)

if st.button("Predecir"):
    # Preparar los datos en formato JSON
    input_data = {
        "pregnancies": pregnancies,
        "glucose": glucose,
        "blood_pressure": blood_pressure,
        "skin_thickness": skin_thickness,
        "insulin": insulin,
        "bmi": bmi,
        "diabetes_pedigree": dpf,
        "age": age
    }
    # Llamada POST al API
    response = requests.post("http://api:8000/predict", json=input_data)
    if response.status_code == 200:
        pred = response.json().get("prediction")
        resultado = "con diabetes" if pred == 1 else "sin diabetes"
        st.write(f"Predicción: {resultado} (clase {pred})")
    else:
        st.error("Error al obtener la predicción de la API.")
