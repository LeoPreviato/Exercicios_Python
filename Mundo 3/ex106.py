from time import sleep

# Tupla contendo códigos ANSI para cores no terminal
tupla_de_cores = (
    '\033[m',        # 0 - Sem cor (reset)
    '\033[0;30;41m', # 1 - Fundo vermelho
    '\033[0;30;42m', # 2 - Fundo verde
    '\033[0;30;43m', # 3 - Fundo amarelo
    '\033[0;30;44m', # 4 - Fundo azul
    '\033[0;30;45m', # 5 - Fundo roxo (magenta)
    '\033[7m',       # 6 - Invertido
)


def titulo(msg, cor=0):
    """
    -> Exibe um título formatado com cor no terminal.

    :param msg: Texto que será exibido como título.
    :param cor: Índice da cor na tupla_de_cores.
    :return: None
    """
    tamanho = len(msg) + 4  # Define o tamanho do título com base no texto

    print(tupla_de_cores[cor], end="")  # Aplica a cor escolhida
    print("=" * tamanho)               # Linha superior
    print(msg.center(tamanho))         # Texto centralizado
    print("=" * tamanho)               # Linha inferior
    print(tupla_de_cores[0], end="")   # Reseta a cor


def ajuda(fun_manu):
    """
    -> Mostra o manual (help) de uma função ou biblioteca.

    :param fun_manu: Nome da função ou biblioteca a ser analisada.
    :return: None
    """
    titulo(f"Acessando o manual do comando '{fun_manu}'", 2)
    sleep(1)

    print(tupla_de_cores[4], end="")  # Aplica cor azul para o help
    help(fun_manu)                   # Exibe o manual
    print(tupla_de_cores[0], end="")  # Reseta a cor

    sleep(1)


# Loop principal do sistema
while True:
    titulo("SISTEMA DE AJUDA PyHELP", 3)

    # Recebe o nome da função ou biblioteca
    funcao_ou_manual = input(
        "Informe uma Função ou uma Biblioteca > "
    ).strip().lower()

    # Condição de parada
    if funcao_ou_manual == "fim":
        titulo("ATÉ LOGO!", 1)
        break
    else:
        ajuda(funcao_ou_manual)
