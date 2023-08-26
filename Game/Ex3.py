import pygame, sys
from pygame.locals import *
WINDOWWIDTH = 400 # Chiều dài cửa sổ
WINDOWHEIGHT = 300 # Chiều cao cửa sổ
# Lập sẵn các màu sắc
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)
pygame.init()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('30 hKhanh = Ex7.3: Vẽ hình đơn giản')
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit() # thoát game
            sys.exit()
    DISPLAYSURF.fill(WHITE)
    pygame.draw.rect(DISPLAYSURF, RED, (10, 10, 100, 50))# Hình chữ nhật
    pygame.draw.rect(DISPLAYSURF, GREEN, (150, 10, 100, 50), 2)#Hình chữ nhật rỗng
    pygame.draw.circle(DISPLAYSURF, RED, (50, 100), 20) # Hình tròn
    pygame.draw.circle(DISPLAYSURF, BLUE, (200, 100), 20, 1)# Hình tròn rỗng
    pygame.draw.ellipse(DISPLAYSURF, RED, (10, 150, 100, 50))# Hình elip
    pygame.draw.ellipse(DISPLAYSURF, GREEN, (150, 150, 100, 50), 3)#Hình elip rỗng
    pygame.draw.polygon(DISPLAYSURF, RED, ((10, 220), (150, 230), (100 ,290), (30, 270)))#Đa giác
    pygame.draw.polygon(DISPLAYSURF, BLUE, ((160, 220), (300, 230), (250 ,290), (180, 270)), 2)#Đa giác rỗng
    pygame.draw.line(DISPLAYSURF, BLACK, (300, 50), (350, 150), 4)# Đoạn thẳng
    pygame.display.update() # hiện thị