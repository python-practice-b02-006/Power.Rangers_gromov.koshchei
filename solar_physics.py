# coding: utf-8
import numpy as np

G = 6,67430*10**(-11)

class Object():
    """Space object class
    """
    def __init__(self, coords, vel, mass, rad, color=(255, 255, 255)):
        self.mass = mass
        """Object mass
        """
  
        self.coords = coords
        """Coordinates
        """
  
        self.vel = vel
        """Velocity
        """
  
        self.force = np.array([0., 0.])
        """Force
        """
  
        self.rad = rad
        """Object radius
        """
  
        self.color = color
        """Object color
        """

    def calculate_force(self, space_objects):
        """Calculate force that move object.  
                                                
        **body** — Object that force move.
        **space_objects** — list of objects that make force.
        """
        self.force[0] = 0   
        self.force[1] = 0 
        
        for body in space_objects:
            self.force[0] += G*body.mass*self.mass/(body.coord[0] - self.coords[0])**2      
            self.force[1] += G*body.mass*self.mass/(body.coord[1] - self.coords[1])**2      
    
    def move(self, dt):
        """Function that move object
        
        **body** — Object to move.
        """
        self.coords[0] = vel[0]*dt + (self.force[0]/self.mass * dt**2)/2
        self.coords[1] = vel[1]*dt + (self.force[1]/self.mass * dt**2)/2
        
        self.vel[0] = self.force[0]/self.mass * dt
        self.vel[1] = self.force[1]/self.mass * dt      

def objects_positions(space_objects, dt):
    """Recalculate objects coords.
    
    **space_objects** — list of objects which coords need to recalculate.
    **dt** — time step
    """
    
    for body in space_objects:
        body.calculate_force(space_objects)
    for body in space_objects:
        body.move()
            
    
if __name__ == "__main__":
    print("This module is not for direct call!")
