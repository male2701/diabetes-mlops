FROM python:3.9-slim

WORKDIR /app

# Instalar dependencias
COPY web/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copiar código fuente de la interfaz
COPY web/app.py app.py

# Exponer puerto y comando de inicio
EXPOSE 8083

CMD ["streamlit", "run", "app.py", "--server.port=8083", "--server.address=0.0.0.0"]
