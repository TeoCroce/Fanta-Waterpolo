from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship
from fantaWaterpoloBackend.database import Base

# Table for the association of the relashionship one to many (One User have 3 fanta-players)


# User class
class User(Base):
    """Users that partecipate to Fanta-Waterpolo"""
    __tablename__ = "users"

    # Definition of all the fields of the table / characteristics of a partecipant to the game
    id = Column(Integer, primary_key = True, index = True)
    username = Column(String, unique = True, index = True)
    password = Column(String)
    role = Column(String, default = "partecipant")
    total_score = Column(Integer, default = 0)

    # Definition of the one to many relationship
    # One user gets multiple real players
    # Back_populates = "owner" connets the user to the real player
    roster = relationship("RealPlayer", back_populates = "owner")


# Modello del Giocatore di Pallanuoto Reale
class RealPlayer(Base):
    """Real Players of the real championship with their marks"""
    __tablename__ = "real_players"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    surname = Column(String, index=True)
    role = Column(String)  # Es: 'Portiere', 'Difensore', 'Attaccante'
    value = Column(Float, default=5.0)
    free_agent = Column(Boolean, default=True)
    
    # Statistiche
    scored_goals = Column(Integer, default=0)
    assits = Column(Integer, default=0)
    esclusions = Column(Integer, default=0)
    red_cards = Column(Integer, default = 0)
    mvp = Column(Integer, default = 0)

    # Mark after every game
    score = Column(String, default = 0)

    # ------------------------------------------------------------------------
    # External key for the one to many relationship: owner_id
    # ------------------------------------------------------------------------
    # we point at the table 'users'. nullable = True cus the player may be not selected
    owner_id = Column(Integer, ForeignKey('users.id'), nullable = True, index = True)

    # many to one relationship: Real Player gets only one User as owner
    owner = relationship("User", back_populates = ("roster"))

