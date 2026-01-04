# Exibe um título centralizado com 55 caracteres preenchidos por "="
print(" Soma ímpares multiplos de três ".center(55, "="))

# Linha em branco para organização visual
print()

# Variável acumuladora que guardará a soma total
soma = 0

# Laço que percorre todos os números de 1 até 499
for cont in range(1, 500):
    # Verifica se o número é ímpar e múltiplo de 3
    if cont % 2 != 0 and cont % 3 == 0:
        # Soma o valor à variável acumuladora
        soma += cont

# Exibe o resultado final da soma
print(f"A soma de todos os números ímpares múltiplos de três é {soma}")
