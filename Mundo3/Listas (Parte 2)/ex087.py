import os
from crayons import red, green, yellow, cyan

logo = cyan("""
  __  __       _        _             
 |  \/  |     | |      (_)        _   
 | \  / | __ _| |_ _ __ _ ____  _| |_ 
 | |\/| |/ _` | __| '__| |_  / |_   _|
 | |  | | (_| | |_| |  | |/ /    |_|  
 |_|  |_|\__,_|\__|_|  |_/___|        
""", bold=True)

os.system("cls")
print(logo)

headquarters = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
add_pairs = add_of_the_third_column = highest_value_of_the_second_line = 0

for row in range(3):
    for column in range(3):
        headquarters[row][column] = int(input(f"Digite um valor para [{row}, {column}]: "))
        if headquarters[row][column] % 2 == 0:
            add_pairs += headquarters[row][column]
        if headquarters[row][2] == headquarters[row][column]:
            add_of_the_third_column += headquarters[row][column]
        if headquarters[1][column] > highest_value_of_the_second_line:
            highest_value_of_the_second_line = headquarters[1][column]

print(cyan("\nMatriz: ", bold=True))

for row in range(3):
    for column in range(3):
        print(f"[ {headquarters[row][column]:^5} ]", end=" ")
    print()

print(f"\nA soma dos valores pares é {cyan(add_pairs, bold=True)}")
print("A soma dos valores da terceira coluna é ", end="")
print(f"{cyan(add_of_the_third_column, bold=True)}")
print("O maior valor da segunda linha é ", end="")
print(f"{cyan(highest_value_of_the_second_line, bold=True)}")