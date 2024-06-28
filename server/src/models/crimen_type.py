from pydantic import BaseModel

class Criminal_Type(BaseModel):
    name: str
    description: str
    severity: str