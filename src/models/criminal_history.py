from pydantic import BaseModel, Field
from datetime import date
from typing import Optional
class Criminal_History(BaseModel):
    criminal_id: str
    crime_type_id: str
    date: date
    location: str
    coordenates_id: Optional[str] = Field(None) # Hace referencia a la colección cordenates
    description: str

