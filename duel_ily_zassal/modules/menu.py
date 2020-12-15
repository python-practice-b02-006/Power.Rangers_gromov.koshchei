# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 16:20:30 2020

@author: Я
"""

import pygame as pg
import os
from modules import gui


class Menu():
    '''
    Menu with some buttons
    '''
    def __init__(self, scr, screensize):
        self.play_button = gui.Button("Play", (int((screensize[0] - 100)/2), int((screensize[1] - 50)/3)),
                                      scr, (100, 50), (int((screensize[0] - 100)/2+30), int((screensize[1] - 50)/3 +17)))
        self.quit_button = gui.Button("Quit", (int((screensize[0] - 100)/2), int(2*(screensize[1] - 50)/3)),
                                      scr, (100, 50), (int((screensize[0] - 100)/2+30), int(2*(screensize[1] - 50)/3 +17)))
        self.guide_button = gui.Button("Guide", (int((screensize[0] - 100) / 2), int((screensize[1] - 50) / 2)),
                                      scr, (100, 50),
                                      (int((screensize[0] - 100) / 2 + 27), int((screensize[1] - 50) / 2 + 17)))

    def set_menu(self, scr, screensize):
        '''
        Show menu on screen
        Args:
            scr: screen
            screensize: width and high of the screen
        Returns:
            None
        '''
        SC_IMG = pg.image.load(os.path.join("Images", "menu.jpg"))
        new_image = pg.transform.scale(SC_IMG, (screensize))
        scr.blit(new_image, (0, 0))
        self.play_button.create()
        self.play_button.active()
        self.quit_button.create()
        self.quit_button.active()
        self.guide_button.create()
        self.guide_button.active()


if __name__ == "__main__":
    print("This module is not for direct call!")
