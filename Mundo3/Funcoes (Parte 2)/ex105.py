import os
from crayons import red, green, blue, yellow, cyan, magenta
from time import sleep

logo = yellow("""
 _____                   _          _ _     _                 _         
|   __|___ ___ ___ ___ _| |___    _| |_|___|_|___ ___ ___ ___|_|___ ___ 
|  |  | -_|  _| .'|   | . | . |  | . | |  _| | . |   | .'|  _| | . |_ -|
|_____|___|_| |__,|_|_|___|___|  |___|_|___|_|___|_|_|__,|_| |_|___|___|
""")

os.system("cls")
print(logo)


def notas(*notas, situacao=False):
    """
    --> Função que analisa notas e situações de vários alunos.
    :param notas: Uma ou mais notas dos alunos (aceita várias)
    :param situacao: Valor opcional que indica se deve ou não adicionar a situação
    :return: Dicionário com várias informações sobre a turma
    """
    analise = dict()
    analise["total"] = len(notas)
    analise["maior"] = max(notas)
    analise["menor"] = min(notas)
    analise["media"] = sum(notas) / len(notas)
    if situacao:
        if analise["media"] >= 7:
            analise["situacao"] = "boa".upper()
        elif analise["media"] >= 5:
            analise["situacao"] = "razoável".upper()
        else:
            analise["situacao"] = "ruim".upper()
    return analise


resposta = notas(3.5, 2, 6.5, 7, 4, 8, situacao=True) 
print(resposta)
help(notas)
