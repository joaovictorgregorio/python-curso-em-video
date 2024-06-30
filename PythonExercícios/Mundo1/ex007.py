import os

def clear_console():
    os.system('cls')

clear_console()

noteOne = float(input('Digite a primeira nota: '))
noteTwo = float(input('Digite a segunda nota: '))

average = (noteOne + noteTwo) / 2

print('A média entre {:.1f} e {:.1f} é igual a: {:.1f}'.format(noteOne, noteTwo, average))