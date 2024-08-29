import moeda
import os

os.system("cls")

preco = float(input('Digite o preço: R$'))
moeda.resumo(preco, 20, 12)
