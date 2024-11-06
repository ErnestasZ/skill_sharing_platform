from datetime import datetime
from db_classes import Lecture, engine, User, get_user, Participant
from sqlalchemy import create_engine, select, func
from sqlalchemy.orm import sessionmaker, selectinload

Session = sessionmaker(bind=engine)

user = get_user('shannon61')


def get_valid_lectures():
    with Session() as session:
        return session.execute(select(Lecture)
                               .options
                               (
                                   selectinload(Lecture.user),
                                   selectinload(Lecture.skill)
        )
            .where(Lecture.start_at > datetime.now())
        ).scalars().all()


def get_lecture(lecture_id):
    with Session() as session:
        return session.get(Lecture, lecture_id)


def register_user_to_lecture(user, lecture):
    # check if user not a teacher
    if user.id == lecture.user_id:
        print("Negalite dalyvauti savo paskaitoje. pasirink kita")
        return False
    # check if lecture has available place
    with Session() as session:
        participants_count = session.execute(
            select(func.count(Participant.id))
            .where(Participant.lecture_id == lecture.id)
        ).scalar()

    if participants_count >= lecture.participants_qty:
        print("Paskaita neturi laisvų vietų, pasirink kitą")
        return False

    paticipant = Participant(
        user_id=user.id,
        lecture_id=lecture.id,
        # is_complete=False,
        # lecture_rating=False,
        subscribed_at=datetime.now()
    )
    session.add(paticipant)
    session.commit()
    print("Į paskaitą užsiregistravai sėkmingai.")
    return True


def select_letures(user):
    print("Pasirinkite įgudžių paskaitą kurioje norite dalyvauti ir užsiregistruok: ")
    # all lectures avalable lectures by start_at

    lectures = get_valid_lectures()

    if lectures:
        for lec in lectures:
            user_rating = 45  # get_user_rating(lecture.user)
            print(f"""{lec.id}. {lec.skill.title}: {
                lec.title} - {lec.start_at.strftime('%Y-%m-%d %H:%M')}, dėsto: {lec.user.first_name}, reitingas {user_rating}""")
        while True:
            lecture_id = input("Pasirinkite paskaitos nr.")
            if not lecture_id or not lecture_id.isdigit():
                print('Pasirinktas neteisingas nr., pasirinkite paskaitos nr.')
                continue

            lecture = get_lecture(lecture_id)
            if not lecture:
                print('Paskaita nerasta, pasirinkite paskaitos nr.')
                continue

            is_register = register_user_to_lecture(user, lecture)
            if not is_register:
                continue
            print(f'paskaita: {lecture.title}')
            break


select_letures(user)

# 13

# wellcome_hd_msg = "Sveiki atvyke į įgūdžių dalijimosi platformą"
# register_hd_msg = "Naujo vartotojo registracija"  # Jevgenijus
# login_hd_msg = "Vartotojo prisijungimas"  # Jevgenijus

# action_msg = "Pasirinkite veiksmą:"
# input_msg = "Kokį veiksmą norite atlikti?: "
# exit_msg = "Baigti darbą"


# def palatfom_menu():
#     print("""
#           Mano
#         1. Sukurkite savo įgudį (user) Skirmante Padaryta
#         2. Sukurkite savo paskaitą (user, skill) Skirmante
#         4. Mano paskaitų sarašas (user) Paulius
#         5. Mano įgudžių sarašas (user) Paulius
#         6. Mano reitingas (user) Raminta
#           Paskaitos
#         7. Užsiregistruok į paskaitą kurioje nori dalyvauti (paskaitų sarasas su laikais, destytojo reitingu) (user, lecture) Paulius , Ernestas
#         8. Paskaitos į kurias prisiregistravęs, bet jos dar neprasidėjusios (user) Ramintai
#         9. Paskaitos kuriose dalyvavau (išskirstytos - baigtos, nebaigtos). (user) Skirmante
#         10. Įvertink paskaitas kuriose dalyvavai. (user, lecture) Skirmante Padaryta
#           Pabaiga
#         11. Baigti darba (atsijungti)  (atsijungimo metu paziureti ar dalyvauja ir ispeti jei taip, ar tikrai nori atsijungti.) (user) Raminta

#           """)
