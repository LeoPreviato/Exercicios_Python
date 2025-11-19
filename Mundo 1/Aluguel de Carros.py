# imprime uma linha com 20 caracteres '=' como separador visual
print("=" * 20)

# imprime o título centralizado em uma largura de 20 caracteres
print("Aluguel de Carros!!!".center(20))

# imprime outra linha de separador
print("=" * 20)

# lê do usuário quantos quilômetros foram percorridos e converte para inteiro
km_percorrido = int(input("Digite quantos km você percorreu com o carro: "))

# lê do usuário quantos dias o carro ficou alugado e converte para inteiro
dias_alugado = int(input("Agora digite quantos dias você ficou com o carro: "))

# calcula o total a pagar: R$0.15 por km mais R$60 por dia
total_pagar = (km_percorrido * 0.15) + (dias_alugado * 60)

# exibe o valor total a pagar (pode ser decimal)
print(f"Você tera que pagar um total de R${total_pagar}")
