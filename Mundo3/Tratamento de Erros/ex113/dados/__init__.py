from time import sleep
from crayons import red, yellow


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
        except KeyboardInterrupt:
            print(yellow("\nO usuário preferiu náo digitar", bold=True))
            sleep(0.5)
            return 0


def leiaFloat(numero):
    """
    -> Função que lê um número real.
    :param numero: Número real
    :return: Retorna o número real digitado
    """
    while True:
        try:
            n = float(input(numero))
            return n
        except ValueError:
            print(red("ERRO! Digite um número real válido.", bold=True))
            sleep(0.5)
        except KeyboardInterrupt:
            print(yellow("\nO usuário preferiu náo digitar", bold=True))
            sleep(0.5)
            return 0
