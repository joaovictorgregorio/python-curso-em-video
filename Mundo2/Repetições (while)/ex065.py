import os, time

logo = """\033[1;31m
______  ___      _____                            ______  ___                                          ______                         
___   |/  /_____ ___(_)_____________   _____      ___   |/  /_________________________   ___   _______ ___  /_________________________
__  /|_/ /_  __ `/_  /_  __ \_  ___/   _  _ \     __  /|_/ /_  _ \_  __ \  __ \_  ___/   __ | / /  __ `/_  /_  __ \_  ___/  _ \_  ___/
_  /  / / / /_/ /_  / / /_/ /  /       /  __/     _  /  / / /  __/  / / / /_/ /  /       __ |/ // /_/ /_  / / /_/ /  /   /  __/(__  ) 
/_/  /_/  \__,_/ /_/  \____//_/        \___/      /_/  /_/  \___//_/ /_/\____//_/        _____/ \__,_/ /_/  \____//_/    \___//____/  
                                                                                                                                      
\033[m"""


def screen():
    os.system("cls")
    print(logo)

    counting_number = 0
    add_of_values = 0
    list_of_values = []
    continue_or_not = True

    while continue_or_not:
        number = int(input("\nDigite um número: "))
        continue_or_not = str(input("Quer continuar? [S/N] ")).upper()[0]
        add_of_values += number
        list_of_values.append(number)
        counting_number += 1
        if continue_or_not == "N":
            continue_or_not = False
    average = add_of_values / counting_number
    print(f"Você digitou \033[1;31m{counting_number}\033[m números e a média foi: \033[1;31m{average:.2f}\033[m")
    print(f"O maior valor digitado foi: \033[1;31m{max(list_of_values)}\033[m e o menor foi: \033[1;31m{min(list_of_values)}\033[m")


screen()