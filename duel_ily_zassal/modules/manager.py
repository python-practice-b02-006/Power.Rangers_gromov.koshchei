from modules import gui, charges, fields, menu, background
import pygame as pg
import easygui


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
            self.fire_b()

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
            if self.menu.play_button.activated:
                self.menu.play_button.click(events, self.fire_b)
            if self.fire_button.activated:
                self.fire_button.click(events, self.add_charge)
        return done

    def quit_b(self):
        self.done = True

    def fire_b(self):
        self.fire_button.create()
        self.fire_button.active()
        self.game = True

    def add_charge(self):
        self.charges.append(charges.Charge(0, 1, self.screen, (200, 10, 200), (255, 255, 255)))

if __name__ == "__main__":
    print("This module is not for direct call!")

