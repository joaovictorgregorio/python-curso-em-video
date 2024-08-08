import os

os.system("cls")

people = {
    "name": "John",
    "gender": 'M',
    "age": 22,
    "city": "New York"
}

print(f"O {people['name']} tem {people['age']} anos")
print("\n")

# Apagando a chave "city" do dicionário
del people["city"]

# Adicionado a chave "city" com valor "New York"
people["city"] = "Los Angeles"

print(people.items())
print("\n")

for key in people.keys():
    print(f"{key}")
print("\n")

for value in people.values():
    print(f"{value}")
print("\n")

for key, value in people.items():
    print(f"{key} = {value}")
print("\n")

# Dicionário dentro de lista
brasil = []
estado1 = {"uf": "Rio de Janeiro", "sigla": "RJ"}
estado2 = {"uf": "São Paulo", "sigla": "SP"}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[1]['sigla'])
print("\n")

estado = dict()
brasil = list()
for item in range(3):
    estado['uf'] = str(input("Unidade Federativa: "))
    estado['sigla'] = str(input("Sigla do Estado: "))
    brasil.append(estado.copy())
print(brasil)
print("\n")

for e in brasil:
    for v in e.values():
        print(v, end=" ")
    print()