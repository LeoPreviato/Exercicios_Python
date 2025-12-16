# imprime uma linha separadora com 51 caracteres '='
print("=" * 51)
# imprime o título centralizado em 51 posições
print("Primeiro e ultimo nome de uma pessoa".center(51))
# imprime outra linha separadora
print("=" * 51)

# lê o nome completo do usuário, converte para minúsculas e remove espaços nas extremidades
nome_completo = input("Digite seu nome completo: ").lower().strip()

# divide a string em palavras e exibe a primeira (primeiro nome)
print(f"Seu primeiro nome é: {nome_completo.split()[0]}")

# divide a string em palavras e exibe a última (último nome)
print(f"Seu segundo nome é: {nome_completo.split()[-1]}")
