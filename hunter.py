# A Hunter class is derived from a Pulsator and then Mobile_Simulton base.
#   It inherits updating+displaying from Pusator/Mobile_Simulton: it pursues
#   any close prey, or moves in a straight line (see Mobile_Simultion).

import model
from prey  import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2


class Hunter(Pulsator, Mobile_Simulton):
    def __init__(self,x,y):
        Mobile_Simulton.__init__(self,x,y,20,20,5,5)  
        Mobile_Simulton.randomize_angle(self)
        self.close = None
        self.count = 30
    pass

    def update(self):
        Mobile_Simulton.move(self)
        for b in model.find(lambda x: issubclass(type(x),Prey)).copy():
            if self.contains(b._x,b._y):
                model.items.remove(b) 
                self._speed = 5   
                self.radius += 0.5
                self.count = 30
                self.change_dimension(1,1)
                self.close = None
        for b in model.find(lambda x: issubclass(type(x),Prey)).copy():
            if self.distance(b._x,b._y) < 200 and self.close == None:
                self.close = b
                self._angle = atan2( b._y - self._y , b._x -self._x  )
                self._speed = 5

        if self.close != None:
            for b in model.find(lambda x: issubclass(type(x),Prey)).copy():
                if self.distance(b._x,b._y) < self.distance(self.close._x,self.close._y):
                    self.close = b
                    self._angle = atan2( b._y - self._y , b._x -self._x  )
                    self._speed = 5
                else:
                    self._angle = atan2( self.close._y - self._y , self.close._x -self._x  )
        self.count = self.count - 1
        if self.count == 0:
            
            self.radius -= 0.5
            self.change_dimension(-1,-1)
            if self._height == 0:
                model.items.remove(self)
            self.count = 30
    def distance(self,x,y):
        return ((self._x -x)**2  + (self._y -y)**2)**.5