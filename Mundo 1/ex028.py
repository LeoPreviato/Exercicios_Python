from random import randint
import pygame

print("=" * 45)
print("Jogo da Adivinhação V.1.0".center(45))
print("=" * 45)

pygame.init()

nome = str(input("Digite seu nome: ")).strip().capitalize()
num = int(input("Agora digite um número para jogar: "))

computador = randint(0, 5)

if num == computador:
    print("Parabéns jogador, você acertou!!!")
    som = pygame.mixer.Sound("ex028_som1.mp3")
else:
    print("você errou!!!")
    som = pygame.mixer.Sound("ex028_som2.mp3")

efeito_sonoro = som.play()

while efeito_sonoro.get_busy():
    pygame.time.Clock().tick(10)

print(f"Foi um prazer jogar com você {nome}!")

pygame.quit()