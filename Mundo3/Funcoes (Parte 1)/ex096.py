import os
import time
from crayons import red, green, yellow, blue, magenta, cyan

logo = red("""
   ___      _         _              _                
  / __|__ _| |__ _  _| |__ _ _ _    /_\  _ _ ___ __ _ 
 | (__/ _` | / _| || | / _` | '_|  / _ \| '_/ -_) _` |
  \___\__,_|_\__|\_,_|_\__,_|_|   /_/ \_\_| \___\__,_|
""", bold=True)

os.system("cls")
print(logo)


def main():
    def calcular_area(largura, comprimento):
        area = largura * comprimento
        print(f"\nA área do terreno {largura}x{comprimento} é de {area}m².")

    time.sleep(0.5)
    print("Controle de Terrenos\n".upper())
    largura = float(input("LARGURA (m): "))
    comprimento = float(input("COMPRIMENTO (m): "))
    calcular_area(largura, comprimento)


main()
