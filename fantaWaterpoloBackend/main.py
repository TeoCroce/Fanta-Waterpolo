from fastapi import FastAPI
from fantaWaterpoloBackend import models                       # Importa i modelli (GiocatoreReale)
from fantaWaterpoloBackend.database import engine,get_db         # Importa l'engine per la connessione

# CREAZIONE DELLE TABELLE: Crea le tabelle nel DB se non esistono
models.Base.metadata.create_all(bind=engine)

# Inizializza l'applicazione FastAPI
app = FastAPI(
    title="Fantanuoto API",
    version="1.0.0",
)

# Endpoint di Test (Root)
@app.get("/")
async def root():
    return {"message": "API Fantanuoto connessa al database!"}