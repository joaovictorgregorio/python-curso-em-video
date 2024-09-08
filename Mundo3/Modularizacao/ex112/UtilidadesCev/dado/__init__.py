def leiaDinheiro(preco):
    from crayons import red

    while True:
        valor = str(input(preco)).replace(",", ".").strip()
        if valor.isalpha():
            print(red(f"ERRO: ''{valor}'' é um preço inválido!", bold=True))
        elif valor == "":
            print(red("ERRO: este campo não pode ficar vazio!", bold=True))
        else:
            return float(valor)
