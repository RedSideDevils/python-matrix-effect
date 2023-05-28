import pygame as pg 
import random
import time 

class MatrixLetter:
    def __init__(self, app):
        self.app      = app 
        self.letters  = "abcdefghijklmnopqrstuvwxyz0123456789"
        self.fontSize = 16
        self.font     = pg.font.SysFont('arial', self.fontSize, bold = True)
        self.columns  = app.WIDTH // self.fontSize
        self.drops    = [1 for i in range(0, self.columns)]

    def draw(self):
        for i in range(0, len(self.drops)):
            char = random.choice(self.letters)
            end = time.time()
            if(int(end - app.start) % 6 < 3):
                color = (0,255,0)
            else:
                color = (255,0,0)
            
            char_render = self.font.render(char, False, color)

            pos = i * self.fontSize, (self.drops[i] - 1) * self.fontSize
            self.app.surface.blit(char_render, pos)

            if self.drops[i] * self.fontSize > app.HEIGHT and random.uniform(0,1) > 0.975:
                self.drops[i] = 0
                

            self.drops[i] = self.drops[i] + 1

    def run(self):
        self.draw() 


class Matrix:
    def __init__(self):
        self.RES = self.WIDTH, self.HEIGHT = 1920, 1080
        pg.init()
        self.screen = pg.display.set_mode(self.RES)
        self.surface = pg.Surface(self.RES, pg.SRCALPHA)
        self.clock = pg.time.Clock()
        self.MatrixLetters = MatrixLetter(self)
        self.start = time.time()

    def draw(self):
        self.surface.fill((0,0,0, 10))
        self.MatrixLetters.run()
        self.screen.blit(self.surface, (0,0))

    def run(self):
        while(True):
            self.draw()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.flip()
            self.clock.tick(30)

if __name__ == "__main__":
    app = Matrix()
    app.run()