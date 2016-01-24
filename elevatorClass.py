### elevatorClass.py ###
'''
This is the class for the Elevator object for the python-elevator-challenge.
'''

    
class Elevator(object):
     def call(self, floor, direction):
         self._logic_delegate.on_called(floor, direction)
 
     def select_floor(self, floor):
         self._logic_delegate.on_floor_selected(floor)

class Elevator(Elevator):
    ### Elevator actions
    '''
    The logic delegate can respond by setting the elevator to move up, move down, or stop. It can also read the current floor and movement direction of the elevator. These actions are accessed through `Callbacks`, a mediator provided by the `Elevator` class to the logic delegate.
    '''
    def __init__(self, logic_delegate, starting_floor=1):
         self._current_floor = starting_floor
         print "%s..." % starting_floor,
         self._motor_direction = None
         self._logic_delegate = logic_delegate
         self._logic_delegate.callbacks = self.Callbacks(self)
 
    class Callbacks(object):
         def __init__(self, outer):
             self._outer = outer
 
         @property
         def current_floor(self):
             return self._outer._current_floor
 
         @property
         def motor_direction(self):
             return self._outer._motor_direction
 
         @motor_direction.setter
         def motor_direction(self, direction):
             self._outer._motor_direction = direction

#class Elevator(Elevator):    
    ### Simulation
    '''
    The simulation runs in steps. Each time step consists of the elevator moving a single floor, or pausing at a floor. Either way, the business logic delegate gets notified. Along the way, we print out the movements of the elevator so that we can keep track of it. We also define a few helper methods that advance the simulation to points of interest, for ease of testing.
    '''
    def step(self):
        delta = 0
        if self._motor_direction == UP: delta = 1
        elif self._motor_direction == DOWN: delta = -1
 
        if delta:
            self._current_floor = self._current_floor + delta
            print "%s..." % self._current_floor,
            self._logic_delegate.on_floor_changed()
        else:
            self._logic_delegate.on_ready()
 
        assert self._current_floor >= 1
        assert self._current_floor <= FLOOR_COUNT
     
    def run_until_stopped(self):
        self.step()
        while self._motor_direction is not None: self.step()
     
    def run_until_floor(self, floor):
        for i in range(100):
            self.step()
            if self._current_floor == floor: break
        else: assert False

