"""Calculadora simples para pintura de parede.

O programa solicita a largura e a altura da parede (em metros), calcula a
área e estima a quantidade de tinta necessária assumindo 1 litro para cada
2 m² (ou seja, rendimento = 2 m² por litro).

Entrada: largura e altura (floats) fornecidos pelo usuário.
Saída: exibe as dimensões, a área e a quantidade de tinta necessária.
"""

# Linha separadora para melhorar a apresentação no terminal
print("=" * 30)

# Título centralizado
print("Pintando sua Parede".center(30))

# Outra linha separadora
print("=" * 30)

# Lê a largura e a altura da parede. Usamos float para aceitar medidas com
# casas decimais (por exemplo 2.5 metros). Se a entrada não for numérica,
# o programa lançará ValueError.
lar = float(input("Digite a largura da parede (em metros): "))
alt = float(input("Agora digite a altura da parede (em metros): "))

# Calcula a área em metros quadrados (m²)
area = lar * alt

# Exibe as dimensões e a área. Formatamos a largura/altura com 1 casa decimal
# e a área com 2 casas decimais para leitura agradável.
print(f"A dimensão da parede é de {lar:.1f} x {alt:.1f} m, ", end="")
print(f"e sua área é de {area:.2f} m²")

# Estimativa de tinta (rendimento de 2 m² por litro). Formatamos com 2 casas
# decimais. A lógica: litros = area / 2
print(f"Será necessário {area / 2:.2f} l de tinta para pintar a parede!")
