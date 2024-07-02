import os

def clear_console():
    os.system('cls')

clear_console()

car_speed = float(input('Digite a velocidade do carro: '))

if car_speed > 80:
    print('Você foi multado!'.upper())
    fine = (car_speed - 80) * 7
    print('Valor da multa: R$ {:.2f}'.format(fine))

print('Tenha um bom dia!'.upper())