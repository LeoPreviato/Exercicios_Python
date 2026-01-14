# Importa a função randint para gerar números aleatórios
from random import randint

# Importa a função sleep para criar pequenas pausas no programa
from time import sleep

# Importa a biblioteca pygame para trabalhar com sons
import pygame

# Título do jogo centralizado
print(" Jogo da Adivinhação V.2.0 ".center(45, "="))
print()

# Inicializa a contagem de tentativas (já começa em 1 pelo primeiro palpite)
num_palpites = 1

# Inicializa todos os módulos do pygame
pygame.init()

# Linha decorativa
print("=" * 45)

# Pede o nome do jogador, remove espaços extras e capitaliza o nome
nome_jogador = str(input("Primeiro digite o nome do jogador: ")).strip().capitalize()

# Pequena pausa para melhorar a experiência do usuário
sleep(0.8)

# Jogador escolhe um número
num_jogador = int(input("Agora digite um número para jogar: "))

# Linha decorativa
print("=" * 45)

# Computador sorteia um número entre 1 e 10
num_computador = randint(1, 10)

# Enquanto o jogador não acertar o número
while num_jogador != num_computador:
    # Carrega o som de erro
    som = pygame.mixer.Sound("ex058_som2.mp3")

    # Toca o som de erro
    som.play()

    # Pede um novo número ao jogador
    num_jogador = int(input("Você errou ❌, digite novamente o número: "))

    # Soma mais uma tentativa
    num_palpites += 1

# Linha decorativa ao acertar
print("=" * 45)

# Carrega o som de acerto
som = pygame.mixer.Sound("ex058_som1.mp3")

# Mensagem de parabéns com o total de tentativas
print(f"Parabéns jogador, você acertou com {num_palpites} tentativas! ✅")

# Pequena pausa antes do som final
sleep(0.8)
print()

# Toca o som de acerto
efeito_sorono = som.play()

# Mantém o programa rodando enquanto o som estiver tocando
while efeito_sorono.get_busy():
    pygame.time.Clock().tick(10)

# Mensagem final personalizada
print(f"Foi um prazer jogar com você {nome_jogador}!")

# Encerra o pygame corretamente
pygame.quit()
