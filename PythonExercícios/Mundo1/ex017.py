from math import hypot
import os

def clear_console():
    os.system('cls')

clear_console()

opposite_side = float(input('Comprimento do cateto oposto: '))
adjacent_side = float(input('Comprimento do cateto adjacente: '))
print('A hipotenusa vai medir {:.2f}'.format(hypot(opposite_side, adjacent_side	)))
