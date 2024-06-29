import objectbase

class PeaBulletBase(objectbase.ObjectBase):



    def checkPosition(self):
        b=super(PeaBulletBase,self).checkPosition()
        if b:
            self.pos[0]+=4
            
        return b