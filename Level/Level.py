import pygame
class Level:
    def __init__(self,Image,Game):
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
    def Get_Image(self):
        return self.Image_Level[self.Etat%len(self.Image_Level)]
    def Get_Nb_Image(self):
        return len(self.Image_Level)