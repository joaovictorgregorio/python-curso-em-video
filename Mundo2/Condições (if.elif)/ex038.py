import os

def clear_console():
    os.system('cls')

clear_console()

def menu():
    print('\033[1;33;40m-=\033[m' * 30)
    print('\033[1;34;40mCOMPARADOR DE NÚMEROS\033[m')
    print('\033[1;33;40m-=\033[m' * 30)

    number_one = int(input('\nDigite o primeiro número inteiro: '))
    number_two = int(input('Digite o segundo número inteiro: '))

    number_comparator(number_one, number_two)

def number_comparator(number_one, number_two):
    if number_one > number_two:
        print('\033[1;32;40m\nO primeiro valor é maior\033[m \033[1;31;40mque o segundo valor\033[m'.format(number_one, number_two))
    elif number_two > number_one:
        print('\033[1;32;40m\nO segundo valor é maior\033[m \033[1;31;40mque o primeiro valor\033[m'.format(number_two, number_one))
    else:
        print(f'\nOs números {number_one} e {number_two} são iguais'.upper())

menu()