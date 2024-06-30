import os

def clear_console():
    if os.name == 'nt':
        os.system('cls')

clear_console()

valueOne = int(input('Digite um valor: '))
valueTwo = int(input('Digite outro valor: '))
sum = valueOne + valueTwo

print('A soma entre {} e {} é igual a: {}'.format(valueOne, valueTwo, sum))