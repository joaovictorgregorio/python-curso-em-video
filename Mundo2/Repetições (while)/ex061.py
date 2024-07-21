import time, os

logo = """\033[34m
  ____                                                     _         _ _                  _   _                   ____    ___  
 |  _ \ _ __ ___   __ _ _ __ ___  ___ ___  __ _  ___      / \   _ __(_) |_ _ __ ___   ___| |_(_) ___ __ _  __   _|___ \  / _ \ 
 | |_) | '__/ _ \ / _` | '__/ _ \/ __/ __|/ _` |/ _ \    / _ \ | '__| | __| '_ ` _ \ / _ \ __| |/ __/ _` | \ \ / / __) || | | |
 |  __/| | | (_) | (_| | | |  __/\__ \__ \ (_| | (_) |  / ___ \| |  | | |_| | | | | |  __/ |_| | (_| (_| |  \ V / / __/ | |_| |
 |_|   |_|  \___/ \__, |_|  \___||___/___/\__,_|\___/  /_/   \_\_|  |_|\__|_| |_| |_|\___|\__|_|\___\__,_|   \_/ |_____(_)___/ 
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
        print(f'{term} \033[34m-->\033[m ', end='')
        term += reason
        count += 1
    
    print('\033[1;34mFIM\033[m')


screen()