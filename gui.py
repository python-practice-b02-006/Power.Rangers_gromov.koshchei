import pygame as pg

pg.init()

WHITE = (255, 255, 255)
GRAY = (168, 168, 168)
DARK_GRAY = (108, 108, 108)


class Button():

    def __init__(self, name, pos, screen, size):
        self.name = name
        self.pos = pos
        self.screen = screen
        self.color = GRAY
        self.size = size
        self.font = pg.font.SysFont("dejavusansmono", 25)
        self.activated = False

    def create(self):
        pg.draw.rect(self.screen, self.color, (self.pos, self.size), 0)
        self.screen.blit((self.font.render(self.name, True, (0, 0, 0))), self.pos)

    def click(self, events, command):
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN \
                    and self.pos[0] <= pg.mouse.get_pos()[0] <= self.pos[0] + self.size[0] \
                    and self.pos[1] <= pg.mouse.get_pos()[1] <= self.pos[1] + self.size[1]:
                return command()
            else:
                return False

    def active(self):
        if self.pos[0] <= pg.mouse.get_pos()[0] <= self.pos[0] + self.size[0] \
                and self.pos[1] <= pg.mouse.get_pos()[1] <= self.pos[1] + self.size[1]:
            self.activated = True
        else:
            self.activated = False


class Slider():

    def __init__(self, coord, screen, size):
        self.posit = coord
        self.size = size
        self.screen = screen
        self.bar_posit = coord
        self.click_pos = [0, 0]
        self.clicked = False
        self.activated = False

    def create(self):
        pg.draw.rect(self.screen, GRAY, (self.posit, self.size), 0)

    def click(self, events):
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN \
                    and self.bar_posit[0] <= pg.mouse.get_pos()[0] <= self.bar_posit[0] + self.size[1] \
                    and self.bar_posit[1] <= pg.mouse.get_pos()[1] <= self.bar_posit[1] + self.size[1]:
                self.clicked = True
                #self.click_pos = pg.mouse.get_pos()
            elif event.type == pg.MOUSEBUTTONUP:
                self.clicked = False

    def move(self):
        pg.draw.rect(self.screen, DARK_GRAY, (self.bar_posit, (self.size[1], self.size[1])), 0)
        if self.clicked:
            self.bar_posit[0] = pg.mouse.get_pos()[0]

    def active(self):
        if self.bar_posit[0] <= pg.mouse.get_pos()[0] <= self.bar_posit[0] + self.size[1] \
                and self.bar_posit[1] <= pg.mouse.get_pos()[1] <= self.bar_posit[1] + self.size[1]:
            self.activated = True
        else:
            self.activated = False


def quit_f():
    return True


clock = pg.time.Clock()
finished = False
SCREEN = pg.display.set_mode((800, 600))
quit_button = Button("quit", (100, 100), SCREEN, (100, 50))
slider = Slider([10, 500], SCREEN, [100, 20])

while not finished:
    clock.tick(60)
    SCREEN.fill((0, 0, 0))
    quit_button.create()
    slider.create()
    slider.active()
    quit_button.active()
    if slider.activated:
        slider.click(pg.event.get())
    slider.move()
    if quit_button.activated:
        finished = quit_button.click(pg.event.get(), quit_f)
    if pg.event.get() == pg.QUIT:
        finished = True
    pg.display.flip()

pg.quit()
