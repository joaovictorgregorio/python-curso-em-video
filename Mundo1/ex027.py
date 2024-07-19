import os

def clear_console():
    os.system('cls')

clear_console()

full_name = str(input('Digite seu nome completo: ')).title().split()

print('Seu primeiro nome é: {}'.format(full_name[0]))
print('Seu último nome é: {}'.format(full_name[-1]))