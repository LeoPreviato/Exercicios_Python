"""Rotinas de entrada e validação de dados para o exercício 112."""

def leiaDinheiro(prompt=""):
    """
    Função que lê e valida a entrada de um valor monetário.

    :param prompt: mensagem exibida para solicitar o valor.
    :return: valor convertido para float.
    """
    while True:
        entrada = input(prompt).replace(",", ".").strip()
        if entrada.replace(".", "").isnumeric():
            valor = float(entrada)
            return valor
        else:
            print(f"\033[31mERRO: '{entrada}' é um preço invalido!\033[m")
