# Tupla contendo os nomes dos produtos e seus respectivos preços
tupla_produtos = ('Macbook', 6400, 'Iphone 13', 3200, 'Mesa', 400, 'Ps5', 3100,
                  'DualSense', 340, 'Pulse 3D', 550, 'Monitor', 900, 'Mochila', 550,
                  'Base Carregsmento', 150)

# Linha de separação
print("=" * 45)

# Título centralizado
print("LISTAGEM DE PREÇOS".center(45))

# Outra linha de separação
print("=" * 45)

# Percorre a tupla pulando de 2 em 2 (nome -> preço)
for i in range(0, len(tupla_produtos), 2):
    # Imprime o nome alinhado à esquerda com pontos
    # e o preço logo em seguida
    print(f"{tupla_produtos[i]:.<32}R$ {tupla_produtos[i+1]}")

# Linha final
print("=" * 45)
