from banner import logo
from verificacao import site_acessivel
import os

os.system("cls")
print(logo)

site = input("Digite o site que deseja acessar: ")
site_acessivel(site)
