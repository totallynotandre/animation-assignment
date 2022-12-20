# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions 


from blackhole import Black_Hole
import model
from prey import Prey

class Pulsator(Black_Hole): 
    def __init__(self,x,y):
        Black_Hole.__init__(self,x,y)
        self.radius = 10
        self.count = 30
    pass



    def update(self):
        for b in model.find(lambda x: issubclass(type(x),Prey)).copy():
            if self.contains(b._x,b._y):
                model.items.remove(b)
                self.change_dimension(1,1)
                self.radius += 0.5  
                self.count = 30             
        self.count = self.count - 1
        if self.count <= 0:
            
            self.radius -= 0.5
            self.change_dimension(-1,-1)
            if self._height == 0:
                model.items.remove(self)
            self.count = 30
                    
                
        pass
    
    def display(self,canvas):
        canvas.create_oval(self._x-self.radius,self._y-self.radius,self._x+self.radius,self._y+self.radius,fill = 'black')
        

    def contains(self,x,y):
        
        if x >= self._x - self._width/2 and x <= self._x + self._width/2:
            if y >= self._y - self._height/2 and y <= self._y + self._height/2:
                
                return True
        else:
            return False