from sqlalchemy.orm import Session
from db_classes import Participant
from sqlalchemy import select


def lecture_rating(session: Session, participant_id: int, like: bool):
    stmt = select(Participant).where(Participant.id == participant_id)
    participant = session.execute(stmt).scalar_one_or_none()

    if participant:
        participant.lecture_rating = like
        session.commit()
        return True 
    return False






