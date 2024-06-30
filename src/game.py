from const import *
import image
import sunflower
class Game(object):
    def __init__(self,ds) -> None:
        self.ds = ds
        self.back = image.Image(PATH_BACK,0,
                                pos=(0,0),
                                size=GAME_SIZE,
                                pathIndexCount=0)
        self.plants= []
        self.summons=[]

        # 创建sunflower
        for i in range(GRID_COUNT[0]):
            for j in range(GRID_COUNT[1]):
                pos = LEFT_TOP[0]+i*GRID_SIZE[0],LEFT_TOP[1]+j*GRID_SIZE[1]
                sf = sunflower.SunFlower(3,pos)
                self.plants.append(sf)

    
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