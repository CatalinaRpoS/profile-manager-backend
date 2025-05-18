from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String, unique=True, index=True)
    phone = Column(String)
    position = Column(String)
    profile_picture = Column(String)

    skills = relationship("Skill", back_populates="owner")
