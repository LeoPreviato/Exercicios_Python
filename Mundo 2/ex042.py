# Exibe um título centralizado com 50 caracteres, preenchendo com '='
print(" Analisando Triângulo V.2.0 ".center(50, "="))

# Solicita ao usuário o valor do lado A e converte para inteiro
lA = int(input("Digite o valor do lado A: "))

# Solicita ao usuário o valor do lado B e converte para inteiro
lB = int(input("Digite o valor do lado B: "))

# Solicita ao usuário o valor do lado C e converte para inteiro
lC = int(input("Digite o valor do lado C: "))

# Verifica a condição de existência de um triângulo
# Cada lado deve ser menor que a soma dos outros dois
if lA < lB + lC and lB < lA + lC and lC < lA + lB:

    # Verifica se todos os lados são iguais
    if lA == lB == lC:
        print("Os lados formam um triângulo EQUILÁTERO.")

    # Verifica se pelo menos dois lados são iguais
    elif lA == lB or lB == lC or lA == lC:
        print("Os lados formam um triângulo ISÓSCELES.")

    # Caso nenhum dos lados seja igual, o triângulo é escaleno
    else:
        print("Os lados formam um triângulo ESCALENO")

# Caso a condição de existência não seja atendida, não forma triângulo
else:
    print("Os valores NÃO formam um triângulo.")
