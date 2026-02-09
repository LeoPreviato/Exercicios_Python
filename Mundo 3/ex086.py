# Título centralizado com 60 caracteres usando '='
print(" Matrix em Python ".center(60, "="))

# Cria uma lista com 3 listas vazias (representam as linhas da matriz)
lista_num = [[], [], []]

# Laço externo → percorre as linhas (0, 1, 2)
for a in range(0, 3):

    # Laço interno → percorre as colunas (0, 1, 2)
    for b in range(0, 3):

        # Pede um número ao usuário indicando posição da matriz, e adiciona na lista
        lista_num[a].append(int(input(f"Digite um valor para [{a}, {b}]: ")))
        
# Percorre cada linha da matriz
for linha in lista_num:

    # Percorre cada valor dentro da linha
    for valor in linha:

        # Mostra o valor formatado:
        # ^3 → centraliza em 3 espaços
        # end=" " → evita quebra de linha
        print(f"[  {valor:^3}  ]", end=" ")

    # Quebra de linha após imprimir toda a linha
    print()

