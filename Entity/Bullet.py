import pygame
from Entity.Entity import Entity
class Bullet(Entity):
    def __init__(self,Image,Game,Sfx,Degat=1,Reverse=False):
        super().__init__(Image, Game,Reverse,Size_X=32,Size_Y=32,Vie=1,Vitesse=20)
        self.Sfx = pygame.mixer.Sound(Sfx)
        self.Has_Hit = False
        self.Degat = Degat