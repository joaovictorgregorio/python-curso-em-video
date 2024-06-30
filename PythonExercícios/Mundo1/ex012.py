import os

def clear_console():
    os.system('cls')

clear_console()

price = float(input('Qual é o preço do produto? R$'))
discount = price * 0.05
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(price, (price - discount)))