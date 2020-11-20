import pygame as pg

pg.init()

G = 6,67430*10**(-11)


class Object:

    def __init__(self):
        self.mass = 0
        self.coords = [0, 0]
        self.vel = [0, 0]
        self.force = [0, 0]
        self.rad = 0
        self.color = (255, 255, 255)
    
    def move(self, dt):
        self.coords[0] += self.vel[0]*dt + (self.force[0]/self.mass * dt**2)/2
        self.coords[1] += self.vel[1]*dt + (self.force[1]/self.mass * dt**2)/2
        self.vel[0] += self.force[0]/self.mass * dt
        self.vel[1] += self.force[1]/self.mass * dt

    def draw(self, screen):
        pg.draw.circle(screen, self.color, (int(self.coords[0]), int(self.coords[1])), int(self.rad), 0)
            
    
if __name__ == "__main__":
    print("This module is not for direct call!")
