"""Programa simples para calcular a média aritmética de duas notas.

Entrada: duas notas (podem ser decimais) fornecidas pelo usuário.
Saída: exibe a média formatada com duas casas decimais.
"""

# Linha de separador para organizar a saída no terminal
print("=" * 40)

# Título centralizado com largura 40
print("Média Aritimética.".center(40))

# Outra linha de separador
print("=" * 40)

# Solicita a primeira nota e converte para float (aceita números decimais)
# Observação: se o usuário digitar algo não numérico, ocorrerá ValueError
nota1 = float(input("Digite a primeira nota do aluno: "))

# Espaço em branco para melhorar a apresentação
print()

# Solicita a segunda nota e converte para float
nota2 = float(input("Digite a segunda nota do aluno: "))

# Espaço em branco para melhorar a apresentação
print()

# Calcula a média aritmética ((nota1 + nota2) / 2) e formata com 2 casas decimais
print(f"A média entre as notas {nota1} e {nota2} é {(nota1 + nota2) / 2:.2f}!")

# Linha final de separador
print("=" * 40)
