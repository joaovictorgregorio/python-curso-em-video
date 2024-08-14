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


def main():
    print("\nAnalisando os valores passados...")
    seis_valores = random.sample(range(1, 10), 6)
    for valor in seis_valores:
        print(f"{valor} ", end=" ")
        time.sleep(0.2)
    print(f"Foram informados {len(seis_valores)} ao todo.")
    maior(seis_valores)

    print("\nAnalisando os valores passados...")
    tres_valores = random.sample(range(1, 10), 3)
    for valor in tres_valores:
        print(f"{valor} ", end=" ")
        time.sleep(0.2)
    print(f"Foram informados {len(tres_valores)} ao todo.")
    maior(tres_valores)


def maior(seis_valores, tres_valores):
    maior_valor_em_seis = max(seis_valores)
    print(f"O maior valor informado foi {maior_valor_em_seis}.")

    maior_valor_em_tres = max(tres_valores)
    print(f"O maior valor informado foi {maior_valor_em_tres}.")


main()
