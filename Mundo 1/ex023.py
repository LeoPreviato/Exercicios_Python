# Imprime uma linha de 45 caracteres '=' para criar uma borda superior
print("=" * 45)

# Imprime o título centralizado em 45 caracteres
print("Separando Digitos de um Número".center(45))

# Imprime outra linha de 45 caracteres '=' para criar uma borda inferior
print("=" * 45)

# Solicita ao usuário que digite um número entre 0 e 9999 e converte para string
num_usuario = str(input("Digite um número entre 0 e 9999: "))

# Usa zfill(4) para preencher a string com zeros à esquerda até ter 4 dígitos
# Isso garante que números menores que 1000 sejam tratados como 4 dígitos (ex: 5 vira '0005')
numeros_separados = num_usuario.zfill(4)

# Imprime os dígitos separados:
# [3] é a unidade (último dígito)
# [2] é a dezena (penúltimo dígito)
# [1] é a centena (antepenúltimo dígito)
# [0] é o milhar (primeiro dígito)
print(f"""A unidade é: {numeros_separados[3]}
A dezena é: {numeros_separados[2]}
A centena é: {numeros_separados[1]}
E o milhar é: {numeros_separados[0]}""")
