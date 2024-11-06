import os, hashlib
from modules import db_classes as db

if __name__ != "__main__":
    exit()

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
        session_state["auth_user"] = user
        result = True

    return result

session_state = {}
wellcome_hd_msg = "Sveiki atvyke į įgūdžių dalijimosi platformą"
register_hd_msg = "Naujo vartotojo registracija"
login_hd_msg = "Vartotojo prisijungimas"

action_msg = "Pasirinkite veiksmą:"
input_msg = "Kokį veiksmą norite atlikti?: "
exit_msg = "Baigti darbą"

def wellcome_menu() -> None:
    action = input(\
f"{wellcome_hd_msg}\n\
{action_msg}\n\
 - prisijungti                  [1]\n\
 - užsiregistruoti              [2]\n\
 - {exit_msg}                 [3]\n\
{input_msg}")
    
    clear()
    match action:
        case "1":
            login()
        case "2":
            pass
        case "3":
            print("Programa baigta!")
            exit()
        case _:
            wellcome_menu()
    clear()

def register_menu():
    pass

clear()

while True:

    if "auth_user" in session_state:
        print("Login successful")
        break
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