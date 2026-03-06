# Importa o modulo moeda
import moeda

# Pede ao usuário para inromar um preço
preco = int(input("Digite o preço: R$"))

# Imprime a metade do preço digitado
print(f"A metade de R${preco} é R${moeda.metade(preco)}")

# Imprime o dobro do preço digitado
print(f"O dobro de R${preco} é R${moeda.dobro(preco)}")

# Imprime o preço digitado com um aumento de 10%
print(f"Aumentando 10%, temos R${moeda.aumento_porcentagem(preco, 10)}")
