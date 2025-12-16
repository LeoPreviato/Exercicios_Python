# Importa o módulo pygame, que é uma biblioteca para desenvolvimento de jogos e multimídia em Python
import pygame

# Inicializa o mixer de áudio do pygame, necessário para reproduzir sons e músicas
pygame.mixer.init()

# Carrega o arquivo de música especificado (neste caso, "ex021.mp3") para o mixer
pygame.mixer.music.load("ex021.mp3")

# Define o volume da música para 70% (0.7 é um valor entre 0.0 e 1.0)
pygame.mixer.music.set_volume(0.7)

# Inicia a reprodução da música carregada
pygame.mixer.music.play()

# Entra em um loop que continua enquanto a música estiver sendo reproduzida (get_busy() retorna True se estiver tocando)
while pygame.mixer.music.get_busy():
    # O 'pass' é uma instrução vazia; o loop aguarda até que a música termine
    pass
