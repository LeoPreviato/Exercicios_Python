# Exibe o título do jogo centralizado
print(" GAME: Pedra, Papel e Tesoura ".center(50, "="))

# Importa a função choice para sorteio
from random import choice

# Importa a função sleep para criar pausas no jogo
from time import sleep

# Importa a biblioteca pygame para tocar sons
import pygame

# Inicializa todos os módulos do pygame
pygame.init()

# Solicita a escolha do jogador, removendo espaços e padronizando a escrita
escolha_jogador = str(input("Escolha Pedra, Papel ou Tesoura para começar: ")).strip().capitalize()

# Lista com as opções válidas do jogo
opcoes = ["Pedra", "Papel", "Tesoura"]

# Valida a escolha do jogador
# Se a opção não estiver na lista, o jogo é encerrado
if escolha_jogador not in opcoes:
    sleep(0.9)
    print("Opção invalida. Escolha Pedra, Papel ou Tesoura")
    pygame.quit()
    exit()

# Linha em branco para organização visual
print()

# Pequena pausa antes do jogo continuar
sleep(0.9)

# Mensagem indicando que o computador vai jogar
print("Minha vez...")

print()
sleep(0.9)

# Sorteia aleatoriamente a escolha do computador
escolha_computador = choice(["Pedra", "Papel", "Tesoura"])

# Animação clássica do Jokenpô
print("JO")
sleep(0.9)

print("KEN")
sleep(0.9)

print("PO!")

print()
sleep(0.9)

# Exibe a escolha do computador
print(f"Eu escolhi {escolha_computador}", end="")

# Exibe o emoji correspondente à escolha do computador
if escolha_computador == "Pedra":
    print("👊")
elif escolha_computador == "Papel":
    print("🖐")
else:
    print("✌️")

print()
sleep(0.9)

# Verifica o resultado do jogo
# Caso as escolhas sejam iguais, ocorre empate
if escolha_jogador == escolha_computador:
    som = pygame.mixer.Sound("ex045_SomEmpate.mp3")
    print("Deu empate!")

# Verifica todas as combinações possíveis de vitória do jogador
elif (
    (escolha_jogador == "Pedra" and escolha_computador == "Tesoura") or
    (escolha_jogador == "Papel" and escolha_computador == "Pedra") or
    (escolha_jogador == "Tesoura" and escolha_computador == "Papel")
):
    som = pygame.mixer.Sound("ex045_SomGanhou.mp3")
    print("Você ganhou!")

# Caso nenhuma das condições acima seja atendida, o jogador perde
else:
    som = pygame.mixer.Sound("ex045_SomPerdeu.mp3")
    print("Você perdeu!")

# Reproduz o efeito sonoro correspondente ao resultado
som.play()

# Aguarda tempo suficiente para o som tocar completamente
sleep(3.5)

# Encerra o pygame corretamente
pygame.quit()
