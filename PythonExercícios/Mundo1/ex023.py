import os

def clear_console():
    os.system('cls')

clear_console()

number = int(input('Digite um número de 0 a 9999: '))
number = str(number).zfill(4)
print('Unidade: {}'.format(number[3]))
print('Dezena: {}'.format(number[2]))
print('Centena: {}'.format(number[1]))
print('Milhar: {}'.format(number[0]))