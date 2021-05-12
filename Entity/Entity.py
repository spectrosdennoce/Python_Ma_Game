import pygame
import copy
class Entity():
    def __init__(self,Image,Game,Reverse=False,Shoot_Entity=None,Position_Bullet_X=None,Position_Bullet_Y=None,Size_X=100,Size_Y=200,Pos_X=250,Pos_Y=250,Vitesse=10,Can_Shoot=False,Vie=3):
        self.Game = Game
        self.Size_Y = Size_Y
        self.Size_X = Size_X
        self.Image = []
        self.Sprite = []
        self.Reverse = Reverse
        self.Pos_Y = int(round(Pos_Y))
        self.Pos_X = int(round(Pos_X))
        for x in Image:
            x = pygame.transform.scale(
                        pygame.image.load(x).convert_alpha(),
                        (self.Size_X,self.Size_Y)
                        )
            if(self.Reverse == True):
                x = pygame.transform.flip(x,True,False)
            self.Sprite += [Sprite(x,self)]
            self.Image += [x]
        self.Vitesse = Vitesse
        self.Can_Shoot = Can_Shoot
        self.Is_Action = False
        self.Is_Shooting = False
        self.Is_Animate = False
        self.Animation_Reverse = False
        self.Is_Away_Shot = False
        self.Has_Shoot = False
        self.frames = 0
        self.Speed = 400
        self.Max_Vie = Vie
        self.Vie = Vie
        self.Etat = 0
        self.Shoot_Entity = Shoot_Entity
        self.Bullet = []
        self.Position_Bullet_Y = Position_Bullet_Y
        self.Position_Bullet_X = Position_Bullet_X

    def Animate(self,Min_Plage,Max_Plage,Reverse = False,function_unleash = None):
        
        if(self.Has_Shoot == False):
            self.Is_Animate = True

        if ((self.Animation_Reverse == False) & (self.Etat == Max_Plage)) | ((self.Animation_Reverse == True) & (self.Etat <= Min_Plage)):
            self.Etat = 0
            self.Is_Animate = False
            self.Has_Shoot = True
            self.Animation_Reverse = False
        
        if(self.Game.Debug == True):
            print("Is_Animate : " + str(self.Is_Animate))
        if(self.Is_Animate):
            if(self.Etat+Min_Plage > Max_Plage):
                function_unleash()
            if(self.Etat+Min_Plage <= Max_Plage) & (self.Animation_Reverse == False):
                if(self.Etat+Min_Plage == Max_Plage):
                    self.Animation_Reverse = Reverse
                self.Etat += 1
            elif (self.Etat > Min_Plage) & (self.Animation_Reverse == True):
                self.Etat -= 1
                
        if(self.Game.Debug == True):
            print("Etat : " + str(self.Etat))

    def Shoot(self):
        self.Shoot_Entity.Get_Image()
        self.Shoot_Entity.Pos_Y = self.Pos_Y + self.Position_Bullet_Y
        self.Shoot_Entity.Pos_X = self.Pos_X + self.Position_Bullet_X
        self.Is_Shooting = True
        try:
            self.Shoot_Entity.Sfx.play().set_volume(self.Game.SFX_Volume)
        except:
            if(self.Game.Debug):
                print("sound bugged")
        self.Bullet.append(copy.copy(self.Shoot_Entity))

    def Get_Image(self):
        x = self.Image[self.Etat%len(self.Image)]
        #sprite
        if(self.Reverse == True):
            x = pygame.transform.flip(x,True,False)
            #sprite
            if(self.Shoot_Entity is not None) & (self.Is_Shooting == False):
                self.Shoot_Entity.Reverse = True
        else:
            if(self.Shoot_Entity is not None) & (self.Is_Shooting == False):
                self.Shoot_Entity.Reverse = False
        self.Get_Sprite().Refresh_Sprite(x,self)
        return x

    def Goto_Left(self):
        self.Reverse = True
        if  (self.Pos_X > 0):
            self.Pos_X -= self.Vitesse
        elif  (self.Pos_X < 0):
            self.Pos_X = 0

    def Goto_Right(self):
        self.Reverse = False
        if (self.Pos_X+self.Size_X < self.Game.SCREEN_WIDTH):
            self.Pos_X += self.Vitesse
        elif (self.Pos_X+self.Size_X > self.Game.SCREEN_WIDTH):
            self.Pos_X = self.Game.SCREEN_WIDTH-self.Size_X

    def Get_Sprite(self):
        return self.Sprite[self.Etat%len(self.Sprite)]

    def Get_Mask_Surface(self):
        return self.Get_Mask().to_surface(surface=None, setsurface=None, unsetsurface=None, setcolor=(255, 0, 0, 255), unsetcolor=(0, 0, 0, 0))

    def Get_Mask(self):
        return self.Get_Sprite().mask

    def Get_Pos(self):
        return (self.Pos_X, self.Pos_Y)

    def Get_Rect(self):
        return self.Get_Sprite().rect
        
    def Get_Offset(self,other):
        return (other.Get_Rect().x - self.Get_Rect().x,other.Get_Rect().y - self.Get_Rect().y)
    
    def IS_Overlaps(self,other):
        return (self.Get_Mask().overlap(other.Get_Mask(),self.Get_Offset(other)))
        

class Sprite(pygame.sprite.Sprite):
    def __init__(self,Image,Entity):
        pygame.sprite.Sprite.__init__(self) 
        self.Refresh_Sprite(Image,Entity)

    def Refresh_Sprite(self,Image,Entity):
        self.image = Image
        self.rect = pygame.Rect(self.image.get_rect(topleft=(Entity.Pos_X,Entity.Pos_Y)))
        self.mask = pygame.mask.from_surface(self.image)