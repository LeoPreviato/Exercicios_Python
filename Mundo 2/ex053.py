# Exibe o título do programa centralizado
print(" Detector de Palíndromo ".center(50, "="))

# Solicita ao usuário uma frase, remove espaços extras e converte para letras minúsculas
frase_usuario = str(input("Digite uma frase: ")).strip().lower()

# Remove todos os espaços da frase para facilitar a comparação
frase_junta = frase_usuario.replace(" ", "")

# Variável que armazenará a frase invertida
palindromo = ""

# Laço que percorre a frase de trás para frente
for letras in range(len(frase_junta) - 1, -1, -1):

    # Adiciona cada letra invertida à variável palindromo
    palindromo += frase_junta[letras]

# Verifica se a frase invertida é igual à frase original (sem espaços)
if palindromo == frase_junta:

    # Exibe mensagem informando que a frase é um palíndromo
    print(f"'{frase_usuario}' é um palíndromo: {palindromo}")

# Caso a frase não seja um palíndromo
else:

    # Exibe mensagem informando que a frase não é um palíndromo
    print(f"{frase_usuario} não é um palíndromo: {palindromo}")
