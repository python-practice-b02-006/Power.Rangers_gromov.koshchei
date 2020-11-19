import pygame as pg
import gui
import IO
import obj
import phys

SCREEN_SIZE = (800, 600)
dt = 0.1

pg.init()

class Manager():

    def __init__(self, screen):
        self.objects = []
        self.input_file = 'input.txt'
        self.output_file = 'output.txt'
        self.button = gui.Button("start", (100, 100), screen, (100, 50))
        self.slider = gui.Slider((100, 500), [100, 500], screen, (20, 100))
        self.screen = screen

    def get_objects(self):
        self.objects = IO.read_obj('planets_characteristics')

    def process(self, events, dt):
        done = self.event_handler(events)
        for body in self.objects:
            body.draw(self.screen)
        self.objects = phys.calculate_force(self.objects)
        for body in self.objects:
            body.move(dt)
        return done

    def event_handler(self, events):
        done = False
        for event in events:
            if event.type == pg.QUIT:
                done = True
        return done


SCREEN = pg.display.set_mode(SCREEN_SIZE)
pg.display.set_caption("Solar system")
clock = pg.time.Clock()
DONE = False
mgr = Manager(SCREEN)
mgr.get_objects()

while not DONE:
    clock.tick(60)
    SCREEN.fill((0,0,0))
    DONE = mgr.process(pg.event.get(), dt)
    pg.display.flip()

pg.quit()