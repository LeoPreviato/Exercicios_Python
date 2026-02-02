# Título do programa, centralizado com '='
print(" Lista ordenada sem Repetiçãoes ".center(60, "="))

# Lista vazia que vai guardar os números em ordem
lista_num = []

# Laço que vai rodar 5 vezes (de 1 até 5)
for cont in range(1, 6):

    # Lê um número digitado pelo usuário
    num = int(input("Digite um valor: "))

    # Se for o primeiro número digitado
    # OU se o número for maior ou igual ao maior valor da lista
    if cont == 1 or num >= max(lista_num):

        # Adiciona o número no final da lista
        lista_num.append(num)

        # Mensagens visuais
        print("=" * 60)
        print("Adicionado ao final da lista...".center(60))
        print("=" * 60)

    # Caso o número NÃO seja o maior
    else:

        # Variável que controla a posição da lista
        pos = 0

        # Enquanto a posição for válida dentro da lista
        while pos <= len(lista_num):

            # Se o número digitado for menor ou igual
            # ao valor que está na posição atual da lista
            if num <= lista_num[pos]:
                # Insere o número exatamente nessa posição
                lista_num.insert(pos, num)

                # Mensagens visuais
                print("=" * 60)
                print(f"Adicionado na posição {pos} da lista...".center(60))
                print("=" * 60)

                # Para o loop, pois o número já foi inserido
                break

            # Avança para a próxima posição da lista
            pos += 1

# Mostra a lista final, já ordenada
print(f"Os valores digitados em ordem foram: {lista_num}")
