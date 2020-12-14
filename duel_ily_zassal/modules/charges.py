import pygame as pg
from modules import vectors
import os

pg.init()


class Charge(pg.sprite.Sprite):

    def __init__(self, m_c, e_c, screen, coord, color, screensize):
        pg.sprite.Sprite.__init__(self)
        self.m_c = m_c
        self.e_c = e_c
        self.vel = vectors.Vector(0, 100, 0)
        self.accel = vectors.Vector(0, 0, 0)
        self.mass = 10
        self.size = abs(1000 / coord[1])
        self.coord = vectors.Vector(coord[0], 10, coord[2])
        self.damage = 1
        self.color = color
        self.screen = screen
        self.force = vectors.Vector(0, 0, 0)
        self.screensize = screensize
        self.ground = screensize[1]
        self.image = pg.image.load(os.path.join("Images", 'bullet.png')).convert()
        self.image = pg.transform.scale(self.image, (int(self.size), int(self.size)))
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (self.coord.x, self.coord.z)
        #self.image = pg.Surface( (self.size_save, self.size_save), )
        #self.rect = (int(self.coord.x) - self.image.get_rect()[0]/2, int(self.coord.z)-self.image.get_rect()[1]/2)
        self.mask = pg.mask.from_surface(self.image)

    def move(self, dt):
        self.coord += self.vel * dt
        self.vel += self.force * (1 / self.mass) * dt
        self.size = abs(1000 / self.coord.y)
        self.image = pg.image.load(os.path.join("Images", 'bullet.png')).convert()
        self.image = pg.transform.scale(self.image, (int(self.size), int(self.size)))
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (self.coord.x, self.coord.z)
        self.ground = int(self.screensize[1] / 1.85 + self.size * self.screensize[1] / 50)
        self.mask = pg.mask.from_surface(self.image)
        
    def update(self, dantes):
        if pg.sprite.collide_mask(self, dantes):
            if self.coord.y > 100 and self.coord.y < 140:
                print("Bang")

    def hide(self):
        self.size = 0

    def became(self):
        self.size += 0


if __name__ == "__main__":
    print("This module is not for direct call!")
