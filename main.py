import pygame as pg
import gui
import solar_IO
import solar_physics

SCREEN_SIZE = (800, 600)

pg.init()


class Manager():

    def __init__(self, screen):
        self.objects = []
        self.input_file = 'input.txt'
        self.output_file = 'output.txt'
        self.button = gui.Button("start", (100,100), screen, (100, 50))
        self.slider = gui.Slider((100, 500), [100, 500], screen, (20, 100))

    def get_objects(self):
        self.objects = solar_IO.read_obj('palnets_characteristics')




screen = pg.display.set_mode(SCREEN_SIZE)
pg.display.set_caption("Solar system")
clock = pg.time.Clock()
done = False

while not done:
    clock.tick(15)

    done = mgr.process(pg.event.get(), screen)

    pg.display.flip()

pg.quit()