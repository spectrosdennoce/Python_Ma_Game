import pygame
class Sprite(pygame.sprite.Sprite):
    def __init__(self,Image,Entity):
        pygame.sprite.Sprite.__init__(self)
        self.Refresh_Sprite(Image,Entity)

    def Refresh_Sprite(self,Image,Entity):
        self.image = Image
        self.rect = pygame.Rect(self.image.get_rect(topleft=(Entity.Pos_X,Entity.Pos_Y)))
        self.mask = pygame.mask.from_surface(self.image)