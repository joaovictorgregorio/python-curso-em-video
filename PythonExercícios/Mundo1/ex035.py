import os

def clear_console():
    os.system('cls')

clear_console()

straight_one = float(input('Digite a primeira reta: '))
straight_two = float(input('Digite a segunda reta: '))
straight_three = float(input('Digite a terceira reta: '))

print('As retas formam um triângulo!' if straight_one + straight_two > straight_three and straight_one + straight_three > straight_two and straight_two + straight_three > straight_one else 'As retas não formam um triângulo!')