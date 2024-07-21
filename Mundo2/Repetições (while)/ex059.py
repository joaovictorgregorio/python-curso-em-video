import os, time

logo = """\033[1;31m
 ___ ___    ___  ____   __ __      ___      ___       ___   ____    __   ___     ___  _____
|   T   T  /  _]|    \ |  T  T    |   \    /  _]     /   \ |    \  /  ] /   \   /  _]/ ___/
| _   _ | /  [_ |  _  Y|  |  |    |    \  /  [_     Y     Y|  o  )/  / Y     Y /  [_(   \_ 
|  \_/  |Y    _]|  |  ||  |  |    |  D  YY    _]    |  O  ||   _//  /  |  O  |Y    _]\__  T
|   |   ||   [_ |  |  ||  :  |    |     ||   [_     |     ||  | /   \_ |     ||   [_ /  \ |
|   |   ||     T|  |  |l     |    |     ||     T    l     !|  | \     |l     !|     T\    |
l___j___jl_____jl__j__j \__,_j    l_____jl_____j     \___/ l__j  \____j \___/ l_____j \___j

\033[m"""

def add(value_one, value_two):
    return value_one + value_two

def multiply(value_one, value_two):
    return value_one * value_two

def menu():
    os.system("cls")
    print(logo)

    
    value_one = int(input("Digite o primeiro valor: "))
    value_two = int(input("Digite o segundo valor: "))

    option = 0

    while option != 5:
        time.sleep(1)
        print("\033[1;31m\n[1]\033[m Somar" +
            "\033[1;31m\n[2]\033[m Multiplicar" +
            "\033[1;31m\n[3]\033[m Maior" +
            "\033[1;31m\n[4]\033[m Novos números" +
            "\033[1;31m\n[5]\033[m Sair do programa\033[m")
        
        option = int(input("\nDigite uma opção: "))
        if option == 1:
            print(f"A soma entre {value_one} + {value_two} = {add(value_one, value_two)}")
        elif option == 2:
            print(f"A multiplicação entre {value_one} * {value_two} = {multiply(value_one, value_two)}")
        elif option == 3:
            print(f"O maior valor entre {value_one} e {value_two} é: {max(value_one, value_two)}")
        elif option == 4:
            menu()
        elif option == 5:
            time.sleep(1)
            print("\033[1;33m\nPrograma encerrado!!!\033[m")
            exit()
        else:
            print("\033[1;31mOpção inválida!!! Tente novamente...\033[m")
            time.sleep(1)


menu()