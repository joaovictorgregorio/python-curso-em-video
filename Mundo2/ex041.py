from datetime import date
from time import sleep
import os

def clear_console():
    os.system('cls')

clear_console()


def scren():
    print('\033[1;37;40m+-\033[m' * 25)
    print('\033[1;35;40mCLASSIFICANDO\033[m \033[1;37;40mATLETAS\033[m')
    print('\033[1;35;40m+-\033[m' * 25)

    year_birthday = int(input('\nDigite o ano de nascimento: '))
    category_validation(year_birthday)

def category_validation(year_birthday):
    current_year = date.today().year

    print('\n\033[1;35;40mPROCESSANDO...\033[m')
    sleep(2)

    if (current_year - year_birthday) <= 9:
        print('\nO atleta está na categoria \033[1;34;40mMIRIM\033[m.')
    elif (current_year - year_birthday) <= 14:
        print('\nO atleta está na categoria \033[1;34;40mINFANTIL\033[m.')
    elif (current_year - year_birthday) <= 19:
        print('\nO atleta está na categoria \033[1;34;40mJÚNIOR\033[m.')
    elif (current_year - year_birthday) == 20:
        print('\nO atleta está na categoria \033[1;34;40mSÊNIOR\033[m.')
    else:
        print('\nO atleta está na categoria \033[1;34;40mMASTER\033[m.')

scren()

