import pygame


class Image(pygame.sprite.Sprite):
    def __init__(self, pathFmt,pathIndex,pos,size=None,pathIndexCount=0) -> None:
        self.pathFmt = pathFmt
        self.pathIndex = pathIndex
        self.size = size
        self.pos = list(pos)
        self.pathIndexCount=pathIndexCount
        #缩放图片对象
        self.updateimage()

    #index改变需要调upateimage
    def updateIndex(self,pathIndex):
        self.pathIndex=pathIndex
        self.updateimage()

    #size改变需要调upateimage
    def updateSize(self,size):
        self.size=size
        self.updateimage()


    def updateimage(self):
        path = self.pathFmt
        if self.pathIndexCount!=0:
            path = path % self.pathIndex 
        self.image = pygame.image.load(path)
        if self.size!=None:
            self.image= pygame.transform.scale(self.image, self.size)

    def getRect(self):
        rect = self.image.get_rect()
        rect.x,rect.y = self.pos
        return rect

    #僵尸做移动的功能
    def doleft(self, speed):
        # 注意 pos不能是tuple，要用list
        self.pos[0] -= speed


    def draw(self, ds):
        ds.blit(self.image,self.getRect())