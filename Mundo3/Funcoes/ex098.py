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
    for i in range(11):
        time.sleep(0.2)
        print(i, end=" ")

    print(cyan("\nContagem de 10 até  0, de 2 em 2:"))
    for i in range(10, -1, -2):
        time.sleep(0.2)
        print(i, end=" ")


contador()