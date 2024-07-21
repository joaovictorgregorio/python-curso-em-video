import os, time

logo = """\033[1;36m
 _______       _             _              _          _______                      _       _  
(_______)     | |           | |            | |        (_______)      _             (_)     | | 
 _       _____| | ____ _   _| | ___      __| | ___     _____ _____ _| |_ ___   ____ _ _____| | 
| |     (____ | |/ ___) | | | |/ _ \    / _  |/ _ \   |  ___|____ (_   _) _ \ / ___) (____ | | 
| |_____/ ___ | ( (___| |_| | | |_| |  ( (_| | |_| |  | |   / ___ | | || |_| | |   | / ___ | | 
 \______)_____|\_)____)____/ \_)___/    \____|\___/   |_|   \_____|  \__)___/|_|   |_\_____|\_)
\033[m"""

def screen():
    os.system("cls")
    print(logo)

    number = int(input("Digite um número: "))

    if number < 0:
        return print("Não é possível calcular o fatorial de um número negativo!")
        screen()
    
    factorial(number)


def factorial(number):
    factorial = 1
    counter = number
    
    print(f"Fatorial do número {number} = ", end="")
    while counter > 0:
        print(f"{counter}", end="")
        print(" x " if counter > 1 else " = ", end="")
        factorial *= counter
        counter -= 1
    print(f"{factorial}")
        

screen()