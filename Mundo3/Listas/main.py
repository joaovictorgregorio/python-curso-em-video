import os

os.system("cls")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Adicionando valor de forma manual na posição desejada
numbers[2] = 109
# Adicionando valor de forma automática na última posição
numbers.append(116)
# Colocando em ordem crescente
numbers.sort()
print(f"Lista em ordem crescente {numbers}")
# Colocando em ordem decrescente
numbers.sort(reverse=True)
print(f"\nLista em ordem decrescente {numbers}")

print(f"\nEssa lista tem {len(numbers)} elementos")

# Inserindo valor na posição desejada e também o valor desejada
numbers.insert(0, 0)
print(f"\nLista após inserção {numbers}")

# Removendo o último valor
numbers.pop()
print(f"\nLista após remoção do último valor {numbers}")

# Removendo um valor específico
numbers.remove(5)
print(f"\nLista após remoção do valor 5: {numbers}")

# Removendo um valor específico e testando se existe
print(numbers.remove(5) if 5 in numbers else "\nO valor 5 não foi encontrado")

# Criando uma lista com valores de 0 a 10
values = list(range(0, 11))
print(f"\nLista de valores: {values}\n")

# Adicionando valores em uma lista vazia e imprimindo a posição e o valor
new_values = list()
for value in range(0, 5):
    new_values.append(int(input(f"Digite um valor para a posição {value}: ")))

for key, value in enumerate(new_values):
    print(f"Índice: {key} Valor: {value}")
print("Finalizado..................")

a = [2, 3, 4, 7]
b = a[:]  # Cria uma cópia de A também da para usar a função A.copy()
b[2] = 8
print(f"\nLista A: {a}")
print(f"Lista B: {b}")