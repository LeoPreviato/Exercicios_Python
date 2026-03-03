# Exibe um título centralizado para o exercício no terminal.
print(" Validando entrada de dados em Python ".center(55, "="))

# Print para separar o código
print()

# Função que lê e valida uma entrada inteira do usuário.
def leiaInt(v: str):
    """
    Valida se a entrada do usuário é um número inteiro.

    Args:
        v (str): Mensagem exibida no input.

    Returns:
        int: Número inteiro validado pelo usuário.
    """
    # Repete até o usuário informar um valor válido.
    while True:
        # Mostra a mensagem recebida por parâmetro e captura o que foi digitado.
        valor = input(v)
        # Verifica se a entrada contém apenas números.
        if valor.isnumeric():
            # Converte para inteiro e encerra a função.
            return int(valor)
        else:
            # Exibe mensagem de erro e repete a leitura.
            print("=" * 55)
            print("\033[31mERRO! Digite um número inteiro válido.\033[m")


# Chama a função de leitura validada.
n = leiaInt("Digite um número: ")
# Mostra o resultado final ao usuário.
print("=" * 55)
print(f"Você acabou de digitar o número {n}")
