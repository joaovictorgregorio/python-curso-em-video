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


def interactive_help(ajuda):
    escreva(f"\033[44mAcessando o manual do comando '{ajuda}'\033[m")
    help(ajuda)


def escreva(txt):
    print("~" * (len(txt)))
    sleep(0.5)
    print(f"  {txt}")
    print("~" * (len(txt)))


ajuda = ''
while True:
    escreva("\033[45mSISTEMA DE AJUDA PyHELP\033[m")
    ajuda = str(input("\nFunção ou Biblioteca > ")).strip().lower()
    if ajuda == "fim":
        break
    else:
        interactive_help(ajuda)
escreva("\033[41mATÉ LOGO\033[m")
