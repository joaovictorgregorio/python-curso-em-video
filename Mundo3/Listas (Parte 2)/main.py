import os

os.system("cls")

teste = list()
teste.append("Gustavo")
teste.append(40)
print(teste)

"""Os dois pontos entre os colchetes são importantes para criar uma cópia da
lista, mantendo os dados coerentes"""
galera = list()
galera.append(teste[:])
teste[0] = "Maria"
teste[1] = 22
galera.append(teste[:])
print(galera)
print("\n")

galera = [["João", 19], ["Ana", 33], ["Joaquim", 13], ["Maria", 45]]
print(galera[0])
print(galera[0][0])
print(galera[1][1])
print(galera[2][1])
print(galera[3][0])
print(galera[3])
print("\n")

for people in galera:
    print(people)

print("\n")
for people in galera:
    print(f"{people[0]} tem {people[1]} anos de idade.")

print("\n")
galera = []
dado = []
for i in range(3):
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Idade: ")))
    galera.append(dado[:])
    dado.clear()

print(galera)
print("\n")

totmaior = totmenor = 0
for p in galera:
    if p[1] >= 21:
        print(f"{p[0]} é maior de idade.")
        totmaior += 1
    else:
        print(f"{p[0]} é menor de idade.")
        totmenor += 1

print(f"Temos {totmaior} maiores e {totmenor} menores de idade.")