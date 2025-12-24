print("=" * 40)
# Imprime o título do programa "Analisando Triângulo V.1.0"
print("Analisando Triângulo V.1.0")
print("=" * 40)

# Solicita ao usuário o valor do lado A e converte para inteiro
lA = int(input("Digite o valor do lado A:"))

# Solicita ao usuário o valor do lado B e converte para inteiro
lB = int(input("Digite o valor do lado B: "))

# Solicita ao usuário o valor do lado C e converte para inteiro
lC = int(input("Digite o valor do lado C: "))

# Verifica a condição para formar um triângulo: cada lado deve ser menor que a soma dos outros dois
# Isso garante que os três lados podem formar um triângulo válido
if lA < lB + lC and lB < lA + lC and lC < lA + lB:
    # Se a condição for verdadeira, imprime que os valores formam um triângulo
    print("Os valores FORMAM um triângulo.")
else:
    # Se a condição for falsa, imprime que os valores não formam um triângulo
    print("Os valores NÃO formam um triângulo.")
