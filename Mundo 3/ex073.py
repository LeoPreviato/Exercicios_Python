# Título do programa, centralizado em 65 caracteres usando "="
print(" Tuplas com Times de Futebol ".center(65, "="))


# Tupla contendo os nomes dos times do Brasileirão.
# A ordem dos times representa a classificação do campeonato.
times_br = (
    'Atlético-MG', 'Botafogo', 'Atlético-PR', 'Chapecoense', 'Coritiba',
    'Flamengo', 'Vasco da Gama', 'Cruzeiro', 'Bahia', 'EC Vitória',
    'Fluminense', 'Grêmio', 'Mirassol', 'Bragantino', 'Remo', 'Santos',
    'São Paulo', 'Corinthians', 'Internacional', 'Palmeiras'
)


# Mostra a lista completa de times com suas respectivas posições
# enumerate() fornece o índice (posição) e o nome do time
# pos + 1 é usado porque o índice começa em 0, mas a colocação começa em 1
for pos, time in enumerate(times_br):
    print(f"{pos+1}º - {time}")


# Linha separadora para organização visual
print('=' * 45)


# Exibe apenas os 5 primeiros colocados do campeonato
print("Os primeiros 5 colocados do Brasileirão são:")

# times_br[:5] pega os cinco primeiros times da tupla
for pos, time in enumerate(times_br[:5]):
    print(f"{pos+1}º - {time}")


# Linha separadora
print('=' * 45)


# Exibe os últimos 4 colocados do campeonato
print("Os últimos 4 colocados são:")

# times_br[-4] pega os times da posição 16 até o final da tupla
# pos + 17 é usado porque esses times começam na 17ª colocação
for pos, time in enumerate(times_br[-4]):
    print(f"{pos+17}º - {time}")


# Linha separadora
print('=' * 45)


# Exibe os times em ordem alfabética
print("Os times em ordem alfabética são:")

# sorted() ordena os times em ordem alfabética
# A tupla original NÃO é modificada
for pos, time in enumerate(sorted(times_br)):
    print(f"{pos+1}º - {time}")


# Linha separadora
print('=' * 45)


# Mostra a posição da Chapecoense na tabela
# index() retorna a posição do time na tupla (começa em 0)
# +1 é usado para mostrar a colocação correta
print(f"A Chapecoense está na {times_br.index('Chapecoense')+1}º posição!")


# Linha separadora final
print('=' * 45)
