def metade_valor(preco):
    metade = preco / 2
    return metade


def dobro_valor(preco):
    dobro = preco * 2
    return dobro


def aumento_valor(preco, taxa):
    aumento = preco + (preco * taxa / 100)
    return aumento


def reducao_valor(preco, taxa):
    reducao = preco - (preco * taxa / 100)
    return reducao