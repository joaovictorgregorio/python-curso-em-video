from time import sleep
import os


def clear_console():
    os.system('cls')

clear_console()

def menu():
    print('\033[7;33;44m+-\033[m' * 25)
    print('\033[1;33;40m\n            PROGRESSÃO ARITMÉTICA\n\033[m')
    print('\033[7;33;44m+-\033[m' * 25 + '\n')

    first_term = int(input('Digite o primeiro termo: '))
    reason = int(input('Digite a razão: '))

    show_pa(first_term, reason)

def show_pa(first_term, reason):
    print('\033[4;33;40m\nOs 10 primeiros termos da PA são:\n\033[m')
    for i in range(10):
        sleep(0.2)
        print(f'\033[1;34;40m{first_term}\033[m')
        first_term += reason

menu()