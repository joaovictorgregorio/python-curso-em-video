from crayons import yellow, red, green, cyan
import time
import os

logo = cyan("""                                                     
 _____     _                    _____     _             
|  |  |___| |___ ___ ___ ___   |  |  |___|_|___ ___ ___ 
|  |  | .'| | . |  _| -_|_ -|  |  |  |   | |  _| . |_ -|
 \___/|__,|_|___|_| |___|___|  |_____|_|_|_|___|___|___|                                                       
""", bold=True)

os.system("cls")
print(logo)

user_values = list()

while True:
    value = int(input("Digite um valor: "))
    if value < 0:
        print(red("Valor inválido! Digite um valor positivo.", bold=True))
        time.sleep(1.5)
        print("\033[F\033[K")
    else:
        if value not in user_values:
            print(green("Valor adicionado com sucesso!", bold=True))
            user_values.append(value)
        else:
            print(yellow("Valor duplicado! Não vou adicionar..."))
        time.sleep(1.5)
        print("\033[F\033[K")
    
    while True:
        option = input("Quer continuar? [S/N] ").strip().upper()[0]
        if option in "S":
            break
        elif option in "N":
            time.sleep(1)
            user_values.sort()
            print(f"\nVocê digitou: {(cyan(user_values, bold=True))}")
            exit()
        else:
            print(red("Opção inválida! Tente novamente.", bold=True))
            time.sleep(1.5)
            print("\033[F\033[K")
