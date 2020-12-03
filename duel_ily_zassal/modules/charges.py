import pygame as pg
from duel_ily_zassal.modules import vectors

pg.init()

class Charge():

    def __init__(self, m_c, e_c, screen, coord, color):
        self.size = 10
        self.m_c = m_c
        self.e_c = e_c
        self.vel = vectors.Vector(0, 50, 0)
        self.accel = vectors.Vector(0, 0, 0)
        self.mass = 10
        self.coord = vectors.Vector(coord[0], coord[1], coord[2])
        self.damage = 1
        self.color = color
        self.screen = screen

    def create(self):
        pg.draw.circle(self.screen, self.color, (int(self.coord.x), int(self.coord.z)), int(self.size))

    def move(self, dt):
        self.coord += self.vel * dt
        self.vel += self.accel * dt
        self.size = 1000 / self.coord.y

