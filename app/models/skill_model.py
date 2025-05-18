from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Skill(Base):
    __tablename__ = "skill"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    level = Column(Integer)
    person_id = Column(Integer, ForeignKey("person.id"))

    owner = relationship("Person", back_populates="skills")