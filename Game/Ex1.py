import pygame, sys
from pygame.locals import *
pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('30 hKhanh = Ex7.1: Màn hình (cửa sổ) Game')
#B4: Vòng lặp chạy liên tục Game cho đến khi nhận sự kiện QUIT (nút x : trên, phải)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit() # thoát game
            sys.exit() # thoát hệ thống (tức là OS)
        ############MINH HỌA VẼ##############
    DISPLAYSURF.fill((255, 255, 255))