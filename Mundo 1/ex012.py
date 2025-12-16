print("=" * 30)
print("Calculando Descontos!".center(30))
print("=" * 30)
# solicita ao usuário o nome do produto e armazena em 'nome_produto'
nome_produto = input("Digite o nome do produto que você pretende comprar: ")

# solicita o preço do produto, converte a entrada (string) para float e armazena em 'preço_produto'
preço_produto = float(input("Agora digite o preço dele R$"))

# calcula o novo preço aplicando 5% de desconto ao preço original
novo_preço = preço_produto - (preço_produto * 5 / 100)

# imprime a primeira parte da mensagem sem quebra de linha (end="")
print(f"O produto {nome_produto} que custava R${preço_produto}, ", end="")

# imprime a segunda parte da mensagem completando a linha com o preço com desconto
print(f"agora custara R${novo_preço} com um desconto de 5%")
