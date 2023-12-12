# Usa la imagen oficial de Python como base
FROM python:3.11.4

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de requerimientos al contenedor
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el contenido del directorio actual al contenedor en /app
COPY main.py api_funct.py ./app/

# Expone el puerto en el que la aplicación se ejecutará
EXPOSE 10000

# Comando para ejecutar la aplicación cuando el contenedor se inicia
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
