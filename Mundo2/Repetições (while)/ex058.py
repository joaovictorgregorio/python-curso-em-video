import os, time, random

logo = """\033[1;32m

   _____                        _                     _ _       _       _                                    ______    ______ 
  (_____)                      | |           /\      | (_)     (_)     | |                                  (_____ \  / __   |
     _  ___   ____  ___      _ | | ____     /  \   _ | |_ _   _ _ ____ | | _   ____  ____ ____  ___     _   _ ____) )| | //| |
    | |/ _ \ / _  |/ _ \    / || |/ _  |   / /\ \ / || | | | | | |  _ \| || \ / _  |/ ___) _  |/ _ \   | | | /_____/ | |// | |
 ___| | |_| ( ( | | |_| |  ( (_| ( ( | |  | |__| ( (_| | |\ V /| | | | | | | ( ( | ( (__( ( | | |_| |   \ V /_______ |  /__| |
(____/ \___/ \_|| |\___/    \____|\_||_|  |______|\____|_| \_/ |_|_| |_|_| |_|\_||_|\____)_||_|\___/     \_/(_______|_)_____/ 
            (_____|                                                                                                           

\033[m"""


def screen():
    os.system("cls")
    print(logo)
    print("Muito prazer em te conhecer, eu sou seu computador... 💻")
    time.sleep(0.3)
    print("Acabei de pensar em um número entre \033[1;32m0\033[m e \033[1;32m10\033[m.")
    time.sleep(0.3)
    print("Será que você consegue adivinhar qual foi? ")
    time.sleep(0.3)

screen()

computer_number = random.randint(1, 10)
user_number = 0

loop = True
attempts = 0
while loop == True:
    user_number = int(input("\nQual o seu palpite? "))
    attempts += 1
    if user_number == computer_number:
        loop = False
        print(f"\nParabéns, você adivinhou o número é o \033[1;32m{computer_number}\033[m")
    elif user_number < computer_number:
        print("\033[1;33mMais... Tente novamente.\033[m")
    else:
        print("\033[1;33mMenos... Tente novamente.\033[m")
        

if attempts == 1:
    print(f"Impressionante, você conseguiu adivinhar com apenas {attempts} tentativa 😱")
else:
    print(f"Você conseguiu adivinhar o número com {attempts} tentativas. 🫡")


