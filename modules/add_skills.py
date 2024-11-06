from db_classes import Skill
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine

def add_skill(session: Session, user_id: int, title: str, description: str):

    existing_skill = session.query(Skill).filter_by(title=title, user_id=user_id).first()
    if existing_skill:
        print("Skill with this title already exists")
        return 

    new_skill = Skill(
        user_id=user_id,
        title=title,
        description=description
    )   

    session.add(new_skill)
    session.commit()
    print(f"Skill {title} succesfully added")


    engine = create_engine("sqlite:///app.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    add_skill(session, user_id=2, title="Test skill", description="this is just a test")

    session.close()