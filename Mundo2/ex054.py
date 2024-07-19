from time import sleep
from datetime import date
import os


def clear_console():
    os.system('cls')

clear_console()

def menu():
    print('\033[7;37;41m*=\033[m' * 25)
    print('\033[37m\n             GRUPO DA MAIORIDADE\n\033[m')
    print('\033[7;37;41m*=\033[m' * 25 + '\n')

    birth_year = []

    for i in range(7):
        year_of_birth = int(input(f'Em que ano a {i+1}ª pessoa nasceu? '))
        birth_year += [year_of_birth]

    older_age_analysis(birth_year)

def older_age_analysis(birth_year):
    over_age = 0
    minor_age = 0
    current_date = date.today().year
    
    for i in range(len(birth_year)):
        age = current_date - birth_year[i]
        if age >= 21:
            over_age += 1
        else:
            minor_age += 1

    print('\033[35m\nanalisando...\n\033[m')
    sleep(2)

    print(f'Ao todo tivemos {over_age} pessoas maiores de idade.')
    print(f'E também tivemos {minor_age} pessoas menores de idade.')


menu()