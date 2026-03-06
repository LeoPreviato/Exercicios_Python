def metade(num=0, formatar=False):
    """
    Calcula a metade do preço informado
    :param num: Recebe o preço informado pelo utilizador
    :param formatar: Recebe um valor bool, se não for chamado, ele será False, por outro lado, será True
    :return: Retorna o valor formatado caso 'Formatar' for True, senão retorna só o valor da conta
    """
    resultado = num / 2
    return moeda(resultado) if formatar else resultado

def dobro(num=0, formatar=False):
    """
    Calcula o dobro do preço informado
    :param num: Recebe o preço informado pelo utilizador
    :param formatar: Recebe um valor bool, se não for chamado, ele será False, senão será True
    :return: Retorna o valor formatado caso 'Formatar' for True, senão retorna só o valor da conta
    """
    resultado = num * 2
    return moeda(resultado) if formatar else resultado

def aumento_porcentagem(num=0, porcen=0, formatar=False):
    """
    Calcula o aumento do preço conforme a percentage
    :param num: Recebe o preço informado pelo utilizador
    :param porcen: Recebe o valor da percentage
    :param formatar: Recebe um valor bool, se não for chamado, ele será False, senão será True
    :return: Retorna o valor formatado caso 'Formatar' for True, senão retorna só o valor da conta
    """
    resultado = num + (num * porcen / 100)
    return moeda(resultado) if formatar else resultado

def reduzindo_porcentagem(num=0, porcen=0, formatar=False):
    """
    Calcula a redução do preço conforme a percentage
    :param num: Recebe o preço informado pelo utilizador
    :param porcen: Recebe o valor da percentage
    :param formatar: Recebe um valor bool, se não for chamado, ele será False, senão será True
    :return: Retorna o valor formatado caso 'Formatar' for True, senão retorna só o valor da conta
    """
    resultado = num - (num * porcen / 100)
    return moeda(resultado) if formatar else resultado

def moeda(num=0):
    """
    Função que formata o resultado do preço
    :param num: Recebe o preço informado
    :return: Retorna o preço digitado já formatado com ','
    """
    return f"R${num:.2f}".replace(".", ",")
