import moeda

preco = int(input("Digite o preço: R$"))

print(f"A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}")

print(f"O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}")

print(f"Aumentando 10%, temos {moeda.aumento_porcentagem(preco, 10, True)}")

print(f"Reduzindo 13%, temos {moeda.reduzindo_porcentagem(preco, 13, True)}")
