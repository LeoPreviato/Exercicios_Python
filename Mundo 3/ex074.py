# Título do programa, centralizado em 65 caracteres usando "="
print(" Maior e Menor Valores em Tupla ".center(65, "="))


# Importa a função randint do módulo random,
# que gera números inteiros aleatórios
from random import randint


# Cria uma tupla com 5 números aleatórios entre 1 e 10
# Cada chamada de randint gera um novo número
tupla_num = (
    randint(1, 10), randint(1, 10), randint(1, 10),
    randint(1, 10), randint(1, 10)
)


# Exibe uma mensagem inicial sem quebrar a linha
print("Os valores gerados foram: ", end="")


# Percorre a tupla e mostra cada número gerado
# end=" " mantém os valores na mesma linha
for n in tupla_num:
    print(n, end=" ")


# Usa a função max() para encontrar o maior valor da tupla
print(f"\nO maior valor foi o número: {max(tupla_num)}")


# Usa a função min() para encontrar o menor valor da tupla
print(f"E o menor valor foi o número: {min(tupla_num)}")
