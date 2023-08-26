import pygame, sys
from pygame.locals import *
pygame.init()

DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('30 hKhanh = Ex7.2: Surface = Layer')
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit() # thoát game
            sys.exit() # thoát hệ thống (tức là OS)
    DISPLAYSURF.fill((255, 255, 255)) # tô nền trắng RGB
    surface2rect = pygame.Surface((150, 50))
    surface2rect.fill((0, 255, 0))
    pygame.draw.rect(surface2rect, (255, 0, 0), (20, 20, 50, 20))
    DISPLAYSURF.blit(surface2rect, (100, 80)) # blit = place
    pygame.display.update()