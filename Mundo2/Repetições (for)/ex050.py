from time import sleep
import os


def clear_console():
    os.system('cls')

clear_console()

def menu():
    print('\033[7;36;47m+-\033[m' * 25)
    print('\033[1;36;40m\n                 SOMA DOS PARES\n\033[m')
    print('\033[7;36;47m+-\033[m' * 25 + '\n')

    numbers = []

    for i in range(1, 7):
        user_numbers = int(input(f'\033[1;37;40mDigite o {i}º número inteiro: \033[m'))
        numbers += [user_numbers]
        sleep(0.2)

    add_even_numbers(numbers)

def add_even_numbers(numbers):
    soma = 0

    for i in numbers:
        if i % 2 == 0:
            soma += i
            
    print(f'\nA soma dos \033[4;33;40mnúmeros pares\033[m é: \033[1;32;40m{soma}\033[m')

menu()