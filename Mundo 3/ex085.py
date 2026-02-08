print(" Listas com pares e Ímpares ".center(60, '='))
# Apenas imprime um título centralizado

lista_num = [[], []]
# Cria uma lista com DUAS listas dentro:
# índice 0 → números pares
# índice 1 → números ímpares

for cont in range(1, 8):
    # Laço que vai rodar 7 vezes (de 1 até 7)

    num = int(input("Digite um valor: "))
    # Lê um número do usuário e converte para inteiro

    if num % 2 == 0:
        # Se o resto da divisão por 2 for zero → número é PAR

        lista_num[0].append(num)
        # Adiciona o número na lista dos PARES (posição 0)
    else:
        # Caso contrário → número é ÍMPAR

        lista_num[1].append(num)
        # Adiciona o número na lista dos ÍMPARES (posição 1)

print("=" * 60)

print(f"Os valores PARES foram: {lista_num[0]}")
# Mostra todos os pares armazenados

print(f"Os valores ÍMPARES foram: {lista_num[1]}")
# Mostra todos os ímpares armazenados
