# Exibe um título centralizado para o programa
print(" Analisador Completo ".center(45, "="))

# Inicializa as variáveis:
# soma_idade → soma de todas as idades
# mulheres_menor_20 → contador de mulheres com menos de 20 anos
# media_idade → média de idade do grupo
# maior_idade_homem → idade do homem mais velho
soma_idade = mulheres_menor_20 = media_idade = maior_idade_homem = 0

# Armazena o nome do homem mais velho
nome_homem_mais_velho = ""

# Laço que irá repetir 4 vezes (4 pessoas no grupo)
for cont in range(1, 5):

    # Lê o nome da pessoa, remove espaços extras e capitaliza
    nome_pessoa = str(input(f"Digite o nome da {cont}º pessoa: ")).strip().capitalize()

    # Lê o sexo, remove espaços, converte para maiúsculo
    # e pega apenas o primeiro caractere
    sexo = str(input("Digite seu sexo [M/F]: ")).strip().upper()[:1]

    # Lê a idade da pessoa
    idade = int(input("Digite sua idade: "))

    # Soma as idades para depois calcular a média
    soma_idade += idade

    # Linha separadora visual
    print("=" * 45)

    # Verifica se a pessoa é do sexo masculino
    if sexo == "M":
        # Se for o primeiro homem ou se a idade for maior que a atual,
        # atualiza o homem mais velho
        if not maior_idade_homem or idade > maior_idade_homem:
            maior_idade_homem = idade
            nome_homem_mais_velho = nome_pessoa
    else:
        # Se não for homem (considerando mulher),
        # verifica se tem menos de 20 anos
        if idade < 20:
            mulheres_menor_20 += 1

# Calcula a média de idade (fixa em 4 pessoas)
media_idade = soma_idade / 4

# Exibe a média de idade do grupo
print(f"A média de idade do grupo é de: {media_idade:.2f} anos")

# Exibe o homem mais velho e a sua idade
print(f"O homem mais velho é o {nome_homem_mais_velho} de {maior_idade_homem} anos")

# Exibe a quantidade de mulheres com menos de 20 anos
print(f"No grupo existem {mulheres_menor_20} mulheres com menos de 20 anos")
