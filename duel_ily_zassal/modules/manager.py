from duel_ily_zassal.modules import gui
import pygame as pg
import easygui


class Manager():

    def __init__(self, screen):
        self.screen = screen
        self.done = False
        self.quit_button = gui.Button('quit', (350,275), self.screen, (100, 50), (375, 285))

    def process(self, events):

        self.quit_button.create()
        self.quit_button.active()

        done = self.event_handler(events)

        return done

    def event_handler(self, events):
        done = False
        for event in events:
            if event.type == pg.QUIT:
                done = True
            if self.quit_button.activated:
                self.quit_button.click(events, self.quit_b)
                done = self.done
        return done

    def quit_b(self):
        self.done = True
