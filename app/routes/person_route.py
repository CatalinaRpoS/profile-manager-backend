from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.person_model import Person
from app.schemas.person_schema import PersonBase, PersonResponse
from app.services.person_service import (
    create_person, get_person, get_all_persons
)

from typing import List

router = APIRouter(prefix="/api/person", tags=["Person"])

@router.post("/", response_model=PersonResponse)
def create_person_route(person: PersonBase, db: Session = Depends(get_db)):
    return create_person(
        db=db,
        name=person.name,
        age=person.age,
        email=person.email,
        phone=person.phone,
        position=person.position,
        profile_picture=person.profile_picture
    )

@router.get("/{person_id}", response_model=PersonResponse)
def get_person_route(person_id: int, db: Session = Depends(get_db)):
    return get_person(db=db, person_id=person_id)

@router.get("/", response_model=List[PersonResponse])
def get_all_persons_route(db: Session = Depends(get_db)):
    return get_all_persons(db=db)
