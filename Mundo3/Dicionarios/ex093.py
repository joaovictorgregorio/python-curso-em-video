import os
import time
from crayons import red, green, yellow, blue, magenta, cyan

logo = magenta("""
   ___         _         _               _                   _         
  / __|__ _ __| |__ _ __| |_ _ _ ___    (_)___  __ _ __ _ __| |___ _ _ 
 | (__/ _` / _` / _` (_-<  _| '_/ _ \   | / _ \/ _` / _` / _` / _ \ '_|
  \___\__,_\__,_\__,_/__/\__|_| \___/  _/ \___/\__, \__,_\__,_\___/_|  
                                      |__/     |___/                   
""", bold=True)

os.system("cls")
print(logo)

football_player = dict()

football_player['nome'] = str(input("Nome do jogador: "))
matches = int(input(f"Quantas partidas {yellow(football_player['nome'], bold=True)} jogou? "))

print("\n")
football_player['gols'] = list()
for gol in range(matches):
    time.sleep(0.3)
    football_player['gols'].append(int(input(f"Quantos gols na partida {yellow(gol+1, bold=True)}? ")))

football_player['total'] = sum(football_player['gols'])

print(magenta("\n" + "-=" * 32))
print(football_player)
print(magenta("-=" * 32 + "\n"))

for key in football_player:
    time.sleep(0.5)
    print(f"O campo {key} tem o valor {football_player[key]}.")

print(magenta("\n" + "-=" * 32))

print(f"O jogador {football_player['nome']} jogou {matches} partidas.")
for i, gol in enumerate(football_player['gols']):
    time.sleep(0.5)
    print(f"   => Na partida {i+1}, fez {gol} gols")

print(f"Foi um total de {football_player['total']} gols.")