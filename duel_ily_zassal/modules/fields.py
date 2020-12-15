from modules import vectors
import pygame as pg


class Field():

    def __init__(self, B, E):
        self.B = vectors.Vector(B[0], B[1], B[2])
        self.E = vectors.Vector(E[0], E[1], E[2])
        self.change = False
        self.dir = 'u'
        self.field_type = True

    def calculate_force(self, bullets):
        local = bullets
        for body in local:
            body.force = 0 * body.force
                    
            body.force = body.force + body.m_c * body.vel @ self.E 
            body.force = body.force - body.m_c * self.B
                
            body.force = body.force + body.e_c * body.vel @ self.B 
            body.force = body.force + body.e_c * self.E
            
        return local

    def change_field(self):
        if self.change:
            if self.field_type:
                if self.dir == 'u':
                    self.E.z -= 10
                elif self.dir == 'l':
                    self.E.x -= 10
                elif self.dir == 'r':
                    self.E.x += 10
                elif self.dir == 'd':
                    self.E.z += 10
            else:
                if self.dir == 'u':
                    self.B.z -= 1
                elif self.dir == 'l':
                    self.B.y -= 1
                elif self.dir == 'r':
                    self.B.y += 1
                elif self.dir == 'd':
                    self.B.z += 1

    def draw(self, screen, screensize):
        if self.field_type:
            f = pg.font.SysFont('garamondполужирный', 26)
            text1 = f.render("Ex = " + str(self.E.x), 0, (255, 0, 0))
            text2 = f.render("Ez = " + str(self.E.z), 0, (255, 0, 0))
            screen.blit(text1, (screensize[0]-100, int(2 * screensize[1]/16)))
            screen.blit(text2, (screensize[0] - 100, int(3 * screensize[1] / 16)))
            text3 = f.render("By = " + str(self.B.y), 0, (100, 100, 100))
            text4 = f.render("Bz = " + str(self.B.z), 0, (100, 100, 100))
            screen.blit(text3, (40, int(2 * screensize[1] / 16)))
            screen.blit(text4, (40, int(3 * screensize[1] / 16)))
        else:
            f = pg.font.SysFont('garamondполужирный', 26)
            text1 = f.render("Ex = " + str(self.E.x), 0, (100, 100, 100))
            text2 = f.render("Ez = " + str(self.E.z), 0, (100, 100, 100))
            screen.blit(text1, (screensize[0]-100, int(2 * screensize[1]/16)))
            screen.blit(text2, (screensize[0] - 100, int(3 * screensize[1] / 16)))
            text3 = f.render("By = " + str(self.B.y), 0, (255, 0, 0))
            text4 = f.render("Bz = " + str(self.B.z), 0, (255, 0, 0))
            screen.blit(text3, (40, int(2 * screensize[1] / 16)))
            screen.blit(text4, (40, int(3 * screensize[1] / 16)))


if __name__ == "__main__":
    print("This module is not for direct call!")
