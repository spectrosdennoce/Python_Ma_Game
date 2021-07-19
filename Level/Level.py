import pygame
from Libs.Sprite import Sprite
class Level:
    def __init__(self,Image,Game,Pos_X = 0, Pos_Y = 0):
        self.Difficulte = 0
        self.Scrolling_Speed = 2
        self.Etat = 0
        self.Gravity = 0.5
    #init level floor
        self.Height_Ground = Game.SCREEN_HEIGHT-300
        self.Image_Level= []
        for x in Image:
            self.Image_Level += [
                pygame.transform.scale(
                    pygame.image.load(x),
                    (Game.SCREEN_WIDTH,Game.SCREEN_HEIGHT)
                    )
                ]
        self.Pos_X = Pos_X
        self.Pos_Y = Pos_Y
        self.Sprite = [Sprite(self.Image_Level[0],self)]
    def Get_Image(self):
        return self.Image_Level[self.Etat%len(self.Image_Level)]
    def Get_Nb_Image(self):
        return len(self.Image_Level)
    def Get_Rect(self):
        return self.Get_Sprite().rect
    def Get_Mask(self):
        return self.Get_Sprite().mask

    def Get_Pos(self):
        return (self.Pos_X, self.Pos_Y)
    def Get_Sprite(self):
        return self.Sprite[self.Etat%len(self.Sprite)]


