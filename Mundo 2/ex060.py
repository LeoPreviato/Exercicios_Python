print(" Calculo do Factorial ".center(50, "="))

# Pede ao usuário um número inteiro para calcular o fatorial
num = int(input("Digite um número para calcular o seu factorial: "))

# Variável que vai armazenar o resultado do fatorial
# Começa em 1 porque 1 é o elemento neutro da multiplicação
fac = 1

# O contador começa com o valor digitado pelo usuário
contador = num

# Enquanto o contador for maior que 1, o laço continua
# Isso evita multiplicar por 1, já que não altera o resultado
while contador > 1:
    fac *= contador      # Multiplica o valor atual do fatorial pelo contador
    contador -= 1        # Decrementa o contador (vai descendo até chegar em 1)

# Exibe o resultado final do cálculo
print(f"O factorial de {num} é {fac}")
