import pygame as pg
import os

class Pushkin():
    pass


class Dantes():

    def __init__(self):
        self.hp = 100
        self.coords = [420, 500, 290]
        
        
    def create(self, scr):
        dantes_surf = pg.image.load(os.path.join("Images", "dantes.png"))
        scr.blit(dantes_surf, (self.coords[0] - 35, self.coords[2]))
    


if __name__ == "__main__":
    print("This module is not for direct call!")
