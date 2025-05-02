FROM python:3.9-slim

WORKDIR /app

# Instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar modelo entrenado y código fuente
COPY model.pkl model.pkl
COPY app.py app.py

# Exponer puerto y comando de inicio
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
