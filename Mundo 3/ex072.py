# Título do programa, centralizado em 60 caracteres usando "="
print(" Números por Extenso ".center(60, "="))

# Tupla com os números escritos por extenso.
# Cada palavra ocupa uma posição (índice) correspondente ao número.
# Exemplo: 0 -> "Zero", 1 -> "Um", ..., 20 -> "Vinte"
numeros = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete",
           "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", "Quatorze", "Quinze",
           "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte")

# Laço principal do programa.
# O while True permite que o usuário consulte vários números,
# só encerrando quando ele escolher a opção "N".
while True:

    # Pede ao usuário que digite um número inteiro entre 0 e 20
    num_utilizador = int(input("Digite um número entre 0 e 20: "))

    # Laço de validação da entrada.
    # Enquanto o número estiver fora do intervalo permitido (0 a 20),
    # o programa continuará pedindo um novo valor.
    while num_utilizador < 0 or num_utilizador > 20:
        print("=" * 60)
        # Mensagem de erro destacada em vermelho,
        # solicitando que o usuário digite um número válido
        num_utilizador = int(
            input("\033[1;31mNúmero invalido\033[m, \033[1mDigite novamente entre 0 e 20:\033[m ")
        )

    # Linha separadora após o usuário digitar um número válido
    print("=" * 60)

    # Exibe o número digitado por extenso.
    # O valor informado pelo usuário é usado como índice da tupla 'numeros'
    print(f"Você digitou o número {numeros[num_utilizador]}")

    # Linha separadora para organização visual do programa
    print("=" * 60)

    # Pergunta ao usuário se deseja continuar o programa
    # strip() remove espaços extras
    # upper() transforma em letra maiúscula
    # [0] pega apenas a primeira letra digitada
    opcao = str(input("Você quer continuar? [S/N]: ")).strip().upper()[0]

    print("=" * 60)

    # Se o usuário digitar "N", o laço principal é encerrado
    if opcao == "N":
        break

# Mensagem final exibida após o encerramento do programa
print("Fim do programa.")
