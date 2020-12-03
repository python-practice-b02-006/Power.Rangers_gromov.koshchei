import pygame as pg
import os

pg.init()


class Background():

    def __init__(self, screen, screen_size):
        self.screen = screen
        self.screen_size = screen_size

    def set_background(self):
        SC_IMG = pg.image.load(os.path.join("Images", "back.jpg"))
        new_image = pg.transform.scale(SC_IMG, (self.screen_size))
        self.screen.blit(new_image, (0, 0))
