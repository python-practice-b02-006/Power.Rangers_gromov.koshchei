import pygame as pg
from solar_system import manager

SCREEN_SIZE = (800, 600)
FPS = 60
dT = 0.001

pg.init()
SCREEN = pg.display.set_mode(SCREEN_SIZE)
pg.display.set_caption("Solar system")
clock = pg.time.Clock()
DONE = False
mgr = manager.Manager(SCREEN, dT)
mgr.get_objects()

while not DONE:
    clock.tick(FPS + 300*mgr.slider.level)
    SCREEN.fill((0,0,0))
    DONE = mgr.process(pg.event.get())
    pg.display.flip()

pg.quit()