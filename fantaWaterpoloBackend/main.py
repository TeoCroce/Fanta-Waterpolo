from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session # Preferiamo sqlalchemy.orm per Session
from fantaWaterpoloBackend import models, schemas, crud # Uso importazioni relative per coerenza con la struttura
from fantaWaterpoloBackend.database import engine, get_db

# --- Configurazione Iniziale e Creazione Tabelle ---
# Questa riga crea tutte le tabelle definite in models.py
# (Assumendo che models.Base sia stato definito e importato correttamente)
models.Base.metadata.create_all(bind=engine) 

# Inizializza l'applicazione FastAPI
app = FastAPI(
    title="Fanta-Waterpolo API",
    version="1.0.0",
    description="API per la gestione della lega di Fanta-Pallanuoto"
)

# --- Endpoint di Test (Root) ---
@app.get("/")
def read_root():
    return {"message": "Welcome to the Fanta-Waterpolo API!"}

# --- Endpoint POST: User Creation ---
@app.post(
        "/users/",
          response_model=schemas.User,
          status_code=status.HTTP_201_CREATED,
          tags=["Users"])

def create_new_user(user: schemas.CreateUser, db: Session = Depends(get_db)):
    """
    Registration of a new User. Checks if the username already exists.
    """
    # 1. First check if the User already exists
    # Assumendo che il modello si chiami models.User
    db_user_check = crud.get_user_by_username(db, username = user.username)
    if db_user_check:
        raise HTTPException(
            status_code=400,
            detail="Username already used"
        )
    
    # 2. Creation of the User
    db_user = crud.create_user(db = db, user = user)
    
    return db_user
