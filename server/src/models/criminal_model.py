from datetime import date
from pydantic import BaseModel, Field
from typing import List, Optional

class Criminal(BaseModel):
    lastname: str
    names: str
    alias: Optional[str] = Field(None) #Alias opcional
    dni: Optional[str] = Field(None) #DNI opcional
    birthdate:Optional[date]= Field(None) #YYYY-MM-DD
    address: Optional[dict] = Field(None) # tipo diccionario, clave valor, similar a un objeto en js
    images: Optional[List[str]] = Field(None) #Lista de imagenes
    criminal_history: List[str]
    related_criminal: Optional[List[str]] = Field(None) #Lista de criminales relacionados
    state: bool = Field(True) #Eliminado o no, por defecto NO.