import pygame
import sys
import image
from const import *
import objectbase
pygame.init()


# 创建窗口
DS = pygame.display.set_mode(GAME_SIZE)
img = image.Image(PATH_BACK,0,(0,0),GAME_SIZE,0)
zombie = objectbase.ObjectBase('pic/zombie/0/%d.png',0,(1280,200),(100, 128),15)
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            #R G B
    DS.fill((255, 0, 255))
    img.draw(DS)
    zombie.update()
    zombie.draw(DS)
    pygame.display.update()
