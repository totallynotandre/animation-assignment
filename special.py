##The Special circle will actively avoid any Prey until it finally decays away






import model
from prey  import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2


class Special(Pulsator, Mobile_Simulton):
    def __init__(self,x,y):
        Mobile_Simulton.__init__(self,x,y,20,20,5,5)  
        Mobile_Simulton.randomize_angle(self)
        self.close = None
    pass

    def update(self):
        Mobile_Simulton.move(self)
        for b in model.find(lambda x: issubclass(type(x),Prey)).copy():
            if self.contains(b._x,b._y):
                model.items.remove(b) 
                self._speed = 5   
                self.close = None
        for b in model.find(lambda x: issubclass(type(x),Prey)).copy():
            if self.distance(b._x,b._y) < 200 and self.close == None:
                self.close = b
                self._angle = atan2( self._x - b._x, self._y - b._y)
                self._speed = 5

        if self.close != None:
            for b in model.find(lambda x: issubclass(type(x),Prey)).copy():
                if self.distance(b._x,b._y) < self.distance(self.close._x,self.close._y):
                    self.close = b
                    self._angle = atan2( self._x - b._x, self._y - b._y )
                    self._speed = 5
                else:
                    self._angle = atan2(  self._y - self.close._y , self._x - self.close._x)  
        self.radius -=0.1
        self.change_dimension(-0.2,-0.2)
        
        if self.radius <= 0:
            model.items.remove(self)
    def distance(self,x,y):
        return ((self._x -x)**2  + (self._y -y)**2)**.5
    
    
    def display(self,canvas):
        canvas.create_oval(self._x-self.radius,self._y-self.radius,self._x+self.radius,self._y+self.radius,fill = 'DarkSlategray1')    