from crayons import magenta, yellow, green, blue, cyan, red
from time import sleep
from os import system

logo = magenta("""
                                                                                                             
 _____         _                             _____ _                    _        _____     _       _       _ 
|_   _|_ _ ___| |___ ___    ___ ___ _____   |_   _|_|_____ ___ ___    _| |___   |   __|_ _| |_ ___| |_ ___| |
  | | | | | . | | .'|_ -|  |  _| . |     |    | | | |     | -_|_ -|  | . | -_|  |   __| | |  _| -_| . | . | |
  |_| |___|  _|_|__,|___|  |___|___|_|_|_|    |_| |_|_|_|_|___|___|  |___|___|  |__|  |___|_| |___|___|___|_|
          |_|                                                                                                
""")

system("cls")
print(logo)
sleep(0.5)
print(magenta("Bem vindo...".upper(), bold=True))

current_list_of_2024_Brasileirao = ('Botafogo', 'Flamengo', 'Palmeiras',
                                    'Fortaleza', 'Cruzeiro', 'São Paulo',
                                    'Bahia', 'Athletico-PR', 'Bragantino',
                                    'Atlético-MG', 'Vasco da Gama', 'Criciúma',
                                    'Juventude', 'Internacional',
                                    'Corinthians', 'EC Vitória', 'Cuiabá',
                                    'Fluminense', 'Grêmio', 'Atlético-GO ',)

sleep(0.5)
print("\nLista de times Brasileirão 2024:")
for position, team in enumerate(current_list_of_2024_Brasileirao):
    print(f"{yellow(position+1, bold=True)}ª {team}")

sleep(0.5)
print("\nOs 5 primeiros são: ", end="")
print(f"{green(current_list_of_2024_Brasileirao[:5], bold=True)}")
sleep(0.5)
print("\nOs 4 últimos são: ", end="")
print(f"{red(current_list_of_2024_Brasileirao[-4:], bold=True)}")
sleep(0.5)
print(f"\nTimes em ordem alfabética: {sorted(current_list_of_2024_Brasileirao)}")
sleep(0.5)
print("\nO Corinthians está na ", end="")
print(f"{current_list_of_2024_Brasileirao.index('Corinthians')+1}ª posição")
