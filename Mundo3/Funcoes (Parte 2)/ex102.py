import os
from crayons import red, green, blue, yellow, cyan, magenta
from time import sleep

logo = blue("""
  ___     _           _      _     _   
 | __|_ _| |_ ___ _ _(_)__ _| |  _| |_ 
 | _/ _` |  _/ _ \ '_| / _` | | |_   _|
 |_|\__,_|\__\___/_| |_\__,_|_|   |_|  
""", bold=True)

os.system("cls")
print(logo)


def fatorial(valor, show=False):
    """
    -> Calcula o fatorial de um número.
    :param valor: O número a ser calculado.
    :param show: (opcional) Mostra ou não a conta.
    :return: O valor do fatorial de um número n.
    """
    fatorial = 1
    for i in range(valor, 0, -1):
        if show:
            print(i, end="", flush=True)
            sleep(0.3)
            if i > 1:
                print(" x ", end="", flush=True)
            else:
                print(" = ", end="", flush=True)
        fatorial *= i
    sleep(0.3)
    return fatorial


print(fatorial(5, True))
