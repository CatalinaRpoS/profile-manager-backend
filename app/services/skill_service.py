from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.skill_model import Skill

def create_skill(db: Session, name: str, level: int, person_id: int):
    existing_skill = db.query(Skill).filter(Skill.name == name, Skill.person_id == person_id).first()
    if existing_skill:
        raise HTTPException(status_code=400, detail="Skill already exists for this person")

    new_skill = Skill(
        name=name,
        level=level,
        person_id=person_id
    )

    db.add(new_skill)
    db.commit()
    db.refresh(new_skill)
    return new_skill

def get_person_skills(db: Session, person_id: int):
    skills = db.query(Skill).filter(Skill.person_id == person_id).all()
    if not skills:
        raise HTTPException(status_code=404, detail="No skills found for this person")
    return skills
