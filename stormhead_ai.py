import pygame as pg
import random
from data.map import map_home

class mob_class():
    def __init__(self) -> None:
        self.x = random.randint(100, 150)
        self.y = 100
        self.spawn = False
        self.stormhead_idle = pg.image.load("data/mobs/stormhead/idle.png")
        self.enem = []

        self.left = False
        self.right = False
        self.radius = 10


    def update_stormhead(self, window ,player):

        if player.x == random.randint(int(player.x), int(player.x + 100)):
            self.spawn = True


        if self.spawn == True:
            self.stormhead_rect = pg.draw.rect(window, (255,0,0),(self.x  + 200- player.camera_x - map_home.map.pos_3 + 20,self.y  + 15, 10,16),1)

            if player.player_hitbox.left >= self.stormhead_rect.right + 10:
                self.x += 1

            if player.player_hitbox .right <= self.stormhead_rect.left -10:
                self.x -= 1




stormhead = mob_class()