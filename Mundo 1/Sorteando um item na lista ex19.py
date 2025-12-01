# imprime um cabeçalho com 45 caracteres de largura
print("=" * 45)
print("Sorteando um item na lista!".center(45))
print("=" * 45)

# importa a função choice para selecionar um elemento aleatório de uma sequência
from random import choice

# lê quatro nomes digitados pelo usuário (um por vez)
aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")

# agrupa os nomes em uma lista para facilitar a escolha
lista_aluno = [aluno1, aluno2, aluno3, aluno4]

# escolhe aleatoriamente um nome da lista e imprime o resultado formatado
print(f"O aluno escolhido para apagar o quadro foi o {choice(lista_aluno)}!")