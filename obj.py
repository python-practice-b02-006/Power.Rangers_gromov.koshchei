import pygame as pg

pg.init()

G = 6,67430*10**(-11)


class Object:
    """Space object class
       (string format:x y vx vy mass rad color)
    """
    def __init__(self): 
    
        self.mass = 0
        """Object mass
        """
        self.coords = [0, 0]
        """Coordinates [X, Y]
        """ 
        self.vel = [0, 0]
        """Velocity [Vx, Vy]
        """
        self.force = [0, 0]
        """Force [Fx, Fy]
        """
        self.rad = 0
        """Object radius
        """
        self.color = (255, 255, 255)
        """Object color
        """
    
    def move(self, dt):
        '''Function that calculate new body coordinates and velocity.
        
        Parameters:
        
        **dt** - time step.
        '''
        self.coords[0] += self.vel[0]*dt + (self.force[0]/self.mass * dt**2)/2
        self.coords[1] += self.vel[1]*dt + (self.force[1]/self.mass * dt**2)/2
        self.vel[0] += self.force[0]/self.mass * dt
        self.vel[1] += self.force[1]/self.mass * dt

    def draw(self, screen):
        '''Function that draws space object.
        
        Parameters:
        
        **screen** - surface to draw on.
        '''
        pg.draw.circle(screen, self.color, (int(self.coords[0]), int(self.coords[1])), int(self.rad), 0)
            
    
if __name__ == "__main__":
    print("This module is not for direct call!")
