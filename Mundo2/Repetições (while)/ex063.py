import os, time

logo = """\033[1;33m
  ______                                     _              _          _______ _ _                                  _        ___     _____  
 / _____)                                   (_)            | |        (_______|_) |                                (_)      (___)   (_____) 
( (____  _____  ____ _   _ _____ ____   ____ _ _____     __| |_____    _____   _| |__   ___  ____  _____  ____ ____ _    _   _ _    _  __ _ 
 \____ \| ___ |/ _  | | | | ___ |  _ \ / ___) (____ |   / _  | ___ |  |  ___) | |  _ \ / _ \|  _ \(____ |/ ___) ___) |  | | | | |  | |/ /| |
 _____) ) ____| |_| | |_| | ____| | | ( (___| / ___ |  ( (_| | ____|  | |     | | |_) ) |_| | | | / ___ ( (__( (___| |   \ V /| |_ |   /_| |
(______/|_____)\__  |____/|_____)_| |_|\____)_\_____|   \____|_____)  |_|     |_|____/ \___/|_| |_\_____|\____)____)_|    \_(_____|_)_____/ 
                  |_|                                                                                                                       
                                                                                                                      
\033[m"""


def screen():
    os.system("cls")
    print(logo)

    terms = int(input("Quantos termos você quer mostrar? "))
    
    fibonacci(terms)

def fibonacci(terms):
    first_term = 0
    second_term = 1
    count = 0
    while count < terms:
        print(f'{first_term} \033[33m-->\033[m ', end='')
        next_term = first_term + second_term
        first_term = second_term
        second_term = next_term
        count += 1
    print('\033[1;33mFIM\033[m')

    continue_fibonacci = str(input("\nDeseja continuar? [S/N] ")).strip().upper()[0]
    if continue_fibonacci not in ("S", "N"):
        print("\033[1;31mOpção inválida. Voltando para o menu principal...\033[m")
        time.sleep(3)
        screen()
    elif continue_fibonacci == 'S':
        screen()
    else:
        print("\n\033[1;33mObrigado por usar o programa!\033[m")
        exit()
        
        

screen()