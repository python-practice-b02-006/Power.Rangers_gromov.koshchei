import pygame as pg
from modules import vectors
import os

pg.init()

class Charge(pg.sprite.Sprite):

    def __init__(self, m_c, e_c, screen, coord, color, screensize, filename, all_sprites):
        super().__init__(all_sprites)   
        self.size = 10
        self.size_save = 1000
        self.m_c = m_c
        self.e_c = e_c
        self.vel = vectors.Vector(0, 100, 0)
        self.accel = vectors.Vector(0, 0, 0)
        self.mass = 10
        self.coord = vectors.Vector(coord[0], coord[1], coord[2])
        self.damage = 1
        self.color = color
        self.screen = screen
        self.force = vectors.Vector(0, 0, 0)
        self.screensize = screensize
        self.ground = screensize[1]
        self.image = pg.Surface( (self.size_save, self.size_save), pg.SRCALPHA, 32)
        pg.draw.circle(self.image, self.color, (10 * self.size, 10 * self.size), 10 * self.size)
        self.rect = (int(self.coord.x) - self.image.get_rect()[0]/2, int(self.coord.z)-self.image.get_rect()[1]/2)
        self.mask = pg.mask.from_surface(self.image)

    def move(self, dt):
        self.coord += self.vel * dt
        self.vel += self.force * (1 / self.mass) * dt
        self.size = abs(1000 / self.coord.y)        
        self.image = pg.Surface( (self.size_save, self.size_save), pg.SRCALPHA, 32)
        pg.draw.circle(self.image, self.color, (int(self.size), int(self.size)), int(self.size))
        self.rect = (int(self.coord.x), int(self.coord.z))        
        self.ground = int(self.screensize[1] / 1.85 + self.size * self.screensize[1] / 50)
        self.mask = pg.mask.from_surface(self.image)

    def hide(self):
        self.size = 0

    def became(self):
        self.size += 0

if __name__ == "__main__":
    print("This module is not for direct call!")
