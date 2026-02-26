print(" Função para Factorial ".center(55, "="))

# Função que calcula o fatorial de um número.
# O parâmetro "show" define se a conta será exibida passo a passo.
def fac(num, show=False):
    """
    -> Calcula o factorial de um número
    :param num: O número que vai ser calculado
    :param show: Mostra ou não a conta (opcional)
    :return: O valor do factorial do número escolhido
    """
    # Import local para usar a função pronta de fatorial quando não precisar mostrar a conta.
    from math import factorial

    # Se "show" for False, retorna direto o resultado da biblioteca.
    if not show:
        return factorial(num)
    else:
        # Se "show" for True, faz o cálculo manual para imprimir cada multiplicação.
        f = 1
        for c in range(num, 0, -1):
            # Mostra o formato da conta: 5 x 4 x 3 x 2 x 1 =
            print(c, end=" x " if c > 1 else " = ")
            # Acumula o resultado da multiplicação.
            f *= c
        return f

# Exemplo de uso da função:
print(fac(5, False))
