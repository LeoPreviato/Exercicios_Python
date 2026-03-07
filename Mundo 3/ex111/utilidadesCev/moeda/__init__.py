"""Funções utilitárias para cálculos e formatação de valores monetários."""

def metade(num=0, formatar=False):
    """
    Função que calcula a metade de um valor.

    :param num: valor numérico informado.
    :param formatar: define se o retorno será formatado como moeda.
    :return: metade do valor, formatada ou não.
    """
    resultado = num / 2
    return moeda(resultado) if formatar else resultado

def dobro(num=0, formatar=False):
    """
    Função que calcula o dobro de um valor.

    :param num: valor numérico informado.
    :param formatar: define se o retorno será formatado como moeda.
    :return: dobro do valor, formatado ou não.
    """
    resultado = num * 2
    return moeda(resultado) if formatar else resultado

def aumento_porcentagem(num=0, porcen=0, formatar=True):
    """
    Função que aplica aumento percentual sobre um valor.

    :param num: valor numérico informado.
    :param porcen: percentual de aumento.
    :param formatar: define se o retorno será formatado como moeda.
    :return: valor com aumento aplicado, formatado ou não.
    """
    resultado = num + (num * porcen / 100)
    return moeda(resultado) if formatar else resultado

def reduzindo_porcentagem(num=0, porcen=0, formatar=False):
    """
    Função que aplica redução percentual sobre um valor.

    :param num: valor numérico informado.
    :param porcen: percentual de redução.
    :param formatar: define se o retorno será formatado como moeda.
    :return: valor com redução aplicada, formatado ou não.
    """
    resultado = num - (num * porcen / 100)
    return moeda(resultado) if formatar else resultado

def moeda(num=0):
    """
    Função que formata um número para o padrão monetário brasileiro.

    :param num: valor numérico informado.
    :return: texto no formato de moeda (ex.: R$10,00).
    """
    return f"R${num:.2f}".replace(".", ",")

def resumo(num=0, aumento=10, reducao=5):
    """
    Função que exibe um resumo com operações sobre o valor informado.

    :param num: valor base para os cálculos.
    :param aumento: percentual usado no cálculo de aumento.
    :param reducao: percentual usado no cálculo de redução.
    :return: None.
    """
    print("=" * 30)
    print("RESUMO DO VALOR".center(35))
    print("=" * 30)
    print(f"Valor Analisado: \t{moeda(num)}")
    print(f"Dobro do Preço: \t{dobro(num, True)}")
    print(f"Metade do Preço: \t{metade(num, True)}")
    print(f"{aumento}% de Aumento: \t{aumento_porcentagem(num, aumento, True)}")
    print(f"{reducao}% de Redução: \t{reduzindo_porcentagem(num, reducao, True)}")
    print("=" * 30)
