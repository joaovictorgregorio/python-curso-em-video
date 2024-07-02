import os

def clear_console():
    os.system('cls')

clear_console()

salary = float(input('Digite o salário: R$ '))
if salary > 1250.00:
    new_salary = salary + (salary * 0.10)
    print('Você ganhou um aumento de 10%, seu novo salário é de: R$ {:.2f}'.format(new_salary))
else:
    new_salary = salary + (salary * 0.15)
    print('Você ganhou um aumento de 15%, seu novo salário é de: R$ {:.2f}'.format(new_salary))