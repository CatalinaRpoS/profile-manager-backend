from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.skill_model import Skill
from app.schemas.skill_schema import SkillBase, SkillResponse
from app.services.skill_service import (
    create_skill, get_person_skills
)

from typing import List

router = APIRouter(prefix="/api/skill", tags=["Skill"])

@router.post("/", response_model=SkillResponse)
def create_skill_route(skill: SkillBase, db: Session = Depends(get_db)):
    return create_skill(
        db=db,
        name=skill.name,
        level=skill.level,
        person_id=skill.person_id
    )

@router.get("/{person_id}", response_model=List[SkillResponse])
def get_person_skills_route(person_id: int, db: Session = Depends(get_db)):
    return get_person_skills(db=db, person_id=person_id)
