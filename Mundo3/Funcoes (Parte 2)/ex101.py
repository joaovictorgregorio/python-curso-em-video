import os
from crayons import red, green, yellow

logo = green("""
             _                
 /\   /\___ | |_ __ _  ___ __ _  ___  
 \ \ / / _ \| __/ _` |/ __/ _` |/ _ \ 
  \ V / (_) | || (_| | (_| (_| | (_) |
   \_/ \___/ \__\__,_|\___\__,_|\___/ 
""", bold=True)

os.system("cls")
print(logo)


def voto(ano_nascimento):
    from time import sleep
    from datetime import datetime
    """
    -> Função que verifica se a pessoa pode votar ou não.
    :param ano_nascimento: Ano de nascimento da pessoa
    :return: Retorna se a pessoa pode votar ou não
    """
    idade = datetime.now().year - ano_nascimento
    if idade < 16:
        sleep(0.3)
        return f"\nCom {idade} anos: " + red("NÃO VOTA.", bold=True)
    elif 16 <= idade < 18 or idade >= 65:
        sleep(0.3)
        return f"\nCom {idade} anos: " + yellow("VOTO OPCIONAL.", bold=True)
    else:
        sleep(0.3)
        return f"\nCom {idade} anos: " + green("VOTO OBRIGATÓRIO.", bold=True)


ano_nascimento = int(input("Em que ano você nasceu? "))
print(voto(ano_nascimento))
