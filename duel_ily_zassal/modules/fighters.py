import pygame as pg
import os

class Pushkin():

    def mouse_gun(self, scr, screensize):
        gun_surf = pg.image.load(os.path.join("Images", "gun.png"))
        gun_rect = gun_surf.get_rect()
        pg.mouse.set_cursor(*pg.cursors.diamond)
        gun_surf = pg.transform.scale(gun_surf, (2*gun_rect[2], 2*gun_rect[3]))
        scr.blit(gun_surf, (screensize[0]/2 - gun_rect[2], screensize[1] - 2*gun_rect[3]))


class Dantes():

    def __init__(self):
        self.hp = 100
        self.coords = [420, 500, 290]
        
        
    def create(self, scr):
        dantes_surf = pg.image.load(os.path.join("Images", "dantes.png"))
        scr.blit(dantes_surf, (self.coords[0] - 35, self.coords[2]))
    


if __name__ == "__main__":
    print("This module is not for direct call!")
