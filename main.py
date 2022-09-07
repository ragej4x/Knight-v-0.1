import random, pygame  as pg
from pygame import mixer
pg.init()

from data import movement
from data import combat
from data import config
from data.map import map_home

import particles


width = config.set.display_res_w
height = config.set.display_res_h

display = pg.display.set_mode((width , height))
fps = pg.time.Clock()
font = pg.font.Font("data/pix.ttf", 18)
bg = pg.image.load("data/black.png")
window = pg.Surface((width//4,height//4))


bg.set_alpha(150)
loop = True


shake_str = 100

def show_fps():
    font_fps = pg.font.Font("data/pix.ttf", config.set.fps_scale)
    fps_display = str(int(fps.get_fps()))
    fps_onscreen_txt = font_fps.render(str("FPS : ") + fps_display, True ,(255,255,250))
    display.blit(fps_onscreen_txt,(config.set.fps_scale//3,config.set.fps_scale//3))

    if config.set.fps >= 66:
        loop = False

    FPS_MONITOR = float(fps.get_fps())
    if FPS_MONITOR <= 40:
        NOTIF = font_fps.render("LOW CLIENT FPS", False, (255,255,255))
        display.blit(NOTIF,(config.set.fps_scale//3 + 100,config.set.fps_scale//3))

def update():
    global loop
    # DISPLAY FPS
    if config.set.display_fps == True:
        show_fps()

    pg.display.flip()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            loop = False

    scale = pg.transform.scale(window,(width, height))
    display.blit(scale,(0 - shake_interval,0 - shake_interval))
    fps.tick(config.set.fps)


class Class_sfx():
    def __init__(self) -> None:
        self.cmb_1 = mixer.Sound("data/sfx/cmb_1_sfx.wav")
sfx = Class_sfx()


class player_Class():
    def __init__(self) -> None:
        self.x = 0
        self.y = 100
        self.jump_height = 7
        self.y_vel = self.jump_height
        self.right = True
        self.left = False
        self.camera_x = 0
        self.camera_y = 0
        self.jump = False
        self.jump_timer = 0
        self.on_g = True
        self.run = False

        self.border = width//10

        self.in_combat_pos = False
        self.timer = 0
        
        self.cmbtrig = False
        self.normal_1 = False
        self.normal_2 = False
        self.normal_3 = False


    def collider(self):

        self.player_hitbox = pg.draw.rect(window, (255,0,0),(self.x + 20 - self.camera_x, self.y + 15, 10,16),1)
      
        if self.right == True and self.left == False :
            self.player_col = pg.draw.rect(window, (0,0,255),(self.x + 30 - self.camera_x, self.y + 20, 15,5),1)
        
        if self.left == True and self.right == False :
            self.player_col = pg.draw.rect(window, (0,0,255),(self.x + 5 - self.camera_x, self.y + 20, 15,5),1)
        


    def update(self):
        self.keyinput = pg.key.get_pressed()
        

        if self.keyinput[pg.K_RIGHT] and self.normal_1 == False and self.normal_2 == False and self.normal_3 == False:
            self.right = True
            self.left = False

            if self.x >= self.camera_x + self.border:
                self.camera_x += 1

        if self.keyinput[pg.K_LEFT] and self.normal_1 == False and self.normal_2 == False and self.normal_3 == False:
            self.left = True
            self.right = False

            if self.x <= self.camera_x:
                self.camera_x -= 1


        if self.keyinput[pg.K_UP] and self.normal_1 == False and self.normal_2 == False and self.normal_3 == False and self.jump_timer == 10:
            self.jump = True
            self.jump_timer = 0


        self.jump_timer += 0.2
        if self.jump_timer >= 10:
            self.jump_timer = 10

        #JUMP RIGHT

        if self.jump == True and self.right == True:
            self.y -= self.y_vel
            self.y_vel -= 0.6
            self.x += 1
            """
            if self.x >= self.camera_x + self.border:
                self.camera_x = self.x - self.border
                """


            if self.y_vel < -self.jump_height:
                self.y = 100
                self.y_vel = self.jump_height
                self.jump = False
            
        #JUMP LEFT
        if self.jump == True and self.left == True:
            self.y -= self.y_vel
            self.y_vel -= 0.6
            self.x -= 1

            """
            if self.x <= self.camera_x:
                self.camera_x = self.x
            """

            
            if self.y_vel < -self.jump_height:
                self.y_vel = self.jump_height
                self.y = 100
                self.jump = False


        if self.x >= self.camera_x + self.border:
            self.camera_x = self.x - self.border

        if self.x <= self.camera_x:
            self.camera_x = self.x

    def animation(self):
        self.run = False
        if self.keyinput[pg.K_RIGHT] and self.left == False and self.jump == False and self.normal_1 == False and self.normal_2 == False and self.normal_3 == False and self.in_combat_pos == False:
            movement.anim.run_loop_right(window,self.x - self.camera_x ,self.y - self.camera_y)
            movement.anim.run_num_right += 0.15
            if movement.anim.run_num_right >= 6:
                movement.anim.run_num_right = 0
            self.x += 1.5
            self.run = True
            # INCOMBAT POS RIGHT
        if self.keyinput[pg.K_RIGHT] and self.left == False and self.jump == False and self.normal_1 == False and self.normal_2 == False and self.normal_3 == False and self.in_combat_pos == True:
            movement.anim.run2_loop_right(window,self.x - self.camera_x ,self.y - self.camera_y)
            movement.anim.run2_num_right += 0.15
            if movement.anim.run2_num_right >= 6:
                movement.anim.run2_num_right = 0
            self.x += 1.5
            self.run = True

        else:
            if self.left == False and self.jump == False and self.normal_1 == False and self.normal_2 == False and self.normal_3 == False and self.in_combat_pos == False and self.run == False:
                movement.anim.idl_loop_right(window,self.x - self.camera_x ,self.y - self.camera_y)
                movement.anim.idl_num_right += 0.13
                if movement.anim.idl_num_right >= 5:
                    movement.anim.idl_num_right = 0

            # INCOMBAT POS RIGHT

            if self.left == False and self.jump == False and self.normal_1 == False and self.normal_2 == False and self.normal_3 == False and self.in_combat_pos == True and self.run == False:
                movement.anim.idl2_loop_right(window,self.x - self.camera_x ,self.y - self.camera_y)
                movement.anim.idl2_num_right += 0.13
                if movement.anim.idl2_num_right >= 5:
                    movement.anim.idl2_num_right = 0


        if self.keyinput[pg.K_LEFT] and self.right == False and self.jump == False and self.normal_1 == False and self.normal_2 == False and self.normal_3 == False and self.in_combat_pos == False:
            movement.anim.run_loop_left(window,self.x - self.camera_x ,self.y - self.camera_y)
            movement.anim.run_num_left += 0.15
            if movement.anim.run_num_left >= 6:
                movement.anim.run_num_left = 0
            self.x -= 1.5
            self.run = True

            # INCOMBAT POS LEFT
        if self.keyinput[pg.K_LEFT] and self.right == False and self.jump == False and self.normal_1 == False and self.normal_2 == False and self.normal_3 == False and self.in_combat_pos == True:
            movement.anim.run2_loop_left(window,self.x - self.camera_x ,self.y - self.camera_y)
            movement.anim.run2_num_left += 0.15
            if movement.anim.run2_num_left >= 6:
                movement.anim.run2_num_left = 0
            self.x -= 1.5
            self.run = True


        else:
            if self.right == False and self.jump == False and self.normal_1 == False and self.normal_2 == False and self.normal_3 == False and self.in_combat_pos == False and self.run == False:
                movement.anim.idl_loop_left(window,self.x - self.camera_x ,self.y - self.camera_y)
                movement.anim.idl_num_left += 0.13
                if movement.anim.idl_num_left >= 5:
                    movement.anim.idl_num_left = 0
            # INCOMBAT POS LEFT
            if self.right == False and self.jump == False and self.normal_1 == False and self.normal_2 == False and self.normal_3 == False and self.in_combat_pos == True and self.run == False:
                movement.anim.idl2_loop_left(window,self.x - self.camera_x ,self.y - self.camera_y)
                movement.anim.idl2_num_left += 0.13
                if movement.anim.idl2_num_left >= 5:
                    movement.anim.idl2_num_left = 0

        if self.jump == True and self.right == True:
            movement.anim.jmp_loop_right(window,self.x - self.camera_x , self.y - self.camera_y)
            movement.anim.jmp_num_right += 0.2
            if movement.anim.jmp_num_right >= 4:
                movement.anim.jmp_num_right = 0

        if self.jump == True and self.left == True :
            movement.anim.jmp_loop_left(window,self.x - self.camera_x , self.y - self.camera_y)
            movement.anim.jmp_num_left += 0.2
            if movement.anim.jmp_num_left >= 4:
                movement.anim.jmp_num_left = 0

# COMBAT    

    def combat(self):
        if self.keyinput[pg.K_q] and self.cmbtrig == False and self.jump == False:
            self.normal_1 = True
            self.cmbtrig = True
            self.in_combat_pos = True

            
        
        if self.in_combat_pos == True:
            self.timer += 0.1
        
        if self.timer >= 50:
            self.in_combat_pos = False
            self.timer = 0

        # COMBAT NORMAL SKILL PHYSICS

        if combat.anim.atk_cmb_3_num_right == 0.2 and self.right == True:
            self.x += 15
            if self.x >= self.camera_x + self.border:
                self.camera_x = self.x - self.border

        if combat.anim.atk_cmb_3_num_left == 0.2 and self.left == True:
            self.x -= 15
            if self.x <= self.camera_x:
                self.camera_x = self.x

    def combat_animation(self):

        # NORMAL SKILL SET RIGHT

        if self.normal_1 == True and self.right == True:
            
            combat.anim.cmb_1_loop_right(window, self.x - self.camera_x , self.y - self.camera_y)
            combat.anim.atk_cmb_1_num_right += 0.2

        if combat.anim.atk_cmb_1_num_right >= 5:
            combat.anim.atk_cmb_1_num_right = 0
            self.normal_1 = False
            self.normal_2 = True
        
        if self.normal_2 == True and self.right == True:
            combat.anim.cmb_2_loop_right(window, self.x - self.camera_x , self.y - self.camera_y)
            combat.anim.atk_cmb_2_num_right += 0.2

        if combat.anim.atk_cmb_2_num_right >= 6:
            combat.anim.atk_cmb_2_num_right = 0
            self.normal_2 = False
            self.normal_3 = True

        if self.normal_3 == True and self.right == True:
            combat.anim.cmb_3_loop_right(window, self.x - self.camera_x , self.y - self.camera_y)
            combat.anim.atk_cmb_3_num_right += 0.2

        if combat.anim.atk_cmb_3_num_right >= 6:
            combat.anim.atk_cmb_3_num_right = 0
            self.normal_3 = False
            self.cmbtrig = False
            sfx.cmb_1.stop()
        # NORMAL SKILL SET LEFT

        if self.normal_1 == True and self.left == True:
            combat.anim.cmb_1_loop_left(window, self.x - self.camera_x , self.y - self.camera_y)
            combat.anim.atk_cmb_1_num_left += 0.2

        if combat.anim.atk_cmb_1_num_left >= 5:
            combat.anim.atk_cmb_1_num_left= 0
            self.normal_1 = False
            self.normal_2 = True
        
        if self.normal_2 == True and self.left == True:
            combat.anim.cmb_2_loop_left(window, self.x - self.camera_x , self.y - self.camera_y)
            combat.anim.atk_cmb_2_num_left += 0.2

        if combat.anim.atk_cmb_2_num_left >= 6:
            combat.anim.atk_cmb_2_num_left = 0
            self.normal_2 = False
            self.normal_3 = True

        if self.normal_3 == True and self.left == True:
            combat.anim.cmb_3_loop_left(window, self.x - self.camera_x , self.y - self.camera_y)
            combat.anim.atk_cmb_3_num_left+= 0.2

        if combat.anim.atk_cmb_3_num_left >= 6:
            combat.anim.atk_cmb_3_num_left = 0
            self.normal_3 = False
            self.cmbtrig = False
            sfx.cmb_1.stop()
    

player = player_Class()


while loop == True:
    player.update()
    window.fill((30,30,30))
    #window.blit(bg,(0 -player.camera_x,0 - player.camera_y))
    map_home.map.update(window , player)

    shake_interval = 0
    if player.keyinput[pg.K_z]:
        shake_interval = random.randint(1,shake_str - 80)
   

    # PLAYER
    player.animation()
    player.combat()
    player.combat_animation()
    player.collider()

    particles.oak_leaf_fx.update(window, player)


    update()
