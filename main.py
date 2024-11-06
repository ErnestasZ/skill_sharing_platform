import os
import hashlib
from modules import db_classes as db
# from modules.functions.rate_lecture10 import rate_lecture
from modules.functions.profile_menu import profile_menu

# usertest = db.get_user('jason51')
# # rate_lecture(usertest)
# exit()

session_state = {}


def clear():
    os.system('cls' if os.name == 'nt' else 'echo -e \\\\033c')


def calc_hash(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()


def login():
    result = False

    login = input("Įveskite prisijungimo vardą arba el.pašto adresą: ")
    clear()
    password = input("Įveskite prisijungimo slaptažodį: ")

    user = db.get_user(login)
    hash = calc_hash(password)

    if user and user.password == hash:
        user.add_auth()
        session_state["auth_user"] = user
        result = True

    return result


def register():
    req_inputs = {
        "field": ["first_name", "last_name", "email", "username", "password"],
        "msg_suffix": ["vardą", "pavardę", "el.paštą", "vartotojo vardą", "slaptažodį"],
        "unique": [False, False, True, True, False]
    }

    clear()
    kwargs = {}
    result = False

    i = 0
    n = len(req_inputs["field"])

    while i < n:
        clear()
        user_input = input(f"Įveskite {req_inputs["msg_suffix"][i]}: ")

        if user_input:
            if req_inputs["unique"][i] and db.get_user(user_input):
                input("Reikšmė ne unikali, toks vartotojas jau užsiregistravęs....")
            else:
                i += 1
                kwargs[req_inputs["field"][i]] = user_input if req_inputs["field"][i] != "password" else calc_hash(
                    user_input)

    new_user = db.add_user(**kwargs)
    if new_user:
        session_state["auth_user"] = new_user
        result = True

    return result


wellcome_hd_msg = "Sveiki atvyke į įgūdžių dalijimosi platformą"
register_hd_msg = "Naujo vartotojo registracija"
login_hd_msg = "Vartotojo prisijungimas"

action_msg = "Pasirinkite veiksmą:"
input_msg = "Kokį veiksmą norite atlikti?: "
exit_msg = "Baigti darbą"

# def profile_menu() -> None:
#     print("""
# 1. Sukurkite savo įgudį (user) Skirmante Padaryta
# 2. Sukurkite savo paskaitą (user, skill) Skirmante
# 4. Mano paskaitų sarašas (user) Paulius
# 5. Mano įgudžių sarašas (user) Paulius
# 6. Mano reitingas (user) Raminta
# 7. Užsiregistruok į paskaitą kurioje nori dalyvauti (paskaitų sarasas su laikais, destytojo reitingu) (user, lecture) Paulius , Ernestas
# 8. Paskaitos į kurias prisiregistravęs, bet jos dar neprasidėjusios (user) Ramintai
# 9. Paskaitos kuriose dalyvavau (išskirstytos - baigtos, nebaigtos). (user) Skirmante
# 10. Įvertink paskaitas kuriose dalyvavai. (user, lecture) Skirmante Padaryta
# 11. Baigti darba (atsijungti)  (atsijungimo metu paziureti ar dalyvauja ir ispeti jei taip, ar tikrai nori atsijungti.) (user) Raminta""")
#     input("Profile menu")
#     exit()

def wellcome_menu() -> None:
    action = input(
        f"{wellcome_hd_msg}\n\
{action_msg}\n\
 - prisijungti                  [1]\n\
 - užsiregistruoti              [2]\n\
 - {exit_msg}                 [3]\n\
{input_msg}")

    clear()
    match action:
        case "1":
            if login():
                profile_menu(session_state["auth_user"])
        case "2":
            if register():
                profile_menu(session_state["auth_user"])
        case "3":
            print("Programa baigta!")
            exit()
        case _:
            wellcome_menu()
    clear()


clear()
while True:

    if "auth_user" in session_state:
        profile_menu(session_state["auth_user"])
    else:
        wellcome_menu()


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
