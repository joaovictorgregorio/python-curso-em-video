import os

def clear_console():
    os.system('cls')

clear_console()

city = str(input('Digite o nome da cidade: ')).upper().strip().startswith('SANTO')

print('O nome da cidade começa com "Santo"' if (city == True) else 'O nome da cidade não começa com "Santo"')