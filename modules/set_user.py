from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker
from db_classes import User, engine
from modules import db_classes as db

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

#Registracija i paskaita

# user2 = db.get_user("username")
# user2.id





Session = sessionmaker(bind=db.engine)
session = Session()


def log_in_logout(user_id, start_at, end_at):
    all_lectures = session.query(db.Lecture).all()
    print(f"Visos paskaitos: {[lecture.title for lecture in all_lectures]}")

    lectures_in_period = [lecture for lecture in all_lectures if start_at <= lecture.start_at <= end_at]
    print(f"Paskaitos, kurios vyksta per laikotarpį {start_at} - {end_at}: {[lecture.title for lecture in lectures_in_period]}")

    for lecture in lectures_in_period:
        participant = session.query(db.Participant).filter_by(
            user_id=user_id,
            lecture_id=lecture.id
        ).first()

    if participant:
            participant.is_complete = True
            session.commit()
            print(f"Paskaita '{lecture.title}' pažymėta kaip uzbaigta vartotojui {user_id}.")
    else:
            print(f"Vartotojas {user_id} nėra uzsiregistraves '{lecture.title}'.")

    user = session.query(db.User).filter_by(id=user_id).first()
    if user:
        new_login = db.Authorization(user_id=user_id, login=datetime.now())
        session.add(new_login)
        session.commit()
        print(f"Vartotojas {user.first_name} {user.last_name} prisijunge.")
    else:
        print(f"Vartotojas su ID {user_id} nerastas.")

       


def log_out(user_id):
   
    user = session.query(db.User).filter_by(id=user_id).first()
    if user:
        new_logout = db.Authorization(user_id=user_id, logout=datetime.now())
        session.add(new_logout)
        session.commit()
        print(f"Vartotojas {user.first_name} {user.last_name} atsijungė.")
    else:
        print(f"Vartotojas su ID {user_id} nerastas.")


        if __name__ == '__main__':
            user_id = 1  
            start_at = datetime(2024, 11, 1, 9, 0, 0)  
            end_at = datetime(2024, 11, 30, 17, 0, 0)  
        
            log_in_logout(user_id, start_at, end_at)
            log_out(user_id)



#baigti darba

# def finish_work(user_id):
#      ongoing_participation = session.query(db.Participant).join(db.Lecture).filter(
#         db.Participant.user_id == user_id,
#         db.Lecture.start_at <= datetime.now(),
#         db.Lecture.end_at >= datetime.now(),
#         db.Participant.is_complete == False  
#     ).all()
     
#     if ongoing_participation:
#         lecture_titles = [participation.lecture.title for participation in ongoing_participation]
#         print(f"Jūs vis dar dalyvaujate šiose paskaitose: {', '.join(lecture_titles)}.")
#         confirm = input("Ar tikrai norite atsijungti? (y/n): ")
        
#         if confirm.lower() != 'y':
#             print("Atsijungimas atšauktas.")
#             return
#         else:
#             print("vykdo atsijungima") 

# new_logout = db.Authorization(user_id=user_id, logout=datetime.now())
# session.add(new_logout)
# session.commit()
# print("Vartotojas sėkmingai atsijunge.")

# if __name__ == '__main__':
#     user_id = 1  
#     finish_work(user_id)
     

 






































    