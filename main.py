import pygame as pg
import gui
import IO
import obj
import phys

SCREEN_SIZE = (800, 600)
FPS = 60
dT = 0.01

pg.init()


class Manager():

    def __init__(self, screen, dt):
        self.objects = []
        self.input_file = 'input.txt'
        self.output_file = 'output.txt'
        self.button = gui.Button("start", (0, 550), screen, (100, 50))
        self.slider = gui.Slider((300, 500), [300, 500], screen, (200, 20))
        self.screen = screen
        self.play = False
        self.dt = dt

    def get_objects(self):
        self.objects = IO.read_obj('planets_characteristics')

    def send_objects(self):
        self.objects = IO.write_obj('planets_characteristics', self.objects)

    def process(self, events):

        self.button.create()
        self.button.active()

        self.slider.create()
        self.slider.active()
        self.slider.move()

        done = self.event_handler(events)

        #self.get_objects()
        for body in self.objects:
            body.draw(self.screen)
        if self.play:
            self.objects = phys.calculate_force(self.objects)
            for body in self.objects:
                body.move(self.dt * self.slider.level)
        #self.send_objects()

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


SCREEN = pg.display.set_mode(SCREEN_SIZE)
pg.display.set_caption("Solar system")
clock = pg.time.Clock()
DONE = False
mgr = Manager(SCREEN, dT)
mgr.get_objects()

while not DONE:
    clock.tick(FPS)
    SCREEN.fill((0,0,0))
    DONE = mgr.process(pg.event.get())
    pg.display.flip()

pg.quit()