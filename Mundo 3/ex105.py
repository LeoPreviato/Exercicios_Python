print(" Analisando e gerando Dicionários ".center(55, "="))


def notas(*num, sit=False):
    """
    Função para analisar notas e situações de vários alunos.
    :param num: Uma ou mais notas dos alunos (aceita várias)
    :param sit: Valor opcional indicando se deve adicionar a situação
    :return: Dicionário com informações sobre a turma
    """
    # Calcula a média das notas recebidas.
    media = sum(num) / len(num)

    # Monta o dicionário base com os dados principais.
    resultado = {
        'Total': len(num),
        'Maior': max(num),
        'Menor': min(num),
        'Média': media
    }

    # Se sit=True, adiciona a classificação da turma com base na média.
    if sit:
        if media >= 7:
            resultado['Situação'] = "BOA"
        elif media >= 5:
            resultado['Situação'] = "RAZOÁVEL"
        else:
            resultado['Situação'] = "RUIM"

    # Retorna o resumo final em formato de dicionário.
    return resultado


# Exemplo de uso da função com várias notas e situação (opcional).
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
