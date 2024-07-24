from os import system
from time import sleep
from random import randint
from crayons import red, green, magenta

logo = """\033[1;35m
   ___                            _____                            
  / _ \__ _ _ __    ___  _   _    \_   \_ __ ___  _ __   __ _ _ __ 
 / /_)/ _` | '__|  / _ \| | | |    / /\/ '_ ` _ \| '_ \ / _` | '__|
/ ___/ (_| | |    | (_) | |_| | /\/ /_ | | | | | | |_) | (_| | |   
\/    \__,_|_|     \___/ \__,_| \____/ |_| |_| |_| .__/ \__,_|_|   
                                                 |_|               
\033[m"""


def screen():
    system("cls")
    print(logo)
    sleep(0.5)
    print(magenta("Bem vindo...".upper()))
    sleep(0.5)
    print(magenta("Vamos jogar?" + " Par ou Impar".upper()))
    odd_or_even_game()


def odd_or_even_game():
    rounds_won = 0
    while True:
        player_number = int(input("\nDigite um número: "))
        player_choice = input("Par ou Impar? [P/I] ").strip().upper()[0]
        computer_number = randint(0, 10)
        result = player_number + computer_number
        print(f"\nVocê jogou {player_number} e o computador {computer_number}. Total de {result}")
        if result % 2 == 0 and player_choice == "P":
            print(green("Você venceu!".upper()))
            rounds_won += 1
            print("Vamos jogar novamente...")
        elif result % 2 != 0 and player_choice == "I":
            print(green("Você venceu!".upper()))
            rounds_won += 1
            print("Vamos jogar novamente...")
        else:
            print(red("Você perdeu!".upper()))
            break
    print(f"\nVocê venceu {rounds_won} rodadas consecutivas!")


screen()