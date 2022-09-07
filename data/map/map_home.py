import pygame as pg


class Map_class():
    def __init__(self) -> None:
        self.bg_layer_1 = pg.image.load("data/map/oak_woods/background_layer_1.map")
        self.bg_layer_2 = pg.image.load("data/map/oak_woods/background_layer_2.map")
        self.bg_layer_3 = pg.image.load("data/map/oak_woods/background_layer_3.map")
        self.block_1 = pg.image.load("data/map/oak_woods/oak_block1.map")
        self.pos_1 = 0
        self.pos_2 = 0
        self.pos_3 = 0
        self.x = 0
        self.y = -30


        
    def update(self , window , player):

        if player.keyinput[pg.K_RIGHT] and player.normal_1 == False and player.normal_2 == False and player.normal_3 == False and player.x >= 16 and player.x <= 69 * 30:
            self.pos_1 += 0.5
            self.pos_2 += 0.7
            self.pos_3 += 0.9

        if player.keyinput[pg.K_LEFT] and player.normal_1 == False and player.normal_2 == False and player.normal_3 == False and player.x >= 16 and player.x <= 69 * 30:
            self.pos_1 -= 0.5
            self.pos_2 -= 0.7
            self.pos_3 -= 0.9

        if player.x >= -70 and player.x <= 150 * 7:
            window.blit(self.bg_layer_1 , (self.x - 79 * 4 - self.pos_1 - player.camera_x ,self.y - player.camera_y))
            window.blit(self.bg_layer_2 , (self.x - 79 * 4 - self.pos_2 - player.camera_x ,self.y - player.camera_y))
            window.blit(self.bg_layer_3 , (self.x - 79 * 4 - self.pos_3 - player.camera_x ,self.y - player.camera_y))
            window.blit(self.block_1 , (self.x - 79 * 4 - player.camera_x - self.pos_3 ,self.y + 165))


        if player.x >= -70 and player.x <= 150 * 7:
            window.blit(self.bg_layer_1 , (self.x - self.pos_1 - player.camera_x ,self.y - player.camera_y))
            window.blit(self.bg_layer_2 , (self.x - self.pos_2 - player.camera_x ,self.y - player.camera_y))
            window.blit(self.bg_layer_3 , (self.x - self.pos_3 - player.camera_x ,self.y - player.camera_y))
            window.blit(self.block_1 , (self.x - player.camera_x - self.pos_3 ,self.y + 165))

        if player.x >= -70 and player.x <= 150 * 8:
            window.blit(self.bg_layer_1 , (self.x + 79 * 4 - self.pos_1 - player.camera_x ,self.y - player.camera_y))
            window.blit(self.bg_layer_2 , (self.x + 79 * 4 - self.pos_2 - player.camera_x ,self.y - player.camera_y))
            window.blit(self.bg_layer_3 , (self.x + 79 * 4 - self.pos_3 - player.camera_x ,self.y - player.camera_y))
            window.blit(self.block_1 , (self.x + 79 * 4 - player.camera_x - self.pos_3 ,self.y + 165))

        if player.x >= 70 * 2 and player.x <= 150 * 9:
            window.blit(self.bg_layer_1 , (self.x + 79 * 8 - self.pos_1 - player.camera_x ,self.y - player.camera_y))
            window.blit(self.bg_layer_2 , (self.x + 79 * 8 - self.pos_2 - player.camera_x ,self.y - player.camera_y))
            window.blit(self.bg_layer_3 , (self.x + 79 * 8 - self.pos_3 - player.camera_x ,self.y - player.camera_y))
            window.blit(self.block_1 , (self.x + 79 * 8 - player.camera_x - self.pos_3 ,self.y + 165))

        if player.x >= 70 * 4 and player.x <= 150 * 10:
            window.blit(self.bg_layer_1 , (self.x + 79 * 12 - self.pos_1 - player.camera_x ,self.y - player.camera_y))
            window.blit(self.bg_layer_2 , (self.x + 79 * 12 - self.pos_2 - player.camera_x ,self.y - player.camera_y))
            window.blit(self.bg_layer_3 , (self.x + 79 * 12 - self.pos_3 - player.camera_x ,self.y - player.camera_y))
            window.blit(self.block_1 , (self.x + 79 * 12 - player.camera_x - self.pos_3 ,self.y + 165))


        if player.x >= 70 * 6 and player.x <= 150 * 11:
            window.blit(self.bg_layer_1 , (self.x + 79 * 16 - self.pos_1 - player.camera_x ,self.y - player.camera_y))
            window.blit(self.bg_layer_2 , (self.x + 79 * 16 - self.pos_2 - player.camera_x ,self.y - player.camera_y))
            window.blit(self.bg_layer_3 , (self.x + 79 * 16 - self.pos_3 - player.camera_x ,self.y - player.camera_y))
            window.blit(self.block_1 , (self.x + 79 * 16 - player.camera_x - self.pos_3 ,self.y + 165))


        if player.x >= 70 * 8 and player.x <= 150 * 12:
            window.blit(self.bg_layer_1 , (self.x + 79 * 20 - self.pos_1 - player.camera_x ,self.y - player.camera_y))
            window.blit(self.bg_layer_2 , (self.x + 79 * 20 - self.pos_2 - player.camera_x ,self.y - player.camera_y))
            window.blit(self.bg_layer_3 , (self.x + 79 * 20 - self.pos_3 - player.camera_x ,self.y - player.camera_y))
            window.blit(self.block_1 , (self.x + 79 * 20 - player.camera_x - self.pos_3 ,self.y + 165))


        if player.x >= 70 * 10 and player.x <= 150 * 18:
            window.blit(self.bg_layer_1 , (self.x + 79 * 24 - self.pos_1 - player.camera_x ,self.y - player.camera_y))
            window.blit(self.bg_layer_2 , (self.x + 79 * 24 - self.pos_2 - player.camera_x ,self.y - player.camera_y))
            window.blit(self.bg_layer_3 , (self.x + 79 * 24 - self.pos_3 - player.camera_x ,self.y - player.camera_y))
            window.blit(self.block_1 , (self.x + 79 * 24 - player.camera_x - self.pos_3 ,self.y + 165))


        if player.x >= 70 * 12 and player.x <= 150 * 19:
            window.blit(self.bg_layer_1 , (self.x + 79 * 28 - self.pos_1 - player.camera_x ,self.y - player.camera_y))
            window.blit(self.bg_layer_2 , (self.x + 79 * 28 - self.pos_2 - player.camera_x ,self.y - player.camera_y))
            window.blit(self.bg_layer_3 , (self.x + 79 * 28 - self.pos_3 - player.camera_x ,self.y - player.camera_y))
            window.blit(self.block_1 , (self.x + 79 * 28 - player.camera_x - self.pos_3 ,self.y + 165))


        if player.x >= 70 * 14 and player.x <= 150 * 25:
            window.blit(self.bg_layer_1 , (self.x + 79 * 32 - self.pos_1 - player.camera_x ,self.y - player.camera_y))
            window.blit(self.bg_layer_2 , (self.x + 79 * 32 - self.pos_2 - player.camera_x ,self.y - player.camera_y))
            window.blit(self.bg_layer_3 , (self.x + 79 * 32 - self.pos_3 - player.camera_x ,self.y - player.camera_y))
            window.blit(self.block_1 , (self.x + 79 * 32 - player.camera_x - self.pos_3 ,self.y + 165))


        if player.x >= 70 * 16 and player.x <= 150 * 26:
            window.blit(self.bg_layer_1 , (self.x + 79 * 36 - self.pos_1 - player.camera_x ,self.y - player.camera_y))
            window.blit(self.bg_layer_2 , (self.x + 79 * 36 - self.pos_2 - player.camera_x ,self.y - player.camera_y))
            window.blit(self.bg_layer_3 , (self.x + 79 * 36 - self.pos_3 - player.camera_x ,self.y - player.camera_y))
            window.blit(self.block_1 , (self.x + 79 * 36 - player.camera_x - self.pos_3 ,self.y + 165))


        if player.x >= 70 * 18 and player.x <= 150 * 27:
            window.blit(self.bg_layer_1 , (self.x + 79 * 40 - self.pos_1 - player.camera_x ,self.y - player.camera_y))
            window.blit(self.bg_layer_2 , (self.x + 79 * 40 - self.pos_2 - player.camera_x ,self.y - player.camera_y))
            window.blit(self.bg_layer_3 , (self.x + 79 * 40 - self.pos_3 - player.camera_x ,self.y - player.camera_y))
            window.blit(self.block_1 , (self.x + 79 * 40 - player.camera_x - self.pos_3 ,self.y + 165))

        if player.x >= 70 * 20 and player.x <= 150 * 28:
            window.blit(self.bg_layer_1 , (self.x + 79 * 44 - self.pos_1 - player.camera_x ,self.y - player.camera_y))
            window.blit(self.bg_layer_2 , (self.x + 79 * 44 - self.pos_2 - player.camera_x ,self.y - player.camera_y))
            window.blit(self.bg_layer_3 , (self.x + 79 * 44 - self.pos_3 - player.camera_x ,self.y - player.camera_y))
            window.blit(self.block_1 , (self.x + 79 * 44 - player.camera_x - self.pos_3 ,self.y + 165))


        if player.x <= 15:
            player.x = 15


        if player.x >= 70 * 30:
            player.x = 70 * 30

map = Map_class()