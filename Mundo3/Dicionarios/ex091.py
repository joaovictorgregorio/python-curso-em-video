import os
from time import sleep
import random
from crayons import red, green, yellow, blue, magenta, cyan

logo = blue("""

""", bold=True)

os.system("cls")
print(logo)

players = dict()

sleep(0.5)
print(yellow("OS VALORES SORTEADOS FORAM: \n", bold=True))

for player in range(4):
    draw_numbers = random.randint(1, 6)
    sleep(0.5)
    print(f"O jogador{player + 1} tirou {yellow(draw_numbers, bold=True)}")
    players[f"jogador{player + 1}"] = draw_numbers

sleep(0.5)
print(cyan("\nRANKING DOS JOGADORES: \n", bold=True))
print(players)

for item in sorted(players, key=players.get, reverse=True):
    print(f"{item} com {players[item]}")