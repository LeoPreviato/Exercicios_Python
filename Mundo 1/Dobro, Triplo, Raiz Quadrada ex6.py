"""Programa que calcula e mostra o dobro, o triplo e a raiz quadrada de um número.

Entrada: um número inteiro fornecido pelo usuário via input().
Saída: mensagens com os resultados calculados.
"""

# Linha de separador para melhorar a apresentação no terminal
print("=" * 40)

# Título centralizado em largura 40
print("Dobro, Triplo, Raiz Quadrada!".center(40))

# Outra linha de separador
print("=" * 40)

# Solicita que o usuário digite um número e converte a entrada para inteiro.
# Observação: se o usuário digitar algo que não seja um número válido, ocorrerá ValueError.
num_usu = int(input("Digite um número qualquer: "))

# Linha separadora antes dos resultados
print("-" * 40)

# Mostra o dobro do número (n * 2)
print(f"O dobro de {num_usu} é {num_usu * 2}.")

# Espaço em branco para separar visualmente as saídas
print()

# Mostra o triplo do número (n * 3)
print(f"O triplo de {num_usu} é {num_usu * 3}.")

# Espaço em branco para separar visualmente as saídas
print()

# Calcula a raiz quadrada usando exponenciação (n ** 0.5) e formata com 1 casa decimal
print(f"E a raiz quadrada de {num_usu} é {num_usu ** (1/2):.1f}")
