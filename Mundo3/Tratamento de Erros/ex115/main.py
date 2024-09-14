from lib.interface import logo, menu, cabecalho, leiaInt
from lib.arquivo import arquivoExiste, criarArquivo, lerArquivo, cadastrar
from crayons import red, yellow
from time import sleep
from os import system

print(logo)

arquivo = 'joaovictorgregorio.txt'

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    escolha = menu(
        [
            "Ver pessoas cadastradas",
            "Cadastrar nova pessoa",
            "Sair do sistema"
        ]
    )

    if escolha == 1:
        # Opção de listar o conteúdo de um arquivo!
        lerArquivo(arquivo)
    elif escolha == 2:
        # Opção de cadastrar uma nova pessoa!
        cabecalho("\nNOVO CADASTRO")
        nome = str(input("\nNome: "))
        idade = leiaInt("Idade: ")
        cadastrar(arquivo, nome, idade)
    elif escolha == 3:
        print(yellow("Saindo do sistema...", bold=True))
        sleep(1.5)
        break
    else:
        print(red("Erro: por favor, digite uma opção válida!", bold=True))
    sleep(4)
    print(yellow("Retornando ao menu principal...", bold=True))
    sleep(1)
    system("cls")
    print(logo)
