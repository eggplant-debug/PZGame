import objectbase
import peabullet

class PeaShooter(objectbase.ObjectBase):
    def __init__(self, id, pos):
        super().__init__(id, pos)
        self.hasBullet=False
    def preSummon(self):
        self.hasBullet=True

    def hasSummon(self):
        """
        决定是否可以产生子弹
        """
        return self.hasBullet
    def doSummon(self):
        if self.hasSummon():
            self.hasBullet=False
            return peabullet.PeaBulletBase(0,(self.pos[0]+20,self.pos[1]+30))