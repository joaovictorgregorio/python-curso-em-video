from time import sleep
from math import pow
import os

def clear_console():
    os.system('cls')

clear_console()

def menu():
    print('\033[1;35;40m+-\033[m' * 25)
    print('\033[1;35;40mCALCULADORA IMC\033[m')
    print('\033[1;35;40m+-\033[m' * 25)

    weight = float(input('Digite seu peso: '))
    height = float(input('Digite sua altura: '))
    imc(weight, height)

def imc(weight, height):
    imc = weight / pow(height, 2.0)
    if (imc < 18.5):
        print(f'\nSeu IMC é de {imc:.1f}, você está \033[1;31;40mAbaixo do peso\033[m.')
    elif (18.5 <= imc < 25):
        print(f'\nSeu IMC é de {imc:.1f}, você está no \033[1;32;40mPeso ideal\033[m.')
    elif (25.0 <= imc < 30):
        print(f'\nSeu IMC é de {imc:.1f}, você está com \033[1;33;40mSobrepeso\033[m.')
    elif (30.0 <= imc < 40):
        print(f'\nSeu IMC é de {imc:.1f}, você está com \033[1;31;40mObesidade\033[m.')
    elif (imc >= 40):
        print(f'\nSeu IMC é de {imc:.1f}, você está com \033[1;31;40mObesidade Mórbida\033[m.')
    else:
        clear_console()
        menu()

menu()