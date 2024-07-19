from time import sleep
import os

def clear_console():
    os.system('cls')

clear_console()

def menu():
    print('\033[1;32;40m+-\033[m' * 25)
    print('\033[1;32;48mGERENCIADOR DE PAGAMENTOS\033[m')
    print('\033[1;32;40m+-\033[m' * 25)
    sleep(0.3)
    print('\033[1;33;40m\n1 - Pagamento à vista dinheiro/cheque\033[m')
    sleep(0.3)
    print('\033[1;33;40m2 - Pagamento à vista cartão\033[m')
    sleep(0.3)
    print('\033[1;33;40m3 - Pagamento 2x no cartão\033[m')
    sleep(0.3)
    print('\033[1;33;40m4 - Pagamento 3x ou mais no cartão\033[m')
    sleep(0.3)

    option = int(input('\nEscolha uma opção: '))

    if (option < 1 or option > 4):
        print('\n\033[1;31;40mOpção inválida\033[m')
        sleep(0.5)
        clear_console()
        menu()

    payment_conditions(option)

def payment_conditions(option):
    product = float(input('Qual o valor do produto? R$'))

    if (option == 1):
        product_discount = product - (product * 0.1)
        print(f'\nO valor a ser pago é de \033[1;32;40mR${product_discount:.2f}\033[m')
    elif (option == 2):
        product_discount = product - (product * 0.05)
        print(f'\nO valor a ser pago é de \033[1;32;40mR${product_discount:.2f}\033[m')
    elif (option == 3):
        installment = product / 2
        print(f'\nO valor a ser pago é de \033[1;32;40mR${product:.2f}\033[m')
        print(f'O valor das parcelas é de \033[1;33;40mR${installment:.2f}\033[m')
    elif (option == 4):
        installment = int(input('Em quantas parcelas deseja pagar? '))
        additional_interest = product + (product * 0.2) 
        installment_value = additional_interest / installment
        print(f'\nO valor a ser pago é de \033[1;32;40mR${additional_interest:.2f}\033[m')
        print(f'O valor das parcelas é de \033[1;33;40mR${installment_value:.2f}\033[m')
    
menu()