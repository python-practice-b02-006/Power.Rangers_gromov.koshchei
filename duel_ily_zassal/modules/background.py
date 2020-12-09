import pygame as pg
import os
from modules import gui
pg.init()


class Background():

    def __init__(self, screen, screen_size):
        self.screen = screen
        self.screen_size = screen_size
        self.pause_button = gui.Button("Pause", (int(screen_size[0]/10),int(screen_size[1]/10)), screen,
                                       (int(screen_size[0]/15), int(screen_size[1]/20)),(int(screen_size[0]/9),
                                                                                         int(screen_size[1]/9))                                )
    def set_background(self):
        SC_IMG = pg.image.load(os.path.join("Images", "back.jpg"))
        new_image = pg.transform.scale(SC_IMG, (self.screen_size))
        self.screen.blit(new_image, (0, 0))
        self.pause_button.create()
        self.pause_button.active()
