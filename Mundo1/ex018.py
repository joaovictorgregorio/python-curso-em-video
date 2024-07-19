from math import radians, sin, cos, tan
import os

def clear_console():
    os.system('cls')

clear_console()

angle = float(input('Digite o ângulo: '))
sine = sin(radians(angle))
print('O seno do ângulo {}° é {:.2f}'.format(angle, sine))
cosine = cos(radians(angle))
print('O cosseno do ângulo {}° é {:.2f}'.format(angle, cosine))
tangent = tan(radians(angle))
print('A tangente do ângulo {}° é {:.2f}'.format(angle, tangent))