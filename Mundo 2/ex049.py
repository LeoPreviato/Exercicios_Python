# Importa a função sleep do módulo time
# Ela é usada para criar pausas no programa
from time import sleep

# Exibe o título do programa centralizado, com '=' preenchendo os lados
print(" Tabuada V.2.0 ".center(50, "="))

# Solicita ao usuário um número inteiro para gerar a tabuada
num_usuario = int(input("Digite um número para saber sua tabuada: "))

# Linha em branco para melhorar a organização da saída
print()

# Pausa de 1 segundo antes de continuar
sleep(1)

# Mensagem informando que a tabuada está sendo carregada
print(f"Carregando tabuada do {num_usuario}...")

# Outra linha em branco para espaçamento visual
print()

# Pausa de 1 segundo
sleep(1)

# Imprime uma linha separadora
print("=" * 12)

# Laço de repetição que vai de 1 até 10
# Responsável por calcular e exibir a tabuada
for tabu in range(1, 11):
    # Mostra a multiplicação do número escolhido pelo contador do laço
    print(f"{num_usuario} x {tabu} = {num_usuario * tabu}")

    # Pequena pausa entre cada linha da tabuada
    sleep(0.8)

# Linha final para fechar visualmente a tabuada
print("=" * 12)
