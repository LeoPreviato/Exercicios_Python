# Cabeçalho visual
print("=" * 35)

# Título centralizado
print("Analisador de Textos".center(35))

# Fechamento do cabeçalho
print("=" * 35)

# Solicita ao usuário que digite o nome completo, converte para string (desnecessário, mas explícito),
# e aplica o método .title() para capitalizar a primeira letra de cada palavra
nome_completo = str(input("Digite o seu nome completo: ")).title()

# Imprime uma linha em branco para espaçamento
print()

# Imprime várias informações sobre o nome usando f-strings para formatação:
# - O nome completo original
# - O nome em minúsculas
# - O nome em maiúsculas
# - O número total de caracteres, removendo espaços (usando replace para substituir espaços por nada e len para contar)
# - O número de caracteres do primeiro nome (usando split() para dividir em palavras e pegar a primeira)
print(f"""Seu nome completo é: {nome_completo}

Seu nome com todas as letras minusculas é: {nome_completo.lower()}

Seu nome com todas as letras maiusculas é: {nome_completo.upper()}

Seu nome tem ao todo {len(nome_completo.replace(' ', ''))} caracteres

O seu primeiro nome tem ao todo {len(nome_completo.split()[0])} caracteres
""")

