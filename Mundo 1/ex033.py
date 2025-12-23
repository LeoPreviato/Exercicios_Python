print("=" * 40)
print("Maior e Menor Valores".center(40))  # imprime o título centralizado em 40 colunas
print("=" * 40)

# lê três números inteiros do usuário
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

# inicializa 'maior' e 'menor' com o primeiro número lido
maior = num1
menor = num1

# compara o segundo número com os valores atuais de maior e menor
if num2 > maior:
    maior = num2
if num2 < menor:
    menor = num2

# compara o terceiro número com os valores atuais de maior e menor
if num3 > maior:
    maior = num3
if num3 < menor:
    menor = num3

# exibe o maior e o menor número encontrados
print(f"O maior número é o {maior}")
print(f"E o menor é o {menor}")
