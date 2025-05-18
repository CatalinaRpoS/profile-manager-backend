from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.person_model import Person

def create_person(db: Session, name: str, age: int, email: str, phone: str, position: str, profile_picture: str):
    existing_person = db.query(Person).filter(Person.email == email).first()
    if existing_person:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_person = Person(
        name=name,
        age=age,
        email=email,
        phone=phone,
        position=position,
        profile_picture=profile_picture
    )

    db.add(new_person)
    db.commit()
    db.refresh(new_person)
    return new_person

def get_person(db: Session, person_id: int):
    person = db.query(Person).filter(Person.id == person_id).first()
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")
    return person

def get_all_persons(db: Session):
    persons = db.query(Person).all()
    return persons