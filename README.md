aktyvuoti virtualę aplinka venv
.\venv\Scripts\activate

atsisiųsti įdiegtas bibliotekas
pip install -r requirements.txt



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
