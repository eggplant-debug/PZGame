import objectbase

class ZombieBase(objectbase.ObjectBase):

    def checkPosition(self):
        b=super(ZombieBase,self).checkPosition()
        if b:
            self.pos[0]-=2
            
        return b