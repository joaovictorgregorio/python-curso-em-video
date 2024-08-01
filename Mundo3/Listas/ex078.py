from crayons import yellow, red, green, blue
import os
import time

logo = blue("""                                                     
 _____     _                   _____                 
|     |___|_|___ ___    ___   |     |___ ___ ___ ___ 
| | | | .'| | . |  _|  | -_|  | | | | -_|   | . |  _|
|_|_|_|__,|_|___|_|    |___|  |_|_|_|___|_|_|___|_|                                                       
""", bold=True)

os.system("cls")
print(logo)

values = list() # Lista vazia
for position in range(0, 5):
    values.append(int(input(f"Digite um valor para a posição {red(position + 1)}: ")))

print(f"\nVocê digitou os valores: {blue(values, bold=True)}")

"""Imprimindo o maior valor e sua posição"""
print(f"O maior valor é {max(values)} e está na posição: ", end="")
print(f"{red(values.index(max(values))+1, bold=True)}")

"""Imprimindo o menor valor e sua posição"""
print(f"O menor valor é {min(values)} e está na posição: ", end="")
print(f"{red(values.index(min(values))+1, bold=True)}")