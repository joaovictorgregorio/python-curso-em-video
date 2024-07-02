import os

def clear_console():
    os.system('cls')

clear_console()

number = int(input('Digite um número: '))
print('par'.upper() if number % 2 == 0 else 'impar'.upper())