import objectbase
import sunlight
class SunFlower(objectbase.ObjectBase):
    def __init__(self, id, pos):
        super().__init__(id, pos)
        self.hasSunlight=False
    def preSummon(self):
        self.hasSunlight=True

    def hasSummon(self):
        """
        决定是否可以产生阳光了
        """
        return self.hasSunlight
    def doSummon(self):
        if self.hasSummon():
            self.hasSunlight=False
            return sunlight.SunLightBase(2,(self.pos[0]+20,self.pos[1]-10))