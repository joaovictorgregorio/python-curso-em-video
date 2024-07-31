from time import sleep
from crayons import green, red, yellow
from os import system

logo = yellow("""
 __    _     _            _        _____                     
|  |  |_|___| |_ ___    _| |___   |  _  |___ ___ ___ ___ ___ 
|  |__| |_ -|  _| .'|  | . | -_|  |   __|  _| -_|  _| . |_ -|
|_____|_|___|_| |__,|  |___|___|  |__|  |_| |___|___|___|___|
""")

system("cls")
print(logo + "\n")

product_price_list = (
    "Lápis", "1.75",
    "Borracha", "2.00",
    "Caderno", "15.90",
    "Estojo", "25.00",
    "Transferidor", "4.20",
    "Compasso", "9.99",
    "Mochila", "120.32",
    "Canetas", "22.30",
    "Livro", "34.90",
    "Caneta", "1.90",
    "Apontador", "3.50",
    "Quadro", "105.00"
    
)

for product in range(0, len(product_price_list)):
    if product % 2 == 0:
        print(f"{product_price_list[product]:.<30}", end="")
    else:
        print(green(f"R${product_price_list[product]:>7}"))