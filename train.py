import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib


def train_model():
    # Cargar datos
    data = pd.read_csv('data/diabetes.csv')
    X = data.drop('Outcome', axis=1)
    y = data['Outcome']

    # División de datos entrenamiento
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Entrenar modelo de regresión logística
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # Evaluar precisión del modelo
    score = model.score(X_test, y_test)
    print(f'Precisión del modelo: {score:.2f}')

    # Crear carpeta de modelo si no existe
    os.makedirs('model', exist_ok=True)
    # Guardar modelo entrenado
    joblib.dump(model, 'api/model.pkl')
    print('Modelo guardado en api/model.pkl')


if __name__ == '__main__':
    train_model()
