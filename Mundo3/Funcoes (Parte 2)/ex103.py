import os
from crayons import red, green, blue, yellow, magenta, cyan
from time import sleep

logo = cyan("""
  ___ _    _              _         _                   _         
 | __(_)__| |_  __ _   __| |___    (_)___  __ _ __ _ __| |___ _ _ 
 | _|| / _| ' \/ _` | / _` / _ \   | / _ \/ _` / _` / _` / _ \ '_|
 |_| |_\__|_||_\__,_| \__,_\___/  _/ \___/\__, \__,_\__,_\___/_|  
                                 |__/     |___/                   
""")

os.system("cls")
print(logo)


def ficha(nome="", gols=""):
    """
    -> Função que retorna a ficha do jogador.
    :param nome: Nome do jogador
    :param gols: Número de gols
    :return: Retorna a ficha do jogador
    """
    if nome == "":
        nome = yellow("<desconhecido>", bold=True)
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    return f"\nO jogador {yellow(nome, bold=True)} fez {gols} gol(s) no campeonato."


nome_jogador = str(input("Nome do Jogador: ")).strip().title()
quantidade_gols = str(input("Número de gols: "))
sleep(0.5)
print(ficha(nome_jogador, quantidade_gols))
