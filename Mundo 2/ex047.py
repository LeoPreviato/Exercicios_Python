# Exibe um título centralizado com 45 caracteres, preenchendo com "="
print(" Contagem de Pares ".center(45, "="))

# Linha em branco para melhorar a organização visual no terminal
print()

# Laço for que percorre apenas números pares
# range(2, 50+1, 2) significa:
# começa em 2, vai até 50 (incluindo) e pula de 2 em 2
for cont in range(2, 50+1, 2):
    # Exibe cada número par na mesma linha, separados por " - "
    print(cont, end=" - ")

# Exibe a palavra "Fim" ao final da contagem
print("Fim")

# Linha em branco para espaçamento
print()

# Mensagem final explicando o que foi exibido
print("Esses foram os números pares entre 1 a 50")
