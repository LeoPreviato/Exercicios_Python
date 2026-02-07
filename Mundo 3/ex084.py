# Título centralizado
print(" Lista composta e analise de Dados ".center(60, "="))

# Lista temporária (guarda UMA pessoa por vez: nome e peso)
dados = list()

# Lista principal (guarda TODAS as pessoas)
pessoas = list()

# Lista só com os pesos (usada pra achar maior e menor)
pesos = list()

# Contador de pessoas cadastradas
tot_pessoas = 0


# Loop infinito (só para quando o usuário digitar N)
while True:
    # Adiciona o nome na lista dados
    dados.append(str(input("Nome: ")).strip().capitalize())

    # Adiciona o peso na lista dados
    dados.append(float(input("Peso: ")))

    # Soma +1 no total de pessoas
    tot_pessoas += 1

    # Copia os dados da pessoa para a lista principal
    pessoas.append(dados.copy())

    print("=" * 60)
    print("CADASTRO REALIZADO COM SUCESSO".center(60))
    print("=" * 60)

    # Limpa a lista dados para reutilizar no próximo cadastro
    dados.clear()

    # Pergunta se quer continuar
    opcao = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
    print("=" * 60)

    # Validação: enquanto não for S ou N, pergunta de novo
    while opcao not in "SN":
        opcao = str(input("Opcão invalida. Quer continuar? [S/N]: ")).strip().upper()[0]
        print("=" * 60)

    # Se o usuário digitar N, sai do while principal
    if opcao == "N":
        break


# Mostra quantas pessoas foram cadastradas
print(f"Ao todo você cadastrou {tot_pessoas} pessoas")


# Percorre todas as pessoas e pega só os pesos
for p in pessoas:
    pesos.append(p[1])


# Descobre o maior peso
maior_peso = max(pesos)

# Descobre o menor peso
menor_peso = min(pesos)


# Mostra o maior peso
print(f"O maior peso foi de {maior_peso}Kg. Peso de ", end="")

# Percorre novamente as pessoas
# e mostra o nome de quem tem o maior peso
for p in pessoas:
    if p[1] == maior_peso:
        print(f"[{p[0]}]", end=" ")


# Mostra o menor peso
print(f"\nO menor peso foi de {menor_peso}Kg. Peso de ", end="")

# Percorre novamente as pessoas
# e mostra o nome de quem tem o menor peso
for p in pessoas:
    if p[1] == menor_peso:
        print(f"[{p[0]}]", end=" ")
