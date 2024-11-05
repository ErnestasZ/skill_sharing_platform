import datetime as dt

# ------------------- JS --------------------
from datetime import date
from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, DATE, ForeignKey, not_, and_, or_, Boolean
from sqlalchemy.orm import DeclarativeBase, declarative_base, relationship, sessionmaker, attributes  # , session
from typing_extensions import Annotated

# class Base(DeclarativeBase):
#     pass
# or
engine = create_engine('sqlite:///app.db')
Base = declarative_base()


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
    part_lectures = relationship("Lectures", secondary='participants', back_populates="part_users")

    # def __init__(self, first_name: str, last_name: str, email: str, username: str, password: str) -> None:
    #     self.first_name = first_name
    #     self.last_name = last_name
    #     self.email = email
    #     self.username = username
    #     self.password = password

    def __repr__(self):
        return f"User_{self.id}: {self.first_name} {self.last_name}, email: {self.email}"


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


# ---------------- end of JS ----------------
# -----------------RB --------------------------------
# Base = declarative_base()


class Participant(Base):
    __tablename__ = "participants"
    id = Column(Integer, primary_key=True)
    lecture_id = Column(Integer, ForeignKey("lectures.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    is_complete = Column(Boolean, default=False)
    lecture_rating = Column(Boolean, default=False)
    subscribed_at = Column(DateTime, default=datetime.now())

    user = relationship("User", back_populates="participants")
    lecture = relationship("Lecture", back_populates="participans")

    def __repr__(self):
        return (f"<Participant(id={self.id}, lecture_id={self.lecture_id}, user_id={self.user_id}, "
                f"is_complete={self.is_complete}, lecture_rating={
                    self.lecture_rating}, "
                f"subscribed_at={self.subscribed_at})>")


# kita klase
# ---------------- PK ----------------
class Skill(Base):
    __tablename__ = "skills"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String(255))
    description = Column(String(255))
    user = relationship("User", back_populates="skills")
    lectures = relationship("Skill", back_populates="skill")

    def __repr__(self):
        return f"Skill_{self.id},{self.user_id} {self.title}, aprašymas: {self.description}"

    # ---------------- end of PK ----------------


class Lectures (Base):
    __tablename__ = "lectures"
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    description = Column(String)
    start_at = Column(DateTime)
    end_at = Column(DateTime)
    user_id = Column(Integer, ForeignKey("users.id"))
    skill_id = Column(Integer, ForeignKey("skills.id"))

    user = relationship("User", back_populates="lectures")
    skill = relationship("Skill", back_populates="lectures")
    participants = relationship("Participant", back_populates="lecture")
    part_users = relationship("Lectures", secondary='participants', back_populates="part_lectures")



    def __repr__(self):
        return (f"Lecture(id={self.id}, title={self.title}, start_at={self.start_at}, end_at={self.end_at}, user_id={self.user_id}, skill_id={self.skill_id} ")


# n-toji klase


# ------------------- JS --------------------
# engine = create_engine('sqlite:///app.db')
# Base.metadata.create_all(engine)

# session_factory = sessionmaker(bind=engine)

# print(f"Add records at {datetime.now()}")
# with session_factory() as session:
#     new_user = User(first_name="Jonas", last_name="Jonaitis", email="john@mail.com", username="johnjon",
#                     password="031edd7d41651593c5fe5c006fa5752b37fddff7bc4e843aa6af0c950f4b9406")
#     auth1 = Authorization(login=datetime.now(), user=new_user)
#     auth2 = Authorization(login=datetime.now(), user=new_user)

#     session.add(new_user)
#     session.add(auth1)
#     session.add(auth2)
#     session.commit()

#     print(new_user)
#     print(auth2)

# print(f"Delete records at {datetime.now()}")
# with session_factory() as session:

#     session.delete(auth1)
#     session.delete(new_user)
#     session.commit()
# ---------------- end of JS ----------------

# skirmante lectures


Base.metadata.create_all(engine)
