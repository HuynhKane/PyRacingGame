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
FPS = 60 # 60 khung hình / giây
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('30 hKhanh = Ex7.4: Game đơn giản = Game CHẠY XE')
class Car():
    def __init__(self):
        self.x = 100 # Vị trí của xe
    ## Tạo surface và thêm hình chiếc xe vào ##
        self.surface = pygame.image.load('car1.png')
    def draw(self): # Hàm dùng để vẽ xe
        DISPLAYSURF.blit(self.surface, (self.x, 100))
    def update(self, moveLeft, moveRight): # Hàm dùng để thay đổi vị trí xe
        if moveLeft == True:
            self.x -= 2
        if moveRight == True:
            self.x += 2
        if self.x + 100 > WINDOWWIDTH:
            self.x = WINDOWWIDTH - 100
        if self.x < 0:
            self.x = 0
car_30hKhanh = Car()
moveLeft = False
moveRight = False
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit() # thoát game
            sys.exit() # thoát hệ thống (tức là OS)
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                 moveLeft = True
            if event.key == K_RIGHT:
                moveRight = True
        if event.type == KEYUP:
            if event.key == K_LEFT:
                moveLeft = False
            if event.key == K_RIGHT:
                moveRight = False
    DISPLAYSURF.fill(WHITE)
    car_30hKhanh.draw()
    pygame.display.update() # hiện thị
    car_30hKhanh.update(moveLeft, moveRight)
    pygame.display.update() # hiện thị
    fpsClock.tick(FPS) # nhảy đồng hồ với chu kỳ FPS