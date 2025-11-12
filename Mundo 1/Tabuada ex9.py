"""Programa que exibe a tabuada de um número inteiro de 1 a 10.

Entrada: número inteiro fornecido pelo usuário.
Saída: tabuada formatada no terminal.
"""

# Imprime linha de separador para organizar a saída
print("=" * 30)

# Título centralizado
print("TABUADA!".center(30))

# Outra linha de separador
print("=" * 30)

# Mensagem de instrução ao usuário (corrigido 'tauada' para 'tabuada')
print("Digite um número qualquer para saber a sua tabuada!")

# Linha em branco para espaçamento
print()

# Solicita o número e converte para inteiro
# Observação: se o usuário digitar algo não numérico, ocorre ValueError
num_usu = int(input("Digite um número: "))

# Linha de separador antes dos resultados
print("=" * 30)

# Exibe a tabuada do número de 1 a 10
print(f"{num_usu} x 1 = {num_usu * 1}")
print(f"{num_usu} x 2 = {num_usu * 2}")
print(f"{num_usu} x 3 = {num_usu * 3}")
print(f"{num_usu} x 4 = {num_usu * 4}")
print(f"{num_usu} x 5 = {num_usu * 5}")
print(f"{num_usu} x 6 = {num_usu * 6}")
print(f"{num_usu} x 7 = {num_usu * 7}")
print(f"{num_usu} x 8 = {num_usu * 8}")
print(f"{num_usu} x 9 = {num_usu * 9}")
print(f"{num_usu} x 10 = {num_usu * 10}")

# Linha final de separador
print("=" * 30)
