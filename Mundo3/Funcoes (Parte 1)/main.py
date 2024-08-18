import os

os.system("cls")

"""
def soma(a, b):
    print(f"A = {a} e B = {b}")
    s = a + b
    print(f"A soma A + B = {s}")


soma(a=9, b=6)
"""

"""
def contador(*num):
    tam = len(num)
    print(f"Recebi os valores {num} e são ao todo {tam} números")


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
"""


def dobra(lista):
    posicao = 0
    while posicao < len(lista):
        lista[posicao] *= 2
        posicao += 1


valores = [6, 3, 9, 5, 4, 7]
dobra(valores)
print(valores)