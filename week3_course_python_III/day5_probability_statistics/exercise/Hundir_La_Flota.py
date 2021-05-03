import pygame, sys

pygame.init()

pantalla = (1280, 720)
pygame.display.set_mode((pantalla))
pygame.display.set_caption('Hundir la Flota')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()