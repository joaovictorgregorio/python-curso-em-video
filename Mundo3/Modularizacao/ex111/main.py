from UtilidadesCev import moeda
import os

os.system("cls")

preco = float(input("Digite um preço: R$"))
moeda.resumo(preco, 50, 10)
