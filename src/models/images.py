from pydantic import BaseModel, Field
from typing import Optional

class Images(BaseModel):
    url:str
    description: Optional[str] = Field(None)