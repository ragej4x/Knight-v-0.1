import pygame as pg
import random
from data.map import map_home

class stormhead_Class():
    def __init__(self) -> None:
        self.x = random.randint(100, 150)
        self.y = 100
        self.spawn = False
        self.stormhead_idle = pg.image.load("data/mobs/stormhead/idle.png")
        self.enem = []

        self.left = False
        self.right = False
        self.radius = 10


        self.idle_count_R = 0
        self.idle_count_L = 0
        self.idle_right = []
        self.idle_left = []

    def idle_right_update(self, window):
        for num in range(1,9):
            idleImg = pg.image.load(f"data/mobs/stormhead/storm_idle{num}.png")
            

    def left_update(self,window):
        pass


    def update(self, window, player):
        

        if player.x == random.randint(int(player.x), int(player.x + 100)):
            self.spawn = True


        if self.spawn == True:
            self.stormhead_rect = pg.draw.rect(window, (255,0,0),(self.x  + 200- player.camera_x - map_home.map.pos_3 + 20,self.y  + 15, 10,16),1)

            if player.player_hitbox.left >= self.stormhead_rect.right + 10:
                self.x += 1

            if player.player_hitbox .right <= self.stormhead_rect.left -10:
                self.x -= 1



stormAni = stormhead_Class()