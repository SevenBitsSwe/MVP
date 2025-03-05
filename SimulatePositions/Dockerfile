FROM python:3.8

# Imposta la directory di lavoro
WORKDIR /app

# Installa solo librerie minime necessarie
RUN apt-get update && apt-get install -y \
  gdal-bin \
  libgdal-dev \
  && apt-get clean && rm -rf /var/lib/apt/lists/*

# Imposta le variabili di ambiente per GDAL
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal
ENV GDAL_VERSION=3.10.0

# Aggiorna pip e installa le dipendenze
RUN pip install --upgrade pip

# Copia i file necessari nella directory di lavoro
COPY requirements.txt .
COPY simulatePosition.py .
COPY dbflink.py .

# Installa le dipendenze Python
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "simulatePosition.py"]