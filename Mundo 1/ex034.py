print("=" * 35)
# Imprime o título "Aumento Múltiplos" centralizado em 35 caracteres
print("Aumento Múltiplos".center(35))
print("=" * 35)

# Solicita ao usuário que digite o salário e converte a entrada para float (número decimal)
salario_funcionario = float(input("Digite o seu salário: R$"))

# Verifica se o salário é maior ou igual a 1250
if salario_funcionario >= 1250:
    # Calcula o aumento de 10%: novo salário = salário original + (salário * 10%)
    aumento = salario_funcionario + (salario_funcionario * 10 / 100)
    # Imprime a mensagem com o novo salário formatado com 2 casas decimais
    print(f"Você recebeu um aumento de 10%, portanto seu novo salário é R${aumento:.2f}")
else:
    # Se o salário for menor que 1250, calcula o aumento de 15%
    aumento = salario_funcionario + (salario_funcionario * 15 / 100)
    # Imprime a mensagem com o novo salário formatado
    print(f"Você recebeu um aumento de 15%, portanto seu novo salário é R${aumento:.2f}")

# Imprime uma mensagem de parabéns ao final
print("Parabéns pelo aumento!")
