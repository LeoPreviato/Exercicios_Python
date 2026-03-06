def metade(num=0):
    """
    Função que calcula a metade
    :param num: recebe o preço que o usuario irá digitar
    :return: retorna a metade do preço
    """
    resultado = num / 2
    return resultado

def dobro(num=0):
    """
    Função que calcula o dobro
    :param num: recebe o preço informado pelo usuario
    :return: retorna o dobro do preço
    """
    resultado = num * 2
    return resultado

def aumento_porcentagem(num=0, porcen=0):
    """
    Função que calcula o aumento do preço conforme a porcentagem
    :param num: Recebe o preço informado
    :param porcen: Recebe o valor da porcentagem
    :return: Retorna o preço com o aumento de 10%
    """
    resultado = num + (num * porcen / 100)
    return resultado
