from solar_system.modules import gui, IO, phys
import pygame as pg
import easygui


class Manager():

    def __init__(self, screen, dt):
        self.objects = []
        self.file = '..\solar_system\modules\planets_characteristics'
        self.button = gui.Button("start", (0, 550), screen, (100, 50), (25, 565))
        self.button2 = gui.Button("file", (110, 550), screen, (100, 50), (140, 565))
        self.slider = gui.Slider((300, 560), [300, 560], screen, (400, 20))
        self.screen = screen
        self.play = False
        self.dt = dt

    def get_objects(self):
        self.objects = IO.read_obj(self.file)

    def process(self, events):

        self.button.create()
        self.button.active()

        self.button2.create()
        self.button2.active()

        self.slider.create()
        self.slider.move()

        for body in self.objects:
            body.draw(self.screen)
        for i in range(200):
            if self.play:
                self.objects = phys.calculate_force(self.objects)
                for body in self.objects:
                    body.move(self.dt)

        done = self.event_handler(events)

        return done

    def event_handler(self, events):
        done = False
        for event in events:
            if event.type == pg.QUIT:
                done = True
        if self.button.activated and not self.play:
            self.button.click(events, self.start)
        elif self.button.activated and self.play:
            self.button.click(events, self.pause)
        self.slider.click(events)
        if self.button2.activated:
            self.button2.click(events, self.get_file)
        return done

    def start(self):
        self.button.name = "pause"
        self.play = True

    def pause(self):
        self.button.name = "start"
        self.play = False

    def get_file(self):
        file_name = easygui.fileopenbox()
        if file_name != None:
            self.file = file_name
            self.get_objects()
            self.button.name = "start"
            self.play = False


if __name__ == "__main__":
    print("This module is not for direct call!")
