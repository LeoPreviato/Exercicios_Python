# Mostra o título do programa centralizado com '='
print(" Maior e Menor Valores ".center(60, "="))

# Variável que controla se o usuário quer continuar
opcao_usuario = "S"

# Variáveis para média, quantidade de números digitados e soma total
media_valores = numeros_digi = soma_valores = 0

# Variáveis que vão armazenar o maior e o menor número digitado
maior_num = menor_num = 0

# Enquanto o usuário não escolher 'N', o programa continua
while opcao_usuario != "N":
    # Pede um número ao usuário
    num_usuario = int(input("Digite um valor: "))

    # Incrementa a quantidade de números digitados
    numeros_digi += 1

    # Soma o valor digitado ao total
    soma_valores += num_usuario

    # Se for o primeiro número digitado
    if numeros_digi == 1:
        # Inicializa maior e menor com o primeiro valor
        maior_num = num_usuario
        menor_num = num_usuario
    else:
        # Verifica se o número digitado é maior que o maior atual
        if num_usuario > maior_num:
            maior_num = num_usuario

        # Verifica se o número digitado é menor que o menor atual
        if num_usuario < menor_num:
            menor_num = num_usuario

    # Pergunta ao usuário se deseja continuar e pega apenas a primeira letra
    opcao_usuario = str(input("Quer continuar [S/N]: ")).strip().capitalize()[0]

    # Linha separadora para melhorar a visualização
    print("-" * 60)

# Calcula a média dos valores digitados
media_valores = soma_valores / numeros_digi

# Mostra a média com duas casas decimais
print(f"A média de todos os números digitados é de: {media_valores:.2f}")

print()

# Mostra o maior e o menor número digitado
print(f"O maior número é o {maior_num} e o menor é o {menor_num}")
