import pygame
class Level:
    def __init__(self,Image,Game):
        self.Difficulte = 0
        self.Scrolling_Speed = 2
        self.Etat = 0
        self.Image_Level= []
        for x in Image:
            self.Image_Level += [pygame.transform.scale(x,(Game.SCREEN_WIDTH,Game.SCREEN_HEIGHT))]
    def Get_Image(self):
        return self.Image_Level[self.Etat%len(self.Image_Level)]
    def Get_Nb_Image(self):
        return len(self.Image_Level)