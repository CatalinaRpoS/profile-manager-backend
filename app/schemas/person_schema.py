from pydantic import BaseModel
from typing import List

class PersonBase(BaseModel):
    name: str
    age: int
    email: str
    phone: str
    position: str
    profile_picture: str

    class Config:
        from_attributes = True

class PersonResponse(PersonBase):
    id: int

    class Config:
        from_attributes = True