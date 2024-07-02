from random import randint
from time import sleep
import os

def clear_console():
    os.system('cls')

clear_console()

user_number = int(input('Tente adivinhar um número de 0 a 5: '))
computer_number = randint(0, 5)

print('processando....'.upper())
sleep(1)
print('\033[0;32;40mVocê venceu!\033[m' if user_number == computer_number else '\033[0;31;40mVocê perdeu!\033[m')