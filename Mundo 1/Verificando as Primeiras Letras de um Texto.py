# Imprime uma linha com 55 sinais de igual para formar o cabeçalho
print("=" * 55)

# Imprime o título centralizado em 55 caracteres
print("Verificando as Primeiras Letras de um Texto".center(55))

# Imprime outra linha de separação
print("=" * 55)

# Pede ao usuário o nome da cidade
# strip() remove espaços extras no início e no fim
# lower() transforma todo o texto em minúsculo
cidade_usuario = str(input("Digite o nome da sua cidade: ")).strip().lower()

# split() separa o texto em palavras
# [0] pega a primeira palavra (o nome inicial da cidade)
# Compara se essa palavra é exatamente 'santo'
# O resultado será True ou False
print(f"Sua cidade começa com 'Santo'?: {cidade_usuario.split()[0] == 'santo'}")
