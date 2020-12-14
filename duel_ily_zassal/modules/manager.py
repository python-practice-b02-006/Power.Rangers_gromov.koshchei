from modules import gui, charges, fields, menu, background, pause, fighters
import pygame as pg
import easygui

class Manager():

    def __init__(self, screen, screensize):
        self.screen = screen
        self.screensize = screensize
        self.done = False
        self.game = False
        self.pause = False
        self.all_sprites = pg.sprite.Group()
        self.pause_window = pause.Pause(self.screen, self.screensize)
        self.charges = []
        self.field = fields.Field((0, 0, 0), (0, 0, 0))
        self.quit_button = gui.Button('quit', (350, 275), self.screen, (100, 50), (375, 285))
        self.menu = menu.Menu(self.screen, self.screensize)
        self.back = background.Background(self.screen, self.screensize)
        self.dantes = fighters.Dantes(self.screensize, 'dantes.png')
        self.all_sprites.add(self.dantes)
        self.pushkin = fighters.Pushkin()
        self.hp = gui.Progress_bar((int(screensize[0]/4), 20), (int(screensize[0]/2), 20),
                                   self.dantes.hp, screen)

    def process(self, events):

        if self.pause:
            self.pause_window.set_pause(self.screen, self.screensize)
            
        if self.game is not True:
            self.menu.set_menu(self.screen, self.screensize)

        self.field.calculate_force(self.charges)
        
        if self.pause == False and self.game == True:
            self.back.set_background()
            self.hp.draw()
            self.all_sprites.draw(self.screen)
            self.all_sprites.update(self.dantes)
            self.pushkin.mouse_gun(self.screen, self.screensize)
            self.dantes.check_dantes_hp()
            self.field.change_field()
            self.field.calculate_force(self.charges)
            
            for charge in self.charges:
                charge.move(0.01)

            for i, charge in enumerate(self.charges):
                if charge.size < 5 and not self.pause:
                    self.charges.remove(charge)
                    self.all_sprites.remove(charge)
                if charge.coord.z > charge.ground:
                    self.charges.remove(charge)
                    self.all_sprites.remove(charge)
                if charge.disappear():
                    self.charges.remove(charge)
                    self.all_sprites.remove(charge)
                
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

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.pause_g()
                    elif event.key == pg.K_RIGHT:
                        self.field.change = True
                        self.field.dir = 'r'
                    elif event.key == pg.K_LEFT:
                        self.field.change = True
                        self.field.dir = 'l'
                    elif event.key == pg.K_UP:
                        self.field.change = True
                        self.field.dir = 'u'
                    elif event.key == pg.K_DOWN:
                        self.field.change = True
                        self.field.dir = 'd'
                if event.type == pg.KEYUP:
                    if event.key == pg.K_RIGHT:
                        self.field.change = False
                    elif event.key == pg.K_LEFT:
                        self.field.change = False
                    elif event.key == pg.K_UP:
                        self.field.change = False
                    elif event.key == pg.K_DOWN:
                        self.field.change = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pos = pg.mouse.get_pos()
                        self.add_charge(pos)
                        
                self.hp.level = self.dantes.hp

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
        for charge in self.charges:
            charge.hide()
        self.pause = True

    def resume(self):
        self.pause = False

    def add_charge(self, pos):
        self.charges.append(charges.Charge(0, 10, self.screen, (pos[0], 5, pos[1]), (255, 255, 255), self.screensize))
        self.all_sprites.add(self.charges[-1])


if __name__ == "__main__":
    print("This module is not for direct call!")