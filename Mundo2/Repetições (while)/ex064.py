import os, time

logo = """\033[36m
 _______                                _                           _                          _                                __   ______ 
(_______)           _                  | |                         (_)                        | |                              /  | / __   |
 _        ____ ____| |_  ____ ____   _ | | ___     _   _ ____  ____ _  ___   ___    _   _ ____| | ___   ____ ____  ___    _   /_/ || | //| |
| |      / ___) _  |  _)/ _  |  _ \ / || |/ _ \   | | | / _  |/ ___) |/ _ \ /___)  | | | / _  | |/ _ \ / ___) _  )/___)  | | | || || |// | |
| |_____| |  ( ( | | |_( ( | | | | ( (_| | |_| |   \ V ( ( | | |   | | |_| |___ |   \ V ( ( | | | |_| | |  ( (/ /|___ |   \ V / | ||  /__| |
 \______)_|   \_||_|\___)_||_|_| |_|\____|\___/     \_/ \_||_|_|   |_|\___/(___/     \_/ \_||_|_|\___/|_|   \____|___/     \_/  |_(_)_____/ 
                                                                                                                                     
\033[m"""


def screen():
    os.system("cls")
    print(logo)
    
    number_of_values = 0
    add_of_values = 0
    value = int(input('\033[36mOBS: [999 para parar].\033[m Digite um número: '))
    
    while value != 999:
        number_of_values += 1
        add_of_values += value
        time.sleep(0.3)
        value = int(input('\033[36mOBS: [999 para parar].\033[m Digite um número: '))

    print(f'\nVocê digitou \033[36m{number_of_values}\033[m números e a soma entre eles foi \033[36m{add_of_values}\033[m.')


screen()