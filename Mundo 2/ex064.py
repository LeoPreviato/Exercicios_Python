# Mostra o título do programa centralizado com '='
print(" Tratando Varios Valores V.1.0 ".center(60, "="))

# Variável que guarda o número digitado pelo usuário
# Variável que soma os números digitados
# Variável que conta quantos números foram digitados
soma = numeros_digitados = num_usuario = 0

# Enquanto o usuário NÃO digitar 999, o loop continua
while num_usuario != 999:
    # Pede um número ao usuário
    num_usuario = int(input("Digite um número qualquer ou [999] para parar: "))

    # Linha separadora visual
    print("-" * 60)

    # Se o número digitado NÃO for o valor de parada (999)
    if num_usuario != 999:
        # Soma o número digitado ao total
        soma += num_usuario

        # Conta mais um número digitado
        numeros_digitados += 1

# Mostra a soma de todos os números digitados (exceto o 999) e quantos números foram digitados
print(f"A soma de todos os número é {soma}, e você digitou {numeros_digitados} números")
