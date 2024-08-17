import os
import time
from crayons import red, green, yellow, blue, magenta, cyan

logo = green("""
 _____             _            _                    
/  __ \           | |          | |               _   
| /  \/ ___  _ __ | |_ __ _  __| | ___  _ __   _| |_ 
| |    / _ \| '_ \| __/ _` |/ _` |/ _ \| '__| |_   _|
| \__/\ (_) | | | | || (_| | (_| | (_) | |      |_|  
 \____/\___/|_| |_|\__\__,_|\__,_|\___/|_|           
""", bold=True)

os.system("cls")
print(logo)


def contador():
    print(yellow("Contagem de 1 até 10, de 1 em 1: ", bold=True))
    time.sleep(1)
    for i in range(10):
        time.sleep(0.3)
        print(i+1, end=" ", flush=True)
    print(yellow("FIM...", bold=True))

    print(cyan("\n\nContagem de 10 até  0, de 2 em 2:", bold=True))
    time.sleep(1)
    for i in range(10, -1, -2):
        time.sleep(0.3)
        print(i, end=" ", flush=True)
    print(cyan("FIM...", bold=True))

    print(magenta("\n\nAgora é a sua vez de personalizar a contagem!", bold=True))
    time.sleep(1)
    inicio = int(input("Início: "))
    fim = int(input("Fim: "))
    passo = abs(int(input("Passo: ")))

    if passo == 0:
        passo = 1

    print("\n" + "*" * 45)
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
    time.sleep(1)
    for i in range(inicio, fim + 1, passo):
        time.sleep(0.3)
        print(i, end=" ", flush=True)
    if inicio > fim:
        for i in range(inicio, fim - 1, -passo):
            time.sleep(0.3)
            print(i, end=" ", flush=True)
    print(magenta("FIM...", bold=True))


contador()
