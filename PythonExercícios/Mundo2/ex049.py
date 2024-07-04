from time import sleep
import os


def clear_console():
    os.system('cls')

clear_console()

def menu():
    print('\033[7;35;47m+-\033[m' * 25)
    print('\033[1;37;40m\n                   TABUADA V2.0\n\033[m')
    print('\033[7;35;47m+-\033[m' * 25 + '\n')
    
    number = int(input('Digite um número para ver sua tabuada: '))
    multiplication_table(number)


def multiplication_table(number):
    print('\n')
    for i in range(1, 11):
        sleep(0.3)
        print(f'{number} x {i} = \033[1;35;40m{number * i}\033[m')

menu()