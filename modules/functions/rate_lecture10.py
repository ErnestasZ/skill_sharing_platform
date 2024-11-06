from datetime import datetime
from ..db_classes import Lecture, engine, User, get_user, Participant
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker, selectinload
from .functions import check_int_input

Session = sessionmaker(bind=engine)

# user = get_user('jason51')


def rate_lecture(user):
    with Session() as session:
        courses = session.execute(select(Participant)
                                  .join(Lecture)
                                  .options(selectinload(Participant.lecture))
                                  .where(Participant.user_id == user.id, Participant.is_complete == True)
                                  ).scalars().all()
    if not courses:
        print('Nepabaigei jokios paskaitos!')
        return
    print("""Pasirinkite paskaitą kuria norite ivertinti:""")
    print("""============================================""")

    for cur in courses:
        rating = 'Nera'
        if cur.lecture_rating:
            rating = 'PATIKO'
        print(f"""[{cur.id}]. Pabaigtos paskaitos {
              cur.lecture.title}, reitingas - {rating}""")
    print("""============================================""")

    while True:
        part_id = check_int_input(input("Iverk paskaitos nr. "))

        # check if id in cources
        if not any(cur.id == part_id for cur in courses):
            print("Nepasirinktas galimas paskaitos ID!")
            continue

        break

    selected_lec = next((cur for cur in courses if cur.id == part_id), None)

    print(f'''Įvertinkite paskaita: [{selected_lec.id}]. Pabaigtos paskaitos {
        selected_lec.lecture.title}, reitingas - {'PATIKO' if selected_lec.lecture_rating else 'nera'}''')
    while True:
        rating = check_int_input(
            input("Pasirink: PATIKO [1] / nevertinu [0]: "))
        if rating not in [0, 1]:
            print("Neteisingas pasirinkimo nr.!")
            continue

        break

    with Session() as session:
        part_by_id = session.get(Participant, part_id)
        part_by_id.lecture_rating = rating
        session.commit()

    print("Įvertinimas paliktas!")


# rate_lecture(user)
