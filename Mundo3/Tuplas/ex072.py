from crayons import yellow, red, blue, green, magenta, cyan
from time import sleep
from os import system


logo = cyan("""
                                                                             
 _____                                         _____     _                   
|   | |_ _ _____ ___ ___ ___    ___ ___ ___   |   __|_ _| |_ ___ ___ ___ ___ 
| | | | | |     | -_|  _| . |  | . | . |  _|  |   __|_'_|  _| -_|   |_ -| . |
|_|___|___|_|_|_|___|_| |___|  |  _|___|_|    |_____|_,_|_| |___|_|_|___|___|
                               |_|                                                                                   
""")


system("cls")
print(logo)
sleep(0.5)
print(yellow("Bem vindo....\n".upper(), bold=True))

numbers_in_full = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
                   'seis', 'sete', 'oito', 'nove', 'dez',
                   'onze', 'doze', 'treze', 'quatorze', 'quinze',
                   'dezesseis', 'dezesete', 'dezeoito', 'dezenove', 'vinte')

number = int(input("Digite um número entre 0 e 20: "))
while number < 0 or number > 20:
    number = int(input("Tente novamente. Digite um número entre 0 e 20: "))    
print(f"Você digitou o número {cyan(numbers_in_full[number].capitalize())}")
