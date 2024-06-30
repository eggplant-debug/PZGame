import time
import image
import data_object
class ObjectBase(image.Image):
    def __init__(self, id, pos):
        self.preIndextime = 0
        self.prePostime=0
        self.id = id
        self.preSummontime=0

        super(ObjectBase, self).__init__(
            self.getData()['PATH'],
            0,
            pos,
            self.getData()['SIZE'], 
            self.getData()['IMAGE_INDEX_COUNT'])

    def getData(self):
        return data_object.data[self.id]

    def getSummonTimeCD(self):
        return self.getData()['SUMMON_CD']

    def getPositionCD(self):
        """
        给子类提供类似接口
        """
        return self.getData()['POSITION_CD']
    

    def getImageIndexCD(self):
        return self.getData()['IMAGE_INDEX_CD']

    def update(self):
        """
        优先调用子类方法
        """
        self.checkImageIndex()
        self.checkPosition()    
        self.checkSummon()

    def checkSummon(self):
        """
        自驱动召唤动画
        """
        if(time.time()-self.preSummontime)<self.getSummonTimeCD():
            return
        self.preSummontime=time.time()
        self.preSummon()
    
    def preSummon(self):
        pass
    
    def getPrice(self):
        return self.getData()['PRICE']


    def checkImageIndex(self):
        """
        自驱动帧动画
        """
        if(time.time()-self.preIndextime)<self.getImageIndexCD():
            return
        self.preIndextime=time.time()
        idx = self.pathIndex+1
        if idx >= self.pathIndexCount:
            idx = 0
        
        self.updateIndex(idx)

        pass
    
    def getSpeed(self):
        return self.getData()['SPEED']
    
    def checkCanLoot(self):
        return self.getData()['CAN_LOOT']

    def checkPosition(self):
        """
        自驱动平移动画
        """
        if(time.time()-self.prePostime) < self.getPositionCD():
            return False
        self.prePostime=time.time()
        
        self.pos=(self.pos[0]+self.getSpeed()[0],self.pos[1]+self.getSpeed()[1])
        
        return True

    def hasSummon(self):
        pass

    def doSummon(self):
        pass
        