import os
from crayons import red, green, yellow, blue, magenta, cyan
from time import sleep

logo = magenta("""
 _____     _ _   _           _          _       _         
|  |  |___| |_|_| |___ ___ _| |___    _| |___ _| |___ ___ 
|  |  | .'| | | . | .'|   | . | . |  | . | .'| . | . |_ -|
 \___/|__,|_|_|___|__,|_|_|___|___|  |___|__,|___|___|___|
""", bold=True)

os.system("cls")
print(logo)


def leiaInt(numero):
    """
    -> Função que lê um número inteiro.
    :param numero: Número inteiro
    :return: Retorna o número inteiro digitado
    """
    while True:
        try:
            n = int(input(numero))
            return n
        except ValueError:
            print(red("ERRO! Digite um número inteiro válido.", bold=True))
            sleep(0.5)


numero = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {numero}")
