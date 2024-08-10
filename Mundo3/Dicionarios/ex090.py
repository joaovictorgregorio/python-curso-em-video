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

student['nome'] = input("Nome: ")
student['media'] = float(input(f"Média de {student['nome']}: "))
if student['media'] >= 7:
    student['situacao'] = green("Aprovado(a)", bold=True)
elif 5 <= student['media'] < 7:
    student['situacao'] = yellow("Recuperação", bold=True)
else:
    student['situacao'] = red("Reprovado(a)", bold=True)

print(yellow("\n" + "-=" * 20))
for key, value in student.items():
    time.sleep(0.3)
    print(f"  -- {key.capitalize()} é igual a {value}")
