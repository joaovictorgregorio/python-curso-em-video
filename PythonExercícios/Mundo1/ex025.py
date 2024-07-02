import os

def clear_console():
    os.system('cls')

clear_console()

full_name = str(input('Digite seu nome completo: ')).upper().strip()

print('O nome contém "SILVA"' if (full_name.find('SILVA') != -1) else 'O nome não contém "SILVA"')