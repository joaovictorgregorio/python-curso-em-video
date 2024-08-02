from crayons import yellow, red, green, cyan
import time
import os

logo = yellow("""                                                        
 __    _     _          _____       _               _     
|  |  |_|___| |_ ___   |     |___ _| |___ ___ ___ _| |___ 
|  |__| |_ -|  _| .'|  |  |  |  _| . | -_|   | .'| . | .'|
|_____|_|___|_| |__,|  |_____|_| |___|___|_|_|__,|___|__,|
""", bold=True)

os.system("cls")
print(logo)

user_numbers = list() # Lista vazia

for number in range(5):
    value = int(input("\nDigite um valor: "))
    if number == 0 or value > user_numbers[-1]:
        user_numbers.append(value)
        print(yellow("Valor adicionado ao final da lista!", bold=True))
    else:
        position = 0
        while position < len(user_numbers):
            if value <= user_numbers[position]:
                user_numbers.insert(position, value)
                print(f"Valor adicionado na posição {yellow(position)}")
                break
            position += 1

print(f"\nOs valores digitados em ordem foram: {yellow(user_numbers)}")