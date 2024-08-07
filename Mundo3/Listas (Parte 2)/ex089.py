import os
import time
from crayons import yellow, green, red, blue, magenta, cyan

logo = red("""
 ______        _            _       
(____  \      | |      _   (_)      
 ____)  ) ___ | | ____| |_  _ ____  
|  __  ( / _ \| |/ _  )  _)| |    \ 
| |__)  ) |_| | ( (/ /| |__| | | | |
|______/ \___/|_|\____)\___)_|_|_|_|
""", bold=True)

os.system("cls")
print(logo)

students = []

while True:
    name = str(input("\nNome: ")).strip().title()
    students.append([name, [], []])
    note1 = float(input("Nota 1: "))
    note2 = float(input("Nota 2: "))
    option = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
    if option == "N":
        break

print(f"\n{yellow('No.')} {green('Nome')} {blue('Média')}")
for i, student in enumerate(students):
    average = (student[1][0] + student[1][1]) / 2
    print(f"{i + 1:<3} {student[0]:<10} {average:.1f}")


    
    