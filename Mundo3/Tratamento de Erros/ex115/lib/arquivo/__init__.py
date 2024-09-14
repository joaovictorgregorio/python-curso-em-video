from crayons import red, green, white
from lib.interface import cabecalho


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print(red("Houve um ERRO na criação do arquivo!", bold=True))
    else:
        print(green(f"Arquivo {white(nome)} criado com sucesso!", bold=True))


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print(red("Erro ao ler o arquivo!", bold=True))
    else:
        cabecalho("\nPESSOAS CADASTRADAS")
        for linha in a:
            dado = linha.split(";")
            dado[1] = dado[1].replace("\n", "")
            print(f"{dado[0]:<30}{dado[1]:>3} anos")
        print(a.read())
    finally:
        a.close()


def cadastrar(arquivo, nome = 'desconhecido', idade = 0):
    try:
        a = open(arquivo, 'at')
    except:
        print(red("Houve um ERRO na abertura do arquivo!", bold=True))
    else:
        try:
            a.write(f"{nome};{idade}\n")
        except:
            print(red("Houve um ERRO na hora de escrever os dados!", bold=True))
        else:
            print(green(f"Novo registro de {white(nome)} adicionado.", bold=True))
            a.close()
