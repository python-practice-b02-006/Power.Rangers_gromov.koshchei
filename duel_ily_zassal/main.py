import pygame as pg
from duel_ily_zassal.modules import manager

SCREEN_SIZE = (800, 600)
FPS = 60

pg.init()
SCREEN = pg.display.set_mode(SCREEN_SIZE)
pg.display.set_caption("Solar system")
clock = pg.time.Clock()
DONE = False
mgr = manager.Manager(SCREEN)

while not DONE:
    clock.tick(FPS)
    SCREEN.fill((0,0,0))
    DONE = mgr.process(pg.event.get())
    pg.display.flip()

pg.quit()