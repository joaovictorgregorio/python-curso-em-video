import os

def clear_console():
    os.system('cls')

clear_console()

phrase = str(input('Digite uma frase: ')).strip().upper()

print('A letra "A" aparece {} vezes na frase.'.format(phrase.count('A')))
print('A primeira letra "A" apareceu na posição {}'.format(phrase.find('A')+1))
print('A última letra "A" apareceu na posição {}'.format(phrase.rfind('A')+1))