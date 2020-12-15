import pygame as pg
from modules import gui
import os
pg.init()


class Guide():

    def __init__(self, screen, screen_size):
        self.screen = screen
        self.screen_size = screen_size
        self.back_button = gui.Button("BACK", (self.screen_size[0] - 200, self.screen_size[1] - 200), self.screen,
                                      (100,50), (self.screen_size[0] - 180, self.screen_size[1] - 190))

    def set_guide_window(self):
        SC_IMG = pg.image.load(os.path.join("Images", "guide.jpg"))
        new_image = pg.transform.scale(SC_IMG, (self.screen_size))
        self.screen.blit(new_image, (0, 0))
        f = pg.font.SysFont('garamondполужирный', 26)
        text = f.render("Main buttons:", 0, (255, 0, 0))
        self.screen.blit(text, (self.screen_size[0] - 200, 100))
        self.back_button.create()
        self.back_button.active()


if __name__ == "__main__":
    print("This module is not for direct call!")