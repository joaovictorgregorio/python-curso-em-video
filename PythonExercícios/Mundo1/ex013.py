import os

def clear_console():
    os.system('cls')

clear_console()

salary = float(input('Qual é o salário do funcionário? R$'))
increase = salary * 0.15
print('Uma funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salary, (increase + salary)))