from modules import gui, charges, fields, menu, background, pause
import pygame as pg
import easygui

check = 0

class Manager():

    def __init__(self, screen, screensize):
        self.screen = screen
        self.screensize = screensize
        self.done = False
        self.game = False
        self.pause = False
        self.pause_window = pause.Pause(self.screen, self.screensize)
        self.charges = []
        self.field = fields.Field((10, 10, 10), (100, 100, 100))
        self.quit_button = gui.Button('quit', (350, 275), self.screen, (100, 50), (375, 285))
        self.menu = menu.Menu(self.screen, self.screensize)
        self.back = background.Background(self.screen, self.screensize)

    def process(self, events):
        if self.pause == True:
            self.pause_window.set_pause(self.screen, self.screensize)

        if self.game is not True:
            self.menu.set_menu(self.screen, self.screensize)

        if self.game == True and self.pause == False:
            self.back.set_background()

        self.field.calculate_force(self.charges)
        if self.pause == False:
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
            if self.pause_window.quit_button.activated:
                self.pause_window.quit_button.click(events, self.quit_b)
                done = self.done
            if self.pause == False and self.game == True:
                if self.back.pause_button.activated:
                    for charge in self.charges:
                        charge.hide()
                    self.back.pause_button.click(events, self.pause_g)
                if event.type == pg.MOUSEBUTTONDOWN and self.back.pause_button.activated == False:
                    if event.button == 1:
                        pos = pg.mouse.get_pos()
                        self.add_charge(pos)
            if self.pause_window.continue_button.activated:
                for charge in self.charges:
                    charge.became()
                self.pause_window.continue_button.click(events, self.resume)
                
            if self.menu.play_button.activated:
                self.menu.play_button.click(events, self.play)   
        return done

    def quit_b(self):
        self.done = True

    def play(self):
        self.game = True

    def pause_g(self):
        self.pause = True

    def resume(self):
        self.pause = False

    def add_charge(self, pos):
        self.charges.append(charges.Charge(0, 1, self.screen, (pos[0], 10, pos[1]), (255, 255, 255)))

if __name__ == "__main__":
    print("This module is not for direct call!")

