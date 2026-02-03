# Título do programa centralizado com '='
print(" Dividindo valores em varias Listas ".center(60, '='))

# Lista que armazena todos os números digitados
tot_numeros = []

# Lista que armazena apenas os números pares
nums_pares = []

# Lista que armazena apenas os números ímpares
nums_impares = []

# Loop principal para entrada de dados
while True:
    # Lê um número inteiro do usuário
    num = int(input("Digite um número: "))

    # Adiciona o número à lista principal
    tot_numeros.append(num)

    # Verifica se o número é par ou ímpar
    if num % 2 == 0:
        nums_pares.append(num)
    else:
        nums_impares.append(num)

    # Pergunta se o usuário deseja continuar
    opcao = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]

    # Linha decorativa
    print("=" * 60)

    # Validação da opção (aceita apenas S ou N)
    while opcao not in "SN":
        opcao = str(input("Opção invalida. Digite novamente [S/N]: ")).strip().upper()[0]

    # Se o usuário escolher 'N', o loop é encerrado
    if opcao == "N":
        break

print("=" * 60)

# Exibe a lista completa com todos os números digitados
print(f"A lista completa é: {tot_numeros}")

# Exibe apenas os números pares
print(f"A lista de números pares é: {nums_pares}")

# Exibe apenas os números ímpares
print(f"A lista de números ímpares é: {nums_impares}")
