# Proyecto MLOps para Predicción de Diabetes

Estudiantes: Fabián Montero - Malena Velásquez

Este proyecto implementa un pipeline completo de MLOps para la predicción de diabetes...

## Ejecutando el proyecto

1. Clonar el repositorio:
git clone <URL-DEL-REPOSITORIO> cd diabetes-mlops

2. Entrenar el modelo:
python train.py

3. Configurar remote de DVC (AWS S3) y subir datos/modelo:
dvc remote add -d awsremote s3://mi-bucket-mlops/diabetes dvc push

4. Levantar contenedores:
docker-compose up -d --build

5. Acceder a:
- API en `http://localhost:8000`
- Interfaz web en `http://localhost:8501`


