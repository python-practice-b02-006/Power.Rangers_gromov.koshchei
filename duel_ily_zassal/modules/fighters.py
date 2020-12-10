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


class Dantes(pg.sprite.Sprite):

    def __init__(self, scr_size, filename, all_sprites):
        super().__init__(all_sprites)
        self.hp = 100
        self.image = pg.image.load(os.path.join("Images", filename))
        self.coords = [self.image.get_rect()[0]+scr_size[0]/2, self.image.get_rect()[1]+4*scr_size[1]/7]        
        self.rect = self.coords
        self.mask = pg.mask.from_surface(self.image)        


if __name__ == "__main__":
    print("This module is not for direct call!")
