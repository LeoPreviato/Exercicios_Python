# Título do programa centralizado
print(" Maior e Menos valores na lista ".center(60, "="))

# Lista vazia para armazenar os números digitados
lista_num = []

# Loop para ler 5 valores do usuário
for cont in range(0, 5):
    lista_num.append(int(input(f"Digite um valor para a posição {cont}: ")))

# Linha separadora
print("=" * 60)

# Mostra todos os valores digitados
print(f"Você digitou os valores: {lista_num}")

# Armazena o maior e o menor valor da lista em variáveis
maior = max(lista_num)
menor = min(lista_num)

# Exibe o maior valor encontrado
print(f"O maior valor digitado foi o {maior} nas posições ", end="")

# Percorre a lista mostrando todas as posições do maior valor
for pos, v in enumerate(lista_num):
    if v == maior:
        print(pos, end="... ")

# Exibe o menor valor encontrado
print(f"\nO menor valor digitado foi o {menor} nas posições ", end="")

# Percorre a lista mostrando todas as posições do menor valor
for pos, v in enumerate(lista_num):
    if v == menor:
        print(pos, end="... ")
