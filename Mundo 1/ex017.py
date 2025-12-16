# Exibe um cabeçalho com linhas e título centralizado
print("=" * 35)
print("Catetos e Hipotenusa".center(35))
print("=" * 35)

# Importa a função hypot da biblioteca math para calcular a hipotenusa
from math import hypot

# Lê do usuário o valor do cateto oposto e converte para float
cateto_o = float(input("Digite o valor do Cateto Oposto: "))

# Lê do usuário o valor do cateto adjacente e converte para float
cateto_ad = float(input("Agora digite o valor do Cateto Adjacente: "))

# Calcula a hipotenusa com math.hypot (faz sqrt(a*a + b*b))
# e imprime o resultado formatado com 2 casas decimais
print(f"O valor da Hipotenusa dos Catetos é {hypot(cateto_o, cateto_ad):.2f}")