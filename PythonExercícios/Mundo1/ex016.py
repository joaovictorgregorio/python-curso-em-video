from math import trunc
import os

def clear_console():
    os.system('cls')

clear_console()

value = float(input('Digite um número decimal: '))
print('O número {} tem a parte inteira {}'.format(value, trunc(value)))

