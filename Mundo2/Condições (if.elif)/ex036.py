import os

def clear_console():
    os.system('cls')

clear_console()

def menu():
    print('\033[1;34;40m-=\033[m' * 30)
    print('\033[1;34;40mEmpréstimo\033[m \033[1;33;40mbancário\033[m')
    print('\033[1;33;40m-=\033[m' * 30)

    home_value = float(input('Digite o valor da casa: R$ '))
    buyer_salary = float(input('Digite o salário do comprador: R$ '))
    years_to_pay = int(input('Digite em quantos anos vai pagar: '))

    calculation_of_benefit(home_value, buyer_salary, years_to_pay)


def calculation_of_benefit(home_value, buyer_salary, years_to_pay):
    calculation_of_benefit = (home_value / years_to_pay) / 12

    print('\033[1;32;40m\nEMPRÉSTIMO APROVADO!\033[m' if (buyer_salary * 0.30) >= (calculation_of_benefit) else '\033[1;31;40m\nEMPRÉSTIMO RECUSADO!\033[m')

menu()
