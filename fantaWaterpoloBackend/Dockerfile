# Usa un'immagine Python ufficiale
FROM python:3.11-slim

# Imposta la directory di lavoro nel container
WORKDIR /app

# Aggiunge la cartella /app al percorso di ricerca dei moduli Python.
ENV PYTHONPATH=/app

# Copia il file dei requisiti e installa le dipendenze
# È cruciale che questo passaggio venga eseguito per installare FastAPI e SQLAlchemy
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia il resto del codice sorgente
# La cartella 'fantaWaterpoloBackend' è copiata qui
COPY . .

# Comando per avviare l'applicazione Uvicorn (FastAPI)
# Questo comando viene specificato in docker-compose.yml, ma è utile qui come default.
CMD ["uvicorn", "fantaWaterpoloBackend.main:app", "--host", "0.0.0.0", "--port", "8000"]
