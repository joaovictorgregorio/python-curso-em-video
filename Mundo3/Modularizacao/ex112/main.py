from ex112.UtilidadesCev import moeda
from ex112.UtilidadesCev import dado
import os

os.system("cls")

preco = float(input("Digite um preço: R$"))
moeda.resumo(preco, 50, 10)
