# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10). 


from prey import Prey


class Ball(Prey): 
    radius = 5
    def __init__(self,x,y):

        self._x = x
        self._y = y
        self._width = 10
        self._height = 10
        self._speed = 5
        self._angle = 2
        Prey.randomize_angle(self)
    def update(self):
        Prey.move(self)
        
        pass
    
    def display(self,canvas):
        
        canvas.create_oval(self._x-Ball.radius,self._y-Ball.radius,self._x+Ball.radius,self._y+Ball.radius,fill = 'blue')
        
        pass
    
    def contains(self,x,y):
        if x >= self._x - 10 and x <= self._x + 10:
            if y >= self._y - 10 and y <= self._y + 10:
                
                return True
        else:
            return False