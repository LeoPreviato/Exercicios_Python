# Título do programa centralizado com '='
print(" Extraindo dados de uma Lista ".center(60, '='))

# Lista vazia para armazenar os valores digitados
lista_num = []

# Loop infinito (será encerrado quando o usuário escolher não continuar)
while True:
    # Adiciona um número inteiro digitado pelo usuário à lista
    lista_num.append(int(input("Digite um valor: ")))

    # Pergunta se o usuário deseja continuar
    opcao = str(input("Você quer continuar? [S/N]: ")).strip().upper()[0]

    # Linha decorativa
    print("=" * 60)

    # Validação da opção (aceita apenas S ou N)
    while opcao not in "SN":
        opcao = str(input("Opção inválida. Digite novamente [S/N]: ")
        ).strip().upper()[0]

    # Se a opção for 'N', encerra o loop
    if opcao == "N":
        break

# Ordena a lista em ordem decrescente
lista_num.sort(reverse=True)

print("=" * 60)

# Usa len() para contar automaticamente quantos elementos existem na lista
print(f"Você digitou {len(lista_num)} elementos.")

# Mostra os valores em ordem decrescente
print(f"Os valores em ordem decrescente são: {lista_num}")

# Verifica se o número 5 está presente na lista
if 5 in lista_num:
    print("✅ O valor 5 faz parte da lista")
else:
    print("❌ O valor 5 não faz parte da lista")
