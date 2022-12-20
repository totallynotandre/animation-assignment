import controller
import model   # Calling update in update_all passes a reference to this model

##Use the reference to this module to pass it to update methods

from ball       import  Ball
from blackhole  import  Black_Hole
from floater    import  Floater
from hunter     import  Hunter
from pulsator   import  Pulsator
from special    import Special


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running = False
cycle = 0
items = set()
preyitems = set()
currAct = None
currType = None

#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running,cycle,items
    running = False
    items = set()
    cycle = 0
    pass


#start running the simulation
def start ():
    global running
    running = True
    pass


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False
    pass


#step just one update in the simulation
def step ():
    global running, cycle 
    running = False
    for b in items.copy():
        b.update()
    cycle = cycle + 1
    
    
    pass


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global currType
    print(kind)
    currType = kind
    pass


#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    print(x,y)
    
    try:
        if currType == 'Ball':
            
            
            add(Ball(x,y))
            
        elif currType == 'Remove':
            
            for b in items.copy():
                
                
                if b.contains(x,y) == True:
                    remove(b)
        elif currType == 'Floater':
            add(Floater(x,y))
        elif currType == 'Black_Hole':
            add(Black_Hole(x,y))
        
        elif currType == 'Pulsator':
            add(Pulsator(x,y))
            
        elif currType == 'Hunter':
            add(Hunter(x,y))  
        elif currType == 'Special':
            add(Special(x,y))  
    except:
        print('fail')
        pass
    pass


#add simulton s to the simulation
def add(s):
    items.add(s)
    
    pass
    

# remove simulton s from the simulation    
def remove(s):
    items.remove(s)
    pass
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    temp = set()
    for x in items.copy():
        if p(x) == True:
            temp.add(x)
    return temp
    pass


#Simulation: for each simulton in the model, call its update, passing it model
#Loop over a set containing all the simultons; do not use type or isinstance:
#  let each simulton's update do the needed work, without this function knowing
#  what kinds of simultons are in the simulation
def update_all():
    global cycle
    if running:
        cycle  += 1
        
        for b in items.copy():
            b.update()
    pass

#Animation: clear then canvas; for each simulton in the model, call display
#  (a) delete all simultons on the canvas; (b) call display on all simultons
#  being simulated, adding back each to the canvas, often in a new location;
#  (c) update the label defined in the controller showing progress 
#Loop over a set containing all the simultons; do not use type or isinstance:
#  let each simulton's display do the needed work, without this function knowing
#  what kinds of simultons are in the simulation
def display_all():
    global cycle
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    
    for b in items:
        b.display(controller.the_canvas)
    
    controller.the_progress.config(text=str(cycle)+" updates/"+str(len(items))+" simulton")
    pass
