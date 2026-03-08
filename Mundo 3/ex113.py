def leiaint(valor):
    """
    Lê um número inteiro com tratamento de erro.

    :param valor: Mensagem exibida no input.
    :return: Número inteiro informado pelo usuário, ou 0 em caso de interrupção.
    """
    while True:
        try:
            num = int(input(valor))
        except (ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um número INTEIRO válido\033[m")
        except KeyboardInterrupt:
            print("\033[31mO usuario optou por não digitar um número aqui\033[m")
            print("=" * 57)
            return 0
        else:
            print("=" * 57)
            return num

def leiafloat(valor):
    """
    Lê um número real com tratamento de erro.

    :param valor: Mensagem exibida no input.
    :return: Número real informado pelo usuário, ou 0 em caso de interrupção.
    """
    while True:
        try:
            num = float(input(valor))
        except (ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um número REAL válido\033[m")
        except KeyboardInterrupt:
            print("\033[31mO usuario optou por não digitar nada aqui\033[m")
            return 0
        else:
            return num


# Solicita ao usuário um número inteiro.
numero_inteiro = leiaint("Informe um valor inteiro: ")
# Solicita ao usuário um número real.
numero_real = leiafloat("Informe um valor real: ")

# Exibe um separador visual no terminal.
print("=" * 57)
# Mostra os valores capturados pelas funções de leitura segura.
print(f"O valor inteiro digitado foi {numero_inteiro}, e o valor real foi {numero_real}")
