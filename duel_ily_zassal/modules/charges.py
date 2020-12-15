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
        self.coord = vectors.Vector(coord[0], coord[1], coord[2])
        self.z0 = self.coord.z
        self.damage = 1
        self.color = color
        self.screen = screen
        self.force = vectors.Vector(0, 0, 0)
        self.screensize = screensize
        self.ground = screensize[1]
        self.image = pg.image.load(os.path.join("Images", 'bullet.png')).convert()
        self.image = pg.transform.scale(self.image, (int(self.size), int(self.size)))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (self.coord.x, self.coord.z)
        self.mask = pg.mask.from_surface(self.image)

    def move(self, dt):
        self.coord += self.vel * dt
        self.vel += self.force * (1 / self.mass) * dt
        self.size = abs(1000 / self.coord.y)
        self.image = pg.image.load(os.path.join("Images", 'bullet.png')).convert()
        self.image = pg.transform.scale(self.image, (int(self.size), int(self.size)))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (self.coord.x, self.coord.z)
        self.ground = int(self.screensize[1] / 1.85 + self.size * self.screensize[1] / 50)
        self.mask = pg.mask.from_surface(self.image)

    def update(self, dantes, group2):
        dead_dc = []
        self_death = False
        for el in group2:
            if el != dantes:
                if el.size >= self.size and el.size <= self.size + 20\
                        and pg.sprite.collide_mask(self, el):
                    dead_dc.append(el)
                    self_death = True
                    self.kill()
                    el.kill()
            elif pg.sprite.collide_mask(self, dantes):
                if 100 < self.coord.y < 140:
                    dantes.hp -= 50
                    self.kill()
                    self_death = True
        return (self_death, dead_dc)

    def hide(self):
        self.size = 0

    def became(self):
        self.size += 0

    def disappear(self):
        if self.coord.z + self.size <= 0 \
                or self.coord.z - self.size >= self.screensize[1] \
                or self.coord.x + self.size <= 0 \
                or self.coord.x - self.size >= self.screensize[0]:
            return True
        else:
            return False


class D_charge(pg.sprite.Sprite):

    def __init__(self, m_c, e_c, screen, color, screensize, dantes):
        pg.sprite.Sprite.__init__(self)
        self.m_c = m_c
        self.e_c = e_c
        self.vel = vectors.Vector(0, -140, 0)
        self.accel = vectors.Vector(0, 0, 0)
        self.mass = 10
        self.coord = vectors.Vector(dantes[0], 200, dantes[1])
        self.size = abs(1000 / self.coord.y)
        self.damage = 1
        self.color = color
        self.screen = screen
        self.force = vectors.Vector(0, 0, 0)
        self.screensize = screensize
        self.ground = screensize[1]
        self.image = pg.image.load(os.path.join("Images", 'd_bullet.png')).convert()
        self.image = pg.transform.scale(self.image, (int(self.size), int(self.size)))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (self.coord.x, self.coord.z)
        self.mask = pg.mask.from_surface(self.image)

    def move(self, dt):
        self.coord += self.vel * dt
        self.vel += self.force * (1 / self.mass) * dt
        self.size = abs(1000 / self.coord.y)
        self.image = pg.image.load(os.path.join("Images", 'd_bullet.png')).convert()
        self.image = pg.transform.scale(self.image, (int(self.size), int(self.size)))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (self.coord.x, self.coord.z)
        self.ground = int(self.screensize[1] / 1.85 + self.size * self.screensize[1] / 50)
        self.mask = pg.mask.from_surface(self.image)

    def update(self, pushkin):
        if self.coord.y < 5:
            pushkin.hp -= 30
            self.coord.y = 5


    def interract(self, charges):
        pass


if __name__ == "__main__":
    print("This module is not for direct call!")
