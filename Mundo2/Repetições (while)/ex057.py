import os

logo = """\033[1;35m

 _     _       _  _     _                                _          ______            _            
(_)   (_)     | |(_)   | |                              | |        (______)          | |           
 _     _ _____| | _  __| |_____  ____ _____  ___      __| |_____    _     _ _____  __| | ___   ___ 
| |   | (____ | || |/ _  (____ |/ ___|____ |/ _ \    / _  | ___ |  | |   | (____ |/ _  |/ _ \ /___)
 \ \ / // ___ | || ( (_| / ___ ( (___/ ___ | |_| |  ( (_| | ____|  | |__/ // ___ ( (_| | |_| |___ |
  \___/ \_____|\_)_|\____\_____|\____)_____|\___/    \____|_____)  |_____/ \_____|\____|\___/(___/ 
                                                                                                   

\033[m"""

def screen():
    os.system("cls")
    print(logo)


screen()

loop = False
while loop == False:
    sexo = str(input("Digite seu sexo [M/F]: ")).strip().upper()[0] # Pega apenas a primeira letra
    if sexo in "MF":
        loop = True
        if sexo == "M":
            print("Sexo masculino registrado com sucesso!")
        else:
            print("Sexo feminino registrado com sucesso!")
    else:
        print("Opção inválida. Tente novamente.")
        


