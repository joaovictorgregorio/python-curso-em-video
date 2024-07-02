import os

def clear_console():
    os.system('cls')

clear_console()

full_name = input('Digite seu nome completo: ')

print('Seu nome completo em maiúsculas: {}'.format(full_name.upper()))
print('Seu nome completo em mainúsculas: {}'.format(full_name.lower()))
print('Quantidade de letras nome completo: {}'.format(len(full_name.replace(' ', ''))))
print('Quantidade de letras primeiro nome: {}'.format(len(full_name.split()[0])))