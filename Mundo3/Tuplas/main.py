from crayons import green, yellow, blue
from time import sleep
from os import system


system("cls")
# lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Bolo', 'Batata Frita')
"""
for comida in lanche:
    sleep(0.5)
    print(f"Eu vou comer {green(comida)}")
print(yellow("\nComi bastante!!!"))
"""

"""
for cont in range(0, len(lanche)):
    sleep(0.5)
    print(f"Eu vou comer {blue(lanche[cont], bold=True)} na posição {cont}")
sleep(0.5)
print(yellow(yellow("\nComi bastante hoje 🍔", bold=True)))
"""

"""
for posicao, comida in enumerate(lanche):
    sleep(0.5)
    print(f"Eu vou comer {yellow(comida, bold=True)}", end=" ")
    print(f"na posição {blue(posicao, bold=True)}")
sleep(0.5)
print(green("\nA comida estava muito boa!!!"))
"""

# print(sorted(lanche))
# print(lanche)

