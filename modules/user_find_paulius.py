from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import or_
 

engine = create_engine('sqlite:///app.db') 
Session = sessionmaker(bind=engine)
session = Session()

from db_classes import User

def Find_user(email):
        stmt = select(User).where( or_(User.email == email, User.username == email)
)
        return session.execute(stmt).scalars().first()  
       

user = Find_user("amy97")
print(f"Naudotojas: {user.first_name}")


