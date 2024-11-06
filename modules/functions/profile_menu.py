from .functions import check_int_input
from .select_lectures7 import select_letures
from .reg_lectures8 import get_user_reg_lecture
from .complete_lectures9 import get_user_compl_lecture
from .rate_lecture10 import rate_lecture


def profile_menu_text() -> None:
    print("""
[1]. Sukurkite savo įgudį.
[2]. Sukurkite savo paskaitą.
[4]. Mano paskaitų sarašas.
[5]. Mano įgudžių sarašas.
[6]. Mano reitingas.
[7]. Užsiregistruok į paskaitą kurioje nori dalyvauti.
[8]. Paskaitos į kurias prisiregistravęs (laukiancios).
[9]. Paskaitos kuriose dalyvavau.
[10]. Įvertink paskaitas kuriose dalyvavai.
[11]. Baigti darba (atsijungti).""")


def profile_menu(user):
    menu_option = {1: 'create_skill',
                   2: 'create_lec',
                   4: 'lect_list',
                   5: 'skill_list',
                   6: 'rating',
                   7: lambda: select_letures(user),
                   8: lambda: get_user_reg_lecture(user),
                   9: lambda: get_user_compl_lecture(user),
                   10: lambda: rate_lecture(user),
                   11: lambda: exit()}

    while True:
        profile_menu_text()
        print('===')
        choice = check_int_input(input("Įveskite pasirinkto menu nr.: "))
        if choice in menu_option:
            menu_option[choice]()
        # break
        # [check_int_input(1, 11, "Iveskite pasirinkima: ")]()
        # input("Profile menu")
        # exit()
