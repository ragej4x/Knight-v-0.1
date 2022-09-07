from itertools import pairwise
import pygame as pg
import random

class oak_leaf_particle():
    def __init__(self):
        
        self.particle = []
        self.x = 5
        self.y = 20


    def update(self , window, player):
        
        for num in range(1,3):
            num += 1
            if num >= 3:
                num = 1
            image = pg.image.load(f"data/particles/oak_leaf{num}.png")
            self.particle.append([random.randint(int(player.x) - 100,int(player.x) + 300), random.randint(0,110), image, 6])

        for particle in self.particle:
            particle[0] -= 1
            particle[1] += 1
            particle[3] -= 0.2

            leaf = pg.transform.scale(particle[2],(particle[3],particle[3]))
            window.blit(leaf,(int(particle[0]) - player.camera_x, int(particle[1])))
            
            if particle[3] <= 1:
                self.particle.remove(particle) 

            if player.x >= player.camera_x + player.border +1:
                particle[0] -= 2
            if player.x <= player.camera_x:
                particle[0] += 2

oak_leaf_fx = oak_leaf_particle()