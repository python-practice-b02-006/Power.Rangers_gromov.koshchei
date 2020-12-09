import pygame as pg
from modules import gui
import os

class Pause():
    def __init__(self, scr, screensize):
        self.continue_button = gui.Button("Continue", (int((screensize[0] - 100)/2), int((screensize[1] - 50)/3)),
                                      scr, (100, 50), (int((screensize[0] - 100)/2+13), int((screensize[1] - 50)/3 +17)))
        self.quit_button = gui.Button("Quit", (int((screensize[0] - 100)/2), int(2*(screensize[1] - 50)/3)),
                                      scr, (100, 50), (int((screensize[0] - 100)/2+30), int(2*(screensize[1] - 50)/3 +17)))

    def set_pause(self, scr, screensize):
        SC_IMG = pg.image.load(os.path.join("Images", "pause.jpg"))
        new_image = pg.transform.scale(SC_IMG, (screensize))
        scr.blit(new_image, (0, 0))
        self.continue_button.create()
        self.continue_button.active()
        self.quit_button.create()
        self.quit_button.active()
        