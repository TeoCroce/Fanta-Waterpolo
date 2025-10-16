from pydantic import BaseModel, ConfigDict
from typing import List, Optional


# Real Player Schema
class PlayerBase(BaseModel):
    name: str
    surname: str
    role: str
    base_score: int = 0

class CreatePlayer(PlayerBase):
    pass

class Player(CreatePlayer):
    id: int
    
    model_config = ConfigDict(from_attributes = True)



# ------------------------------
# Schemas for Users
# ------------------------------
class UserBase(BaseModel):
    username: str
    role: Optional[str] = "partecipant"

class CreateUser(UserBase):
    password: str   # will be saved in an encrypted way

# schema for the visualization of a User
class User(CreateUser):
    id: int
    username: str
    role: str
    total_score: int

    # Roster = list of players selected by the user as part of the "team"
    roster: List[Player] = []

    model_config = ConfigDict(from_attributes=True)
        