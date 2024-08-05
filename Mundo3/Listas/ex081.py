import time
import os
from crayons import yellow, red, green, blue

logo = red("""                                                            
 _____     _           _       _          _       _         
|   __|_ _| |_ ___ ___|_|___ _| |___    _| |___ _| |___ ___ 
|   __|_'_|  _|  _| .'| |   | . | . |  | . | .'| . | . |_ -|
|_____|_,_|_| |_| |__,|_|_|_|___|___|  |___|__,|___|___|___|                                                           
""", bold=True)

os.system("cls")
print(logo)

user_values = list() 

while True:
    value = int(input("\nDigite um valor: "))
    user_values.append(value)
    if value < 0:
        print(red("Valor inválido! Digite um valor positivo.", bold=True))
        user_values.pop()
        time.sleep(1.5)
        print("\033[F\033[K")
    while True:
        option = input("Quer continuar? [S/N] ").strip().upper()[0]
        if option in "S":
            break
        elif option not in "SN":
            print(red("Opção inválida! Tente novamente.", bold=True))
            time.sleep(1.5)
            print("\033[F\033[K")
        elif option in "N":
            time.sleep(1)
            print(f"\nVocê digitou {len(user_values)} elementos")
            user_values.sort(reverse=True)
            print(f"Os valores em ordem descrescente: {user_values}")
            if 5 in user_values:
                print(green(f"O valor 5 está na lista e na posição {user_values.index(5)}ª", bold=True))
            else:
                print(red("O valor 5 não está na lista", bold=True))
            exit()