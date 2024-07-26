from os import system
from crayons import red
from time import sleep

logo = red("""
 _____      _                     _               _____  ___  
/__   \__ _| |__  _   _  __ _  __| | __ _  __   _|___ / / _ \ 
  / /\/ _` | '_ \| | | |/ _` |/ _` |/ _` | \ \ / / |_ \| | | |
 / / | (_| | |_) | |_| | (_| | (_| | (_| |  \ V / ___) | |_| |
 \/   \__,_|_.__/ \__,_|\__,_|\__,_|\__,_|   \_/ |____(_)___/ 
                                                              
""", bold=True)


def screen():
    system("cls")
    print(logo)
    sleep(0.5)
    print(red("Bem-vindo....".upper(), bold=True))
    multiplication_table()


def multiplication_table():
    while True:
        sleep(0.5)
        print(red("\nDigite um número negativo para sair".upper(), bold=True))
        sleep(0.5)
        value = int(input("Quer ver a tabuada de qual valor? "))
        if value < 0:
            break
        for count in range(1, 11):
            print(f"{value} x {count} = {value * count}")
    sleep(1)
    print(red("\nPrograma encerrado. Volte sempre!".upper(), bold=True))


screen()