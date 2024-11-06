from sqlalchemy.orm import Session
from db_classes import Lecture


def create_lecture(session: Session, user, skill, title: str, description:str):
    if not user or not skill:
        print("User and skill has to be given")
        return False
    
    new_lecture = Lecture(
        user_id=user.id,
        skill_id=skill.id,
        title=title,
        description=description
    )

    session.add(new_lecture)
    session.commit()

    print(f"Lecture {title} succesfully added")
    return True