print("=" * 40)
print("Conversor de Real para Dolar!".center(40))
print("=" * 40)
print("Digite quantos Reais você deseja gastar para comprar o Dolar?")

# Pergunta ao usuário quanto em Reais ele quer converter
# e converte a entrada (string) para um número de ponto flutuante
valor_compra = float(input("Digite aqui R$"))

# Mostra o resultado formatado com duas casas decimais
print(f"Com R${valor_compra} você poderá comprar US${valor_compra / 5.37:.2f}")# Calcula quantos Dólares serão obtidos usando uma taxa fixa (5.37)