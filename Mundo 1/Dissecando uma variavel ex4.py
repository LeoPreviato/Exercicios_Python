# Pede ao usuário que digite algo. A função input() sempre retorna uma string (tipo 'str').
resposta_usuario = input("Digite algo: ")

# Imprime uma linha de separador para organizar a saída na tela
print("=" * 40)

# Exibe o tipo primitivo da variável 'resposta_usuario'. Esperamos 'str'.
print(f"O tipo primitivo de {resposta_usuario} é {type(resposta_usuario)}")

# Verifica propriedades da string usando métodos do tipo str:
# isalpha()  -> True se todos os caracteres forem letras (sem espaços ou sinais)
print(f"O que você digitou é alfabético?: {resposta_usuario.isalpha()}!")

# isnumeric() -> True se todos os caracteres forem numéricos (dígitos)
print(f"O que você digitou só tem números?: {resposta_usuario.isnumeric()}!")

# isalnum() -> True se todos os caracteres forem letras ou números (sem espaços/símbolos)
print(f"O que você digitou é alfanumérico?: {resposta_usuario.isalnum()}!")

# isupper() -> True se todas as letras na string estiverem em maiúsculas
print(f"Todas as letras são maiúsculas?: {resposta_usuario.isupper()}!")

# islower() -> True se todas as letras na string estiverem em minúsculas
print(f"Todas as letras são minúsculas?: {resposta_usuario.islower()}!")

# istitle() -> True se a string estiver no formato título (cada palavra com inicial maiúscula)
print(f"A primeira letra é capitalizada?: {resposta_usuario.istitle()}!")

# isspace() -> True se a string contiver apenas espaços em branco
print(f"O que você digitou só tem espaços?: {resposta_usuario.isspace()}!")

# Linha final de separador
print("=" * 40)
