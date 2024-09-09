import os
from crayons import yellow, blue, red

os.system("cls")

logo = yellow("""
 _____                _     _               _   _         
|     |___ ___ _ _   |_|___| |_ ___ ___ ___| |_|_|_ _ ___ 
| | | | -_|   | | |  | |   |  _| -_|  _| .'|  _| | | | . |
|_|_|_|___|_|_|___|  |_|_|_|_| |___|_| |__,|_| |_|\_/|___|
""", bold=True)


def leiaInt(numero):
    from time import sleep
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
        except KeyboardInterrupt:
            print(yellow("\nO usuário preferiu náo digitar", bold=True))
            sleep(0.5)
            return 0


def menu(lista):
    """
    Função para mostrar o menu
    :param lista: Lista de opções
    :return: Retorna a opção escolhida
    """
    for i, v in enumerate(lista):
        print(f"{blue(i+1, bold=True)} - {v}")
    
    opcao = leiaInt("\nEscolha uma opção: ")
    return opcao
