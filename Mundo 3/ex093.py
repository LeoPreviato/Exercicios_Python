print(" Cadastro de jogador de Futebol ".center(60, '='))
# Imprime um título centralizado com 60 caracteres preenchidos por '='

dados = dict()
# Cria um dicionário vazio para guardar os dados do jogador

lista_gols = list()
# Cria uma lista vazia para armazenar os gols de cada partida

dados['Nome'] = str(input("Nome do Jogador: ")).strip().capitalize()
# Pede o nome do jogador, remove espaços extras e deixa a primeira letra maiúscula
# Guarda no dicionário com a chave 'Nome'

partidas = int(input(f"Quantas partidas {dados['Nome']} jogou? R: "))
# Pergunta quantas partidas o jogador jogou

cont = 1
# Contador para controlar o while

tot_gols = 0
# Variável que vai somar todos os gols

while cont <= partidas:
    # Loop que roda enquanto o contador for menor ou igual ao número de partidas

    gols = int(input(f"Quantos gols na partida {cont}? R: "))
    # Pede quantos gols fez nessa partida

    tot_gols += gols
    # Soma os gols dessa partida ao total geral

    lista_gols.append(gols)
    # Adiciona os gols dessa partida na lista

    cont += 1
    # Incrementa o contador (vai para a próxima partida)

dados['Gols'] = lista_gols
# Guarda a lista de gols dentro do dicionário

dados['Total'] = tot_gols
# Guarda o total de gols no dicionário

print("=" * 60)

print(dados)
# Mostra o dicionário completo (debug/visualização rápida)

print("=" * 60)

for k, v in dados.items():
    # Percorre cada chave (k) e valor (v) do dicionário

    print(f"O campo {k} tem o valor {v}.")
    # Mostra cada campo separadamente

print("=" * 60)

print(f"O jogador {dados['Nome']} jogou {partidas} partidas.")
# Mostra quantas partidas o jogador jogou

for pos, g in enumerate(lista_gols):
    # enumerate fornece posição (pos) e valor (g) da lista

    print(f"   - Na partida {pos+1}, fez {g} gols.")
    # Mostra os gols de cada partida

print(f"Foi um total de {dados['Total']}")
# Mostra o total de gols marcados
