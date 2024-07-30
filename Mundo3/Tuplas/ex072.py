from crayons import yellow, red, blue, green, magenta, cyan
from time import sleep
from os import system


logo = cyan("""
                                                                             
 _____                                         _____     _                   
|   | |_ _ _____ ___ ___ ___    ___ ___ ___   |   __|_ _| |_ ___ ___ ___ ___ 
| | | | | |     | -_|  _| . |  | . | . |  _|  |   __|_'_|  _| -_|   |_ -| . |
|_|___|___|_|_|_|___|_| |___|  |  _|___|_|    |_____|_,_|_| |___|_|_|___|___|
                               |_|                                                                                   
""")


def screen():
    system("cls")
    print(logo)
    sleep(0.5)
    print(yellow("Bem vindo....\n".upper(), bold=True))
    analyze_number()


def analyze_number():
    numbers_in_full = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
                       'seis', 'sete', 'oito', 'nove', 'dez',
                       'onze', 'doze', 'treze', 'quatorze', 'quinze',
                       'dezesseis', 'dezesete', 'dezeoito', 'dezenove', 'vinte')

    while True:
        number = int(input("Digite um número entre 0 e 20: "))
        if 0 <= number <= 20:
            break
        print(yellow("Tente novamente. "), end=" ")
    print(f"\nVocê digitou o número {cyan(numbers_in_full[number].capitalize())}")
    continue_analyzing()


def continue_analyzing():
    while True:
        continue_analyzing = input("Quer continuar? [S/N] ").strip().upper()[0]
        if continue_analyzing == "S":
            analyze_number()
        elif continue_analyzing == "N":
            sleep(0.5)
            print(cyan("\nFinalizado. Obrigado até a próxima!!!".upper()))
            exit()
        print(red("Resposta inválida. Tente novamente. ", bold=True), end="")


screen()
