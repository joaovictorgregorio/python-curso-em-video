import os
import time
import random
from crayons import red, green, yellow, blue, magenta, cyan

logo = yellow("""
 _____     _            _____                       
|     |___|_|___ ___   |   | |_ _ _____ ___ ___ ___ 
| | | | .'| | . |  _|  | | | | | |     | -_|  _| . |
|_|_|_|__,|_|___|_|    |_|___|___|_|_|_|___|_| |___|
""", bold=True)

os.system("cls")
print(logo)


def maior(numeros_aleatorios):
    print(yellow("-=" * 25, bold=True))
    print("Analisando os valores passados...")
    time.sleep(1)
    for numero in numeros_aleatorios:
        print(f"{numero}", end=" ", flush=True)
        time.sleep(0.3)
    time.sleep(0.5)
    print(f"\nForam informados {len(numeros_aleatorios)} valores ao todo.")
    time.sleep(0.5)
    if numeros_aleatorios == []:
        print("O maior valor informado foi 0")
    else:
        print(f"O maior valor informado foi {max(numeros_aleatorios)}\n")


seis_numeros_aleatorios = random.sample(range(1, 10), 6)
maior(seis_numeros_aleatorios)

tres_numeros_aleatorios = random.sample(range(1, 10), 3)
maior(tres_numeros_aleatorios)

dois_numeros_aleatorios = random.sample(range(1, 10), 2)
maior(dois_numeros_aleatorios)

numero_aleatorio = random.sample(range(1, 10), 1)
maior(numero_aleatorio)

nenhum_numero = []
maior(nenhum_numero)
