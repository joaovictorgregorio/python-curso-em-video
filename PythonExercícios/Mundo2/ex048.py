from time import sleep
import os


def clear_console():
    os.system('cls')

clear_console()

def menu():
    print('\033[7;34;47m+-\033[m' * 25)
    print('\033[1;34;40m\n         SOMA ÍMPARES MÚLTIPLOS DE TRÊS\n\033[m')
    print('\033[7;34;47m+-\033[m' * 25)
    print('\n')
    sleep(2)

    sum_odd_numbers()

def sum_odd_numbers():
    soma = 0
    for i in range(1, 501, 2):
        if (i % 3 == 0):
            soma += i
    print(
        f'A soma de todos os valores ímpares múltiplos de \033[1;34;40m3\033[m no intervalo de \033[1;34;40m1\033[m a \033[1;34;40m500\033[m é: \033[1;32;40m{soma}\033[m'
    )

menu()