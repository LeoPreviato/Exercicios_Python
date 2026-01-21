# Título do programa centralizado com '='
print(" Tabuada V.3.0 ".center(50, "="))

# Laço infinito para permitir várias tabuadas
while True:
    # Usuário escolhe qual tabuada quer ver
    num_tabuada = int(input("Quer ver a tabuada de qual valor?: "))

    # Linha separadora
    print("=" * 50)

    # Condição de parada:
    # Se o número for negativo, o programa encerra
    if num_tabuada < 0:
        print("Programa encerrado.")
        break  # sai do while
    else:
        # Laço para gerar a tabuada de 1 até 10
        for cont in range(1, 11):
            print(f"{num_tabuada} x {cont} = {num_tabuada * cont}")

        # Linha separadora após exibir a tabuada
        print("=" * 50)
