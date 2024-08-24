def metade_valor(preco, formatacao):
    if formatacao:
        return moeda(preco)
    metade = preco / 2
    return metade


# def dobro_valor(preco, formatacao):
#     if formatacao:
#         return moeda(preco)
#     dobro = preco * 2
#     return dobro


# def aumento_valor(preco, taxa, formatacao):
#     if formatacao:
#         return moeda(preco)
#     aumento = preco + (preco * taxa / 100)
#     return aumento


# def reducao_valor(preco, taxa, formatacao):
#     if formatacao:
#         return moeda(preco)
#     reducao = preco - (preco * taxa / 100)
#     return reducao


def moeda(preco):
    formatacao = f"R${preco:.2f}".replace(".", ",")
    return formatacao
