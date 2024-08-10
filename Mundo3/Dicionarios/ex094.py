import os
import time
from crayons import red, green, yellow, blue, magenta, cyan

logo = blue("""
  ___  _    _                   _                _    _    _           
 |   \(_)__(_)___ _ _  __ _ _ _(_)___ ___  ___  | |  (_)__| |_ __ _ ___
 | |) | / _| / _ \ ' \/ _` | '_| / _ (_-< / -_) | |__| (_-<  _/ _` (_-<
 |___/|_\__|_\___/_||_\__,_|_| |_\___/__/ \___| |____|_/__/\__\__,_/__/
""", bold=True)

os.system('cls')
print(logo)

group_of_people = list()
person = dict()

while True:
    person['nome'] = str(input("\nNome: "))
    person['sexo'] = str(input("Sexo: [M/F] ")).strip().upper()[0]
    person['idade'] = int(input("Idade: "))
    group_of_people.append(person.copy())

    option = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if option == 'N':
        break

"""Imprimindo alguns dados sobre o grupo de pessoas"""
time.sleep(0.5)
print(f"\n-- O grupo tem {len(group_of_people)} pessoas.")
women = list()
add = 0
for person in group_of_people:
    add += person['idade']
    average_age = add / len(group_of_people)
    if person['sexo'] == 'F':
        women.append(person['nome'])
time.sleep(0.5)
print(f"-- A média de idade é de {average_age:.2f} anos.")
time.sleep(0.5)
print(f"-- As mulheres cadastradas foram: {women}")
time.sleep(0.5)
print("-- Lista de pessoas que estão acima da média:")
for person in group_of_people:
    if person['idade'] > average_age:
        time.sleep(0.5)
        print(f"nome = {person['nome']}; sexo = {person['sexo']}; idade = {person['idade']};")