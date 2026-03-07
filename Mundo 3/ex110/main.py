# Importa o modulo moeda
import moeda

# Lê o valor informado pelo usuário para gerar o resumo.
preco = int(input("Digite o preço: R$"))

# Exibe análise com aumento e redução percentuais predefinidos.
moeda.resumo(preco, 80, 35)
