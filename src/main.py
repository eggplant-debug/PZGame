import pygame
import sys
import image
from const import *
import zombiebase
import peabullet
import sunlight
import sunflower
pygame.init()


# 创建窗口
DS = pygame.display.set_mode(GAME_SIZE)
img = image.Image(PATH_BACK,0,(0,0),GAME_SIZE,0)
zombie = zombiebase.ZombieBase(1,(1280,200))
Peabullet =peabullet.PeaBulletBase(0,(0,200))
Sunlight = sunlight.SunLightBase(2,(200,300))

sfList = []
for i in range(GRID_COUNT[0]):
    for j in range(GRID_COUNT[1]):
        pos = LEFT_TOP[0]+i*GRID_SIZE[0],LEFT_TOP[1]+j*GRID_SIZE[1]
        sf = sunflower.SunFlower(3,pos)
        sfList.append(sf)
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
    Peabullet.update()
    Peabullet.draw(DS)

    Sunlight.update()
    Sunlight.draw(DS)

    for sf in sfList:
        sf.update()
        sf.draw(DS)
    pygame.display.update()
