import os
from crayons import yellow, blue

logo = blue("""
 __   __  _______  _______  ______    ___   _______ 
|  |_|  ||   _   ||       ||    _ |  |   | |       |
|       ||  |_|  ||_     _||   | ||  |   | |____   |
|       ||       |  |   |  |   |_||_ |   |  ____|  |
|       ||       |  |   |  |    __  ||   | | ______|
| ||_|| ||   _   |  |   |  |   |  | ||   | | |_____ 
|_|   |_||__| |__|  |___|  |___|  |_||___| |_______|
""", bold=True)

os.system("cls")
print(logo)

headquarters = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for row in range(3):
    for column in range(3):
        headquarters[row][column] = int(input(f"Digite um valor para [{row}, {column}]: "))

for row in range(3):
    for column in range(3):
        print(f"[ {headquarters[row][column]:^5} ]", end=" ")
    print()