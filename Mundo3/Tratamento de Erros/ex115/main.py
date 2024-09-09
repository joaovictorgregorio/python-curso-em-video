from lib.interface import logo
from lib.interface import menu
from crayons import red, yellow
from time import sleep
from os import system

print(logo)

while True:
    escolha = menu(
        [
            "Ver pessoas cadastradas",
            "Cadastrar nova pessoa",
            "Sair do sistema"
        ]
    )

    if escolha == 1:
        print("Opção 1")
    elif escolha == 2:
        print("Opção 2")
    elif escolha == 3:
        print(yellow("Saindo do sistema...", bold=True))
        sleep(1.5)
        break
    else:
        print(red("Erro: por favor, digite uma opção válida!", bold=True))
    sleep(1.5)
    system("cls")
    print(logo)
