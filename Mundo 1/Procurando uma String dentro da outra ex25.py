# Imprime uma linha separadora composta por 50 sinais de igual
print("=" * 50)
# Imprime o título centralizado em um campo de 50 caracteres
print("Procurando uma string dentro da outra".center(50))
# Imprime novamente a linha separadora
print("=" * 50)

# Lê o nome completo do usuário, remove espaços extras nas extremidades e formata cada palavra com inicial maiúscula
nome_usuario = str(input("Digite seu nome completo: ")).strip().title()

# Verifica se a substring 'Silva' está presente em nome_usuario (a verificação é sensível a maiúsculas/minúsculas,
# mas como usamos .title() acima, nomes como "silva" serão convertidos para "Silva" e a checagem funcionará)
print(f"Seu nome possui 'Silva'?: {'Silva' in nome_usuario}!")
