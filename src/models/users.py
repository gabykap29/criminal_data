from datetime import date
from pydantic import BaseModel

class Users(BaseModel):
    lastname: str
    names: str
    username: str
    password: str
    old_password: str
    role: str
    createdAt: date
    state: bool