# importa a função trunc do módulo math para truncar (remover a parte decimal) de um número float
from math import trunc

# imprime uma linha de separação com 35 caracteres '='
print("=" * 35)

# imprime o título centralizado em um campo de 35 caracteres
print("Conversor de Real para Inteiro".center(35))

# imprime outra linha de separação
print("=" * 35)

# lê um número real digitado pelo usuário e converte a entrada (string) para float
num_usuario = float(input("Digite um número real qualquer: "))

# imprime o resultado usando f-string; trunc(num_usuario) remove a parte decimal sem arredondar
print(f"O número {num_usuario} convertido para um número inteiro é {trunc(num_usuario)}")
