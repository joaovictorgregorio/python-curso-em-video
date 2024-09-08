def resumo(preco, aumento, reducao):
    from crayons import yellow
    """
    --> Retorna um resumo do valor
    :param preco: valor a ser calculado
    :param aumento: porcentagem do aumento
    :param reducao: porcentagem da redução
    :return: resumo do valor
    """
    print("\n")
    print(yellow("-" * 35))
    print("RESUMO DO VALOR".center(35))
    print(yellow("-" * 35))
    print(f"Preço analisado: \t{moeda(preco)}")
    print(f"Dobro do preço: \t{dobro_valor(preco, True)}")
    print(f"Metade do preço: \t{metade_valor(preco, True)}")
    print(f"{aumento}% de aumento: \t{aumento_valor(preco, aumento, True)}")
    print(f"{reducao}% de redução: \t{reducao_valor(preco, reducao, True)}")
    print("-" * 35)


def metade_valor(preco, formatacao=False):
    """
    --> Retorna a metade do preço
    :param preco: valor a ser calculado
    :param formatacao: (opcional) se True, retorna o valor formatado
    :return: valor da metade do preço
    """
    metade = preco / 2
    return metade if formatacao is False else moeda(metade)


def dobro_valor(preco, formatacao=False):
    """
    --> Retorna o dobro do preço
    :param preco: valor a ser calculado
    :param formatacao: (opcional) se True, retorna o valor formatado
    :return: valor do dobro do preço
    """
    dobro = preco * 2
    return dobro if formatacao is False else moeda(dobro)


def aumento_valor(preco, taxa, formatacao=False):
    """
    --> Retorna o valor aumentado
    :param preco: valor a ser calculado
    :param taxa: porcentagem do aumento
    :param formatacao: (opcional) se True, retorna o valor formatado
    :return: valor aumentado
    """
    aumento = preco + (preco * taxa / 100)
    return aumento if formatacao is False else moeda(aumento)


def reducao_valor(preco, taxa, formatacao=False):
    """
    --> Retorna o valor reduzido
    :param preco: valor a ser calculado
    :param taxa: porcentagem do aumento
    :param formatacao: (opcional) se True, retorna o valor formatado
    :return: valor reduzido
    """
    reducao = preco - (preco * taxa / 100)
    return reducao if formatacao is False else moeda(reducao)


def moeda(preco):
    """
    --> Retorna o valor formatado
    :param preco: valor a ser formatado
    :return: valor formatado
    """
    formatacao = f"R${preco:.2f}".replace(".", ",")
    return formatacao
