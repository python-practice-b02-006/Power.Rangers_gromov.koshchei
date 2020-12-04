from modules import gui, charges, fields, menu, background
import pygame as pg
import easygui

check = 0

class Manager():

    def __init__(self, screen, screensize):
        self.screen = screen
        self.screensize = screensize
        self.done = False
        self.game = False
        self.charges = []
        self.field = fields.Field((10, 10, 10), (100, 100, 100))
        self.quit_button = gui.Button('quit', (350, 275), self.screen, (100, 50), (375, 285))
        self.fire_button = gui.Button('fire', (500, 500), self.screen, (100, 50), (525, 510))
        self.menu = menu.Menu(self.screen, self.screensize)
        self.back = background.Background(self.screen, self.screensize)

    def process(self, events):

        if self.game is not True:
            self.menu.set_menu(self.screen, self.screensize)

        if self.game == True:
            self.back.set_background()

        self.field.calculate_force(self.charges)
        for charge in self.charges:
            charge.create()
            charge.move(0.01)

        done = self.event_handler(events)

        return done

    def event_handler(self, events):
        done = False
        for event in events:
            if event.type == pg.QUIT:
                done = True
            if self.menu.quit_button.activated:
                self.menu.quit_button.click(events, self.quit_b)
                done = self.done
            if self.game:
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pos = pg.mouse.get_pos()
                        self.add_charge(pos)     
                
            if self.menu.play_button.activated:
                self.menu.play_button.click(events, self.play)   
        return done

    def quit_b(self):
        self.done = True

    def play(self):
        self.game = True

    def add_charge(self, pos):
        self.charges.append(charges.Charge(0, 1, self.screen, (pos[0], 10, pos[1]), (255, 255, 255)))

if __name__ == "__main__":
    print("This module is not for direct call!")

