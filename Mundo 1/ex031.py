# Exibe um cabeçalho decorativo com 35 caracteres
print("=" * 35)
print("Custo da Viagem".center(35))
print("=" * 35)

# Lê a distância da viagem em quilômetros e converte para inteiro
distancia_viagem = int(input("Informe a distancia da sua viagem: "))

# Se a distância for até 200 km (inclusive), aplica tarifa de R$0,50 por km
if distancia_viagem <= 200:
    preco_passagem = distancia_viagem * 0.50
    # Exibe o preço formatado com duas casas decimais
    print(f"O preço da sua passagem será de R${preco_passagem:.2f}")
else:
    # Para distâncias acima de 200 km, aplica tarifa reduzida de R$0,40 por km
    preco_passagem = distancia_viagem * 0.40
    print(f"O preço da sua passagem será de R${preco_passagem:.2f}")

# Mensagem de despedida
print("Boa viagem!")
