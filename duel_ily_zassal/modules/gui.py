import pygame as pg

pg.init()

WHITE = (255, 255, 255)
GRAY = (168, 168, 168)
DARK_GRAY = (108, 108, 108)


class Button():

    def __init__(self, name, pos, screen, size, text_pos):
        self.name = name
        self.pos = pos
        self.screen = screen
        self.color = GRAY
        self.size = size
        self.text_pos = text_pos
        self.font = pg.font.SysFont("dejavusansmono", 25)
        self.activated = False

    def create(self):
        pg.draw.rect(self.screen, self.color, (self.pos, self.size), 0)
        self.screen.blit((self.font.render(self.name, True, (0, 0, 0))), self.text_pos)

    def click(self, events, command):
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN \
                    and self.pos[0] <= pg.mouse.get_pos()[0] <= self.pos[0] + self.size[0] \
                    and self.pos[1] <= pg.mouse.get_pos()[1] <= self.pos[1] + self.size[1]:
                command()

    def active(self):
        if self.pos[0] <= pg.mouse.get_pos()[0] <= self.pos[0] + self.size[0] \
                and self.pos[1] <= pg.mouse.get_pos()[1] <= self.pos[1] + self.size[1]:
            self.activated = True
        else:
            self.activated = False


class Progress_bar():

     def __init__(self, coord, size, level, screen, name, color):
         self.coord = coord
         self.size = size
         self.level = level
         self.lev_max = level
         self.screen = screen
         self.name = name
         self.color = color
     def draw(self):
         pg.draw.rect(self.screen, (255,255,255), (self.coord, self.size), 0)
         f = pg.font.SysFont('arial', 26)
         text = f.render(self.name, 0, (255, 255, 255))
         self.screen.blit(text, (self.coord[0] + 5, self.coord[1] -30))
         if self.level <= 0:
             self.level = 0
         pg.draw.rect(self.screen, self.color,
                      (self.coord, (int(self.size[0]*self.level/self.lev_max), self.size[1])), 0)



class Dialog():
    pass


class Text_box():
    pass


if __name__ == "__main__":
    print("This module is not for direct call!")

