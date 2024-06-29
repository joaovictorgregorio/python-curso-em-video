import os
import math

def clear_console():
    os.system('cls')

clear_console()

value = int(input('Digite um valor: '))

print('O dobro de {} é igual a: {}'.format(value, (value * 2)))
print('O triplo de {} é igual a: {}'.format(value, (value * 3)))
print('A raiz quadrada de {} é igual a: {:.2f}'.format(value, math.sqrt(value)))