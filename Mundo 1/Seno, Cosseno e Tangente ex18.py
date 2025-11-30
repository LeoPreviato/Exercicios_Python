# Exibe um cabeçalho com linhas e título centralizado
print("=" * 40)
print("Seno, Cosseno e Tangente".center(40))
print("=" * 40)

# Importa funções necessárias: converte graus -> radianos e calcula seno, cosseno e tangente
from math import radians, sin, cos, tan

# Lê do usuário um ângulo em graus (aceita decimais) e converte para float
angulo_qualquer = float(input("Digite um ângulo qualquer: "))

# Converte o ângulo de graus para radianos, exigido pelas funções trigonométricas do módulo math
conversao_radianos = radians(angulo_qualquer)

# Calcula e mostra o seno do ângulo com duas casas decimais
print(f"O seno de {angulo_qualquer} é {sin(conversao_radianos):.2f}")
# Calcula e mostra o cosseno do ângulo com duas casas decimais
print(f"O cosseno de {angulo_qualquer} é {cos(conversao_radianos):.2f}")
# Calcula e mostra a tangente do ângulo com duas casas decimais
print(f"E o tangente de {angulo_qualquer} é {tan(conversao_radianos):.2f}")