# Mostra o título do programa centralizado com '='
print(" Sequencia de Fibonacci V.1.0 ".center(50, "="))

# Pede ao usuário quantos números da sequência ele quer ver
num_usuario = int(input("Digite quantos números da sequência: "))

# Primeiro número da sequência de Fibonacci
termo1 = 0

# Segundo número da sequência de Fibonacci
termo2 = 1

# Contador começa em 2 porque já temos dois números (0 e 1)
cont = 2

# Mostra o primeiro e o segundo número da sequência
print(termo1, termo2, end=" → ")

# Enquanto o contador for menor que a quantidade desejada
while cont < num_usuario:
    # Soma os dois últimos números da sequência
    soma = termo1 + termo2

    # Mostra o próximo número da sequência
    print(soma, end=" → ")

    # Atualiza o valor de 'termo1' para o antigo 'termo2'
    termo1 = termo2

    # Atualiza o valor de 'termo2' para o novo número da sequência
    termo2 = soma

    # Incrementa o contador
    cont += 1

# Indica o fim da sequência
print("Fim da Sequencia")
