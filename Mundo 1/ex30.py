from time import sleep  # importa sleep para pausar a execução por um tempo

# cabeçalho simples para o usuário
print("=" * 30)
print("Par ou ímpar?".center(30))
print("=" * 30)

# lê um número do usuário e converte para inteiro
num_usuario = int(input("Digite um número para saber se é Par ou Ímpar: "))

sleep(1)  # pequena pausa para melhorar a experiência do usuário

# verifica a paridade usando o operador módulo (%)
# se num_usuario % 2 == 0 então é par, caso contrário é ímpar
if num_usuario % 2 == 0:
    print(f"O número {num_usuario} é PAR!")
else:
    print(f"O número {num_usuario} é ÍMPAR!")
