# Mostra um título centralizado com '=' ocupando 60 caracteres
print(" Jogo de dados em Python ".center(60, '='))

# Importa a função randint para gerar números aleatórios
from random import randint

# Importa sleep para dar pequenas pausas no programa (efeito visual)
from time import sleep

# Cria um dicionário com 4 jogadores
# Cada jogador recebe um número aleatório de 1 a 6 (simulando um dado)
dados = {
    'Jogador 1': randint(1, 6),
    'Jogador 2': randint(1, 6),
    'Jogador 3': randint(1, 6),
    'Jogador 4': randint(1, 6)
}

# Mostra o texto inicial
print("Valores sorteados:")

# Percorre o dicionário mostrando quanto cada jogador tirou
for k, v in dados.items():
    sleep(0.8)  # pausa de 0.8 segundos
    print(f"O {k} tirou o {v} no dado")

# Linha separadora
print("=" * 60)

# Título do ranking
print("Ranking dos jogadores:")

# sorted() ordena os jogadores
# dados.items() transforma o dicionário em tuplas (Jogador, valor)
# lambda tupla: tupla[1] diz para ordenar usando o valor do dado
# reverse=True coloca do maior para o menor
ranking = sorted(dados.items(), key=lambda tupla: tupla[1], reverse=True)

# enumerate cria as posições do ranking começando em 1
for pos, jogador in enumerate(ranking, start=1):
    sleep(0.8)  # pequena pausa para efeito visual
    # jogador[0] é o nome
    # jogador[1] é o valor do dado
    print(f"{pos}º lugar: {jogador[0]} com {jogador[1]}")
