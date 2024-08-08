import os
import time
from crayons import red, green, yellow, blue, magenta, cyan

logo = yellow("""                                                 
 ____  _     _                 _        _____     _   _           
|    \|_|___|_|___ ___ ___ ___|_|___   |  _  |_ _| |_| |_ ___ ___ 
|  |  | |  _| | . |   | .'|  _| | . |  |   __| | |  _|   | . |   |
|____/|_|___|_|___|_|_|__,|_| |_|___|  |__|  |_  |_| |_|_|___|_|_|
                                             |___|                
""")

os.system("cls")
time.sleep(0.5)
print(logo)

student = dict()

student['name'] = input("Nome: ")
student['media'] = float(input(f"Média de {student['name']}: "))

print(f"\nNome é igual a {yellow(student['name'], bold=True)}")
print(f"Média é igual a {blue(student['media'], bold=True)}")
if student['media'] >= 7:
    print(f"Situação é igual a {green('Aprovado', bold=True)}")
else:
    print(f"Situação é igual a {red('Reprovado', bold=True)}")