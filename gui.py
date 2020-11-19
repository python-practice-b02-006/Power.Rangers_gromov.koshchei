import pygame as pg

pg.init()

WHITE = (255, 255, 255)
GRAY = (168, 168, 168)
DARK_GRAY = (108, 108, 108)


class Button():
    '''Button class
    '''

    def __init__(self, name, pos, screen, size):
        self.name = name
        self.pos = pos
        self.screen = screen
        self.color = GRAY
        self.size = size
        self.font = pg.font.SysFont("dejavusansmono", 25)
        self.activated = False

    def create(self):
        '''Create button on the surface
        '''
        pg.draw.rect(self.screen, self.color, (self.pos, self.size), 0)
        self.screen.blit((self.font.render(self.name, True, (0, 0, 0))), self.pos)

    def click(self, events, command):
        '''Check click on the button and execute command
        
        Parametrs:
        **events** - Pygame events.
        **command** - Command to execute.
        '''
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN \
                    and self.pos[0] <= pg.mouse.get_pos()[0] <= self.pos[0] + self.size[0] \
                    and self.pos[1] <= pg.mouse.get_pos()[1] <= self.pos[1] + self.size[1]:
                command()

    def active(self):
        '''Check button is activated(button down)
        '''
        if self.pos[0] <= pg.mouse.get_pos()[0] <= self.pos[0] + self.size[0] \
                and self.pos[1] <= pg.mouse.get_pos()[1] <= self.pos[1] + self.size[1]:
            self.activated = True
        else:
            self.activated = False


class Slider():
    '''Slider class
    '''

    def __init__(self, coord, coord2, screen, size):
        self.posit = coord
        self.size = size
        self.screen = screen
        self.bar_posit = coord2
        self.clicked = False
        self.activated = False
        self.level = self.bar_posit[0]/(self.size[0] - self.size[1])

    def create(self):
        '''Create slider on the surface
        '''
        pg.draw.rect(self.screen, GRAY, (self.posit, self.size), 0)
        pg.draw.rect(self.screen, DARK_GRAY, (self.bar_posit, (self.size[1], self.size[1])), 0)

    def click(self, events):
        '''Check click on the slider
        
        Parametrs:
        **events** - Pygame events.
        '''
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN \
                    and self.bar_posit[0] <= pg.mouse.get_pos()[0] <= self.bar_posit[0] + self.size[1] \
                    and self.bar_posit[1] <= pg.mouse.get_pos()[1] <= self.bar_posit[1] + self.size[1]:
                self.clicked = True
            elif event.type == pg.MOUSEBUTTONUP:
                self.clicked = False

    def move(self):
        '''Move slider
        '''
        pos = pg.mouse.get_pos()
        if not self.activated:
            self.clicked = False
        if self.clicked:
            if self.posit[0] + int(self.size[1]/2) <= pos[0] <= self.posit[0] + self.size[0] - int(self.size[1]/2):
                self.bar_posit[0] = pos[0] - int(self.size[1]/2)
        self.level = (self.bar_posit[0] - self.posit[0]) / (self.size[0] - self.size[1])

    def active(self):
        '''Check slider is active(button down and mouse in the square)
        '''        
        if self.bar_posit[0] <= pg.mouse.get_pos()[0] <= self.bar_posit[0] + self.size[1] \
                and self.bar_posit[1] <= pg.mouse.get_pos()[1] <= self.bar_posit[1] + self.size[1]:
            self.activated = True
        else:
            self.activated = False


if __name__ == "__main__":
    print("This module is not for direct call!")
