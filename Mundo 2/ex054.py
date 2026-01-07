# Exibe o título do programa centralizado
print(" Grupo da Maioridade ".center(40, "="))

# Contador de pessoas com 21 anos ou mais
maiores_21 = 0

# Contador de pessoas com menos de 21 anos
menor_21 = 0

# Laço que irá repetir 7 vezes (para 7 pessoas)
for cont in range(1, 8):

    # Exibe uma linha separadora
    print("-" * 40)

    # Solicita a idade da pessoa atual
    idade_usuario = int(input(f"Digite a idade da {cont}º pessoa: "))

    # Verifica se a pessoa é maior de idade (21 anos ou mais)
    if idade_usuario >= 21:

        # Incrementa o contador de maiores de 21
        maiores_21 += 1

    # Caso a pessoa seja menor de 21 anos
    else:

        # Incrementa o contador de menores de 21
        menor_21 += 1

# Exibe uma linha final de separação
print("=" * 40)

# Mostra a quantidade de pessoas maiores de idade
print(f"{maiores_21} pessoas são MAIORES de idade!")

# Pula uma linha para melhorar a visualização
print()

# Mostra a quantidade de pessoas menores de idade
print(f"{menor_21} pessoas são MENORES de idade!")
