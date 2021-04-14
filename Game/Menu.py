from Game.Display_Config import Display_Interface,pygame,ConfigParser,mixer,Level
class Menu(Display_Interface):
    def __init__(self):
        super().__init__()
        
        #get_Ressource
        self.Display.fill((0,0,0))
        Image_Bg = [pygame.image.load(r"./Image/Menu_Title_Bg_Play.png"),pygame.image.load(r"./Image/Menu_Title_Bg_Options.png"),pygame.image.load(r"./Image/Menu_Title_Bg_Quit.png")]
        self.Level = [Level(Image_Bg,self)]

    def HandleEvent(self):
            height_ground = self.SCREEN_HEIGHT-self.SCREEN_HEIGHT/4
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[getattr(pygame, "K_"+self.TOUCHE["escape"])]:
                        pygame.quit()
                    if keys[getattr(pygame, "K_"+self.TOUCHE["haut"])] & (self.Level[0].Etat != 0):
                        self.Level[0].Etat = self.Level[0].Etat-1
                    if keys[getattr(pygame, "K_"+self.TOUCHE["bas"])] & (self.Level[0].Etat < self.Level[0].Get_Nb_Image()-1):
                        self.Level[0].Etat = self.Level[0].Etat+1
                    if keys[getattr(pygame, "K_"+self.TOUCHE["enter"])]:
                        if self.Level[0].Etat ==0:
                            self.Running = False
                        elif self.Level[0].Etat == 1:
                            pygame.quit()
                        elif self.Level[0].Etat == 2:
                            pygame.quit()
    def Update(self):
        self.Display.fill((0,0,0))
        self.Display.blit(self.Level[0].Get_Image(),(0, 0))
        pygame.display.flip()
