# Imprime o nome do programa e uma linha de 45 caracteres '=' para criar uma borda visual
print("=" * 45)
print("Sorteando uma ordem na lista!".center(45))
print("=" * 45)

# Importa a função 'shuffle' do módulo 'random', que será usada para embaralhar a lista
from random import shuffle

# Solicita ao usuário o nome dos quatro alunos
aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")

# Cria uma lista contendo os nomes dos quatro alunos
lista_alunos = [aluno1, aluno2, aluno3, aluno4]

# Embaralha aleatoriamente a ordem dos elementos na lista 'lista_alunos'
shuffle(lista_alunos)

# Imprime a mensagem final com a ordem sorteada dos alunos, usando f-string para inserir a lista
print(f"A ordem dos alunos para entregar o trabalho será: {lista_alunos}!")
