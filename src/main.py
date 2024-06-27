import pygame
import sys
import image
pygame.init()


# 创建窗口
DS = pygame.display.set_mode((1280, 600))
img = image.Image('pic/other/back.png',(1280, 600))
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            #R G B
    DS.fill((255, 0, 255))
    img.draw(DS)
    pygame.display.update()
