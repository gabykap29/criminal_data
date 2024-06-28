from datetime import date
from pydantic import BaseModel,Field
from typing import Optional

class Cordenates_Point(BaseModel):
    criminal_id: str
    crimen_type_id: str
    location: dict  #coordenadas.
    head_value: int
    timestamp: date # fecha 
    createdAt: date
    user: str
    