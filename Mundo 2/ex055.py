# Exibe um título centralizado para o programa
print(" Maior e Menor da Sequencia ".center(55, "="))

# Inicializa as variáveis que irão armazenar o maior e o menor peso
maior_peso = menor_peso = 0

# Variáveis para guardar os nomes da pessoa com maior e menor peso
nome_maior_peso = ""
nome_menor_peso = ""

# Laço de repetição que irá executar 7 vezes (para 7 pessoas)
for cont in range(1, 6):

    # Solicita o nome da pessoa, remove espaços extras e capitaliza a primeira letra
    nome = str(input(f"Digite o nome da {cont}º pessoa: ")).strip().capitalize()

    # Solicita o peso da pessoa e converte para float
    peso = float(input("Agora digite o seu peso: "))

    # Condição usada apenas na primeira execução do laço
    # Serve para inicializar corretamente os valores de maior e menor peso
    if cont == 1:
        maior_peso = peso
        nome_maior_peso = nome
        menor_peso = peso
        nome_menor_peso = nome
    else:
        # Verifica se o peso atual é maior que o maior peso armazenado
        if peso > maior_peso:
            maior_peso = peso
            nome_maior_peso = nome

        # Verifica se o peso atual é menor que o menor peso armazenado
        elif peso < menor_peso:
            menor_peso = peso
            nome_menor_peso = nome

    # Exibe uma linha separadora a cada iteração
    print("=" * 40)

# Exibe o resultado final com o nome e o peso da pessoa mais pesada
print(f"O maior peso foi do {nome_maior_peso} com {maior_peso}kg")

# Exibe o resultado final com o nome e o peso da pessoa mais leve
print(f"E o menor peso foi do {nome_menor_peso} com {menor_peso}kg")
