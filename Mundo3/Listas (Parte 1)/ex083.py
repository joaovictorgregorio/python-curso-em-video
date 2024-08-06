import time
import os
from crayons import yellow, red, green, blue

logo = blue("""
   __                                          
  /__\_  ___ __  _ __ ___  ___ ___  __ _  ___  
 /_\ \ \/ / '_ \| '__/ _ \/ __/ __|/ _` |/ _ \ 
//__  >  <| |_) | | |  __/\__ \__ \ (_| | (_) |
\__/ /_/\_\ .__/|_|  \___||___/___/\__,_|\___/ 
          |_|                                                        
""", bold=True)

os.system("cls")
print(logo)

expression = str(input("Digite a expressão: "))
if expression.count("(") == expression.count(")"):
    print(green("Sua expressão está correta!", bold=True))
else:
    print(red("Sua expressão está errada!", bold=True))