import os
from crayons import red, green, yellow

logo = yellow("""
 __    _     _          _____                           _____                           
|  |  |_|___| |_ ___   |  _  |___ ___ ___ ___    ___   |     |_____ ___ ___ ___ ___ ___ 
|  |__| |_ -|  _| .'|  |   __| .'|  _| -_|_ -|  | -_|  |-   -|     | . | .'|  _| -_|_ -|
|_____|_|___|_| |__,|  |__|  |__,|_| |___|___|  |___|  |_____|_|_|_|  _|__,|_| |___|___|
                                                                   |_|                  
""")

os.system("cls")
print(logo)

main_list = [[], []]

for number in range(7):
    temporary_number = int(input(f"Digite o {number + 1}º número: "))
    if temporary_number % 2 == 0:
        main_list[0].append(temporary_number)
    else:
        main_list[1].append(temporary_number)

main_list[0].sort()
main_list[1].sort()
print(f"\nOs números pares digitados foram: {main_list[0]}")
print(f"Os números ímpares digitados foram: {main_list[1]}")