# imprime uma linha de 30 caracteres "=" como separador visual
print("=" * 30)

# imprime o título centralizado em uma largura de 30 caracteres
print("Reajuste Salarial".center(30))

# imprime outra linha de separador
print("=" * 30)

# solicita ao usuário o salário atual e converte a entrada (string) para float
salario_atual = float(input("Digite o seu salário atual R$:"))

# calcula o novo salário aplicando 15% de aumento sobre o salário atual
novo_salario = salario_atual + (salario_atual * 15 / 100)

# exibe o salário antigo (valor lido)
print(f"Seu salário antigo era de R${salario_atual}.")

# exibe o novo salário após o aumento de 15%
print(f"Agora com 15% de aumento será R${novo_salario}.")
