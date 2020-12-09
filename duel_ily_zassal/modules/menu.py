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
        self.play_button = gui.Button("Play", (int((screensize[0] - 100)/2), int((screensize[1] - 50)/3)),
                                      scr, (100, 50), (int((screensize[0] - 100)/2+30), int((screensize[1] - 50)/3 +17)))
        self.quit_button = gui.Button("Quit", (int((screensize[0] - 100)/2), int(2*(screensize[1] - 50)/3)),
                                      scr, (100, 50), (int((screensize[0] - 100)/2+30), int(2*(screensize[1] - 50)/3 +17)))

    def set_menu(self, scr, screensize):
        SC_IMG = pg.image.load(os.path.join("Images", "menu.jpg"))
        new_image = pg.transform.scale(SC_IMG, (screensize))
        scr.blit(new_image, (0, 0))
        self.play_button.create()
        self.play_button.active()
        self.quit_button.create()
        self.quit_button.active()
        
    def mouse_gun(self, pos, scr):
        gun_surf = pg.image.load(os.path.join("Images", "gun.png"))
        scr.blit(gun_surf, (pos[0]-35, pos[1]))