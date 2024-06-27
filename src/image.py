import pygame


class Image(pygame.sprite.Sprite):
    def __init__(self, path,size) -> None:
        self.path = path
        self.size = size
        self.image = pygame.image.load(path)
        #缩放图片对象
        self.image= pygame.transform.scale(self.image, self.size)
    def draw(self, ds):
        ds.blit(self.image,self.image.get_rect())