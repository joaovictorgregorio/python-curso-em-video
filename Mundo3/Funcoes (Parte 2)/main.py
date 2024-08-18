import os

os.system("cls")

# Mostra no console a funcionalidade do comando, que está dentro do HELP
help(abs)

# Outro forma de mostrar a funcionalidade do comando
print(abs.__doc__)

# Usando docstrings
def contador(inicio, fim, passo):
    """
    -> Faz uma contagem e mostra na tela.
    :param inicio: Início da contagem
    :param fim: Fim da contagem
    :param passo: Passo da contagem
    :return: Sem retorno
    """
    contagem = inicio
    while contagem <= fim:
        print(f"{contagem} ", end="")
        contagem += passo
    print("FIM!")


help(contador)

# Usando parâmetros opcionais
def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: Primeiro valor
    :param b: Segundo valor
    :param c: Terceiro valor
    :return: Sem retorno
    """
    soma = a + b + c
    print(f"A soma vale {soma}")


help(somar)
somar(3, 2, 5)
somar(8, 4)
somar()

# Exercício prático dos conceitos aprendidos
def fatorial(num=1):
    """
    -> Calcula o fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostra ou não a conta.
    :return: O valor do fatorial de um número num.
    """
    fatorial = 1
    for contador in range(num, 0, -1):
        fatorial *= contador
    return fatorial


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f"\nOs resultados são {f1}, {f2} e {f3}")


def par(n=0):
    """
    -> Verifica se um número é par.
    :param n: O número a ser verificado.
    :return: True ou False
    """
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input("\nDigite um número: "))
if par(num):
    print("É par!")
else:
    print("Não é par!")