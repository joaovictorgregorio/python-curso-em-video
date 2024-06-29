import os

def clear_console():
    os.system('cls')

clear_console()

value = int(input('Digite um valor: '))

print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(value, (value - 1), (value + 1)))
