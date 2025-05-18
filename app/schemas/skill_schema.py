from pydantic import BaseModel
from typing import List

class SkillBase(BaseModel):
    name: str
    level: int
    person_id: int
    
    class Config:
        from_attributes = True

class SkillResponse(SkillBase):
    id: int

    class Config:
        from_attributes = True
