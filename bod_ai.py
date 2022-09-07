import pygame as pg

class mob_class():
    def __init__(self):
        self.x , self.y = 0,120
        self.bod_rect = pg.Rect(self.x ,self.y ,(10,17))
        self.bod_img = pg.image.load("data/mobs/bod/")
        pass
    
    def animation(self,window):  
        pass

    def update(self, window):
        pass


bod = mob_class()