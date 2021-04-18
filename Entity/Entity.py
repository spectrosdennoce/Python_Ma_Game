import pygame
class Entity():
    def __init__(self,Image,Game,Reverse=False,Shoot_Entity=None,Position_Bullet_X=None,Position_Bullet_Y=None,Size_X=100,Size_Y=200,Pos_X=250,Pos_Y=250,Vitesse=10,Can_Shoot=False,Vie=3):
        self.Game = Game
        self.Size_Y = Size_Y
        self.Size_X = Size_X
        self.Image = []
        self.Sprite = []
        self.Reverse = Reverse
        self.Pos_Y = Pos_Y
        self.Pos_X = Pos_X
        for x in Image:
            imagex = pygame.image.load(x)
            x = pygame.transform.scale(
                        pygame.image.load(x).convert_alpha(),
                        (self.Size_X,self.Size_Y)
                        )
            if(self.Reverse == True):
                x = pygame.transform.flip(x,True,False)
            self.Sprite += [Sprite(x,Pos_X,Pos_Y)]
            self.Image += [x]
            
        self.Vitesse = Vitesse
        self.Can_Shoot = Can_Shoot
        self.Is_Action = False
        self.Is_Shooting = False
        self.Is_Animate = False
        self.Vie = Vie
        self.Etat = 0
        self.Shoot_Entity = Shoot_Entity
        self.Position_Bullet_Y = Position_Bullet_Y
        self.Position_Bullet_X = Position_Bullet_X
    def Shoot(self,Reverse = False):
        self.Shoot_Entity.Pos_Y = self.Pos_Y + self.Position_Bullet_Y
        self.Shoot_Entity.Pos_X = self.Pos_X + self.Position_Bullet_X
        self.Etat = 0
        self.Is_Shooting = True
        self.Is_Animate = True
        while (self.Etat < len(self.Image)):
            self.Etat = self.Etat+1
            self.Game.HandleEvent()
            self.Game.Update()
        if(Reverse == True):
            while (self.Etat > 0):
                self.Etat = self.Etat-1
                self.Game.HandleEvent()
                self.Game.Update()
        self.Is_Animate = False
        self.Shoot_Entity.Sfx.play().set_volume(0.1)
    def Get_Image(self):
        x = self.Image[self.Etat%len(self.Image)]
        #sprite
        self.Sprite[self.Etat%len(self.Image)].Refresh_Sprite(x,self.Pos_X,self.Pos_Y)
        if(self.Reverse == True):
            x = pygame.transform.flip(x,True,False)
            #sprite
            self.Sprite[self.Etat%len(self.Image)].Refresh_Sprite(x,self.Pos_X,self.Pos_Y)
            if(self.Shoot_Entity is not None) & (self.Is_Shooting == False):
                self.Shoot_Entity.Reverse = True
        else:
            if(self.Shoot_Entity is not None) & (self.Is_Shooting == False):
                self.Shoot_Entity.Reverse = False
        return x
    def Goto_Right(self):
        self.Reverse = False
        if (self.Pos_X+self.Size_X < self.Game.SCREEN_WIDTH):
            self.Pos_X += self.Vitesse
        elif (self.Pos_X+self.Size_X > self.Game.SCREEN_WIDTH):
            self.Pos_X = self.Game.SCREEN_WIDTH-self.Size_X
    def Goto_Left(self):
        self.Reverse = True
        if  (self.Pos_X > 0):
            self.Pos_X -= self.Vitesse
        elif  (self.Pos_X < 0):
            self.Pos_X = 0

class Sprite(pygame.sprite.Sprite):
    def __init__(self,Image,Pos_X,Pos_Y):
        self.Refresh_Sprite(Image,Pos_X,Pos_Y)
    
    def Refresh_Sprite(self,Image,Pos_X,Pos_Y):
        self.image = Image
        self.rect = pygame.Rect(self.image.get_rect(topleft=(Pos_X,Pos_Y)))
        self.mask = pygame.mask.from_surface(self.image)