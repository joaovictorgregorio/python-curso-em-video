import time, os, random

logo = """\033[1;36m
  __  __      _                                             _                                      _      
 |  \/  |__ _(_)___ _ _   ___   _ __  ___ _ _  ___ _ _   __| |__ _   ___ ___ __ _ _  _ ___ _ _  __(_)__ _ 
 | |\/| / _` | / _ \ '_| / -_) | '  \/ -_) ' \/ _ \ '_| / _` / _` | (_-</ -_) _` | || / -_) ' \/ _| / _` |
 |_|  |_\__,_|_\___/_|   \___| |_|_|_\___|_||_\___/_|   \__,_\__,_| /__/\___\__, |\_,_\___|_||_\__|_\__,_|
                                                                               |_|                        

\033[m"""

def screen():
    os.system("cls")
    print(logo)

    weights = []

    for i in range(5):
        time.sleep(0.3)
        people = float(input(f"Peso da {i+1}ª pessoa: "))
        weights += [people]

    print(f"\nMaior peso: \033[1;32m{max(weights)}Kg\033[m\nMenor peso: \033[1;36m{min(weights)}Kg\033[m")


screen()