import os
import time
from datetime import datetime
from crayons import red, green, yellow, blue, magenta, cyan

logo = cyan("""
   ____          _           _                ____ _____ ____  ____  
  / ___|__ _  __| | __ _ ___| |_ _ __ ___    / ___|_   _|  _ \/ ___| 
 | |   / _` |/ _` |/ _` / __| __| '__/ _ \  | |     | | | |_) \___ \ 
 | |__| (_| | (_| | (_| \__ \ |_| | | (_) | | |___  | | |  __/ ___) |
  \____\__,_|\__,_|\__,_|___/\__|_|  \___/   \____| |_| |_|   |____/ 
""", bold=True)

os.system("cls")
print(logo)

worker = dict()

worker['nome'] = str(input("Nome: ").strip())
worker['idade'] = datetime.now().year - int(input("Ano de nascimento: ").strip())
worker['ctps'] = int(input("Carteira de trabalho (0 não tem): ").strip())
if worker['ctps'] != 0:
    worker['contratação'] = int(input("Ano de contratação: ").strip())
    worker['salário'] = float(input("Salário: R$").strip())
    worker['aposentadoria'] = worker['idade'] + ((worker['contratação'] + 35) - datetime.now().year)
else:
    worker['ctps'] = 0

print("-=" * 30)
print(worker)
print("-=" * 30)

for key, value in worker.items():
    time.sleep(0.5)
    print(f"{cyan(key, bold=True)} tem o valor {yellow(value, bold=True)}")