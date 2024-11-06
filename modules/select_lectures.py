from datetime import datetime
from db_classes import Lecture, engine, User
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)


def select_letures(user):
    print("Pasirinkite įgudžių paskaitą kurioje norite dalyvauti ir užsiregistruok :")
    # all lectures avalable lectures by start_at
    with Session() as session:
        lectures = session.execute(select(Lecture).join(User).where(
            Lecture.start_at < datetime.now())).scalars().all()

        if lectures:
            for lec in lectures:
                print(f"""{lec.id}. {
                      lec.title} - {lec.start_at.strftime('%Y-%m-%d %H:%M')}, dėsto: {lec.user.first_name}""")
            while True:
                lecture_id = input("Pasirinkite paskaitos nr.")
                if not lecture_id and not lecture_id.isdigit():
                    raise ValueError
                    # find lecture
                    pass
                break

        else:
            print("Nėra galiojančių paskaitų.")

        print(f"Pasirink paskaitos numerį: ")


wellcome_hd_msg = "Sveiki atvyke į įgūdžių dalijimosi platformą"
register_hd_msg = "Naujo vartotojo registracija"  # Jevgenijus
login_hd_msg = "Vartotojo prisijungimas"  # Jevgenijus

action_msg = "Pasirinkite veiksmą:"
input_msg = "Kokį veiksmą norite atlikti?: "
exit_msg = "Baigti darbą"


def palatfom_menu():
    print("""
          Mano
        1. Sukurkite savo įgudį (user) Skirmante Padaryta
        2. Sukurkite savo paskaitą (user, skill) Skirmante
        4. Mano paskaitų sarašas (user) Paulius
        5. Mano įgudžių sarašas (user) Paulius
        6. Mano reitingas (user) Raminta
          Paskaitos
        7. Užsiregistruok į paskaitą kurioje nori dalyvauti (paskaitų sarasas su laikais, destytojo reitingu) (user, lecture) Paulius , Ernestas
        8. Paskaitos į kurias prisiregistravęs, bet jos dar neprasidėjusios (user) Ramintai
        9. Paskaitos kuriose dalyvavau (išskirstytos - baigtos, nebaigtos). (user) Skirmante
        10. Įvertink paskaitas kuriose dalyvavai. (user, lecture) Skirmante Padaryta 
          Pabaiga
        11. Baigti darba (atsijungti)  (atsijungimo metu paziureti ar dalyvauja ir ispeti jei taip, ar tikrai nori atsijungti.) (user) Raminta
          
          """)
