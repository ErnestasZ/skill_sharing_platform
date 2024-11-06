import datetime as dt

from datetime import date
from datetime import datetime

from sqlalchemy import create_engine, Column, Boolean, Integer, Float, String, DateTime, DATE, ForeignKey, select, not_, and_, or_
from sqlalchemy.orm import DeclarativeBase, Session, declarative_base, relationship, sessionmaker, attributes  # , session
from typing_extensions import Annotated

engine = create_engine('sqlite:///app.db')
session_factory = sessionmaker(bind=engine)

# class Base(DeclarativeBase):
#     pass
# or
Base = declarative_base()

class Authorization(Base):
    __tablename__ = "auths"
    id = Column("id", Integer, primary_key=True)
    login = Column(DateTime)
    logout = Column(DateTime)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="auths")

    # def __init__(self, login: datetime = None, logout: datetime = None) -> None:
    #     self.login = login
    #     self.logout = logout

    def __repr__(self):
        return f"{self.user}, login: {self.login}, logout: {self.logout}"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(25))
    last_name = Column(String(25))
    email = Column(String(50), unique=True)
    username = Column(String(10), unique=True)
    password = Column(String(64))  # sha-256
    auths = relationship(
        "Authorization", back_populates="user", cascade="all, delete")
    skills = relationship("Skill", back_populates="user")
    lectures = relationship("Lecture", back_populates="user")
    participants = relationship("Participant", back_populates="user")
    # part_lectures = relationship(
    #     "Lecture", secondary='participants', back_populates="part_users")

    # def __init__(self, first_name: str, last_name: str, email: str, username: str, password: str) -> None:
    #     self.first_name = first_name
    #     self.last_name = last_name
    #     self.email = email
    #     self.username = username
    #     self.password = password

    def add_auth(self, session = session_factory()):
        now = datetime.now()
        auth = Authorization(login=now, logout=now, user_id=self.id)
        session.add(auth)
        session.commit()

    def get_auths(self) -> list:
        stmt = select(Authorization).where(Authorization.user_id == self.id)
        return session_factory().execute(stmt).scalars().all()

    def last_auth(self) -> (Authorization | None):
        auths = sorted(self.get_auths(), key=lambda Authorization:Authorization.login, reverse=True)
        return auths[0] if auths else None

    def __repr__(self):
        return f"User_{self.id}: {self.first_name} {self.last_name}, email: {self.email}"

class Participant(Base):
    __tablename__ = "participants"
    id = Column(Integer, primary_key=True)
    lecture_id = Column(Integer, ForeignKey("lectures.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    is_complete = Column(Boolean, default=False)
    lecture_rating = Column(Boolean, default=False)
    subscribed_at = Column(DateTime, default=datetime.now())

    user = relationship("User", back_populates="participants")
    lecture = relationship("Lecture", back_populates="participants")

    def __repr__(self):
        return (f"<Participant(id={self.id}, lecture_id={self.lecture_id}, user_id={self.user_id}, "
                f"is_complete={self.is_complete}, lecture_rating={
                    self.lecture_rating}, "
                f"subscribed_at={self.subscribed_at})>")

class Skill(Base):
    __tablename__ = "skills"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String(255))
    description = Column(String(255))
    user = relationship("User", back_populates="skills")
    lectures = relationship("Lecture", back_populates="skill")

    def __repr__(self):
        return f"Skill_{self.id},{self.user_id} {self.title}, aprašymas: {self.description}"

class Lecture(Base):
    __tablename__ = "lectures"
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    description = Column(String)
    start_at = Column(DateTime)
    end_at = Column(DateTime)
    user_id = Column(Integer, ForeignKey("users.id"))
    skill_id = Column(Integer, ForeignKey("skills.id"))
    participants_qty = Column(Integer)
    user = relationship("User", back_populates="lectures")
    skill = relationship("Skill", back_populates="lectures")
    participants = relationship("Participant", back_populates="lecture")
    # part_users = relationship(
    #     "User", secondary='participants', back_populates="part_lectures")

    def __repr__(self):
        return (f"Lecture(id={self.id}, title={self.title}, start_at={self.start_at}, end_at={self.end_at}, user_id={self.user_id}, skill_id={self.skill_id} ")

Base.metadata.create_all(engine)

def add_user(session = session_factory(), **kwargs) -> (User | Exception):
    new_user = User(**kwargs)
    try:
        session.add(new_user)
    except Exception as err:
        session.rollback()
        return err
    else:
        session.commit()
        new_user.add_auth(session)
        return new_user
    
def get_user(login: str, session=session_factory()) -> (User | None):
    stmt = select(User).where(or_(User.username == login, User.email == login))
    return session.execute(stmt).scalars().first()
