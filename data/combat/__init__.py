import pygame as pg
class combat_Class():
    def __init__(self) -> None:
        self.atk_cmb_1_num_left = 0
        self.atk_cmb_1_num_right = 0
        self.atk_cmb_2_num_left = 0
        self.atk_cmb_2_num_right = 0
        self.atk_cmb_3_num_left = 0
        self.atk_cmb_3_num_right = 0
        self.atk_cmb_1_list_right = []
        self.atk_cmb_2_list_right = []
        self.atk_cmb_3_list_right = []
        self.atk_cmb_1_list_left = []
        self.atk_cmb_2_list_left = []
        self.atk_cmb_3_list_left = []

    def cmb_1_loop_right(self,window,x,y):
        for num in range(1,6):
            self.atk_cmb_1_anim_right = pg.image.load(f"data/combat/atk_cmb_1 ({num}).anim")
            self.atk_cmb_1_list_right.append(self.atk_cmb_1_anim_right)
            window.blit(self.atk_cmb_1_list_right[int(self.atk_cmb_1_num_right)],(x,y))

    def cmb_1_loop_left(self,window,x,y):
        for num in range(1,6):

            self.atk_cmb_1_anim_left= pg.image.load(f"data/combat/atk_cmb_1 ({num}).anim")
            self.atk_cmb_1_anim_left = pg.transform.flip(self.atk_cmb_1_anim_left, True, False)
            self.atk_cmb_1_list_left.append(self.atk_cmb_1_anim_left)
            window.blit(self.atk_cmb_1_list_left[int(self.atk_cmb_1_num_left)],(x,y))
    
    def cmb_2_loop_right(self,window,x,y):
        for num in range(1,7):

            self.atk_cmb_2_anim_right = pg.image.load(f"data/combat/atk_cmb_2 ({num}).anim")
            self.atk_cmb_2_list_right.append(self.atk_cmb_2_anim_right)
            window.blit(self.atk_cmb_2_list_right[int(self.atk_cmb_2_num_right)],(x,y))
            
    def cmb_2_loop_left(self,window,x,y):
        for num in range(1,7):

            self.atk_cmb_2_anim_left = pg.image.load(f"data/combat/atk_cmb_2 ({num}).anim")
            self.atk_cmb_2_anim_left = pg.transform.flip(self.atk_cmb_2_anim_left, True, False)
            self.atk_cmb_2_list_left.append(self.atk_cmb_2_anim_left)
            window.blit(self.atk_cmb_2_list_left[int(self.atk_cmb_2_num_left)],(x,y))

    def cmb_3_loop_right(self,window , x,y):
        for num in range(1,7):
            self.atk_cmb_3_anim_right = pg.image.load(f"data/combat/atk_cmb_3 ({num}).anim")
            self.atk_cmb_3_list_right.append(self.atk_cmb_3_anim_right)
            window.blit(self.atk_cmb_3_list_right[int(self.atk_cmb_3_num_right)],(x,y))
    
    def cmb_3_loop_left(self, window, x,y):
        for num in range(1,7):
            self.atk_cmb_3_anim_left = pg.image.load(f"data/combat/atk_cmb_3 ({num}).anim")
            self.atk_cmb_3_anim_left = pg.transform.flip(self.atk_cmb_3_anim_left, True, False)
            self.atk_cmb_3_list_left.append(self.atk_cmb_3_anim_left)
            window.blit(self.atk_cmb_3_list_left[int(self.atk_cmb_3_num_left)],(x,y))

anim = combat_Class()