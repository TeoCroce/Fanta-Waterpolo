from sqlalchemy import Column, Integer, String, Float, Boolean
from fantaWaterpoloBackend.database import Base

# Modello del Giocatore di Pallanuoto Reale
class GiocatoreReale(Base):
    __tablename__ = "giocatori_reali"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    cognome = Column(String, index=True)
    ruolo = Column(String)  # Es: 'Portiere', 'Difensore', 'Attaccante'
    squadra_reale = Column(String)
    prezzo = Column(Float, default=5.0)
    disponibile = Column(Boolean, default=True)
    
    # Statistiche
    goal_segnati = Column(Integer, default=0)
    assist_fatti = Column(Integer, default=0)
    espulsioni = Column(Integer, default=0)

