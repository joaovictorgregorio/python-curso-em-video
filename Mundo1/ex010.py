import os

def clear_console():
    os.system('cls')

clear_console()

def convert_reais_to_dollar(valueInReais, exchangeRate = 5.59):
    valueInDollars = valueInReais / exchangeRate
    return valueInDollars

money = float(input('Quantos reais você tem? R$'))
convert = convert_reais_to_dollar(money)

print('Com R${:.2f} você pode comprar US${:.2f}'.format(money, convert))
