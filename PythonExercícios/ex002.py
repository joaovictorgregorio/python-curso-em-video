import os

def limpar_console():
    if os.name == 'nt':
        os.system('cls')

limpar_console()

nome = input('Qual o seu nome? ')

print('É bom ver você aqui {}!'.format(nome))
print('Muito bom ver você aqui', nome)
