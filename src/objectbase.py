import time
import image
class ObjectBase(image.Image):
    def __init__(self, pathFmt, pathIndex, pos, size=None, pathIndexCount=0):
        super(ObjectBase, self).__init__(pathFmt, pathIndex, pos, size, pathIndexCount)
        self.preIndextime = 0
        self.prePostime=0
    

    def update(self):
        self.checkImageIndex()
        self.checkPosition()    


    
    def checkImageIndex(self):
        """
        自驱动帧动画
        """
        if(time.time()-self.preIndextime)<0.2:
            return
        self.preIndextime=time.time()
        idx = self.pathIndex+1
        if idx >= self.pathIndexCount:
            idx = 0
        
        self.updateIndex(idx)

        pass


    def checkPosition(self):
        """
        自驱动平移动画
        """
        if(time.time()-self.prePostime)<0.2:
            return
        self.prePostime=time.time()
        
        self.pos[0] -=2


        pass