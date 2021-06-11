from Entity.Entity import Entity
from Game.Display_Config import pygame
class Enemy(Entity):
    def __init__(self,Image,Game,Pos_X,Pos_Y,Shoot_Entity,Position_Bullet_X,Position_Bullet_Y,Vie=10,Vitesse=3,Reverse=False):
        super().__init__(Image, Game,Reverse,Position_Bullet_X=Position_Bullet_X,Position_Bullet_Y=Position_Bullet_Y,Size_X=80,Vitesse=Vitesse,Can_Shoot=True,Vie=Vie,Pos_X=Pos_X,Pos_Y=Pos_Y,Shoot_Entity=Shoot_Entity)
    def Print_Screen(self):
        if(self.Game.Debug):
            self.Game.Display.set_at(self.Get_Pos(), (255,255,0,255))
        #show enemy masque image
        self.Game.Display.blit(self.Get_Image(),self.Get_Pos())
        if(self.Game.Debug):
            self.Game.Display.blit(self.Get_Mask_Surface(),(self.Get_Pos()))
        
        pygame.draw.rect(self.Game.Display,(40,150,40,255),pygame.Rect(self.Get_Rect().x-10.1,self.Get_Rect().y-20.1,(self.Size_X+22),12))
        pygame.draw.rect(self.Game.Display,(255,0,0,255),pygame.Rect(self.Get_Rect().x-10,self.Get_Rect().y-20,(self.Size_X+20),10))
        pygame.draw.rect(self.Game.Display,(0,255,0,255),pygame.Rect(self.Get_Rect().x-10,self.Get_Rect().y-20,(self.Vie/self.Max_Vie*(self.Size_X+20)),10))