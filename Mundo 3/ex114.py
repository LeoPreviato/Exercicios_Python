import urllib.request
import urllib.error

def verificar_site(url):
    """
    Verifica se um site está acessível.

    :param url: Endereço do site a ser testado.
    :return: True se o site responder, False em caso de erro de acesso.
    """
    try:
        urllib.request.urlopen(url)
    except urllib.error.URLError:
        return False
    else:
        return True

# Testa a conectividade com o site informado.
if verificar_site("https://www.python.org"):
    # Mensagem exibida quando o site está acessível.
    print("\033[32mConsegui acessar o site 'Pudim' com sucesso.\033[m")
else:
    # Mensagem exibida quando o site não está acessível.
    print("\033[31mO site 'Pudim' não esta acessivel no momento.\033[m")
