import pygame as pg
from modules import gui
import os
pg.init()


class Guide():

    def __init__(self, screen, screen_size):
        self.screen = screen
        self.screen_size = screen_size
        self.back_button = gui.Button("BACK", (self.screen_size[0] - 250, self.screen_size[1] - 100), self.screen,
                                      (90,40), (self.screen_size[0] - 230, self.screen_size[1] - 90))


    def set_guide_window(self):
        SC_IMG = pg.image.load(os.path.join("Images", "guide.jpg"))
        new_image = pg.transform.scale(SC_IMG, (self.screen_size))
        self.screen.blit(new_image, (0, 0))
        pg.draw.rect(self.screen, (255, 255, 255), (self.screen_size[0] - 430, 30, 385, 460) )
        many_words = "     Main buttons:\nEsc - pause the game\nMouse button - fire\nF - change field management\n" \
                     "K_RIGHT - increase x component of field\nK_LEFT - reduce x component of field\n" \
                     "K_UP - increase y component of field\nK_DOWN - reduce y component of field"
        f = pg.font.SysFont('bookmanoldstyleполужирныйкурсив', 26)
        words = [word.split(' ') for word in many_words.splitlines()]  # 2D array where each row is a list of words.
        space = f.size(' ')[0]  # The width of a space.
        max_width, max_height = self.screen.get_size()
        x, y = self.screen_size[0] - 430, 50
        for line in words:
            for word in line:
                word_surface = f.render(word, 0, (255, 0, 0))
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = self.screen_size[0] - 350  # Reset the x.
                    y += word_height  # Start on new row.
                self.screen.blit(word_surface, (x, y))
                x += word_width + space
            x = self.screen_size[0] - 400  # Reset the x.
            y += word_height  # Start on new row.


        self.back_button.create()
        self.back_button.active()


if __name__ == "__main__":
    print("This module is not for direct call!")