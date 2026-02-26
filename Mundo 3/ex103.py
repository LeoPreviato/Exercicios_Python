print(" Ficha do Jogador ".center(55, "="))

def ficha(nome, gol):
    """
    -> Ficha para guardar os dados do jogador
    :param nome: Recebe o nome do jogador, se não for informado um nome, ele será desconhecido
    :param gol: Recebe a quantidade de gols do jogador, se os gols não forem ditados, ele será 0
    :return: Retorna o nome e a quantidade de gols do jogador
    """
    # Se o nome vier vazio, define um valor padrão.
    if not nome:
        nome = "<Desconhecido>"
    # Converte gols para inteiro apenas se for um número válido.
    if gol.isnumeric():
        gol = int(gol)
    else:
        # Caso não seja numérico, assume 0 gols.
        gol = 0
    print("=" * 55)
    return f"O jogador {nome} tem {gol} gol(s) na carreira."

# Lê o nome informado e aplica limpeza básica de espaços/capitalização.
nome_jogador = str(input("Informe o nome do jogador: ")).strip().capitalize()

# Lê a quantidade de gols como texto para validar depois.
quantidade_gols = str(input("Agora digite quantos gol(s) ele tem: ")).strip()

# Exibe a ficha formatada com os dados tratados.
print(ficha(nome_jogador, quantidade_gols))
