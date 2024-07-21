import time, os

logo = """\033[32m
  _____                                                               _ _                  _   _                  ____   ___  
 |  __ \                                                   /\        (_) |                | | (_)                |___ \ / _ \ 
 | |__) | __ ___   __ _ _ __ ___  ___ ___  __ _  ___      /  \   _ __ _| |_ _ __ ___   ___| |_ _  ___ __ _  __   ____) | | | |
 |  ___/ '__/ _ \ / _` | '__/ _ \/ __/ __|/ _` |/ _ \    / /\ \ | '__| | __| '_ ` _ \ / _ \ __| |/ __/ _` | \ \ / /__ <| | | |
 | |   | | | (_) | (_| | | |  __/\__ \__ \ (_| | (_) |  / ____ \| |  | | |_| | | | | |  __/ |_| | (_| (_| |  \ V /___) | |_| |
 |_|   |_|  \___/ \__, |_|  \___||___/___/\__,_|\___/  /_/    \_\_|  |_|\__|_| |_| |_|\___|\__|_|\___\__,_|   \_/|____(_)___/ 
                   __/ |                                                                                                      
                  |___/                                                                                                       
\033[m"""

def screen():
    os.system("cls")
    print(logo)

    first_term = int(input('Digite o primeiro termo: '))
    reason = int(input('Digite a razão da PA: '))
    print('\n')

    pa(first_term, reason)


def pa(first_term, reason):
    count = 1
    term = first_term
    while count <= 10:
        print(f'{term} \033[32m-->\033[m ', end='')
        term += reason
        count += 1
    
    print('\033[1;32mPAUSA\033[m')
    
    more = int(input('Quantos termos você quer mostrar a mais? '))
   
    while more != 0:
        count = 1
        while count <= more:
            print(f'{term} \033[32m-->\033[m ', end='')
            term += reason
            count += 1
        print('\033[1;32mPAUSA\033[m')
        more = int(input('Quantos termos você quer mostrar a mais? '))
    print('\033[1;32mFIM\033[m')


screen()