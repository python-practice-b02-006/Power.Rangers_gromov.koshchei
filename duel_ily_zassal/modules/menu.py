# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 16:20:30 2020

@author: Я
"""

import pygame as pg
import os
from modules import gui



class Menu():
    def __init__(self, scr, screensize):
        self.play_button = gui.Button("Play", (350, 185), scr, (100, 50), (380, 200))
        self.quit_button = gui.Button("Quit", (350, 385), scr, (100, 50), (380, 400))

    def set_menu(self, scr, screensize):
        SC_IMG = pg.image.load(os.path.join("Images", "menu.jpg"))
        new_image = pg.transform.scale(SC_IMG, (screensize))
        scr.blit(new_image, (0, 0))
        self.play_button.create()
        self.play_button.active()
        self.quit_button.create()
        self.quit_button.active()