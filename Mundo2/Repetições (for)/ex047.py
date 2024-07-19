from time import sleep
import os


def clear_console():
    os.system('cls')

clear_console()

def menu():
    print('\033[1;34;47m+-\033[m' * 25)
    print('\033[1;36;40m\n              CONTAGEM DE PARES\n\033[m')
    print('\033[1;34;47m+-\033[m' * 25)
    print('\n')
    sleep(2)

    count_even_numbers()

def count_even_numbers():
    for i in range(2, 52, 2):
        print(f'\033[1;36;40m{i}\033[m', end=' ')

menu()