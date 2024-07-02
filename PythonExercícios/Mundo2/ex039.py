from datetime import date
import os

def clear_console():
    os.system('cls')

clear_console()


def scren():
    print('\033[1;32;40m-=\033[m' * 30)
    print('\033[1;37;40mALISTAMENTO\033[m \033[1;32;40mMILITAR\033[m')
    print('\033[1;37;40m-=\033[m' * 30)

    year_of_birthday = int(input('\nAno de nascimento: '))
    military_enlistment(year_of_birthday)

def military_enlistment(year_of_birthday):
    age = date.today().year - year_of_birthday

    if age < 18:
        years_remaining = 18 - age
        print(f'\033[1;33;40mAinda falta {years_remaining} ano(s) para o seu alistamento\033[m')
    elif age > 18:
        years_past = age - 18
        print(f'Já passou {years_past} ano(s) do tempo do seu alistamento')
    else:
        print('\033[1;31;40mVocê deve se alistar IMEDIATAMENTE!\033[m')

scren()