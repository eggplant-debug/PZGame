from const import *
import image
import sunflower
import pygame
class Game(object):
    def __init__(self,ds) -> None:
        self.ds = ds
        self.back = image.Image(PATH_BACK,0,
                                pos=(0,0),
                                size=GAME_SIZE,
                                pathIndexCount=0)
        self.plants= []
        self.summons=[]
        # 二维矩阵，是否有植物
        self.hasPlants=[]
        for i in range(GRID_COUNT[0]):
            col = []
            for j in range(GRID_COUNT[1]):
                col.append(0)
            self.hasPlants.append(col)

     
    def getIndexByPos(self,pos):
        x=(pos[0]-LEFT_TOP[0])//GRID_SIZE[0]
        y=(pos[1]-LEFT_TOP[1])//GRID_SIZE[1]
        return x,y
    
    def draw(self):
        self.back.draw(self.ds)
        for plant in self.plants:
            plant.draw(self.ds)
        for summon in self.summons:
            summon.draw(self.ds)

    def update(self):
        self.back.update(self.ds)
        for plant in self.plants:
            plant.update()
            if plant.hasSummon():
                summ = plant.doSummon()
                self.summons.append(summ)
        for summon in self.summons:
            summon.update()

    def addSunFlower(self,x,y):
        """
        抽离出添加向日葵的逻辑，为后面鼠标响应事件做打算
        """
        if x<0 or x>=GRID_COUNT[0]:
            return
        if y<0 or y>=GRID_COUNT[1]:
            return


        if self.hasPlants[x][y]==1:
            return
        pos = LEFT_TOP[0]+x*GRID_SIZE[0],LEFT_TOP[1]+y*GRID_SIZE[1]
        sf = sunflower.SunFlower(SUNFLOWER_ID,pos)
        self.plants.append(sf)
        self.hasPlants[x][y]=1

        
    
    def checkLoot(self,mousePos):
        for summon in self.summons:
            if not summon.checkCanLoot():
                continue
            rect = summon.getRect()
            if rect.collidepoint(mousePos):
                self.summons.remove(summon)
                return True
        return False
            


    def checkAddPlant(self,mousePos,PlantId):
        x,y = self.getIndexByPos(mousePos)
        if PlantId == SUNFLOWER_ID:
            self.addSunFlower(x,y)


    def mouseClickHandler(self,btn):
        mousePos = pygame.mouse.get_pos()
        if self.checkLoot(mousePos):
            return
        if btn == 1:

            self.checkAddPlant(mousePos,SUNFLOWER_ID)
