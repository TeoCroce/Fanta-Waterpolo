from sqlalchemy.orm import Session
from fantaWaterpoloBackend import models, schemas

# Function to find User by username
def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

# Funzione per creare un utente nel database (Password in Chiaro)
def create_user(db: Session, user: schemas.CreateUser):
    
    # 1. Crea l'oggetto ORM usando la password in chiaro.
    # Assumiamo che models.User.password esista (come modificato nel punto 1.A)
    db_user = models.User(
        username=user.username,
        role=user.role,
        password=user.password, # <--- Qui salviamo la password in chiaro
        total_score=0 # Valore di default
    )
    
    # 2. Salva nel database
    db.add(db_user)
    db.commit()
    db.refresh(db_user) # Aggiorna l'oggetto per ottenere l'ID

    return db_user

