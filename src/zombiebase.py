import objectbase

class ZombieBase(objectbase.ObjectBase):
    def __init__(self, pathFmt, pathIndex, pos, size=None, pathIndexCount=0):
        super().__init__(pathFmt, pathIndex, pos, size, pathIndexCount)

    def getPositionCD(self):
        return 0.2

    def checkPosition(self):
        b=super(ZombieBase,self).checkPosition()
        if b:
            self.pos[0]-=2
            
        return b