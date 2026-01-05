# Exibe o título do programa centralizado, usando '=' como preenchimento
print(" Soma dos pares ".center(45, "="))

# Variável acumuladora que vai guardar a soma dos números pares
soma_pares = 0

# Laço de repetição que será executado 6 vezes
# A variável 'lupi' serve como contador (de 1 até 6)
for lupi in range(1, 7):
    # Solicita um número ao usuário a cada iteração
    num_usuario = int(input(f"Digite o {lupi}º número: "))

    # Verifica se o número digitado é par
    if num_usuario % 2 == 0:
        # Se for par, soma o valor à variável acumuladora
        soma_pares += num_usuario

# Linha em branco para melhorar a organização da saída
print()

# Exibe o resultado final da soma dos números pares digitados
print(f"A soma de todos os números PARES é: {soma_pares}")
