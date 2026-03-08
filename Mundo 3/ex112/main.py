
from utilidadesCev import moeda, dados

# Lê e valida o valor monetário informado pelo usuário.
valor = dados.leiaDinheiro("Digite o preço: R$")

# Exibe análise com aumento e redução percentuais predefinidos.
moeda.resumo(valor, 80, 35)
