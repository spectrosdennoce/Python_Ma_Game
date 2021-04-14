import pygame

class Entity:
    def __init__(self,Image,Game,Shoot_Entity=None,Position_Bullet_X=None,Position_Bullet_Y=None,Size_X=50,Size_Y=100,Pos_X=250,Pos_Y=250,Vitesse=10,Can_Shoot=False,Vie=3):
        self.Game = Game
        self.Size_Y = Size_Y
        self.Size_X = Size_X
        self.Image= []
        for x in Image:
            self.Image += [pygame.transform.scale(x,(self.Size_X,self.Size_Y))]
        self.Pos_Y = Pos_Y
        self.Pos_X = Pos_X
        self.Vitesse = Vitesse
        self.Can_Shoot = Can_Shoot
        self.Is_Action = False
        self.Is_Shooting = False
        self.Vie = Vie
        self.Etat = 0
        self.Shoot_Entity = Shoot_Entity
        self.Position_Bullet_Y = Position_Bullet_Y
        self.Position_Bullet_X = Position_Bullet_X
    def Shoot(self):
        self.Shoot_Entity.Pos_Y = self.Pos_Y + self.Position_Bullet_Y
        self.Shoot_Entity.Pos_X = self.Pos_X + self.Position_Bullet_X
        self.Is_Shooting = True
        self.Shoot_Entity.Sfx.play().set_volume(0.1)
    def Get_Image(self):
        return self.Image[self.Etat%len(self.Image)]