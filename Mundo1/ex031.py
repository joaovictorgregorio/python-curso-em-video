import os

def clear_console():
    os.system('cls')

clear_console()

trip_distance = float(input('Digite a distância da viagem: '))

ticket_price = trip_distance * 0.5 if trip_distance <= 200 else trip_distance * 0.45
print('O preço da passagem é R$ {:.2f}'.format(ticket_price))
