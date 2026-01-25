# Linha decorativa
print("=" * 50)

# Título do programa centralizado
print("BANCO DEV".center(50))

# Linha decorativa
print("=" * 50)

# Usuário digita o valor que deseja sacar
valor = int(input("💵\033[1mDigite um valor para sacar: R$\033[m"))

# Linha decorativa
print("=" * 50)

# Começamos sempre pela maior cédula disponível
cedula = 50

# Contador de quantas cédulas daquela nota serão usadas
tot_cedula = 0

# Loop infinito, só será parado com o break
while True:

    # Se ainda der para sacar a cédula atual
    if valor >= cedula:
        valor -= cedula          # Subtrai o valor da cédula do total
        tot_cedula += 1          # Conta mais uma cédula usada

    else:
        # Se pelo menos uma cédula dessa foi usada, mostra o resultado
        if tot_cedula > 0:
            print(f"Total de {tot_cedula} cédulas de R${cedula}")

        # Troca para a próxima cédula menor
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1

        # Zera o contador para começar a contar a nova cédula
        tot_cedula = 0

        # Quando o valor chegar a zero, o saque terminou
        if valor == 0:
            break

# Linha decorativa final
print("=" * 50)

# Mensagem de encerramento
print("Volte sempre ao BANCO DEV! Tenha um bom dia!")
