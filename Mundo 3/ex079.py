# Título do programa, centralizado com 65 caracteres usando '='
print(" Valores únicos em uma Lista ".center(65, '='))

# Lista vazia que vai armazenar apenas valores únicos
lista_valores = []

# Laço infinito, só será encerrado quando o usuário escolher não continuar
while True:
    # Solicita um número ao usuário e converte para inteiro
    num = int(input("Digite um valor: "))

    # Verifica se o número ainda NÃO está na lista
    if num not in lista_valores:
        # Adiciona o número à lista
        lista_valores.append(num)

        # Linha separadora
        print("=" * 60)

        # Mensagem em verde indicando sucesso
        print("\033[1;32mValor adicionado com sucesso!\033[m".center(60))
    else:
        # Caso o número já exista na lista
        print("=" * 60)

        # Mensagem em vermelho indicando valor duplicado
        print("\033[1;31mValor duplicado! Não vou adicionar!\033[m".center(65))

    # Linha separadora
    print("=" * 60)

    # Pergunta ao usuário se deseja continuar
    opcao = str(input("Você quer continuar? [S/N]: ")).strip().upper()[0]

    # Enquanto a opção não for 'S' nem 'N', pede novamente
    while opcao not in "SN":
        opcao = str(input("Opção invalida. Digite novamente [S/N]: ")).strip().upper()[0]

    # Se o usuário escolher 'N', o laço é encerrado
    if opcao == "N":
        break

# Ordena os valores da lista em ordem crescente
lista_valores.sort()

# Mostra na tela todos os valores digitados (sem repetições)
print(f"Você digitou os valores: {lista_valores}")
