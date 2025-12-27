# Exibe o título centralizado em um espaço de 30 caracteres
print("=" * 30)
print("Comparando Números".center(30))
print("=" * 30)

# Solicita o primeiro número, converte o texto digitado para inteiro (int) e guarda na variável
numero1 = int(input("Digite o primeiro número: "))

# Solicita o segundo número e também o converte para inteiro
numero2 = int(input("Digite o segundo número: "))

# Inicia a estrutura condicional
if numero1 > numero2:
    # Se a primeira condição for verdadeira, executa este bloco
    print(f"O número {numero1} é o maior!")

elif numero1 < numero2:
    # Se a primeira for falsa, mas esta for verdadeira, executa este bloco
    print(f"O número {numero2} é o maior!")

else:
    # Se nenhuma das condições acima for atendida (ou seja, se forem iguais)
    print("Os dois números são iguais!")
