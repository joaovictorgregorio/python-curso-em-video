import os
import time
import random
from crayons import red, green, yellow, blue, magenta, cyan

logo = red("""
  ___          _                        ___                     
 / __| ___ _ _| |_ ___ __ _ _ _   ___  / __| ___ _ __  __ _ _ _ 
 \__ \/ _ \ '_|  _/ -_) _` | '_| / -_) \__ \/ _ \ '  \/ _` | '_|
 |___/\___/_|  \__\___\__,_|_|   \___| |___/\___/_|_|_\__,_|_|  
""", bold=True)

os.system("cls")
print(logo)


def sorteia():
    numeros = random.sample(range(1, 10), 5)

    print("Sorteando 5 valores da lista: ", end="", flush=True)
    time.sleep(1)
    for numero in numeros:
        print(f"{numero}", end=" ", flush=True)
        time.sleep(0.3)
    print("PRONTO...")
    somaPar(numeros)


def somaPar(numeros):
    print(f"\nSomando os valores pares de {numeros}, ", end="", flush=True)
    soma = 0
    for numero in numeros:
        if numero % 2 == 0:
            soma += numero
    time.sleep(1)
    print(f"temos {soma}")


sorteia()
