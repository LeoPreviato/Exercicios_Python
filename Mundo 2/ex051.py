# Exibe o título do programa centralizado, usando '=' como preenchimento
print(" Progressão Aritmética ".center(50, "="))

# Linha em branco para melhorar a organização visual
print()

# Solicita ao usuário o primeiro termo da Progressão Aritmética (a₁)
primeiro_termo = int(input("Digite o primeiro termo da PA: "))

# Solicita ao usuário a razão da Progressão Aritmética (r)
razao = int(input("Agora digite a razão da PA: "))

# Linha em branco para separar a entrada da saída
print()

# Laço de repetição que será executado 11 vezes (de 0 até 10)
# Cada repetição representa a posição do termo na PA
for cont in range(1, 11):
    # Fórmula do termo geral da PA:
    # a_n = a_1 + (n - 1) * r
    # Aqui, 'cont' começa em 0, então a fórmula fica adaptada:
    # termo = primeiro_termo + cont * razao
    PA = primeiro_termo + (cont - 1) * razao

    # Exibe cada termo da PA na mesma linha, separado por " - "
    # O parâmetro end evita a quebra de linha automática
    print(PA, end=" - ")

# Mensagem final indicando o término da progressão
print("Fim da Progressão Aritmética!")
