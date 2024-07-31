from crayons import red, green, yellow, blue
from os import system
from time import sleep

logo = blue("""                                              
 _____         _                                        _     
|     |___ ___| |_ ___ ___ ___ _____    _ _ ___ ___ ___|_|___ 
|   --| . |   |  _| .'| . | -_|     |  | | | . | . | .'| |_ -|
|_____|___|_|_|_| |__,|_  |___|_|_|_|   \_/|___|_  |__,|_|___|
                      |___|                    |___|          
""", bold=True)


system("cls")
print(logo)

words = (
    "aprender", "programar", "linguagem", "python", "curso", "gratis",
    "estudar", "praticar", "trabalhar", "mercado", "programador", "futuro"
)

for word in words:
    print(f"\nNa palavra {yellow(word.upper(), bold=True)} temos ", end="")
    for letter in word:
        if letter.lower() in "aeiou":
            print(f"{blue(letter, bold=True)}", end=" ")