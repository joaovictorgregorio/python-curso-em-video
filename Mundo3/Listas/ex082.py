import time
import os
from crayons import yellow, red, green, blue

logo = yellow("""
 _____         _            _ _     _           
|  |  |___ ___|_|___ ___   | |_|___| |_ ___ ___ 
|  |  | .'|  _| | .'|_ -|  | | |_ -|  _| .'|_ -|
 \___/|__,|_| |_|__,|___|  |_|_|___|_| |__,|___|                                                          
""", bold=True)

os.system("cls")
print(logo)

user_values = list()
even_values = list()
odd_values = list()

while True:
    value = int(input("\nDigite um valor: "))
    user_values.append(value)
    if value < 0:
        print(red("Valor inválido! Digite um valor positivo.", bold=True))
        user_values.pop()
        time.sleep(1)
        print("\033[F\033[K")
    while True:
        option = input("Quer continuar? [S/N] ").strip().upper()[0]
        if option in "S":
            break
        elif option not in "SN":
            print(red("Opção inválida! Tente novamente.", bold=True))
            time.sleep(1)
            print("\033[F\033[K")
        elif option in "N":
            time.sleep(1)
            for value in user_values:
                if value % 2 == 0:
                    even_values.append(value)
                else:
                    odd_values.append(value)
            user_values.sort()
            even_values.sort()
            odd_values.sort()
            print(f"\nLista completa: {yellow(user_values, bold=True)})")
            print(f"Lista de pares: {blue(even_values, bold=True)}")
            print(f"Lista de ímpares: {green(odd_values, bold=True)}")
            exit()