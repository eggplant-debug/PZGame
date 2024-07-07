import objectbase
import peabullet
import time

class PeaShooter(objectbase.ObjectBase):
    def __init__(self, id, pos):
        super().__init__(id, pos)
        self.hasBullet=False
        self.hasShoot=False
    def preSummon(self):
        """
        前摇动画，hasShoot为True时才会播放
        """
        self.hasShoot=True
        self.pathIndex=0


    def hasSummon(self):
        """
        决定是否可以产生子弹
        """
        return self.hasBullet
    def doSummon(self):
        if self.hasSummon():
            self.hasBullet=False
            return peabullet.PeaBulletBase(0,(self.pos[0]+self.size[0]-10,self.pos[1]+30))
        
    def checkImageIndex(self):
        """
        自驱动帧动画
        """
        if(time.time()-self.preIndextime)<self.getImageIndexCD():
            return
        self.preIndextime=time.time()
        idx = self.pathIndex+1
        if idx ==8 and self.hasShoot:
            self.hasBullet=True
        if idx >= self.pathIndexCount:
            """
            因为8之前都是播放动画的index，所以如果这里超了，无论cd多久，仍然是不播放shoot的动画。

            只要被重置为0后，实际也满足了shoot的条件
            """
            idx = 9
        
        self.updateIndex(idx)
