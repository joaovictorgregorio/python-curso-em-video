import os, time

logo = """\033[1;32m
                                                                                                                          
  _____                 __   _                   _                    ___                            __         _         
 (_____)  _            (__) (_) ____            (_)        _        _(___)_                         (__)  ____ (_)_       
(_)___(_)(_)__    ____  (_)  _ (____)  ____   __(_)  ___  (_)__    (_)   (_)  ___    __   __   ____  (_) (____)(___) ___  
(_______)(____)  (____) (_) (_)(_)__  (____) (____) (___) (____)   (_)    _  (___)  (__)_(__) (____) (_)(_)_(_)(_)  (___) 
(_)   (_)(_) (_)( )_( ) (_) (_) _(__)( )_( )(_)_(_)(_)_(_)(_)      (_)___(_)(_)_(_)(_) (_) (_)(_)_(_)(_)(__)__ (_)_(_)_(_)
(_)   (_)(_) (_) (__)_)(___)(_)(____) (__)_) (____) (___) (_)        (___)   (___) (_) (_) (_)(____)(___)(____) (__)(___) 
                                                                                              (_)                         
                                                                                              (_)                         
\033[m"""


def screen():
    os.system("cls")
    print(logo)
    registered_people()

def registered_people():
    average_age_of_people = 0
    total_number_of_women_under_20_years_old = 0
    older_man = 0
    older_man_name = ""

    for people in range(1, 5):
        time.sleep(0.3)
        print(f"\n{people}ª pessoa".upper())
        name = str(input(f"\nNome da {people}ª pessoa: ")).strip().title()
        age = int(input(f"Idade da {people}ª pessoa: "))
        gender = str(input(f"Sexo da {people}ª pessoa [M/F]: ")).strip().upper()

        average_age_of_people += age / 4

        if gender == "F" and age < 20:
            total_number_of_women_under_20_years_old += 1
        else:
            if age > older_man:
                older_man = age
                older_man_name = name
        
    print(f"A média de idade das pessoas é de: {average_age_of_people} anos")
    print(f"O nome do homem mais velho é: {older_man_name} com {older_man} anos")
    print(f"O número de mulheres com menos de 20 anos é: {total_number_of_women_under_20_years_old}")
        
        
screen()