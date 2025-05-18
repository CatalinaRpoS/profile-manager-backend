from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine, Base, get_db
from app.models.person_model import Person
from app.models.skill_model import Skill

from app.routes import person_route, skill_route

def init_db():
    Base.metadata.create_all(bind=engine)

    db = next(get_db())
    if not db.query(Person).first():
        default_person = Person(
            name="Catalina Restrepo Salgado",
            age=20,
            email="corporativeemail@mail.com",
            phone="3001234567",
            position="Software Engineer",
            profile_picture="https://xsgames.co/randomusers/avatar.php?g=female"
        )

        db.add(default_person)
        db.commit()
        db.refresh(default_person)

        default_person.skills = [
            Skill(name="Python", level=10),
            Skill(name="JavaScript", level=8),
            Skill(name="SQL", level=8),
            Skill(name="HTML", level=10),
            Skill(name="CSS", level=8),
            Skill(name="Java", level=7),
            Skill(name="Docker", level=5),
            Skill(name="Git", level=9),
            Skill(name="FastAPI", level=8),
            Skill(name="React", level=8),
        ]

        # Asignar la relación directamente y dejar que SQLAlchemy maneje person_id
        for skill in default_person.skills:
            skill.owner = default_person

        db.add_all(default_person.skills)
        db.commit()
        db.close()
        print("Default person created in the database.")
    else:
        print("Default person already exists in the database.")

init_db()

app = FastAPI(title="Profile Manager API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(person_route.router)
app.include_router(skill_route.router)

@app.get("/")
async def root():
    return {"message": "Welcome to Profile Manager API!"}
