import os

def clear_console():
    os.system('cls')

clear_console()

def multiplication_table_screen():
    print('========================')

def multiplication_table(number):
    multiplication_table_screen()

    for i in range(1, 11):
        print('{} x {} = {}'.format(number, i, (number * i)))

    multiplication_table_screen()

number = int(input('Digite um número para ver sua tabuada: '))
multiplication_table(number)