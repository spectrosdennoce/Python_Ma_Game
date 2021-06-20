from Entity.Entity import Entity
import pygame
class Personnage(Entity):
    def __init__(self,Image,Game,Shoot_Entity,Position_Bullet_X,Position_Bullet_Y,Reverse=False,Jump_Heigth = -10):
        super().__init__(Image, Game,Reverse,
        #bullet
        Position_Bullet_X=Position_Bullet_X,Position_Bullet_Y=Position_Bullet_Y,Can_Shoot=True,Shoot_Entity=Shoot_Entity,
        #information
        Vie=1,Pos_X=Game.SCREEN_WIDTH/2,Vitesse = 7,Pos_Y=Game.SCREEN_HEIGHT-300)
        self.Level = 0
        self.Is_Jump = False
        self.Is_Away_Jump = False
        self.Jump_Heigth = Jump_Heigth
        self.Jump_Heigth_Init = Jump_Heigth
    def print_life(self):
        pygame.draw.rect(self.Game.Display,(40,150,40,255),pygame.Rect(10.1,10.1,(self.Size_X+22),12))
        pygame.draw.rect(self.Game.Display,(255,0,0,255),pygame.Rect(10,10,(self.Size_X+20),10))
        pygame.draw.rect(self.Game.Display,(0,255,0,255),pygame.Rect(10,10,(self.Vie/self.Max_Vie*(self.Size_X+20)),10))
    def jump(self):
        if(self.Is_Jump == True):
            self.Pos_Y += self.Jump_Heigth
            self.Jump_Heigth += self.Game.Level[self.Level].Gravity
            if(self.Pos_Y > self.Game.Level[self.Level].Height_Ground):
                self.Is_Jump = False
                self.Is_Away_Jump = False
                self.Jump_Heigth = self.Jump_Heigth_Init
        if self.Is_Jump == False:
            self.Etat=0
    def Set_Jump(self):
        self.Is_Jump = True
    # reference mon code sur du c++
    # double pos_x = bill.front()->getY();
    # if(bill.front()->getJump() == true){
    #     bill.front()->setY(bill.front()->getY()+jump_heigth);
    #     jump_heigth += gravity;
    #     if(bill.front()->getY() > height_ground){
    #         bill.front()->setJump(false);
    #         jump_heigth = jump_heigth_init;
    #     }
    # }