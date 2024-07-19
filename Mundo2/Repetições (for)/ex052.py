from time import sleep
import os


def clear_console():
    os.system('cls')

clear_console()

def menu():
    print('\033[7;31;47m+-\033[m' * 25)
    print('\033[1;31;40m\n                  NÚMEROS PRIMOS\n\033[m')
    print('\033[7;31;47m+-\033[m' * 25 + '\n')

    number = int(input('Digite um número: '))
    is_cousin(number)

def is_cousin(number):
    number_of_divisons = 0 

    for i in range(1, number + 1):
        if number % i == 0:
            print('\033[33m', end='')
            number_of_divisons += 1
        else:
            print('\033[31m', end='')
        print(f'{i} ', end='')

    print(f'\n\033[mO número {number} foi divisível {number_of_divisons} vezes')
    if number_of_divisons == 2:
        print('E por isso ele \033[32mÉ PRIMO!')
    else:
        print('E por isso ele \033[31mNÃO É PRIMO!')

menu()