import random
import os
import time
from crayons import green, yellow

logo = green("""
  __  __                 ___                
 |  \/  |___ __ _ __ _  / __| ___ _ _  __ _ 
 | |\/| / -_) _` / _` | \__ \/ -_) ' \/ _` |
 |_|  |_\___\__, \__,_| |___/\___|_||_\__,_|
            |___/                           
""", bold=True)

os.system("cls")
print(logo)

amount_of_games = int(input("Quantos jogos você quer que eu sorteie? "))

print(yellow(f"\nSorteando {amount_of_games} jogos\n".upper()))
for game in range(amount_of_games):
    numbers = random.sample(range(1, 61), 6)
    time.sleep(0.5)
    print(f"Jogo {game + 1}: {sorted(numbers)}")