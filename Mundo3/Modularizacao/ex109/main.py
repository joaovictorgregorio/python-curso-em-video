import os
import moeda

os.system("cls")

preco = float(input("Digite um preço: R$"))
print(f"A metade de {moeda.moeda(preco)} é {moeda.metade_valor(preco)}")
print(f"O dobro de {moeda.moeda(preco)} é {moeda.dobro_valor(preco, True)}")
print(f"Aumentando {moeda.moeda(preco)} em 10%, temos {moeda.aumento_valor(preco, 10)}")
print(f"Reduzindo {moeda.moeda(preco)} em 13%, temos {moeda.reducao_valor(preco, 13, True)}")
help(moeda)