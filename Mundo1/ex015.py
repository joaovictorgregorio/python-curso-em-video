import os

def clear_console():
    os.system('cls')

clear_console()

days = int(input('Para quantos dias o carro foi alugado? '))
km = float(input('Quantos quilômetros o carro percorreu? '))
payment = (60 * days) + (0.15 * km)
print('O total a pagar é de R${:.2f}'.format(payment)) 