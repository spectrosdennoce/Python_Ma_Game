import pygame
from Entity.Entity import Entity
class Bullet(Entity):
    def __init__(self,Image,Game,Sfx = None):
        super().__init__(Image, Game,Size_X=32,Size_Y=32,Vie=1,Vitesse=20)
        self.Sfx = Sfx