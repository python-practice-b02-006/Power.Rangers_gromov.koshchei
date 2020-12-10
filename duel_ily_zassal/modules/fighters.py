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

    def __init__(self, scr_size):
        self.hp = 100
        self.coords = [scr_size[0]/2  + 20, 500, scr_size[1]/2 + 40]
        
        
    def create(self, scr):
        dantes_surf = pg.image.load(os.path.join("Images", "dantes.png"))
        scr.blit(dantes_surf, (self.coords[0] - 35, self.coords[2]))


if __name__ == "__main__":
    print("This module is not for direct call!")
