from math import cos
from math import sin
from math import tan
import os

def clear_console():
    os.system('cls')

clear_console()

angle = int(input('Digite o ângulo: '))
print('O seno do ângulo {}° é {:.2f}'.format(angle, sin(angle)))
print('O cosseno do ângulo {}° é {:.2f}'.format(angle, cos(angle)))
print('A tangente do ângulo {}° é {:.2f}'.format(angle, tan(angle)))