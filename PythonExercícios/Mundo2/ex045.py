from time import sleep
from random import choice
import os


def clear_console():
    os.system('cls')

clear_console()

def menu():
    print('\033[1;35;47m+-\033[m' * 25)
    print('\033[1;35;40m\n                 J O K E N P Ô\n\033[m')
    print('\033[1;35;47m+-\033[m' * 25)

    choose_player = str(input('\nEscolha pedra, papel ou tesoura: ')).lower()
    computer_playing_jokenpo(choose_player)

def computer_playing_jokenpo(choose_player):
    options = ['pedra', 'papel', 'tesoura']
    choose_computer = choice(options)

    print(f'\nVocê escolheu: {choose_player}')
    print(f'O computador escolheu: {choose_computer}')

    if (choose_player == choose_computer):
        print('\033[1;33;40m\nEMPATE\033[m')
    else:
        if (
            (choose_player == 'pedra' and choose_computer == 'tesoura') or 
            (choose_player == 'papel' and choose_computer == 'pedra') or 
            (choose_player == 'tesoura' and choose_computer == 'papel')
        ):
            print('\033[1;32;40m\nVOCÊ VENCEU\033[m')
        else:
            print('\033[1;31;40m\nVOCÊ PERDEU\033[m')

menu()