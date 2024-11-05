from datetime import datetime
from sqlalchemy.orm import sessionmaker
from db_classes import User, engine

session_factory=sessionmaker(bind=engine)


def set_user(first_name: str, last_name: str, email: str, username: str, password: str) -> User:
    print(f"Adding record at {datetime.now()}")
    with session_factory() as session:

        new_user = User(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
        session.add(new_user)
        session.commit()
        
        print(new_user)
        return new_user
    

new_user = set_user(
first_name="Tomas",
last_name="Saulevicius",
email="labas@gmail.com",
username="tomas123",
password="slapt555"
)
print(new_user)

print("User details:")
print(f"First Name: {new_user.first_name}")
print(f"Last Name: {new_user.last_name}")
print(f"Email: {new_user.email}")
print(f"Username: {new_user.username}")
print(f"Password: {new_user.password}")
    