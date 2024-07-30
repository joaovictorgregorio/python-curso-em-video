from crayons import green, red, yellow, cyan, blue
from os import system
from time import sleep

logo = red("""                                                                                             
 _____         _ _              _          _       _                                          _           _     
|  _  |___ ___| |_|___ ___    _| |___    _| |___ _| |___ ___    ___ _____    _ _ _____ ___   | |_ _ _ ___| |___ 
|     |   | .'| | |_ -| -_|  | . | -_|  | . | .'| . | . |_ -|  | -_|     |  | | |     | .'|  |  _| | | . | | .'|
|__|__|_|_|__,|_|_|___|___|  |___|___|  |___|__,|___|___|___|  |___|_|_|_|  |___|_|_|_|__,|  |_| |___|  _|_|__,|
                                                                                                     |_|        
""", bold=True)

system("cls")
print(logo)
print(red("Bem vindo ao programa....\n".upper()))

for count in range(0, 4):
    sleep(0.2)
    if count == 0:
        number1 = int(input("Digite um número: "))
    elif count == 1:
        number2 = int(input("Digite outro número: "))
    elif count == 2:
        number3 = int(input("Digite mais um número: "))
    else:
        number4 = int(input("Digite o último número: "))

values_entered = (number1, number2, number3, number4)

print(f"\nVocê digitou os valores: {yellow(values_entered)}")
print(f"O valor 9 apareceu {values_entered.count(9)} vezes")
print(f"O valor 3 apareceu na {values_entered.index(3)+1}ª posição" if 3
      in values_entered else "O valor 3 não foi digitado em nenhuma posição")
print(f"Os valores pares digitados foram: ", end="")
for value in values_entered:
    if value % 2 == 0:
        print(f"{yellow(value, bold=True)} ", end="")