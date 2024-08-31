from UtilidadesCev import moeda
from UtilidadesCev import dado
import os

os.system("cls")

preco = dado.leiaDinheiro("Digite um preço: R$")
moeda.resumo(preco, 50, 10)
