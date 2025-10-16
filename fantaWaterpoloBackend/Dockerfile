
# 1. Immagine Base: Scegliamo una versione leggera di Python
FROM python:3.11-slim

# 2. Imposta l'ambiente di lavoro all'interno del container
WORKDIR /app

# 3. Copia i requirements.txt e installa le dipendenze
# Copiamo il requirements.txt dal livello superiore (Fanta-Waterpolo/)
# e lo incolliamo in /app nel container.
COPY ../requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copia tutto il codice sorgente del backend nel container
# Copia il contenuto della cartella fantaWaterpoloBackend nel workdir /app
COPY . /app/fantaWaterpoloBackend

# 5. Espone la porta standard di FastAPI
EXPOSE 8000

# 6. Comando di avvio: avvia l'app con Uvicorn
# Usa 0.0.0.0 come host per ascoltare tutte le connessioni in Docker.
# Il nome del modulo è quello che ci ha dato problemi prima: <pacchetto>.<file>:<istanza>
CMD ["/bin/bash", "-c", "export PYTHONPATH=$PYTHONPATH:/app && uvicorn fantaWaterpoloBackend.main:app --host 0.0.0.0 --port 8000"]