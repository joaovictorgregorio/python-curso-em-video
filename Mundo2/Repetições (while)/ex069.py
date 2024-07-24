from os import system
from time import sleep
from crayons import blue, red

logo = """\033[1;34m                                                                 
 _____         _ _              _          _       _              _                            
|  _  |___ ___| |_|___ ___    _| |___    _| |___ _| |___ ___    _| |___    ___ ___ _ _ ___ ___ 
|     |   | .'| | |_ -| -_|  | . | -_|  | . | .'| . | . |_ -|  | . | . |  | . |  _| | | . | . |
|__|__|_|_|__,|_|_|___|___|  |___|___|  |___|__,|___|___|___|  |___|___|  |_  |_| |___|  _|___|
                                                                          |___|       |_|      
\033[m"""


def screen():
    system("cls")
    print(logo)
    sleep(0.5)
    print(blue("Bem-vindo....".upper(), bold=True))
    sleep(0.5)
    register_people()


people_over_18_years_old = []
amount_of_men = []
women_under_20 = []


def register_people():
    print(blue("\nCadastre uma pessoa".upper(), bold=True))

    age = int(input("Idade: "))
    if age > 18:
        people_over_18_years_old.append(age)

    while True:
        gender = str(input("Sexo: [M/F] ").strip().upper())
        if gender == "M" or gender == "F":
            if gender == "M":
                amount_of_men.append(gender)
            elif gender == "F" and age < 20:
                women_under_20.append(gender)
            break
        else:
            print(red("Opção inválida. Tente novamente.", bold=True))
            sleep(0.8)
            print("\033[F\033[K", end="")

    while True:
        continue_register = input("Quer continuar? [S/N] ").strip().upper()
        if continue_register == "N":
            sleep(1)
            print(blue("\nFinalizando...".upper(), bold=True))
            print(f"Total de pessoas com mais de 18 anos: {len(people_over_18_years_old)}")
            print(f"Ao todo temos {len(amount_of_men)} homens cadastrados.")
            if len(women_under_20) == 0:
                print("Não temos mulheres abaixo de 20 anos.")
            elif len(women_under_20) == 1:
                print("Tem 1 mulher abaixo de 20 anos.")
            else:
                print(f"Temos {len(women_under_20)} mulheres abaixo de 20 anos.")
            exit()
        elif continue_register == "S":
            register_people()
        else:
            print(red("Opção inválida. Tente novamente.", bold=True))
            sleep(0.8)
            print("\033[F\033[K", end="")


screen()
