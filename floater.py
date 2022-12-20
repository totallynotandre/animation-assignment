# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage 


##from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random, randrange, uniform


class Floater(Prey): 
    radius = 5
    def __init__(self,x,y):
        self._x = x
        self._y = y
        self._width = 10
        self._height = 10
        self._speed = 5
        self._angle = 2
        Prey.randomize_angle(self)
    pass

    def display(self,canvas):
        
        canvas.create_oval(self._x-Floater.radius,self._y-Floater.radius,self._x+Floater.radius,self._y+Floater.radius,fill = 'red')
        
        pass
    
    
    def update(self):
        if randrange(1,100) >= 70:
            if randrange(1,100) >= 50:
                self._speed = self._speed + uniform(0.1, 0.5)
                if self._speed > 7:
                    self._speed = 7
            else:
                self._speed = self._speed - uniform(0.1, 0.5)
                if self._speed < 3:
                    self._speed = 3
            if randrange(1,100) >= 50:
                self._angle= self._angle + uniform(0.1, 0.5)

            else:
                self._angle = self._angle - uniform(0.1, 0.5)

            
        Prey.move(self)
        
    def contains(self,x,y):
        if x >= self._x - 10 and x <= self._x + 10:
            if y >= self._y - 10 and y <= self._y + 10:
                
                return True
        else:
            return False