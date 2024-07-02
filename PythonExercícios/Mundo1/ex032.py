from datetime import date
import os

def clear_console():
    os.system('cls')

clear_console()

year = int(input('Digite um ano: '))

if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('O ano {} é BISSEXTO'.format(year))
else: 
    print('O ano {} é NÃO BISSEXTO'.format(year))