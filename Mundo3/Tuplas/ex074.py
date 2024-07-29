from crayons import magenta, yellow, green, blue, cyan, red
from os import system
from time import sleep
from random import randint

logo = green("""
                                                                                                                      
 _____     _                   _____                            _                                 _____         _     
|     |___|_|___ ___    ___   |     |___ ___ ___ ___    _ _ ___| |___ ___ ___ ___    ___ _____   |_   _|_ _ ___| |___ 
| | | | .'| | . |  _|  | -_|  | | | | -_|   | . |  _|  | | | .'| | . |  _| -_|_ -|  | -_|     |    | | | | | . | | .'|
|_|_|_|__,|_|___|_|    |___|  |_|_|_|___|_|_|___|_|     \_/|__,|_|___|_| |___|___|  |___|_|_|_|    |_| |___|  _|_|__,|
                                                                                                           |_|        
""", bold=True)

system("cls")
print(logo)
print(green("Bem vindo....".upper()))

random_number_tuple = (randint(0, 10), randint(0, 10), randint(0, 10),
                       randint(0, 10), randint(0, 10))

sleep(0.5)
print(f"\nOs valores sorteados foram: {random_number_tuple}")
sleep(0.5)
print(f"\nO maior valor sorteado foi {max(random_number_tuple)}")
sleep(0.5)
print(f"O menor valor sorteado foi {min(random_number_tuple)}")