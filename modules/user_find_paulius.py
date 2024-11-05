from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///example.db') 
Session = sessionmaker(bind=engine)
session = Session()

from db_classes import User

def Find_user(email):
        stmt = select(User).where(User.email == email)
        return session.execute(stmt).scalars().first()  
       

users = Find_user("a@a.com")
for user in users:
    print(f"Naudotojas: {user.first_name} {user.last_name}")
