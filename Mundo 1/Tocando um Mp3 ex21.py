import pygame

pygame.mixer.init()

pygame.mixer.music.load("Tocando um mp3.mp3")

pygame.mixer.music.set_volume(0.7)

pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pass
