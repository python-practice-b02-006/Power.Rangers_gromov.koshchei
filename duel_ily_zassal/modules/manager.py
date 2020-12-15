from modules import gui, charges, fields, menu, background, pause, fighters, final
import pygame as pg
import easygui

RED = (255, 0, 0)
GREEN = (158, 209, 48)
class Manager():

    def __init__(self, screen, screensize):
        self.screen = screen
        self.screensize = screensize
        self.done = False
        self.game = False
        self.pause = False
        self.group1 = pg.sprite.Group()
        self.group2 = pg.sprite.Group()
        self.pause_window = pause.Pause(self.screen, self.screensize)
        self.charges = []
        self.d_charges = []
        self.field = fields.Field((0, 0, 0), (0, 0, 0))
        self.quit_button = gui.Button('quit', (350, 275), self.screen, (100, 50), (375, 285))
        self.menu = menu.Menu(self.screen, self.screensize)
        self.back = background.Background(self.screen, self.screensize)
        self.dantes = fighters.Dantes(self.screen, self.screensize, 'dantes.png')
        self.shot = 0
        self.group2.add(self.dantes)
        self.d_b_count = 6
        self.pushkin = fighters.Pushkin(screen, screensize)
        self.p_hp = gui.Progress_bar((int(screensize[0]/70), 40), (int(screensize[0]/2.5), 20),
                                   self.pushkin.hp, screen, "Pushkin", GREEN)
        self.d_hp = gui.Progress_bar((int(screensize[0]/1.7), 40), (int(screensize[0]/2.5), 20),
                                   self.dantes.hp, screen, "Dantes", RED)


    def process(self, events):

        if self.pause:
            self.pause_window.set_pause(self.screen, self.screensize)
            
        if self.game == False:
            self.menu.set_menu(self.screen, self.screensize)

        self.field.calculate_force(self.charges)
        
        if self.pause == False and self.game == True:
            self.back.set_background()
            self.d_hp.draw()
            self.p_hp.draw()
            self.group2.draw(self.screen)
            self.group1.draw(self.screen)
            # self.group1.update(self.dantes, self.group2)
            self.group2.update(self.pushkin)
            self.pushkin.mouse_gun()
            self.pushkin.check_pushkin_hp()
            self.dantes.check_dantes_hp(self.screen, self.screensize)
            self.field.change_field()
            self.field.calculate_force(self.charges)
            self.d_hp.level = self.dantes.hp
            self.p_hp.level = self.pushkin.hp

            if self.dantes.hp and self.shot == 1:
                self.dantes.move()

            for charge in self.charges:
                charge.move(0.01)
                
                if len(self.d_charges) == 0 and self.dantes.hp > 0:
                        if self.d_b_count > 0:
                            self.d_charges.append(charges.D_charge(0, 1, self.screen, (255, 255, 255), self.screensize, self.dantes.coords))
                            self.group2.add(self.d_charges[-1])
                            self.d_b_count -= 1
                            self.shot = 1

            for i, charge in enumerate(self.charges):
                if charge.size < 5 and not self.pause:
                    self.charges.remove(charge)
                    self.group1.remove(charge)
                if charge.coord.z > charge.ground:
                    self.charges.remove(charge)
                    self.group1.remove(charge)
                if charge.disappear():
                    self.charges.remove(charge)
                    self.group1.remove(charge)
                dead = charge.update(self.dantes, self.group2)
                if dead[0]:
                    for d in dead[1]:
                        self.d_charges.remove(d)
                        self.group2.remove(d)
                    self.charges.remove(charge)
                    self.group1.remove(charge)

            for d_charge in self.d_charges:
                if d_charge.coord.y <= 5:
                    self.d_charges.remove(d_charge)
                    self.group2.remove(d_charge)
                d_charge.move(0.01)

        done = self.event_handler(events)

        return done

    def event_handler(self, events):
        done = False
        for event in events:

            if event.type == pg.QUIT:
                done = True

            if self.pushkin.lose.restart_button.activated:
                self.pushkin.lose.restart_button.click(events, self.restart)

            if self.dantes.win.restart_button.activated:
                self.dantes.win.restart_button.click(events, self.restart)

            if self.menu.quit_button.activated:
                self.menu.quit_button.click(events, self.quit_b)
                done = self.done

            if self.pushkin.lose.quit_button.activated:
                self.pushkin.lose.quit_button.click(events, self.quit_b)
                done = self.done

            if self.dantes.win.quit_button.activated:
                self.dantes.win.quit_button.click(events, self.quit_b)
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
        self.group1.add(self.charges[-1])

    def restart(self):
        self.game = False
        self.pushkin.hp = 60
        self.dantes.hp = 100


if __name__ == "__main__":
    print("This module is not for direct call!")
