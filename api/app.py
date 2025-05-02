from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Esquema de entrada para validación de FastAPI
class DiabetesInput(BaseModel):
    pregnancies: float
    glucose: float
    blood_pressure: float
    skin_thickness: float
    insulin: float
    bmi: float
    diabetes_pedigree: float
    age: float

app = FastAPI(title="Diabetes Prediction API")

# Cargar modelo entrenado
model = joblib.load("model.pkl")

@app.get("/")
def read_root():
    return {"message": "API de Predicción de Diabetes"}

@app.post("/predict")
def predict(data: DiabetesInput):
    # Preparar vector de características
    features = np.array([[data.pregnancies, data.glucose, data.blood_pressure,
                          data.skin_thickness, data.insulin, data.bmi,
                          data.diabetes_pedigree, data.age]])
    # Hacer predicción
    prediction = model.predict(features)[0]
    return {"prediction": int(prediction)}
