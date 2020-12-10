import pygame as pg
import os


class Pushkin():

    def __init__(self, scr, screensize):
        self.gun_surf = pg.image.load(os.path.join("Images", "gun.png"))
        self.gun_rect = self.gun_surf.get_rect()
        self.scr = scr
        self.screensize = screensize

    def mouse_gun(self):
        gun_surf = pg.transform.scale(self.gun_surf, (2*self.gun_rect[2], 2*self.gun_rect[3]))
        self.scr.blit(gun_surf,
                      (self.screensize[0]/2 - self.gun_rect[2], self.screensize[1] - 2*self.gun_rect[3]))


class Dantes():

    def __init__(self, scr_size):
        self.hp = 100
        self.coords = [scr_size[0]/2 + 20, 500, scr_size[1]/2 + 40]
        
        
    def create(self, scr):
        dantes_surf = pg.image.load(os.path.join("Images", "dantes.png"))
        scr.blit(dantes_surf, (self.coords[0] - 35, self.coords[2]))


if __name__ == "__main__":
    print("This module is not for direct call!")
