import os
from crayons import red, green, yellow, magenta
import time

logo = magenta("""
 _     _     _                                              _        
| |   (_)   | |                                            | |       
| |    _ ___| |_ __ _    ___ ___  _ __ ___  _ __   ___  ___| |_ __ _ 
| |   | / __| __/ _` |  / __/ _ \| '_ ` _ \| '_ \ / _ \/ __| __/ _` |
| |___| \__ \ || (_| | | (_| (_) | | | | | | |_) | (_) \__ \ || (_| |
\_____/_|___/\__\__,_|  \___\___/|_| |_| |_| .__/ \___/|___/\__\__,_|
                                           | |                       
                                           |_|                       
""", bold=True)

os.system("cls")
print(logo)

temporary_list = []
main_list = []
greater_weight = lower_weight = 0

while True:
    temporary_list.append(str(input("\nNome: ")).strip().title())
    temporary_list.append(float(input("Peso: ")))
    main_list.append(temporary_list[:])
    temporary_list.clear()
    if len(main_list) == 1:
        greater_weight = lower_weight = main_list[0][1]
    else:
        if main_list[-1][1] > greater_weight:
            greater_weight = main_list[-1][1]
        if main_list[-1][1] < lower_weight:
            lower_weight = main_list[-1][1]
    while True:
        option = input("Quer continuar? [S/N] ").strip().upper()[0]
        if option in "S":
            break
        elif option in "N":
            print(f"Ao todo foram cadastrados {len(main_list)} pessoas")
            print(f"O maior peso foi de {greater_weight}Kg. Peso de ", end="")
            for people in main_list:
                if people[1] == greater_weight:
                    print(f"[{people[0]}]", end=" ")
            print(f"\nO menor peso foi de {lower_weight}Kg. Peso de ", end="")
            for people in main_list:
                if people[1] == lower_weight:
                    print(f"[{people[0]}]", end=" ")
            exit()
        else:
            print(red("Opção inválida! Tente novamente.", bold=True))
            time.sleep(1.5)
            print("\033[F\033[K")