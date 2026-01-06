# Importa a função sleep para criar pausas na execução
from time import sleep

# Exibe o título do programa centralizado
print(" Números Primos ".center(50, "="))

# Solicita ao usuário um número inteiro
num_usuario = int(input("Digite um número qualquer: "))

# Pula uma linha para melhor organização no terminal
print()

# Pausa de 1 segundo para efeito visual
sleep(1)

# Exibe mensagem de análise do número
print("Analisando número...")

# Pula uma linha para separar a saída
print()

# Nova pausa para deixar o programa mais fluido
sleep(1)

# Variável que contará a quantidade de divisores do número
divisores = 0

# Laço que testa todos os possíveis divisores de 1 até o próprio número
for divi in range(1, num_usuario + 1):

    # Verifica se a divisão é exata (resto igual a zero)
    if num_usuario % divi == 0:

        # Incrementa o contador sempre que encontra um divisor
        divisores += 1

# Verifica se o número possui exatamente dois divisores
if divisores == 2:

    # Exibe mensagem informando que o número é primo
    print(f"O número {num_usuario} é primo! ✅")

# Caso o número não tenha apenas dois divisores
else:

    # Exibe mensagem informando que o número não é primo
    print(f"O número {num_usuario} não é primo! ❌")
