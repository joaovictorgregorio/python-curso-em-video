import os

def clear_console():
    if os.name == 'nt':
        os.system('cls')

clear_console()

something = input('Digite algo: ')

print('O tipo primitivo desse valor é ', type(something))
print('Só tem espaços: ', something.isspace())
print('É um número: ', something.isnumeric())
print('É alfabético: ', something.isalpha())
print('É alfanúmerico: ', something.isalnum())
print('Está em minúsculas: ', something.islower())
print('Está em maiúsculas: ', something.isupper())
print('Está capitalizada: ', something.istitle())