from os import system
from crayons import yellow

logo = yellow("""
 _     _             _                                                                              _______ _              
(_)   (_)           (_)                                                                            (_______) |             
 _     _ _____  ____ _  ___   ___    ____  _   _ ____  _____  ____ ___   ___     ____ ___  ____     _____  | | _____  ____ 
| |   | (____ |/ ___) |/ _ \ /___)  |  _ \| | | |    \| ___ |/ ___) _ \ /___)   / ___) _ \|    \   |  ___) | |(____ |/ _  |
 \ \ / // ___ | |   | | |_| |___ |  | | | | |_| | | | | ____| |  | |_| |___ |  ( (__| |_| | | | |  | |     | |/ ___ ( (_| |
  \___/ \_____|_|   |_|\___/(___/   |_| |_|____/|_|_|_|_____)_|   \___/(___/    \____)___/|_|_|_|  |_|      \_)_____|\___ |
                                                                                                                    (_____|
""")


def screen():
    system("cls")
    print(logo)
    number_with_flags()


def number_with_flags():
    count_numbers = number = add = 0
    while True:
        number = int(input("[999 para interromper]. Digite um número: "))
        if number == 999:
            break
        add += number
        count_numbers += 1
    print(f"\nA soma dos {count_numbers} valores foi: {add}")


screen()