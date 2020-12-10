import pygame as pg
import os

class Pushkin():

    def mouse_gun(self, pos, scr, screensize):
        gun_surf = pg.image.load(os.path.join("Images", "gun.png"))
        scr.blit(gun_surf, (pos[0] - 35, pos[1]))
        gun_rect = gun_surf.get_rect(
            bottomright=(300, 400))
        new_image = pg.transform.scale(gun_surf, (2*gun_rect[2], 2*gun_rect[3]))
        scr.blit(new_image, (screensize[0]/2 - gun_rect[2], screensize[1] - 2*gun_rect[3]))


class Dantes():

    def __init__(self):
        self.hp = 100
        self.coords = [420, 500, 290]
        
        
    def create(self, scr):
        dantes_surf = pg.image.load(os.path.join("Images", "dantes.png"))
        scr.blit(dantes_surf, (self.coords[0] - 35, self.coords[2]))
    


if __name__ == "__main__":
    print("This module is not for direct call!")
