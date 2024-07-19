import os

def clear_console():
    os.system('cls')

clear_console()

number_one = int(input('Digite o primeiro número: '))
number_two = int(input('Digite o segundo número: '))
number_three = int(input('Digite o terceiro número: '))

bigger = max(number_one, number_two, number_three)
smaller = min(number_one, number_two, number_three)

print('O maior número é {}'.format(bigger))
print('O menor número é {}'.format(smaller))