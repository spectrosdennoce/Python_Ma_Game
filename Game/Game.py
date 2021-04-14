from Game.Display_Config import Display_Interface,pygame,ConfigParser,mixer,Level
from Entity.Personage import Personnage
from Entity.Enemy import Enemy
from Entity.Bullet import Bullet
class Game(Display_Interface):
    def __init__(self):
        super().__init__()
        #init music
        mixer.music.load(r"./Music/songamu1.mp3")
        mixer.music.set_volume(0.2)
        #mixer.music.play(-1)
        self.Rythme = 1200
        self.BPM = 60
        self.milliseconds_until_event = self.Rythme
        self.milliseconds_since_event = 0
        #get_Ressource
        Image_Bg_Lvl1 = [pygame.image.load(r"./Image/bg1.png")]
        Image_Player = [pygame.image.load(r"./Image/Perso.png")]
        Image_Bullet = [pygame.image.load(r"./Image/Bullet.png")]
        Image_Mob1 = [pygame.image.load(r"./Image/mob.png"),pygame.image.load(r"./Image/mob1.png"),pygame.image.load(r"./Image/mob2.png")]
        Image_Mob2 = [pygame.image.load(r"./Image/mobground1.png"),pygame.image.load(r"./Image/mobground2.png")]
        Sfx = pygame.mixer.Sound(r"./sfx/gun.wav")
        #init player
        self.Player = Personnage(Image=Image_Player,Game=self,Position_Bullet_X=50,Position_Bullet_Y=20,Shoot_Entity=Bullet(Image_Bullet,self,Sfx))
        #init enemy
        self.Enemy = [
        Enemy(Image=Image_Mob1,Game=self,Position_Bullet_X=0,Position_Bullet_Y=40,Shoot_Entity=Bullet(Image_Bullet,self,Sfx),Pos_X=self.SCREEN_WIDTH-self.SCREEN_WIDTH/3,Pos_Y=self.SCREEN_HEIGHT-self.SCREEN_HEIGHT/3),
        Enemy(Image=Image_Mob2,Position_Bullet_X=0,Position_Bullet_Y=20,Game=self,Shoot_Entity=Bullet(Image_Bullet,self,Sfx),Pos_X=self.SCREEN_WIDTH/2-self.SCREEN_WIDTH/3,Pos_Y=self.SCREEN_HEIGHT-self.SCREEN_HEIGHT/3)
        ]
        #init Level
        self.Level = [Level(Image_Bg_Lvl1,self)]

    def HandleEvent(self):
        height_ground = self.SCREEN_HEIGHT-self.SCREEN_HEIGHT/4
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.Running = False
        keys = pygame.key.get_pressed()
        if keys[getattr(pygame, "K_"+self.TOUCHE["escape"])]:
            self.Running = False

        if keys[getattr(pygame, "K_"+self.TOUCHE["haut"])] & (self.Player.Pos_Y > 0) & (self.Player.Is_Action == True):
            self.Player.Pos_Y -= self.Player.Vitesse
        elif keys[getattr(pygame, "K_"+self.TOUCHE["haut"])] & (self.Player.Pos_Y < 0) & (self.Player.Is_Action == True):
            self.Player.Pos_Y = 0

        if keys[getattr(pygame, "K_"+self.TOUCHE["bas"])] & (self.Player.Pos_Y+self.Player.Size_Y < self.SCREEN_HEIGHT):
            self.Player.Pos_Y += self.Player.Vitesse
        elif keys[getattr(pygame, "K_"+self.TOUCHE["bas"])] & (self.Player.Pos_Y+self.Player.Size_Y > self.SCREEN_HEIGHT):
            self.Player.Pos_Y = self.SCREEN_HEIGHT-self.Player.Size_Y

        if keys[getattr(pygame, "K_"+self.TOUCHE["droite"])] & (self.Player.Pos_X+self.Player.Size_X < self.SCREEN_WIDTH):
            self.Player.Pos_X += self.Player.Vitesse
        elif keys[getattr(pygame, "K_"+self.TOUCHE["droite"])] & (self.Player.Pos_X+self.Player.Size_X > self.SCREEN_WIDTH):
            self.Player.Pos_X = self.SCREEN_WIDTH-self.Player.Size_X

        if keys[getattr(pygame, "K_"+self.TOUCHE["gauche"])] & (self.Player.Pos_X > 0):
            self.Player.Pos_X -= self.Player.Vitesse
        elif keys[getattr(pygame, "K_"+self.TOUCHE["gauche"])] & (self.Player.Pos_X < 0):
            self.Player.Pos_X = 0

        if keys[getattr(pygame, "K_"+self.TOUCHE["space"])] & (self.Player.Is_Shooting == False):
            if self.Player.Is_Action == True:
                self.Player.Shoot()

    def Rythme_fonc(self):
        if ((self.milliseconds_since_event >= self.milliseconds_until_event-self.BPM)):
            pygame.draw.rect(self.Display,(255,0,255),pygame.Rect(self.SCREEN_WIDTH-100,self.SCREEN_HEIGHT-100,self.SCREEN_WIDTH,self.SCREEN_HEIGHT))
            self.Player.Is_Action = True
            if self.milliseconds_since_event >= self.milliseconds_until_event+self.BPM:
                self.milliseconds_since_event = 0
                for i in self.Enemy:
                    if(i.Etat % len(i.Image) == len(i.Image)-1) & (i.Can_Shoot == True):
                        i.Shoot()
                    i.Etat += 1
                self.Player.Etat += 1
                self.Player.Is_Action = False
            self.milliseconds_until_event = self.Rythme

    def Update(self):
        self.Display.fill((0,0,0))
        self.Display.blit(self.Level[self.Player.Level].Get_Image(),(0, 0))
        self.Display.blit(self.Player.Get_Image(),(self.Player.Pos_X, self.Player.Pos_Y))
        for Enemy_unique in self.Enemy:
            if (Enemy_unique.Is_Shooting == True):
                    Enemy_unique.Game.Display.blit(pygame.transform.flip(Enemy_unique.Shoot_Entity.Get_Image(),True,False),(Enemy_unique.Shoot_Entity.Pos_X, Enemy_unique.Shoot_Entity.Pos_Y))
                    if Enemy_unique.Shoot_Entity.Pos_X < self.SCREEN_WIDTH:
                        Enemy_unique.Shoot_Entity.Pos_X -= Enemy_unique.Shoot_Entity.Vitesse
                    else:
                        Enemy_unique.Is_Shooting = False

            self.Display.blit(Enemy_unique.Get_Image(),(Enemy_unique.Pos_X, Enemy_unique.Pos_Y))

        if (self.Player.Is_Shooting == True):
            self.Player.Game.Display.blit(self.Player.Shoot_Entity.Get_Image(),(self.Player.Shoot_Entity.Pos_X, self.Player.Shoot_Entity.Pos_Y))
            if self.Player.Shoot_Entity.Pos_X < self.SCREEN_WIDTH:
                self.Player.Shoot_Entity.Pos_X += self.Player.Shoot_Entity.Vitesse
            else:
                self.Player.Is_Shooting = False
                
        self.milliseconds_since_event += pygame.time.Clock().tick(self.frames_per_second)
        self.Rythme_fonc()

        pygame.display.flip()
