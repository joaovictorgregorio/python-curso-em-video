from time import sleep
from os import system
from crayons import cyan, red

main_logo = cyan("""
 ______        _          _    _        _    _                                             _____                   _         _              
(______) ____ (_)_       (_)_ (_) ____ (_)_ (_)              ____      ____               (_____)  _              (_)       (_)_       ____ 
(_)__   (____)(___) ____ (___) _ (____)(___) _    ___  ____ (____)    (____)  __   __     (_)__(_)(_)__  ___    __(_) _   _ (___) ___ (____)
(____)  (_)__ (_)  (____)(_)  (_)(_)__ (_)  (_) _(___)(____)(_)__    (_)_(_) (__)_(__)    (_____) (____)(___)  (____)(_) (_)(_)  (___)(_)__ 
(_)____  _(__)(_)_( )_( )(_)_ (_) _(__)(_)_ (_)(_)___( )_( ) _(__)   (__)__ (_) (_) (_)   (_)     (_)  (_)_(_)(_)_(_)(_)_(_)(_)_(_)_(_)_(__)
(______)(____) (__)(__)_) (__)(_)(____) (__)(_) (____)(__)_)(____)    (____)(_) (_) (_)   (_)     (_)   (___)  (____) (___)  (__)(___)(____)
""", bold=True)

secondary_logo = cyan("""
                                                              
 _____         _        _____     _             _             
|  _  |___ ___| |___   |     |___| |_ ___ ___ _| |_ _ _ _ ___ 
|     | . | . | | -_|  |   --| .'|  _| .'|   | . | | | | | .'|
|__|__|  _|  _|_|___|  |_____|__,|_| |__,|_|_|___|___|\_/|__,|
      |_| |_|                                                 
""")


def screen():
    system("cls")
    sleep(0.5)
    print(main_logo)
    sleep(0.5)
    print(secondary_logo)
    sleep(0.5)
    print(cyan("Bem vindo a nossa loja....\n".upper(), bold=True))
    register_purchased_products()


total_purchased = []
products_over_one_thousand = []
cheapest_product = []
purchased_products = []


def register_purchased_products():
    print(cyan("\nCadastre um novo produto".upper(), bold=True))

    name_product = input("Nome do produto: ").strip()
    purchased_products.append(name_product)

    price_product = float(input("Preço: R$"))
    if price_product > 1000:
        products_over_one_thousand.append(price_product)
        total_purchased.append(price_product)
    else:
        total_purchased.append(price_product)

    while True:
        continue_register = input("Quer continuar? [S/N] ").strip().upper()
        if continue_register == "N":
            sleep(1)
            print(cyan("\nFinalizando...".upper(), bold=True))
            sleep(0.5)
            print(f"Total da compra foi R${sum(total_purchased):.2f}")
            if len(products_over_one_thousand) == 0:
                print("Não tem produtos custando mais de R$1000.00")
            elif len(products_over_one_thousand) == 1:
                print("Tem 1 produto custando mais de R$1000.00")
            else:
                print(f"Tem {len(products_over_one_thousand)}", end=" ")
                print("produtos custando mais de R$1000.00")
            print(f"O produto mais barato foi", end=" ")
            print(f"{purchased_products[total_purchased.index(min(total_purchased))]}", end=" ")
            print(f"que custou R${min(total_purchased):.2f}")
            exit()
        elif continue_register == "S":
            register_purchased_products()
        else:
            print(red("Opção inválida. Tente novamente.", bold=True))
            sleep(0.8)
            print("\033[F\033[K", end="")


screen()