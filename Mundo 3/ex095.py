# Dicionário que vai guardar os dados de UM jogador por vez
dados_jogador = dict()

# Lista principal que vai guardar TODOS os jogadores cadastrados
lista_jogador = list()

# Laço principal para cadastrar vários jogadores
while True:

    # Lista de gols nasce vazia a cada novo jogador
    lista_gols = list()

    # Recebe o nome do jogador
    dados_jogador['Nome'] = str(input("Nome do Jogador: ")).strip().capitalize()

    # Quantidade de partidas jogadas
    num_partidas = int(input(f"Quantas partidas {dados_jogador['Nome']} jogou? R: "))

    cont = 1          # contador de partidas
    tot_gols = 0      # acumulador do total de gols

    # Laço para cadastrar os gols de cada partida
    while cont <= num_partidas:
        gols = int(input(f"Quantos gols na partida {cont}? R: "))

        # Adiciona os gols da partida na lista
        lista_gols.append(gols)

        # Soma os gols ao total
        tot_gols += gols

        cont += 1

    # Salva a lista de gols no dicionário do jogador
    dados_jogador['Gols'] = lista_gols

    # Salva o total de gols do jogador
    dados_jogador['Total'] = tot_gols

    # Adiciona uma cópia do dicionário na lista principal
    lista_jogador.append(dados_jogador.copy())

    # Pergunta se o usuário quer continuar cadastrando
    opc = input("Quer continuar? [S/N]: ").strip().upper()
    print("=" * 60)

    # Validação da opção
    while opc == "" or opc[0] not in "SN":
        opc = input("Opção invalida. Digite novamente: ").strip().upper()
        print("=" * 60)

    # Usa apenas a primeira letra válida
    opc = opc[0]

    # Se escolher N, encerra o cadastro
    if opc == "N":
        break

# Cabeçalho da tabela
print(f"{'Cod':<4}{'Nome':<12}{'Gols':<25}{'Total':>6}")
print("-" * 60)

# Mostra todos os jogadores cadastrados
for pos, v in enumerate(lista_jogador):
    gols_str = str(v['Gols'])  # transforma a lista em string para alinhar
    print(f"{pos:<4}{v['Nome']:<12}{gols_str:<25}{v['Total']:>6}")

print("-" * 60)

# Laço para mostrar o levantamento individual de cada jogador
while True:
    escolha_jogador = int(input("Mostrar dados de qual jogador? R: "))
    print("-" * 60)

    # Código de saída
    if escolha_jogador == 999:
        break

    # Validação do índice
    if escolha_jogador < 0 or escolha_jogador >= len(lista_jogador):
        print("Não existe nenhum jogador com esse número.")
        continue

    # Mostra o nome do jogador escolhido
    print(
        f" LEVANTAMENTO DO JOGADOR {lista_jogador[escolha_jogador]['Nome']} "
        .center(60, '=')
    )

    # Mostra os gols partida por partida
    for pos, v in enumerate(lista_jogador[escolha_jogador]['Gols']):
        print(f"- No jogo {pos+1} fez {v} gols.")

    print("-" * 60)
