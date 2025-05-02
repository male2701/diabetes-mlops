# Proyecto MLOps para Predicción de Diabetes

Estudiantes: Fabián Montero - Malena Velásquez

Este proyecto implementa un pipeline completo de MLOps para la predicción de diabetes...

## Ejecutando el proyecto

1. Clonar el repositorio:
git clone <URL-DEL-REPOSITORIO> cd diabetes-mlops

2. Entrenar el modelo:
python train.py

3. Levantar contenedores:
docker-compose up -d --build

4. Acceder a:
 ```
- API en `http://hostname:8000`

% docker run -p 8000:8000 api-diabetes:develop
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)

- Interfaz web en `http://hostname:8083`

% docker run -p 8083:8083 web-diabetes:develop
Collecting usage statistics. To deactivate, set browser.gatherUsageStats to false.
You can now view your Streamlit app in your browser.
URL: http://0.0.0.0:8083
```


