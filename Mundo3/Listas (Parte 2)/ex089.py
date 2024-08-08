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

"""Inserção de dados dos alunos e verificação de continuidade do programa"""
token = []
while True:
    name = str(input("\nNome: ")).strip().title()
    note1 = float(input("Nota 1: "))
    note2 = float(input("Nota 2: "))
    average = (note1 + note2) / 2
    token.append([name, [note1, note2], average])
    option = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
    if option == "N":
        break

"""Mostra as informações dos alunas de forma tabular"""
print("\n" + red("-" * 26, bold=True))
print(f"{'No.':<4} {'NOME':<10} {'MÉDIA':>8}")
print(red("-" * 26, bold=True))
for i, student in enumerate(token):
    average = (student[1][0] + student[1][1]) / 2
    print(f"{i + 1:<4} {student[0]:<10} {student[2]:>8.1f}")

"""Mostra as notas de cada aluno individualmente"""
while True:
    option = int(input("\nMostrar notas de qual aluno? (999 interrompe): "))
    if option == 999:
        break
    if option <= len(token):
        print(f"Notas de {token[option - 1][0]} são {token[option - 1][1]}")
    else:
        print(red("Opção inválida. Tente novamente.", bold=True))

print(yellow("\nPrograma finalizado...", bold=True))