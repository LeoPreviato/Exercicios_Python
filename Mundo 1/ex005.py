# Programa simples que mostra o antecessor e o sucessor de um número

# Imprime uma linha de separador para organizar a saída
print("=" * 30)

# Imprime o título centralizado em uma largura de 30 caracteres
print("Antecessor e Sucessor!".center(30))

# Outra linha de separador
print("=" * 30)

# Pede que o usuário digite um número e converte a entrada (string) para inteiro
# Se o usuário digitar algo que não seja número, o programa lançará ValueError
num_usu = int(input("Digite um número qualquer: "))

# Linha separadora antes do resultado
print("-" * 30)

# Calcula e exibe o antecessor (n - 1)
print(f"O antecessor de {num_usu} é {num_usu - 1}.")

# Imprime uma linha em branco para espaçamento (mesma que print() sem argumentos)
print()

# Calcula e exibe o sucessor (n + 1)
print(f"E o sucessor de {num_usu} é {num_usu + 1}.")
