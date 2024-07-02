import os

def clear_console():
    os.system('cls')

clear_console()


def scren():
    print('\033[1;37;40m+-\033[m' * 25)
    print('\033[1;31;40mSISTEMA DE APROVAÇÃO\033[m \033[1;37;40mPARA O PRÓXIMO ANO\033[m')
    print('\033[1;31;40m+-\033[m' * 25)

    note_one = float(input('\nDigite a primeira nota: '))
    note_two = float(input('Digite a segunda nota: '))
    average(note_one, note_two)
    
def average(note_one, note_two):
    
    average = (note_one + note_two) / 2.0

    if average < 5.0:
        print(f'\nSua média foi de {average:.1f} e você está \033[1;31;40mREPROVADO\033[m.')
    elif average >= 5.0 and average <= 6.9:
        print(f'\nSua média foi de {average:.1f} e você está \033[1;33;40mRECUPERAÇÃO\033[m.')
    else:
        print(f'\nSua média foi de {average:.1f} e você está de \033[1;32;40mAPROVADO\033[m.')

scren()