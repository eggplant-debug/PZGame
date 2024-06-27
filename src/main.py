import pygame
import sys
import image
pygame.init()


# 创建窗口
DS = pygame.display.set_mode((1280, 600))
img = image.Image('pic/other/back.png',(0,0),(1280, 600))
img_zb = image.Image('pic/zombie/0/0.png',(1280,200),(100, 128))
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            #R G B
    DS.fill((255, 0, 255))
    img.draw(DS)
    img_zb.doleft(0.3)
    img_zb.draw(DS)
    pygame.display.update()
