import urllib
import urllib.request


def site_acessivel(site):
    from crayons import green, red

    try:
        site = urllib.request.urlopen(site)
    except urllib.error.URLError:
        print(red("O site não está acessível no momento.", bold=True))
    else:
        print(green("Consegui acessar o site com sucesso!", bold=True))
        # print(site.read()) retorna o código html do site
