from solar_system import gui, phys, IO
import pygame as pg


class Manager():

    def __init__(self, screen, dt):
        self.objects = []
        self.input_file = 'input.txt'
        self.output_file = 'output.txt'
        self.button = gui.Button("start", (0, 550), screen, (100, 50), (25, 565))
        self.button2 = gui.Button("file", (110, 550), screen, (100, 50), (140, 565))
        self.slider = gui.Slider((300, 560), [300, 560], screen, (400, 20))
        self.screen = screen
        self.play = False
        self.dt = dt

    def get_objects(self):
        self.objects = IO.read_obj('planets_characteristics')

    def process(self, events):

        self.button.create()
        self.button.active()

        self.button2.create()
        self.button2.active()

        self.slider.create()
        self.slider.active()
        self.slider.move()

        done = self.event_handler(events)

        for body in self.objects:
            body.draw(self.screen)
        if self.play:
            self.objects = phys.calculate_force(self.objects)
            for body in self.objects:
                body.move(self.dt)

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
        if self.slider.activated:
            self.slider.click(events)
        return done

    def start(self):
        self.button.name = "pause"
        self.play = True

    def pause(self):
        self.button.name = "start"
        self.play = False


if __name__ == "__main__":
    print("This module is not for direct call!")
