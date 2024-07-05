from time import sleep
import os


def clear_console():
    os.system('cls')

clear_console()

def menu():
    print('\033[1;34;47m+-\033[m' * 25)
    print('\033[1;36;40m\n              CONTAGEM REGRESSIVA\n\033[m')
    print('\033[1;34;47m+-\033[m' * 25)
    sleep(2)

    countdown()

def countdown():
    for i in range(10, -1, -1):
        print(i)
        sleep(1)
        clear_console()
    
    print('\033[1;31;40mPreparar\033[m')
    sleep(1)
    print('\033[1;33;40mAcionar\033[m')
    sleep(1)
    print('\033[1;32;40mFOGO 🔥🔥🔥\033[m')

menu()