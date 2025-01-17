from const import *
import image
import sunflower
import pygame
import time
import random
import zombiebase
import data_object
import peashooter
import asyncio
import asyncclient
from share.const import *
class Game(object):
    def __init__(self,ds) -> None:
        self.ds = ds
        self.back = image.Image(PATH_BACK,0,
                                pos=(0,0),
                                size=GAME_SIZE,
                                pathIndexCount=0)
        
        self.lose = image.Image(PATH_LOSE,0,
                                pos=(0,0),
                                size=GAME_SIZE,
                                pathIndexCount=0)
        self.isGameOver = False
        self.plants= []
        self.zombies=[]
        self.summons=[]
        self.gold=100
        self.goldFont = pygame.font.Font(None, 60)

        self.killedZombie = 0
        self.zombieFont = pygame.font.Font(None, 60)


        # 二维矩阵，是否有植物
        self.hasPlants=[]
        self.zombieGenerateTime=0

        for i in range(GRID_COUNT[0]):
            col = []
            for j in range(GRID_COUNT[1]):
                col.append(0)
            self.hasPlants.append(col)


        self.client = asyncclient.AsyncClient(self,SERVER_IP,SERVER_PORT)

     
    def getIndexByPos(self,pos):
        x=(pos[0]-LEFT_TOP[0])//GRID_SIZE[0]
        y=(pos[1]-LEFT_TOP[1])//GRID_SIZE[1]
        return x,y
    
    def renderFont(self):
        textimage=self.goldFont.render("Gold:"+str(self.gold),True,(0,0,0))
        self.ds.blit(textimage,(13,20))

        textimage=self.goldFont.render("Gold:"+str(self.gold),True,(255,255,255))
        self.ds.blit(textimage,(10,20))


        textimage=self.zombieFont.render("Score:"+str(self.killedZombie),True,(0,0,0))
        self.ds.blit(textimage,(13,60))

        textimage=self.zombieFont.render("Score:"+str(self.killedZombie),True,(255,255,255))
        self.ds.blit(textimage,(10,60))


    def draw(self):
        self.back.draw(self.ds)
        for plant in self.plants:
            plant.draw(self.ds)
        for summon in self.summons:
            summon.draw(self.ds)
        for zom in self.zombies:
            zom.draw(self.ds)

        self.renderFont()

        if self.isGameOver:
            self.lose.draw(self.ds)

    def update(self):
        print("gold:",self.gold)
        self.back.update(self.ds)
        for plant in self.plants:
            plant.update()
            if plant.hasSummon():
                summ = plant.doSummon()
                self.summons.append(summ)
        for summon in self.summons:
            summon.update()
        
        for zom in self.zombies:
            zom.update()

        # 僵尸时间检查
        if time.time()-self.zombieGenerateTime>ZOMIE_GENERATE_TIME:
            self.zombieGenerateTime=time.time()
            self.addZombie(ZOMIE_BORN_X,random.randint(0,GRID_COUNT[1]-1))

        self.checkSummonVSZombie()
        self.checkZombieVSPlant()


        for zom in self.zombies:
            if zom.getRect().x<0:
                self.isGameOver=True

        for summon in self.summons:
            if summon.getRect().x>GAME_SIZE[0] or summon.getRect().y>GAME_SIZE[1]:
                self.summons.remove(summon)

                # 思考下为啥要break 
                break
            
    def checkZombieVSPlant(self):
        for zom in self.zombies:
            for plant in self.plants:
                if zom.isCollide(plant):
                    self.fight(zom,plant)
                    if plant.hp<=0:
                        self.plants.remove(plant)





    def checkSummonVSZombie(self):
        for summon in self.summons:
            for zom in self.zombies:
                if summon.isCollide(zom):
                    self.fight(summon,zom)
                    if zom.hp<=0:
                        self.zombies.remove(zom)
                        self.killedZombie+=1
                        
                    if summon.hp<=0:
                        self.summons.remove(summon)

                    return
                
    




    def addZombie(self,x,y):
        pos = LEFT_TOP[0]+x*GRID_SIZE[0],LEFT_TOP[1]+y*GRID_SIZE[1]
        zm = zombiebase.ZombieBase(1,pos)
        self.zombies.append(zm)

        

    def addSunFlower(self,x,y):
        """
        抽离出添加向日葵的逻辑，为后面鼠标响应事件做打算
        """
       
        pos = LEFT_TOP[0]+x*GRID_SIZE[0],LEFT_TOP[1]+y*GRID_SIZE[1]
        sf = sunflower.SunFlower(SUNFLOWER_ID,pos)
        self.plants.append(sf)
        self.hasPlants[x][y]=1


    def addPeaShooter(self,x,y):
        """
        抽离出添加向日葵的逻辑，为后面鼠标响应事件做打算
        """
       
        pos = LEFT_TOP[0]+x*GRID_SIZE[0],LEFT_TOP[1]+y*GRID_SIZE[1]
        sf = peashooter.PeaShooter(PEASHOOTER_ID,pos)
        self.plants.append(sf)
        self.hasPlants[x][y]=1
    
        
    
    def checkLoot(self,mousePos):
        for summon in self.summons:
            if not summon.checkCanLoot():
                continue
            rect = summon.getRect()
            if rect.collidepoint(mousePos):
                self.summons.remove(summon)
                self.gold+=summon.getPrice()
                return True
        return False
            


    def checkAddPlant(self,pos,objId):
        x,y = pos
        """
        return 的逻辑最好全放在一起
        
        """
        if self.gold<data_object.data[objId]['PRICE']:
            return
        if x<0 or x>=GRID_COUNT[0]:
            return
        if y<0 or y>=GRID_COUNT[1]:
            return
        if self.hasPlants[x][y]==1:
            return
        
        
        self.gold -= data_object.data[objId]['PRICE']
        if objId == SUNFLOWER_ID:
            self.addSunFlower(x,y)
        elif objId == PEASHOOTER_ID:
            self.addPeaShooter(x,y)
        
    def fight(self,a,b):
        while True:
            a.hp -= b.attk
            b.hp -= a.attk
            if a.hp<=0:
                return False
            if b.hp<=0:
                return True
        return False

    def mouseClickHandler(self,btn):
        if self.isGameOver:
            return 

        mousePos = pygame.mouse.get_pos()
        if self.checkLoot(mousePos):
            return
        if btn == 1:

            self.checkAddPlant(mousePos,SUNFLOWER_ID)

            asyncio.run(self.client.c2s({"type":C2S_ADD_FLOWER,"pos":self.getIndexByPos(mousePos)}))

        elif btn == 2:
            self.checkAddPlant(self.getIndexByPos(mousePos),PEASHOOTER_ID)