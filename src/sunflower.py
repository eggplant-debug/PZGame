import objectbase
import sunlight
class SunFlower(objectbase.ObjectBase):
    def __init__(self, id, pos):
        super().__init__(id, pos)
        self.sunlights=[]

    def preSummon(self):
        sl = sunlight.SunLightBase(2,(self.pos[0]+20,self.pos[1]-10))
        self.sunlights.append(sl)

    def update(self):
        super().update()
        for sl in self.sunlights:
            sl.update()


    def draw(self,ds):
        super(SunFlower,self).draw(ds)
        for sl in self.sunlights:
            sl.draw(ds)

