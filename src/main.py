import pygame
import os 
import sys

current_path = os.path.dirname(os.path.realpath(__file__))
print(current_path)

top_path = os.path.dirname(current_path)
sys.path.append(top_path)


import image
from const import *
import zombiebase
import peabullet
import sunlight
from game import *
pygame.init()


# 创建窗口
DS = pygame.display.set_mode(GAME_SIZE)
img = image.Image(PATH_BACK,0,(0,0),GAME_SIZE,0)
game = Game(DS)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            sys.exit()
            #R G B
        elif event.type==pygame.MOUSEBUTTONDOWN:
            game.mouseClickHandler(event.button)
            
    DS.fill((255, 0, 255))
    
    game.update()
    game.draw()
    

    pygame.display.update()

