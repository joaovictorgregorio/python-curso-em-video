from crayons import magenta, yellow
from os import system
from time import sleep

logo = magenta("""
 _______       _                _______ _                               _               ______  _     _    _                            
(_______)     (_)              (_______) |         _                   (_)             (_____ \| |   (_)  | |                           
 _       _____ _ _   _ _____    _____  | | _____ _| |_  ____ ___  ____  _  ____ ___      ____) ) |_____   | |__   ___   ____ _____  ___ 
| |     (____ | ( \ / |____ |  |  ___) | || ___ (_   _)/ ___) _ \|  _ \| |/ ___) _ \    / ____/|_____  |  |  _ \ / _ \ / ___|____ |/___)
| |_____/ ___ | |) X (/ ___ |  | |_____| || ____| | |_| |  | |_| | | | | ( (__| |_| |  | (_____      | |  | | | | |_| | |   / ___ |___ |
 \______)_____|_(_/ \_)_____|  |_______)\_)_____)  \__)_|   \___/|_| |_|_|\____)___/   |_______)     |_|  |_| |_|\___/|_|   \_____(___/ 
""", bold=True)


def available_notes(value):
    total = value
    bank_note = [50, 20, 10, 1]
    while True:
        for note in bank_note:
            if total >= note:
                count = total // note
                total -= count * note
                print(f"Total de {count} cédulas de R${note}")
        break


def cash_machine():
    value = int(input("\nQue valor você quer sacar? R$"))
    available_notes(value)
    print(yellow("\nObrigado por utilizar nossos serviços".upper(), bold=True))


def screen():
    system("cls")
    print(logo)
    sleep(0.5)
    print(yellow("Bem vindo ao caixa eletrônico...".upper(), bold=True))
    cash_machine()


screen()