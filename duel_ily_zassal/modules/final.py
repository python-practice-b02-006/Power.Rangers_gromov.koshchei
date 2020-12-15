import pygame as pg
from modules import gui
import os

class Win():
    def __init__(self, scr, screensize):
        self.restart_button = gui.Button("Restart", (int((screensize[0] - 100)/2), int((screensize[1] - 70)/3)),
                                      scr, (100, 50), (int((screensize[0] - 100)/2+19), int((screensize[1] - 70)/3 +17)))
        self.quit_button = gui.Button("Quit", (int((screensize[0] - 100)/2), int(2*(screensize[1] - 90)/3)),
                                      scr, (100, 50), (int((screensize[0] - 100)/2+30), int(2*(screensize[1] - 90)/3 +17)))

    def duel_winner(self, scr, screensize):
        pg.mouse.set_cursor(*pg.cursors.arrow)
        SC_IMG = pg.image.load(os.path.join("Images", "win.jpg"))
        new_image = pg.transform.scale(SC_IMG, (screensize))
        scr.blit(new_image, (0, 0))
        self.restart_button.create()
        self.restart_button.active()
        self.quit_button.create()
        self.quit_button.active()

class Lose():
    def __init__(self, scr, screensize):
        self.restart_button = gui.Button("Restart", (int((screensize[0] - 100)/2), int((screensize[1] - 70)/3)),
                                      scr, (100, 50), (int((screensize[0] - 100)/2+19), int((screensize[1] - 70)/3 +17)))
        self.quit_button = gui.Button("Quit", (int((screensize[0] - 100)/2), int(2*(screensize[1] - 100)/3)),
                                      scr, (100, 50), (int((screensize[0] - 100)/2+30), int(2*(screensize[1] - 100)/3 +17)))

    def duel_loser(self, scr, screensize):
        pg.mouse.set_cursor(*pg.cursors.arrow)
        SC_IMG = pg.image.load(os.path.join("Images", "lose.png"))
        new_image = pg.transform.scale(SC_IMG, (screensize))
        scr.blit(new_image, (0, 0))
        self.restart_button.create()
        self.restart_button.active()
        self.quit_button.create()
        self.quit_button.active()


if __name__ == "__main__":
    print("This module is not for direct call!")
