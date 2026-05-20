import pygame
pygame.init()
pygame.mixer_music.load('musica.wav.mp3')
pygame.mixer_music.play()
while pygame.mixer_music.get_busy():
    pygame.time.Clock().tick(10)
