import os

def clear_console():
    os.system('cls')

clear_console()

def screen():
    print('=*' * 30)
    width = float(input('Largura da parede: '))
    height = float(input('Altura da parede: '))
    area_square_meters(width, height)
    print('=*' * 30)

def area_square_meters(width, height):
    area = width * height
    print('Sua parede tem a dimensão de {:.2f} x {:.2f} e sua área é de {:.3f}m².'.format(width, height, area))
    liters_of_paint(area)

def liters_of_paint(area):
    liters = area / 2
    print('Para pintar essa parede, você precisará de {:.4f}l de tinta.'.format(liters))

screen()

