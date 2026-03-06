import moeda  # importa o módulo `moeda`

preco = float(input("Digite o preço: R$"))  # lê o preço do usuário e converte para inteiro

# Usa a função `moeda.moeda()` para formatar a exibição do valor e `moeda.metade()` para calcular metade.
print(f"A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}")

# Mostra o dobro formatado (dobro também é calculado pelo módulo `moeda`).
print(f"O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}")

# A função `aumento_porcentagem` calcula o valor com aumento de 10%
print(f"Aumentando 10%, temos {moeda.moeda(moeda.aumento_porcentagem(preco, 10))}")
