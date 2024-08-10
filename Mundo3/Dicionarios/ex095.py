import os
import time
from crayons import red, green, yellow, blue, magenta, cyan

logo = cyan("""
   ___         _         _               _                   _                    _   
  / __|__ _ __| |__ _ __| |_ _ _ ___    (_)___  __ _ __ _ __| |___ _ _ ___ ___  _| |_ 
 | (__/ _` / _` / _` (_-<  _| '_/ _ \   | / _ \/ _` / _` / _` / _ \ '_/ -_|_-< |_   _|
  \___\__,_\__,_\__,_/__/\__|_| \___/  _/ \___/\__, \__,_\__,_\___/_| \___/__/   |_|  
                                      |__/     |___/                                  
""", bold=True)

os.system("cls")
print(logo)

football_player = dict()
list_players = list()

while True:
    football_player['nome'] = str(input("\nNome do jogador: "))
    matches = int(input(f"Quantas partidas {yellow(football_player['nome'], bold=True)} jogou? "))

    football_player['gols'] = list()
    for gol in range(matches):
        time.sleep(0.3)
        football_player['gols'].append(int(input(f"  -- Quantos gols na partida {yellow(gol+1, bold=True)}? ")))
    football_player['total'] = sum(football_player['gols'])
    list_players.append(football_player.copy())
    while True:
        option = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
        if option in "SN":
            break
        print(red("Opção inválida. Tente novamente!", bold=True))
    if option == "N":
        break

print("\n")
print(f"{'COD':<5}{'NOME':<20}{'GOLS':<30}{'TOTAL':<5}")
for cod, player in enumerate(list_players):
    print(f"{cod:<5}{player['nome']:<20}{str(player['gols']):<30}{player['total']:<5}")

while True:
    cod = int(input("\nMostrar dados de qual jogador? (999 para parar) "))
    if cod == 999:
        print(cyan("  -- Obrigado por usar o programa!".upper(), bold=True))
        break
    if cod >= len(list_players):
        print(red(f"Não existe jogador com código {cod}.", bold=True))
    else:
        print(f" -- LEVANTAMENTO DO JOGADOR {yellow(list_players[cod]['nome'], bold=True)}:")
        for gol in range(len(list_players[cod]['gols'])):
            print(f"    Na partida {gol+1}, fez {list_players[cod]['gols'][gol]} gols.")