import os

def clear_console():
    os.system('cls')

clear_console()

def screen():
    print('\033[1;34;40m*=\033[m' * 30)
    print('\033[1;34;40m\nCONVERSÃO DA BASE\033[m \033[1;33;40mDECIMAL\033[m')
    print('\033[1;33;40m\n1 para binário\033[m')
    print('\033[1;33;40m2 para octal\033[m')
    print('\033[1;33;40m3 para hexadecimal\n\033[m')
    print('\033[1;33;40m*=\033[m' * 30)

    decimal_number = int(input('\nDigite um número inteiro: '))
    
    conversion_basis = int(input('Digite a base de conversão (binário, octal ou hexadecimal): '))
    
    if conversion_basis < 1 or conversion_basis > 3:
        clear_console()
        screen()
    elif conversion_basis == 1:
        conversion_binary(decimal_number)
    elif conversion_basis == 2:
        conversion_octal(decimal_number)
    else:
        conversion_hexadecimal(decimal_number)

def conversion_binary(decimal_number):
    binary_number = bin(decimal_number)[2:]
    print('\033[1;34;47m\nEm binário:\033[m {}'.format(binary_number))

def conversion_octal(decimal_number):
    octal_number = oct(decimal_number)[2:]
    print('\033[1;34;47mEm octal:\033[m {}'.format(octal_number))
    

def conversion_hexadecimal(decimal_number):
    hexadecimal_number = hex(decimal_number)[2:].upper()
    print('\033[1;34;47mEm hexadecimal:\033[m {}'.format(hexadecimal_number))

screen()