# Título do programa centralizado com '='
print(" Varios Números Com Flag ".center(60, "="))

# Variáveis de controle:
# cont -> conta quantos números válidos foram digitados
# soma -> acumula a soma dos valores
cont = soma = 0

# Laço infinito, só será interrompido pelo break
while True:
    # Usuário digita um número ou 999 para encerrar
    num = int(input("Digite um valor qualquer ou digite (999 para parar): "))

    # Verifica se o número é a flag de parada
    if num == 999:
        break  # encerra o laço

    # Conta mais um número válido
    cont += 1

    # Soma o número digitado
    soma += num

# Linha separadora final
print("=" * 60)

# Exibe o resultado final
print(f"A soma dos {cont} valores é {soma}")
