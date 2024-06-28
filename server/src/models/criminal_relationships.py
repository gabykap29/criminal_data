from pydantic import BaseModel


class Criminal_Relationships(BaseModel):
    from_criminal_id: str
    to_criminal_id: str
    relationship_type: str
    details: str
    