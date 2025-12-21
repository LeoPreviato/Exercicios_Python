from random import randint
import pygame

# Mostra um cabeçalho simples formatado
print("=" * 45)
print("Jogo da Adivinhação V.1.0".center(45))
print("=" * 45)

# Inicializa todos os módulos do pygame (inclui mixer para som)
pygame.init()

# Lê o nome do jogador e normaliza (remove espaços e coloca a primeira letra maiúscula)
nome = str(input("Digite seu nome: ")).strip().capitalize()
# Lê o número que o jogador escolhe (pode lançar ValueError se não for inteiro)
num = int(input("Agora digite um número para jogar: "))

# Computador escolhe um número aleatório entre 0 e 5 (inclusive)
computador = randint(0, 5)

# Compara escolha do jogador com a do computador e carrega o som correspondente
if num == computador:
    print("Parabéns jogador, você acertou!!!")
    # Carrega o efeito sonoro de acerto (verificar se o arquivo existe no diretório)
    som = pygame.mixer.Sound("ex028_som1.mp3")
else:
    print(f"você errou!!!, eu digitei o número {computador}")
    # Carrega o efeito sonoro de erro
    som = pygame.mixer.Sound("ex028_som2.mp3")

# Reproduz o som e obtém o objeto Channel retornado por play()
efeito_sonoro = som.play()

# Aguarda enquanto o som estiver tocando; usa Clock.tick para não travar a CPU
while efeito_sonoro.get_busy():
    pygame.time.Clock().tick(10)

# Mensagem final para o jogador
print(f"Foi um prazer jogar com você {nome}!")

# Encerra todos os módulos do pygame
pygame.quit()
