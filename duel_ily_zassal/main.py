import pygame as pg
from modules import manager

SCREEN_SIZE = (1200, 700)
FPS = 60
global all_sprites

pg.init()
SCREEN = pg.display.set_mode(SCREEN_SIZE)
pg.display.set_caption("Gun of Kolganov (A.k. duel ily zassal)")
clock = pg.time.Clock()
DONE = False
mgr = manager.Manager(SCREEN, SCREEN_SIZE)

while not DONE:
    clock.tick(FPS)
    SCREEN.fill((0,0,0))
    DONE = mgr.process(pg.event.get())
    pg.display.flip()

pg.quit()