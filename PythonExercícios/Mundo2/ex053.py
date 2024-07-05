from time import sleep
import os


def clear_console():
    os.system('cls')

clear_console()

def menu():
    print('\033[7;34;47m+-\033[m' * 25)
    print('\033[1;36;40m\n              DETECTOR DE PALÍNDROMO\n\033[m')
    print('\033[7;34;47m+-\033[m' * 25 + '\n')

    phrase = str(input('Digite uma frase: ')).strip().upper()

    palindrome_phrase(phrase)

def palindrome_phrase(phrase):
    phrase_without_spaces = ''.join(phrase.split())
    reverse_phrase = phrase_without_spaces[::-1]

    print('\033[1;36;40m\nAnalisando...\n\033[m')
    sleep(2)

    print(f'A frase \033[33m{phrase}\033[m de forma invertida fica \033[33m{reverse_phrase}\033[m')

    if (phrase_without_spaces == reverse_phrase):
        print(f'A frase \033[32mé um palíndromo!')
    else:
        print(f'A frase \033[31mnão é um palíndromo!')


menu()