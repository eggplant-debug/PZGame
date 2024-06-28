import objectbase

class PeaBulletBase(objectbase.ObjectBase):
    def __init__(self, pathFmt, pathIndex, pos, size=None, pathIndexCount=0):
        super(PeaBulletBase,self).__init__(pathFmt, pathIndex, pos, size, pathIndexCount)


    def getPositionCD(self):
        return 0.08

    def checkPosition(self):
        b=super(PeaBulletBase,self).checkPosition()
        if b:
            self.pos[0]+=4
            
        return b