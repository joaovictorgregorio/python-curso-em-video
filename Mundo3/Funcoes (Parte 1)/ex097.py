import os
import time
from crayons import red, green, yellow, blue, magenta, cyan

logo = blue("""
  ___     _     _     ___                 _      _ 
 | _ \_ _(_)_ _| |_  | __|____ __  ___ __(_)__ _| |
 |  _/ '_| | ' \  _| | _|(_-< '_ \/ -_) _| / _` | |
 |_| |_| |_|_||_\__| |___/__/ .__/\___\__|_\__,_|_|
                            |_|                    
""", bold=True)

os.system("cls")
print(logo)


def escreva(txt):
    print("~" * (len(txt) + 4))
    print(f"  {txt}")
    print("~" * (len(txt) + 4))


escreva("Olá, Mundo!")
escreva("João Victor Gregorio da Silva")
escreva("Curso")
escreva("Pi")