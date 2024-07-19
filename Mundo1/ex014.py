import os

def clear_console():
    os.system('cls')

clear_console()

celsius = float(input('Informe a temperatura em °C: '))
fahrenheit = (celsius * 9/5) + 32
print('A temperatura de {:.1f}°C corresponde a {:.1f}°F.'.format(celsius, fahrenheit))