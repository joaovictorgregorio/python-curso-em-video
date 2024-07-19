from time import sleep
import os

def clear_console():
    os.system('cls')

clear_console()

def screen():
    print('\033[1;36;40m+-\033[m' * 25)
    print('\033[1;36;40mANALISANDO TRIÂNGULOS\033[m')
    print('\033[1;36;40m+-\033[m' * 25)

    straight_one = float(input('Digite a primeira reta: '))
    straight_two = float(input('Digite a segunda reta: '))
    straight_three = float(input('Digite a terceira reta: '))
    forming_triangle(straight_one, straight_two, straight_three)

def forming_triangle(straight_one, straight_two, straight_three):
    print('\033[1;36;40m\nANALISANDO...\033[m')
    sleep(2)

    if (
        (straight_one + straight_two > straight_three) and 
        (straight_one + straight_three > straight_two) and 
        (straight_two + straight_three > straight_one)
    ):
        print('\033[1;32;40m\nAs retas formam um triângulo!\033[m')
        if straight_one == straight_two == straight_three:
            print('O triângulo é \033[1;34;40mEQUILÁTERO\033[m')
        elif straight_one != straight_two and straight_two != straight_three and straight_one != straight_three:
            print('O triângulo é \033[1;34;40mESCALENO\033[m')
        else:
            print('O triângulo é \033[1;34;40mISÓSCELES\033[m')
    else:
        print('\033[1;31;40m\nAs retas não formam um triângulo!\033[m')

screen()