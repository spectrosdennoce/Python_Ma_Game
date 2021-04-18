from Game.Display_Config import Display_Interface,pygame,ConfigParser,mixer,Level,glob
from Libs.Read_Raw import raw,Get_All_From_Folder
from Entity.Personage import Personnage
from Entity.Enemy import Enemy
from Entity.Bullet import Bullet
class Game(Display_Interface):
    def __init__(self):
        super().__init__()


    #get_Ressource
        ##get_image
        Image_Bg_Lvl1 = Get_All_From_Folder("./Image/Background/",".png")
        Image_Player = Get_All_From_Folder("./Image/Player/",".png")
        Image_Bullet = Get_All_From_Folder("./Image/Bullet/Bullet/",".png")
        Image_Laser = Get_All_From_Folder("./Image/Bullet/Laser/",".png")
        Image_Mob1 = Get_All_From_Folder("./Image/Mob/Sorcerer/",".png")
        Image_Mob2 = Get_All_From_Folder("./Image/Mob/TrucWip/",".png")
        Image_Mob3 = Get_All_From_Folder("./Image/Mob/Ship/",".png")
        
        ##get_sound
        Sfx = raw("./sfx/gun.wav")

    #init music
        mixer.music.load(r"./Music/songamu1.mp3")
        mixer.music.set_volume(0.2)
        #mixer.music.play(-1)
        self.Rythme = 1200
        self.BPM = 60
        self.milliseconds_until_event = self.Rythme
        self.milliseconds_since_event = 0


    #init player
        self.Player = Personnage(Image=Image_Player,Game=self,Position_Bullet_X=80,Position_Bullet_Y=40,Shoot_Entity=Bullet(Image_Bullet,self,Sfx))
    #init enemy
        self.Enemy = [
        Enemy(Image=Image_Mob1,Game=self,Position_Bullet_X=0,Vie = 9,Position_Bullet_Y=40,Shoot_Entity=Bullet(Image_Bullet,self,Sfx,Reverse=True),Pos_X=self.SCREEN_WIDTH-self.SCREEN_WIDTH/3,Pos_Y=self.SCREEN_HEIGHT-self.SCREEN_HEIGHT/3),
        Enemy(Image=Image_Mob2,Position_Bullet_X=0,Position_Bullet_Y=20,Game=self,Shoot_Entity=Bullet(Image_Bullet,self,Sfx,Reverse=True),Pos_X=self.SCREEN_WIDTH/2-self.SCREEN_WIDTH/3,Pos_Y=self.SCREEN_HEIGHT-self.SCREEN_HEIGHT/3),
        Enemy(Image=Image_Mob3,Position_Bullet_X=0,Position_Bullet_Y=89,Game=self,Shoot_Entity=Bullet(Image_Laser,self,Sfx),Pos_X=self.SCREEN_WIDTH-self.SCREEN_WIDTH/2,Pos_Y=self.SCREEN_HEIGHT-self.SCREEN_HEIGHT/3)
        ]
    #init Level
        self.Level = [Level(Image_Bg_Lvl1,self)]

    #init Controler
    def HandleEvent(self):
        height_ground = self.SCREEN_HEIGHT-self.SCREEN_HEIGHT/4
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.Running = False
        keys = pygame.key.get_pressed()
        if keys[getattr(pygame, "K_"+self.TOUCHE["escape"])]:
            self.Running = False

        if keys[getattr(pygame, "K_"+self.TOUCHE["haut"])] & (self.Player.Pos_Y > 0):
            self.Player.Pos_Y -= self.Player.Vitesse
        elif keys[getattr(pygame, "K_"+self.TOUCHE["haut"])] & (self.Player.Pos_Y < 0):
            self.Player.Pos_Y = 0

        if keys[getattr(pygame, "K_"+self.TOUCHE["bas"])] & (self.Player.Pos_Y+self.Player.Size_Y < self.SCREEN_HEIGHT):
            self.Player.Pos_Y += self.Player.Vitesse
        elif keys[getattr(pygame, "K_"+self.TOUCHE["bas"])] & (self.Player.Pos_Y+self.Player.Size_Y > self.SCREEN_HEIGHT):
            self.Player.Pos_Y = self.SCREEN_HEIGHT-self.Player.Size_Y

        if keys[getattr(pygame, "K_"+self.TOUCHE["droite"])]:
            self.Player.Goto_Right()

        if keys[getattr(pygame, "K_"+self.TOUCHE["gauche"])]:
            self.Player.Goto_Left()

        if keys[getattr(pygame, "K_"+self.TOUCHE["space"])] & (self.Player.Is_Shooting == False):
            if self.Player.Is_Action == True:
                self.Player.Shoot(True)

    #init Rythme_based
    def Rythme_fonc(self):

        if ((self.milliseconds_since_event >= self.milliseconds_until_event-self.BPM)):
            self.Player.Is_Action = True
            if self.milliseconds_since_event >= self.milliseconds_until_event+self.BPM:
                self.milliseconds_since_event = 0
                for i in self.Enemy:
                    if(i.Can_Shoot == True):
                        i.Shoot()
                self.Player.Is_Action = False
            self.milliseconds_until_event = self.Rythme
      
    #init Update
    def Update(self):
        #init black background
        self.Display.fill((0,0,0))
        #set image fonction level
        self.Display.blit(self.Level[self.Player.Level].Get_Image(),(0, 0))
        #get image pour tout enemy
        if ((self.milliseconds_since_event >= self.milliseconds_until_event-self.BPM)):
            pygame.draw.rect(self.Display,(255,0,255),pygame.Rect(self.SCREEN_WIDTH-100,self.SCREEN_HEIGHT-100,self.SCREEN_WIDTH,self.SCREEN_HEIGHT))

        for Enemy_unique in self.Enemy:
            if(Enemy_unique.Vie == 10):
                self.Display.blit(Enemy_unique.Get_Image(),(Enemy_unique.Pos_X, Enemy_unique.Pos_Y))
            else:
                self.Display.blit(Enemy_unique.Mask[Enemy_unique.Etat%len(Enemy_unique.Image)].to_surface(surface=None, setsurface=None, unsetsurface=None, setcolor=(255, 0, 0, 255), unsetcolor=(0, 0, 0, 0)),(Enemy_unique.Pos_X, Enemy_unique.Pos_Y))
        
            if (Enemy_unique.Is_Shooting == True) & (Enemy_unique.Is_Animate == False):
                    self.Display.blit(Enemy_unique.Shoot_Entity.Get_Image(),(Enemy_unique.Shoot_Entity.Pos_X, Enemy_unique.Shoot_Entity.Pos_Y))
                    if Enemy_unique.Shoot_Entity.Pos_X > 0:
                        Enemy_unique.Shoot_Entity.Pos_X -= Enemy_unique.Shoot_Entity.Vitesse
                    else:
                        Enemy_unique.Is_Shooting = False

        if (self.Player.Is_Shooting == True) & (self.Player.Is_Animate == False):
            if(self.Player.Shoot_Entity.Reverse == False):
                self.Display.blit(self.Player.Shoot_Entity.Get_Image(),(self.Player.Shoot_Entity.Pos_X, self.Player.Shoot_Entity.Pos_Y))
                self.Display.blit(self.Player.Shoot_Entity.Mask[self.Player.Etat%len(self.Player.Image)].to_surface(surface=None, setsurface=None, unsetsurface=None, setcolor=(255, 0, 0, 255), unsetcolor=(0, 0, 0, 0)),(self.Player.Shoot_Entity.Pos_X, self.Player.Shoot_Entity.Pos_Y))
        
                if self.Player.Shoot_Entity.Pos_X < self.SCREEN_WIDTH:
                    self.Player.Shoot_Entity.Pos_X += self.Player.Shoot_Entity.Vitesse
                else:
                    self.Player.Is_Shooting = False
            else:
                self.Display.blit(self.Player.Shoot_Entity.Get_Image(),(self.Player.Shoot_Entity.Pos_X-self.Player.Size_X, self.Player.Shoot_Entity.Pos_Y))
                self.Display.blit(self.Player.Shoot_Entity.Mask[self.Player.Etat%len(self.Player.Image)].to_surface(surface=None, setsurface=None, unsetsurface=None, setcolor=(255, 0, 0, 255), unsetcolor=(0, 0, 0, 0)),(self.Player.Shoot_Entity.Pos_X-self.Player.Size_X, self.Player.Shoot_Entity.Pos_Y))
        
        
                if self.Player.Shoot_Entity.Pos_X > 0:
                    self.Player.Shoot_Entity.Pos_X -= self.Player.Shoot_Entity.Vitesse
                else:
                    self.Player.Is_Shooting = False
        #if pygame.sprite.spritecollide(self.Player, self.Enemy, False, pygame.sprite.collide_mask):
         #   print("colide")
        #get image du joueur
        self.Display.blit(self.Player.Get_Image(),(self.Player.Pos_X, self.Player.Pos_Y))
        self.Display.blit(self.Player.Mask[self.Player.Etat%len(self.Player.Image)].to_surface(surface=None, setsurface=None, unsetsurface=None, setcolor=(255, 0, 0, 255), unsetcolor=(0, 0, 0, 0)),(self.Player.Pos_X, self.Player.Pos_Y))
        
        self.milliseconds_since_event += pygame.time.Clock().tick(self.frames_per_second)
        pygame.display.flip()
