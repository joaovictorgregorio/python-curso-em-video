import os
import moeda

os.system("cls")

preco = float(input("Digite um preço: R$"))
print(f"A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade_valor(preco))}")
print(f"O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro_valor(preco))}")
print(f"Aumentando {moeda.moeda(preco)} em 10%, temos {moeda.moeda(moeda.aumento_valor(preco, 10))}")
print(f"Reduzindo {moeda.moeda(preco)} em 13%, temos {moeda.moeda(moeda.reducao_valor(preco, 13))}")
