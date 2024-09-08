import os
from crayons import cyan
from banner import logo
from dados import leiaInt, leiaFloat

os.system("cls")
print(logo)

numero_inteiro = leiaInt("Digite um número inteiro: ")
numero_real = leiaFloat("Digite um número real: ")
print(f"\nO número inteiro digitado foi {cyan(numero_inteiro)}", end="")
print(f" e o número real digitado foi {cyan(numero_real)}")
