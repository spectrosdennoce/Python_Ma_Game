import pygame,math
from Entity.Entity import Entity
class Bullet(Entity):
    def __init__(self,Image,Game,Sfx,Degat=1,Reverse=False,Trajectoire=0):
        super().__init__(Image, Game,Reverse,Size_X=32,Size_Y=32,Vie=1,Vitesse=20)
        self.Sfx = pygame.mixer.Sound(Sfx)
        self.Has_Hit = False
        self.Degat = Degat
        self.Trajectoire = Trajectoire
    def right(self,owner):
        self.Pos_X += self.Vitesse
        self.Pos_Y = self.Get_Trajectoire(owner)
    def left(self,owner):
        self.Pos_X -= self.Vitesse
        self.Pos_Y = self.Get_Trajectoire(owner)
    def Get_Trajectoire(self,owner):
        if(self.Trajectoire == 0):
            return self.Pos_Y
        elif(self.Trajectoire == 1):
            return int(math.sin((self.Pos_X-owner.Get_Shoot_Point()[0])/50) * 100 + owner.Get_Shoot_Point()[1])
        elif(self.Trajectoire == -1):
            return int(-math.sin((self.Pos_X-owner.Get_Shoot_Point()[0])/50) * 100 + owner.Get_Shoot_Point()[1])
