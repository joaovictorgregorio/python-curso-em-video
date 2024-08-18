import os
from crayons import red, green, blue, yellow, cyan, magenta
from time import sleep

logo = yellow("""
 _____     _                   _   _            _       _     _         
|     |___| |_ ___ ___ ___ ___| |_|_|_ _ ___   | |_ ___| |___|_|___ ___ 
|-   -|   |  _| -_|  _| .'|  _|  _| | | | -_|  |   | -_| | . | |   | . |
|_____|_|_|_| |___|_| |__,|___|_| |_|\_/|___|  |_|_|___|_|  _|_|_|_|_  |
                                                         |_|       |___|
""", bold=True)

os.system("cls")
print(logo)


def interactive_help():
    while True:
        ajuda = str(input("\nFunção ou Biblioteca > ")).strip().lower()
        if ajuda == "fim":
            print("\033[41m\nAté logo!\033[m")
            break
        escreva(f"Acessando o manul do comando `{ajuda}`")
        print(cyan("\n", help(ajuda)))


def escreva(txt):
    print("~" * (len(txt)))
    print(f"  {txt}")
    print("~" * (len(txt)))

    while True:
        ajuda = str(input("\nFunção ou Biblioteca > ")).strip().lower()
        if ajuda == "fim":
            print("\033[41m\nAté logo!\033[m")
            break
        escreva(f"Acessando o manul do comando `{ajuda}`")
        return help(ajuda)


escreva("\033[45mSISTEMA DE AJUDA PyHELP\033[m")