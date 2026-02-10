# Mostra o título centralizado
print(" Palpites para a mega Sena ".center(55, '='))

# Importa função para gerar números aleatórios
from random import randint

# Importa função para criar pausa entre prints
from time import sleep

# Lista temporária (vai guardar os 6 números de cada jogo)
lista_temp = list()

# Lista principal (vai guardar todos os jogos)
lista_prin = list()

# Contador de jogos
cont = 1

# Pergunta quantos jogos o usuário quer
quantia_jogos = int(input("Quantos jogos você quer que eu sorteie? R: "))

# Mostra quantos jogos serão sorteados
print(f" SORTEANDO {quantia_jogos} JOGOS".center(55, '='))

# Enquanto ainda não atingir a quantidade de jogos
while cont <= quantia_jogos:

    # Enquanto a lista temporária não tiver 6 números
    while len(lista_temp) < 6:

        # Sorteia um número entre 1 e 60
        numeros = randint(1, 60)

        # Só adiciona se ainda não existir na lista
        if numeros not in lista_temp:
            lista_temp.append(numeros)

    # Organiza os números em ordem crescente
    lista_temp.sort()

    # Copia os 6 números para a lista principal
    lista_prin.append(lista_temp.copy())

    # Limpa a lista temporária para o próximo jogo
    lista_temp.clear()

    # Incrementa o contador
    cont += 1

# Mostra todos os jogos gerados
for pos, j in enumerate(lista_prin):
    sleep(1)  # pausa de 1 segundo entre cada jogo
    print(f"Jogo {pos+1}: {j}")

# Mensagem final
print(" BOA SORTE! ".center(55, '='))
