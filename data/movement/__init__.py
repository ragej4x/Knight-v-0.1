import pygame as pg
class movement_Class():
    def __init__(self) -> None:
        self.idl_num_left = 0
        self.idl_num_right = 0
        self.idl2_num_left = 0
        self.idl2_num_right = 0
        self.run_num_left = 0
        self.run_num_right = 0
        self.run2_num_left = 0
        self.run2_num_right = 0
        self.jmp_num_left = 0
        self.jmp_num_right = 0
        self.idl_list_right = []
        self.idl2_list_right = []
        self.run_list_right = []
        self.jmp_list_right = []
        self.run2_list_right = []
        self.run2_list_left = []
        self.idl_list_left = []
        self.run_list_left = []
        self.jmp_list_left = []
        self.idl2_list_left = []


    def idl_loop_right(self,window , x,y):
        for num in range(1,5):
            self.idl_anim_right = pg.image.load(f"data/movement/idl{num}.anim")
            self.idl_list_right.append(self.idl_anim_right)
            window.blit(self.idl_list_right[int(self.idl_num_right)],(x,y))
            

    def idl_loop_left(self,window , x,y):
        for num in range(1,5):
            self.idl_anim_left = pg.image.load(f"data/movement/idl{num}.anim")
            self.idl_anim_left = pg.transform.flip(self.idl_anim_left, True , False)
            self.idl_list_left.append(self.idl_anim_left)
            window.blit(self.idl_list_left[int(self.idl_num_left)],(x,y))


    def run_loop_right(self,window,x,y):
        for num in range(1,7):

            self.run_anim_right = pg.image.load(f"data/movement/run{num}.anim")
            self.run_list_right.append(self.run_anim_right)
            window.blit(self.run_list_right[int(self.run_num_right)],(x,y))
            
    def run_loop_left(self,window,x,y):
        for num in range(1,7):
            self.run_anim_left = pg.image.load(f"data/movement/run{num}.anim")
            self.run_anim_left = pg.transform.flip(self.run_anim_left, True , False)
            self.run_list_left.append(self.run_anim_left)
            window.blit(self.run_list_left[int(self.run_num_left)],(x,y))

    def jmp_loop_right(self,window,x,y):
        for num in range(1,5):
            self.jmp_anim_right = pg.image.load(f"data/movement/jmp ({num}).anim")
            self.jmp_list_right.append(self.jmp_anim_right)
            window.blit(self.jmp_list_right[int(self.jmp_num_right)],(x,y))

 
    def jmp_loop_left(self,window,x,y):
        for num in range(1,5):
            self.jmp_anim_left = pg.image.load(f"data/movement/jmp ({num}).anim")
            self.jmp_anim_left = pg.transform.flip(self.jmp_anim_left, True , False)
            self.jmp_list_left.append(self.jmp_anim_left)
            window.blit(self.jmp_list_left[int(self.jmp_num_left)],(x,y))     

    def idl2_loop_right(self,window,x,y):
        for num in range(1,5):
            self.idl2_anim_right = pg.image.load(f"data/movement/idl2_{num}.anim")
            self.idl2_list_right.append(self.idl2_anim_right)
            window.blit(self.idl2_list_right[int(self.idl2_num_right)], (x,y))
    
    def idl2_loop_left(self,window,x,y):
        for num in range(1,5):
            self.idl2_anim_left = pg.image.load(f"data/movement/idl2_{num}.anim")
            self.idl2_anim_left = pg.transform.flip(self.idl2_anim_left, True, False)
            self.idl2_list_left.append(self.idl2_anim_left)
            window.blit(self.idl2_list_left[int(self.idl2_num_left)], (x,y))

    def run2_loop_right(self, window , x ,y):
        for num in range(1,7):
            self.run2_anim_right = pg.image.load(f"data/movement/run2_{num}.anim")
            self.run2_list_right.append(self.run2_anim_right)
            window.blit(self.run2_list_right[int(self.run2_num_right)],(x,y))


    def run2_loop_left(self, window , x ,y):
        for num in range(1,7):
            self.run2_anim_left = pg.image.load(f"data/movement/run2_{num}.anim")
            self.run2_anim_left = pg.transform.flip(self.run2_anim_left ,True , False)
            self.run2_list_left.append(self.run2_anim_left)
            window.blit(self.run2_list_left[int(self.run2_num_left)],(x,y))

anim = movement_Class()