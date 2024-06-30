from random import shuffle
import os

def clear_console():
    os.system('cls')

clear_console()

students = []

for i in range(4):
    student = input('Nome do {}º aluno: '.format(i+1))
    students.append(student) 

shuffle(students)

print('O aluno sorteado foi: {}'.format(students[0]))